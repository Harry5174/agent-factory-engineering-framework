from __future__ import annotations

import copy
import hashlib
import os
import socket
import stat
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import pytest
import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = (REPOSITORY_ROOT / "tools" / "validate_afef.py").resolve()
FRAMEWORK_SNAPSHOT_ROOTS = (
    ("tools", REPOSITORY_ROOT / "tools"),
    ("schemas-v0.2", REPOSITORY_ROOT / "schemas" / "v0.2"),
)
ADOPTED_AFEF_COMMIT = "02e231276f5a642d486c8035bceaee61dbfc3500"
PIN_DIAGNOSTIC_SHA256 = (
    "070d40c5a4b074336dbf7d564bd091f7478e1ffbc58465a8246bbfa817f886d0"
)
REFERENCE_DIAGNOSTIC_SHA256 = (
    "23229e2c6673ac80297f83346d76a560217c5a8856b6a75ff390cd857c6a4377"
)
EXPECTED_ADOPTER_INVENTORY = (
    (".", "directory"),
    (".afef/", "directory"),
    (".afef/project-manifest.yaml", "regular-file"),
    (".afef/specifications/", "directory"),
    (".afef/specifications/spec-0001.md", "regular-file"),
    (".afef/work-records/", "directory"),
    (".afef/work-records/work-0001.yaml", "regular-file"),
)

MANIFEST = {
    "schema_version": "0.2.0",
    "project": {
        "id": "clean-room-adopter",
        "name": "Clean-room adopter",
    },
    "repository": {
        "identity": "local/clean-room-adopter",
    },
    "afef": {
        "version": "0.2.0",
        "commit": ADOPTED_AFEF_COMMIT,
    },
    "constitution": {
        "inline": [
            "Only bounded local reads are represented by this adoption proof.",
        ],
    },
    "paths": {
        "specifications": ".afef/specifications",
        "work_records": ".afef/work-records",
    },
}

SPECIFICATION = {
    "schema_version": "0.2.0",
    "specification_id": "SPEC-0001",
    "title": "Inspect local project records",
    "owner": "clean-room-owner",
    "specification_status": "draft",
    "delivery_status": "not_started",
    "acceptance_criteria": [
        {
            "id": "AC-0001",
            "description": "The bounded local-read work record is conforming.",
        },
    ],
}

WORK_RECORD = {
    "schema_version": "0.2.0",
    "work_id": "WORK-0001",
    "related_specifications": ["SPEC-0001"],
    "risk_profile": "lean",
    "scope": {
        "in_scope": ["Read adopter-owned records locally."],
        "out_of_scope": ["Writes, external operations, publication, and release."],
    },
    "authorization_envelope": {
        "operations": [
            {
                "operation_id": "OP-READ",
                "effect_class": "local-read",
                "decision": "permitted",
                "authorization_requirement": "bounded_work_envelope",
            },
        ],
    },
    "implementation_state": "not_started",
    "reviews": [],
    "final_gate": {
        "status": "not_issued",
    },
    "human_checkpoint": {
        "status": "not_reached",
        "next_required_action": "Obtain implementation supervisor review.",
    },
}


def _is_within(path: Path, possible_parent: Path) -> bool:
    return path.resolve().is_relative_to(possible_parent.resolve())


@dataclass(frozen=True)
class EntryState:
    entry_type: str
    mode: int
    mtime_ns: int
    ctime_ns: int
    owner_id: int | None
    group_id: int | None
    byte_size: int | None = None
    sha256: str | None = None
    symlink_target: str | None = None


@dataclass(frozen=True)
class ValidationRun:
    result: subprocess.CompletedProcess[bytes]
    adopter_before: dict[str, EntryState]
    adopter_after: dict[str, EntryState]
    framework_before: dict[str, EntryState]
    framework_after: dict[str, EntryState]
    post_run_inventory: tuple[tuple[str, str], ...]


