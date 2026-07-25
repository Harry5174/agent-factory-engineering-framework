from __future__ import annotations

import copy
import hashlib
import socket
import subprocess
import sys
from pathlib import Path

import pytest
import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = (REPOSITORY_ROOT / "tools" / "validate_afef.py").resolve()
FRAMEWORK_INPUTS = (
    VALIDATOR_PATH,
    *(sorted((REPOSITORY_ROOT / "schemas" / "v0.2").glob("*.schema.json"))),
)
ADOPTED_AFEF_COMMIT = "02e231276f5a642d486c8035bceaee61dbfc3500"
PIN_DIAGNOSTIC_SHA256 = (
    "070d40c5a4b074336dbf7d564bd091f7478e1ffbc58465a8246bbfa817f886d0"
)
REFERENCE_DIAGNOSTIC_SHA256 = (
    "23229e2c6673ac80297f83346d76a560217c5a8856b6a75ff390cd857c6a4377"
)
EXPECTED_ADOPTER_FILES = {
    ".afef/project-manifest.yaml",
    ".afef/specifications/spec-0001.md",
    ".afef/work-records/work-0001.yaml",
}

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


def _file_hashes(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def _framework_hashes() -> dict[str, str]:
    return {
        path.relative_to(REPOSITORY_ROOT).as_posix(): hashlib.sha256(
            path.read_bytes()
        ).hexdigest()
        for path in FRAMEWORK_INPUTS
    }


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


def _assert_minimum_local_inventory(adopter_root: Path) -> None:
    assert _file_hashes(adopter_root).keys() == EXPECTED_ADOPTER_FILES
    assert not (adopter_root / ".git").exists()
    assert not (adopter_root / ".github").exists()
    assert not (adopter_root / ".env").exists()
    forbidden_names = {"credentials", "secrets", "remote", "external-service"}
    assert not any(
        part.lower() in forbidden_names
        for path in adopter_root.rglob("*")
        for part in path.relative_to(adopter_root).parts
    )


def _run_validator(
    adopter_root: Path, external_cwd: Path
) -> subprocess.CompletedProcess[bytes]:
    absolute_python = Path(sys.executable)
    absolute_adopter = adopter_root.resolve()
    child_environment = {"PYTHONDONTWRITEBYTECODE": "1"}

    assert absolute_python.is_absolute()
    assert VALIDATOR_PATH.is_absolute()
    assert absolute_adopter.is_absolute()
    assert not _is_within(absolute_adopter, REPOSITORY_ROOT)
    assert not _is_within(external_cwd, REPOSITORY_ROOT)
    assert "PATH" not in child_environment

    adopter_before = _file_hashes(adopter_root)
    framework_before = _framework_hashes()
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
    assert _file_hashes(adopter_root) == adopter_before
    assert _framework_hashes() == framework_before
    return result


def _assert_conformance_failure(result: subprocess.CompletedProcess[bytes]) -> None:
    assert result.returncode == 1
    assert result.stderr == b""
    assert result.stdout
    assert all(
        line.startswith(b"CONFORMANCE|") for line in result.stdout.splitlines()
    )
    assert b"Traceback" not in result.stdout
    assert b"E_INTERNAL" not in result.stdout


def test_explicit_minimum_adopter_validates_from_a_clean_room(tmp_path: Path) -> None:
    adopter_root = (tmp_path / "adopter").resolve()
    external_cwd = (tmp_path / "outside-working-directory").resolve()
    external_cwd.mkdir()
    _write_adopter(adopter_root)

    _assert_minimum_local_inventory(adopter_root)
    result = _run_validator(adopter_root, external_cwd)

    assert result.returncode == 0
    assert result.stdout == b""
    assert result.stderr == b""


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

    for adopter_root in (pin_adopter, reference_adopter):
        _assert_minimum_local_inventory(adopter_root)
        results = [_run_validator(adopter_root, external_cwd) for _ in range(8)]
        for result in results:
            _assert_conformance_failure(result)
        assert {
            (result.returncode, result.stdout, result.stderr) for result in results
        } == {(results[0].returncode, results[0].stdout, results[0].stderr)}

    pin_result = _run_validator(pin_adopter, external_cwd)
    reference_result = _run_validator(reference_adopter, external_cwd)
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