def _entry_type(mode: int) -> str:
    classifications = (
        (stat.S_ISREG, "regular-file"),
        (stat.S_ISDIR, "directory"),
        (stat.S_ISLNK, "symlink"),
        (stat.S_ISFIFO, "fifo"),
        (stat.S_ISSOCK, "socket"),
        (stat.S_ISCHR, "character-device"),
        (stat.S_ISBLK, "block-device"),
    )
    for predicate, name in classifications:
        if predicate(mode):
            return name
    return "other"


def _nanoseconds(metadata: os.stat_result, exact: str, fallback: str) -> int:
    value = getattr(metadata, exact, None)
    if value is not None:
        return int(value)
    return int(getattr(metadata, fallback) * 1_000_000_000)


def _hash_regular_file(
    path: Path, stable_key: str, metadata: os.stat_result
) -> str:
    if not hasattr(os, "O_NOFOLLOW"):
        raise AssertionError(f"O_NOFOLLOW unavailable while snapshotting {stable_key}")
    flags = os.O_RDONLY | os.O_NOFOLLOW
    if hasattr(os, "O_BINARY"):
        flags |= os.O_BINARY
    try:
        descriptor = os.open(path, flags)
    except OSError as error:
        raise AssertionError(
            f"unable to open regular file {stable_key} without following symlinks "
            f"({type(error).__name__})"
        ) from None
    try:
        opened_metadata = os.fstat(descriptor)
        stable_metadata = (
            stat.S_IMODE(metadata.st_mode),
            metadata.st_size,
            _nanoseconds(metadata, "st_mtime_ns", "st_mtime"),
            _nanoseconds(metadata, "st_ctime_ns", "st_ctime"),
            getattr(metadata, "st_uid", None),
            getattr(metadata, "st_gid", None),
        )
        opened_stable_metadata = (
            stat.S_IMODE(opened_metadata.st_mode),
            opened_metadata.st_size,
            _nanoseconds(opened_metadata, "st_mtime_ns", "st_mtime"),
            _nanoseconds(opened_metadata, "st_ctime_ns", "st_ctime"),
            getattr(opened_metadata, "st_uid", None),
            getattr(opened_metadata, "st_gid", None),
        )
        if not stat.S_ISREG(opened_metadata.st_mode):
            raise AssertionError(
                f"entry type changed while snapshotting {stable_key}"
            )
        if opened_stable_metadata != stable_metadata:
            raise AssertionError(f"entry changed while snapshotting {stable_key}")
        digest = hashlib.sha256()
        while chunk := os.read(descriptor, 1024 * 1024):
            digest.update(chunk)
        return digest.hexdigest()
    except OSError as error:
        raise AssertionError(
            f"unable to read regular file {stable_key} ({type(error).__name__})"
        ) from None
    finally:
        os.close(descriptor)


def _snapshot_entry(
    *,
    path: Path,
    relative_path: Path,
    root_label: str,
    snapshot: dict[str, EntryState],
) -> None:
    relative_key = "." if relative_path == Path(".") else relative_path.as_posix()
    stable_key = f"{root_label}:{relative_key}"
    try:
        metadata = path.lstat()
    except OSError as error:
        raise AssertionError(
            f"unable to inspect {stable_key} with lstat ({type(error).__name__})"
        ) from None

    entry_type = _entry_type(metadata.st_mode)
    sha256 = None
    symlink_target = None
    byte_size = metadata.st_size if entry_type == "regular-file" else None
    if entry_type == "regular-file":
        sha256 = _hash_regular_file(path, stable_key, metadata)
    elif entry_type == "symlink":
        try:
            symlink_target = os.readlink(path)
        except OSError as error:
            raise AssertionError(
                f"unable to read symlink target {stable_key} "
                f"({type(error).__name__})"
            ) from None

    snapshot[stable_key] = EntryState(
        entry_type=entry_type,
        mode=stat.S_IMODE(metadata.st_mode),
        mtime_ns=_nanoseconds(metadata, "st_mtime_ns", "st_mtime"),
        ctime_ns=_nanoseconds(metadata, "st_ctime_ns", "st_ctime"),
        owner_id=getattr(metadata, "st_uid", None),
        group_id=getattr(metadata, "st_gid", None),
        byte_size=byte_size,
        sha256=sha256,
        symlink_target=symlink_target,
    )

    if entry_type != "directory":
        return
    try:
        with os.scandir(path) as entries:
            child_names = sorted(entry.name for entry in entries)
    except OSError as error:
        raise AssertionError(
            f"unable to enumerate directory {stable_key} "
            f"({type(error).__name__})"
        ) from None
    for child_name in child_names:
        child_relative = (
            Path(child_name)
            if relative_path == Path(".")
            else relative_path / child_name
        )
        _snapshot_entry(
            path=path / child_name,
            relative_path=child_relative,
            root_label=root_label,
            snapshot=snapshot,
        )


def _snapshot_roots(
    roots: tuple[tuple[str, Path], ...],
) -> dict[str, EntryState]:
    snapshot: dict[str, EntryState] = {}
    for root_label, root in roots:
        if ":" in root_label or "/" in root_label:
            raise AssertionError(f"invalid snapshot root label {root_label!r}")
        _snapshot_entry(
            path=root,
            relative_path=Path("."),
            root_label=root_label,
            snapshot=snapshot,
        )
    return dict(sorted(snapshot.items()))


def _adopter_inventory(
    snapshot: dict[str, EntryState],
) -> tuple[tuple[str, str], ...]:
    inventory: list[tuple[str, str]] = []
    for stable_key, state in snapshot.items():
        if not stable_key.startswith("adopter:"):
            raise AssertionError("adopter snapshot contains another root label")
        relative_key = stable_key.removeprefix("adopter:")
        display_path = (
            f"{relative_key}/"
            if state.entry_type == "directory" and relative_key != "."
            else relative_key
        )
        inventory.append((display_path, state.entry_type))
    return tuple(inventory)


def _write_adopter(
    adopter_root: Path,
    *,
    manifest: dict | None = None,
    specification: dict | None = None,
    work_record: dict | None = None,
) -> None:
    specifications = adopter_root / ".afef" / "specifications"
    work_records = adopter_root / ".afef" / "work-records"
    specifications.mkdir(parents=True)
    work_records.mkdir(parents=True)

    manifest_data = copy.deepcopy(MANIFEST if manifest is None else manifest)
    specification_data = copy.deepcopy(
        SPECIFICATION if specification is None else specification
    )
    work_record_data = copy.deepcopy(
        WORK_RECORD if work_record is None else work_record
    )

    (adopter_root / ".afef" / "project-manifest.yaml").write_text(
        yaml.safe_dump(manifest_data, sort_keys=False),
        encoding="utf-8",
    )
    (specifications / "spec-0001.md").write_text(
        "---\n"
        + yaml.safe_dump(specification_data, sort_keys=False)
        + "---\n\n# Inspect local project records\n",
        encoding="utf-8",
    )
    (work_records / "work-0001.yaml").write_text(
        yaml.safe_dump(work_record_data, sort_keys=False),
        encoding="utf-8",
    )


def _assert_minimum_local_inventory(
    adopter_root: Path,
    snapshot: dict[str, EntryState] | None = None,
) -> dict[str, EntryState]:
    current = (
        _snapshot_roots((("adopter", adopter_root),))
        if snapshot is None
        else snapshot
    )
    assert _adopter_inventory(current) == EXPECTED_ADOPTER_INVENTORY
    return current


def _run_validator(
    adopter_root: Path, external_cwd: Path
) -> ValidationRun:
    absolute_python = Path(sys.executable)
    absolute_adopter = adopter_root.resolve()
    child_environment = {"PYTHONDONTWRITEBYTECODE": "1"}

    assert absolute_python.is_absolute()
    assert REPOSITORY_ROOT.is_absolute()
    assert VALIDATOR_PATH.is_absolute()
    assert absolute_adopter.is_absolute()
    assert not _is_within(absolute_adopter, REPOSITORY_ROOT)
    assert not _is_within(external_cwd, REPOSITORY_ROOT)
    assert "PATH" not in child_environment

    adopter_before = _assert_minimum_local_inventory(adopter_root)
    framework_before = _snapshot_roots(FRAMEWORK_SNAPSHOT_ROOTS)
    result = subprocess.run(
        [
            str(absolute_python),
            str(VALIDATOR_PATH),
            "--project",
            str(absolute_adopter),
        ],
        cwd=external_cwd,
        env=child_environment,
        capture_output=True,
        check=False,
    )
    adopter_after = _snapshot_roots((("adopter", adopter_root),))
    framework_after = _snapshot_roots(FRAMEWORK_SNAPSHOT_ROOTS)
    assert adopter_after == adopter_before
    assert framework_after == framework_before
    _assert_minimum_local_inventory(adopter_root, adopter_after)
    return ValidationRun(
        result=result,
        adopter_before=adopter_before,
        adopter_after=adopter_after,
        framework_before=framework_before,
        framework_after=framework_after,
        post_run_inventory=_adopter_inventory(adopter_after),
    )


def _assert_conformance_failure(result: subprocess.CompletedProcess[bytes]) -> None:
    assert result.returncode == 1
    assert result.stderr == b""
    assert result.stdout
    assert all(
        line.startswith(b"CONFORMANCE|") for line in result.stdout.splitlines()
    )
    assert b"Traceback" not in result.stdout
    assert b"E_INTERNAL" not in result.stdout


@pytest.mark.parametrize(
    "mutation",
    [
        "added-empty-directory",
        "added-symlink",
        "changed-symlink-target",
        "entry-type-change",
        "regular-file-content",
        "permission-mode",
        "modification-time",
    ],
)
def test_full_state_snapshot_detects_bounded_mutations(
    tmp_path: Path, mutation: str
) -> None:
    root = tmp_path / "snapshot-root"
    root.mkdir()
    subject = root / "entry"
    subject.write_text("before", encoding="utf-8")
    link = root / "link"
    if mutation == "changed-symlink-target":
        link.symlink_to("entry")

    before = _snapshot_roots((("self-check", root),))

    if mutation == "added-empty-directory":
        (root / "empty").mkdir()
    elif mutation == "added-symlink":
        link.symlink_to("entry")
    elif mutation == "changed-symlink-target":
        link.unlink()
        link.symlink_to("other")
    elif mutation == "entry-type-change":
        subject.unlink()
        subject.mkdir()
    elif mutation == "regular-file-content":
        subject.write_text("after", encoding="utf-8")
    elif mutation == "permission-mode":
        subject.chmod(stat.S_IMODE(subject.lstat().st_mode) ^ stat.S_IXUSR)
    elif mutation == "modification-time":
        metadata = subject.lstat()
        os.utime(
            subject,
            ns=(metadata.st_atime_ns, metadata.st_mtime_ns + 1_000_000_000),
            follow_symlinks=False,
        )
    else:
        raise AssertionError(f"unknown mutation {mutation!r}")

    after = _snapshot_roots((("self-check", root),))

    assert after != before
    if mutation == "added-empty-directory":
        assert after["self-check:empty"].entry_type == "directory"
    elif mutation == "added-symlink":
        assert after["self-check:link"].symlink_target == "entry"
    elif mutation == "changed-symlink-target":
        assert before["self-check:link"].symlink_target == "entry"
        assert after["self-check:link"].symlink_target == "other"
    elif mutation == "entry-type-change":
        assert before["self-check:entry"].entry_type == "regular-file"
        assert after["self-check:entry"].entry_type == "directory"
    elif mutation == "regular-file-content":
        assert before["self-check:entry"].sha256 != after["self-check:entry"].sha256
    elif mutation == "permission-mode":
        assert before["self-check:entry"].mode != after["self-check:entry"].mode
    elif mutation == "modification-time":
        assert (
            before["self-check:entry"].mtime_ns
            != after["self-check:entry"].mtime_ns
        )


def test_explicit_minimum_adopter_validates_from_a_clean_room(tmp_path: Path) -> None:
    adopter_root = (tmp_path / "adopter").resolve()
    external_cwd = (tmp_path / "outside-working-directory").resolve()
    external_cwd.mkdir()
    _write_adopter(adopter_root)

    _assert_minimum_local_inventory(adopter_root)
    run = _run_validator(adopter_root, external_cwd)

    assert run.result.returncode == 0
    assert run.result.stdout == b""
    assert run.result.stderr == b""


def test_controlled_clean_room_failures_are_deterministic(tmp_path: Path) -> None:
    external_cwd = (tmp_path / "outside-working-directory").resolve()
    external_cwd.mkdir()

    invalid_manifest = copy.deepcopy(MANIFEST)
    invalid_manifest["afef"]["version"] = ""
    invalid_manifest["afef"]["commit"] = "not-a-full-commit"
    pin_adopter = (tmp_path / "invalid-pin-adopter").resolve()
    _write_adopter(pin_adopter, manifest=invalid_manifest)

    invalid_work_record = copy.deepcopy(WORK_RECORD)
    invalid_work_record["related_specifications"] = ["SPEC-9999"]
    reference_adopter = (tmp_path / "invalid-reference-adopter").resolve()
    _write_adopter(reference_adopter, work_record=invalid_work_record)

    runs_by_scenario: dict[str, list[ValidationRun]] = {}
    for scenario, adopter_root in (
        ("pin", pin_adopter),
        ("reference", reference_adopter),
    ):
        _assert_minimum_local_inventory(adopter_root)
        runs = [_run_validator(adopter_root, external_cwd) for _ in range(8)]
        runs_by_scenario[scenario] = runs
        for run in runs:
            _assert_conformance_failure(run.result)
        assert {
            (run.result.returncode, run.result.stdout, run.result.stderr)
            for run in runs
        } == {
            (
                runs[0].result.returncode,
                runs[0].result.stdout,
                runs[0].result.stderr,
            )
        }

    pin_result = runs_by_scenario["pin"][0].result
    reference_result = runs_by_scenario["reference"][0].result
    assert b"E_SCHEMA_MINLENGTH" in pin_result.stdout
    assert b"E_SCHEMA_PATTERN" in pin_result.stdout
    assert b"E_WORK_SPECIFICATION_REFERENCE" in reference_result.stdout
    assert hashlib.sha256(pin_result.stdout).hexdigest() == PIN_DIAGNOSTIC_SHA256
    assert (
        hashlib.sha256(reference_result.stdout).hexdigest()
        == REFERENCE_DIAGNOSTIC_SHA256
    )


def test_validator_logic_retains_an_in_process_network_guard(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    adopter_root = (tmp_path / "adopter").resolve()
    _write_adopter(adopter_root)

    def forbidden_socket(*args: object, **kwargs: object) -> None:
        raise AssertionError("network access attempted")

    monkeypatch.setattr(socket, "socket", forbidden_socket)
    monkeypatch.setattr(sys, "dont_write_bytecode", True)

    import importlib.util

    module_spec = importlib.util.spec_from_file_location(
        "afef_clean_room_validator", VALIDATOR_PATH
    )
    assert module_spec is not None and module_spec.loader is not None
    validator = importlib.util.module_from_spec(module_spec)
    sys.modules[module_spec.name] = validator
    module_spec.loader.exec_module(validator)

    diagnostics, operational = validator.validate_project(adopter_root)

    assert diagnostics == []
    assert operational is False
