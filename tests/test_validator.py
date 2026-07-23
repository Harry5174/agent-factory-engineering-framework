from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import shutil
import socket
import subprocess
import sys
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPOSITORY_ROOT / "tools" / "validate_afef.py"
FIXTURES = Path(__file__).parent / "fixtures"
SCHEMAS = REPOSITORY_ROOT / "schemas" / "v0.2"

MODULE_SPEC = importlib.util.spec_from_file_location("afef_validator", VALIDATOR_PATH)
assert MODULE_SPEC is not None and MODULE_SPEC.loader is not None
validator = importlib.util.module_from_spec(MODULE_SPEC)
sys.modules[MODULE_SPEC.name] = validator
MODULE_SPEC.loader.exec_module(validator)


def run_validator(project: Path, *extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(VALIDATOR_PATH),
            "--project",
            str(project),
            *extra,
        ],
        cwd=REPOSITORY_ROOT,
        text=True,
        capture_output=True,
        check=False,
        env={**os.environ, "PYTHONHASHSEED": "random"},
    )


def copy_fixture(name: str, destination: Path) -> Path:
    project = destination / name
    shutil.copytree(FIXTURES / name, project)
    return project


def load_manifest(project: Path) -> dict:
    path = project / ".afef" / "project-manifest.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def write_manifest(project: Path, manifest: dict) -> None:
    path = project / ".afef" / "project-manifest.yaml"
    path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")


def file_snapshot(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


@pytest.mark.parametrize(
    ("fixture", "expected_code"),
    [
        ("valid", 0),
        ("missing-manifest", 1),
        ("malformed-manifest", 1),
        ("schema-invalid-manifest", 1),
        ("schema-invalid-specification", 1),
        ("schema-invalid-work-record", 1),
        ("escaping-path", 1),
        ("missing-record-directory", 1),
        ("reference-mismatch", 1),
        ("multiple-historical", 0),
        ("concurrent-active", 0),
        ("multiple-diagnostics", 1),
    ],
)
def test_every_static_fixture(fixture: str, expected_code: int) -> None:
    result = run_validator(FIXTURES / fixture)

    assert result.returncode == expected_code
    assert "Traceback" not in result.stdout
    assert "Traceback" not in result.stderr


def test_all_three_schemas_are_draft_2020_12_valid() -> None:
    schema_files = sorted(SCHEMAS.glob("*.schema.json"))

    assert [path.name for path in schema_files] == [
        "project-manifest.schema.json",
        "specification.schema.json",
        "work-record.schema.json",
    ]
    for path in schema_files:
        schema = json.loads(path.read_text(encoding="utf-8"))
        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        Draft202012Validator.check_schema(schema)


def test_schema_invalid_fixtures_report_expected_category() -> None:
    expected = {
        "schema-invalid-manifest": ".afef/project-manifest.yaml",
        "schema-invalid-specification": ".afef/specifications/invalid.md",
        "schema-invalid-work-record": ".afef/work-records/invalid.yaml",
    }

    for fixture, path in expected.items():
        result = run_validator(FIXTURES / fixture)
        assert result.returncode == 1
        assert f"CONFORMANCE|{path}|E_SCHEMA_" in result.stdout


def test_non_hashable_schema_invalid_values_remain_conformance_failures(
    tmp_path: Path,
) -> None:
    project = copy_fixture("valid", tmp_path)
    specification = project / ".afef" / "specifications" / "spec-0001.md"
    specification.write_text(
        specification.read_text(encoding="utf-8").replace(
            'specification_id: "SPEC-0001"', "specification_id:\n  - invalid"
        ),
        encoding="utf-8",
    )
    work_record = project / ".afef" / "work-records" / "work-0001.yaml"
    work_record.write_text(
        work_record.read_text(encoding="utf-8").replace(
            'work_id: "WORK-0001"', "work_id:\n  nested: invalid"
        ),
        encoding="utf-8",
    )

    result = run_validator(project)

    assert result.returncode == 1
    assert "E_SCHEMA_TYPE" in result.stdout
    assert result.stderr == ""
    assert "Traceback" not in result.stdout


def test_malformed_yaml_keys_remain_conformance_failures(tmp_path: Path) -> None:
    project = copy_fixture("valid", tmp_path)
    manifest = project / ".afef" / "project-manifest.yaml"
    manifest.write_text("? [invalid, key]\n: value\n", encoding="utf-8")

    result = run_validator(project)

    assert result.returncode == 1
    assert "E_YAML_PARSE" in result.stdout
    assert result.stderr == ""
    assert "Traceback" not in result.stdout


def test_manifest_discovery_is_normative_nonrecursive_and_not_configurable() -> None:
    result = run_validator(FIXTURES / "missing-manifest")
    unsupported_option = subprocess.run(
        [
            sys.executable,
            str(VALIDATOR_PATH),
            "--manifest",
            ".afef/nested/project-manifest.yaml",
        ],
        cwd=REPOSITORY_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 1
    assert result.stdout.splitlines() == [
        "CONFORMANCE|.afef/project-manifest.yaml|E_MANIFEST_MISSING|"
        "normative project manifest is missing"
    ]
    assert unsupported_option.returncode == 2
    assert unsupported_option.stderr.startswith("OPERATIONAL|-|E_USAGE|")


def test_nested_record_directories_are_not_traversed() -> None:
    result = run_validator(FIXTURES / "valid")

    assert result.returncode == 0
    assert result.stdout == ""
    assert result.stderr == ""


def test_project_relative_and_absolute_declared_paths_are_rejected(
    tmp_path: Path,
) -> None:
    escaping = run_validator(FIXTURES / "escaping-path")
    project = copy_fixture("valid", tmp_path)
    manifest = load_manifest(project)
    manifest["paths"]["specifications"] = "/absolute/specifications"
    write_manifest(project, manifest)
    absolute = run_validator(project)

    assert escaping.returncode == 1
    assert "E_PATH_INVALID" in escaping.stdout
    assert absolute.returncode == 1
    assert "E_PATH_INVALID" in absolute.stdout
    assert "/absolute/specifications" not in absolute.stdout
    assert str(tmp_path) not in absolute.stdout


def test_symlink_escape_is_rejected(tmp_path: Path) -> None:
    project = copy_fixture("valid", tmp_path)
    outside = tmp_path / "outside"
    outside.mkdir()
    shutil.rmtree(project / ".afef" / "specifications")
    (project / ".afef" / "specifications").symlink_to(outside, target_is_directory=True)

    result = run_validator(project)

    assert result.returncode == 1
    assert "E_PATH_ESCAPE" in result.stdout
    assert str(tmp_path) not in result.stdout


def test_normative_manifest_symlink_escape_is_rejected(tmp_path: Path) -> None:
    project = copy_fixture("valid", tmp_path / "project")
    outside_manifest = tmp_path / "outside-manifest.yaml"
    manifest_path = project / ".afef" / "project-manifest.yaml"
    shutil.copyfile(manifest_path, outside_manifest)
    manifest_path.unlink()
    manifest_path.symlink_to(outside_manifest)

    result = run_validator(project)

    assert result.returncode == 1
    assert "E_PATH_ESCAPE" in result.stdout
    assert str(tmp_path) not in result.stdout


def test_missing_empty_duplicate_overlapping_and_unsupported_directories(
    tmp_path: Path,
) -> None:
    missing = run_validator(FIXTURES / "missing-record-directory")

    empty_project = copy_fixture("valid", tmp_path / "empty")
    for child in (empty_project / ".afef" / "work-records").iterdir():
        child.unlink()
    empty = run_validator(empty_project)

    unsupported_project = copy_fixture("valid", tmp_path / "unsupported")
    (unsupported_project / ".afef" / "specifications" / "notes.txt").write_text(
        "unsupported", encoding="utf-8"
    )
    unsupported = run_validator(unsupported_project)

    duplicate_project = copy_fixture("valid", tmp_path / "duplicate")
    manifest = load_manifest(duplicate_project)
    manifest["paths"]["work_records"] = manifest["paths"]["specifications"]
    write_manifest(duplicate_project, manifest)
    duplicate = run_validator(duplicate_project)

    overlap_project = copy_fixture("valid", tmp_path / "overlap")
    manifest = load_manifest(overlap_project)
    manifest["paths"]["work_records"] = ".afef"
    write_manifest(overlap_project, manifest)
    overlap = run_validator(overlap_project)

    assert "E_RECORD_DIRECTORY_MISSING" in missing.stdout
    assert "E_RECORD_DIRECTORY_EMPTY" in empty.stdout
    assert "E_RECORD_EXTENSION" in unsupported.stdout
    assert "E_RECORD_DIRECTORY_DUPLICATE" in duplicate.stdout
    assert "E_RECORD_DIRECTORY_OVERLAP" in overlap.stdout


def test_constitution_reference_must_resolve_inside_project(tmp_path: Path) -> None:
    project = copy_fixture("valid", tmp_path)
    manifest = load_manifest(project)
    manifest["constitution"] = {"reference": "governance/constitution.md"}
    write_manifest(project, manifest)

    missing = run_validator(project)
    constitution = project / "governance" / "constitution.md"
    constitution.parent.mkdir()
    constitution.write_text("# Fictional constitution\n", encoding="utf-8")
    present = run_validator(project)

    assert missing.returncode == 1
    assert "E_CONSTITUTION_MISSING" in missing.stdout
    assert present.returncode == 0


def test_duplicate_record_id_and_supersession_relationships(tmp_path: Path) -> None:
    duplicate_project = copy_fixture("valid", tmp_path / "duplicate")
    original = duplicate_project / ".afef" / "specifications" / "spec-0001.md"
    shutil.copyfile(original, original.with_name("spec-duplicate.md"))
    duplicate = run_validator(duplicate_project)

    supersession_project = copy_fixture("multiple-historical", tmp_path / "supersession")
    successor = supersession_project / ".afef" / "specifications" / "spec-0002.md"
    successor.write_text(
        successor.read_text(encoding="utf-8").replace(
            'supersedes:\n  - "SPEC-0001"', "supersedes: []"
        ),
        encoding="utf-8",
    )
    supersession = run_validator(supersession_project)

    assert duplicate.stdout.count("E_DUPLICATE_SPECIFICATION_ID") == 2
    assert "E_SUPERSESSION" in supersession.stdout


def test_duplicate_work_ids_and_unknown_specification_dependencies(
    tmp_path: Path,
) -> None:
    project = copy_fixture("valid", tmp_path)
    work = project / ".afef" / "work-records" / "work-0001.yaml"
    shutil.copyfile(work, work.with_name("work-duplicate.yaml"))
    specification = project / ".afef" / "specifications" / "spec-0001.md"
    specification.write_text(
        specification.read_text(encoding="utf-8").replace(
            "dependencies: []", 'dependencies:\n  - "SPEC-9999"'
        ),
        encoding="utf-8",
    )

    result = run_validator(project)

    assert result.returncode == 1
    assert result.stdout.count("E_DUPLICATE_WORK_ID") == 2
    assert "E_SPECIFICATION_REFERENCE" in result.stdout


def test_work_references_authorization_keys_and_actor_separation() -> None:
    mismatch = run_validator(FIXTURES / "reference-mismatch")
    multiple = run_validator(FIXTURES / "multiple-diagnostics")

    assert "E_WORK_SPECIFICATION_REFERENCE" in mismatch.stdout
    assert "E_OPERATION_ID" in multiple.stdout
    assert multiple.stdout.count("E_AUTHORIZATION_BINDING") == 2
    assert multiple.stdout.count("E_ACTOR_SEPARATION") == 2


def test_authorization_id_uniqueness_and_independent_reviewer_separation(
    tmp_path: Path,
) -> None:
    project = copy_fixture("valid", tmp_path)
    work_path = project / ".afef" / "work-records" / "work-0001.yaml"
    work = yaml.safe_load(work_path.read_text(encoding="utf-8"))
    work["risk_profile"] = "high_assurance"
    work["authorization_envelope"]["authorization_references"] = [
        {
            "authorization_id": "AUTH-DUPLICATE",
            "reference": "fictional-reference-one",
            "operation_ids": ["OP-READ"],
        },
        {
            "authorization_id": "AUTH-DUPLICATE",
            "reference": "fictional-reference-two",
            "operation_ids": ["OP-READ"],
        },
    ]
    work["independent_review"] = {
        "status": "accepted",
        "reviewer": {
            "actor_id": "fixture-implementer",
            "role": "independent_reviewer",
        },
        "evidence_reference": "evidence/fictional-review.md",
        "reviewed_at": "2026-01-01T00:00:00Z",
    }
    work_path.write_text(yaml.safe_dump(work, sort_keys=False), encoding="utf-8")

    result = run_validator(project)

    assert result.returncode == 1
    assert "E_AUTHORIZATION_ID" in result.stdout
    assert "independent reviewer actor_id equals implementer actor_id" in result.stdout


def test_manifest_afef_pins_obey_accepted_schema_formats(tmp_path: Path) -> None:
    project = copy_fixture("valid", tmp_path)
    manifest = load_manifest(project)
    manifest["afef"]["version"] = ""
    manifest["afef"]["commit"] = "short"
    write_manifest(project, manifest)

    result = run_validator(project)

    assert result.returncode == 1
    assert "E_SCHEMA_MINLENGTH" in result.stdout
    assert "E_SCHEMA_PATTERN" in result.stdout


def test_multiple_historical_and_concurrent_active_records_are_accepted() -> None:
    historical = run_validator(FIXTURES / "multiple-historical")
    concurrent = run_validator(FIXTURES / "concurrent-active")

    assert historical.returncode == 0
    assert concurrent.returncode == 0


def test_diagnostics_are_sorted_and_repeated_output_is_byte_identical() -> None:
    first = run_validator(FIXTURES / "multiple-diagnostics")
    second = run_validator(FIXTURES / "multiple-diagnostics")
    lines = first.stdout.splitlines()

    assert first.returncode == second.returncode == 1
    assert first.stdout.encode() == second.stdout.encode()
    assert first.stderr.encode() == second.stderr.encode()
    assert lines == sorted(
        lines,
        key=lambda line: (
            line.split("|", 3)[1],
            line.split("|", 3)[2],
            line.split("|", 3)[3],
            line.split("|", 3)[0],
        ),
    )


def test_exit_codes_and_no_traceback_for_expected_invalid_input() -> None:
    valid = run_validator(FIXTURES / "valid")
    invalid = run_validator(FIXTURES / "malformed-manifest")
    usage = subprocess.run(
        [sys.executable, str(VALIDATOR_PATH)],
        cwd=REPOSITORY_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert valid.returncode == 0
    assert invalid.returncode == 1
    assert usage.returncode == 2
    assert usage.stderr.startswith("OPERATIONAL|-|E_USAGE|")
    assert "Traceback" not in invalid.stdout + invalid.stderr + usage.stderr


def test_operational_failure_uses_exit_two_without_traceback(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    def fail_to_load_schemas() -> None:
        raise validator.OperationalFailure(".", "fictional schema read failure")

    monkeypatch.setattr(validator, "_load_schemas", fail_to_load_schemas)

    result = validator.main(["--project", str(FIXTURES / "valid")])
    captured = capsys.readouterr()

    assert result == 2
    assert captured.out == ""
    assert captured.err == (
        "OPERATIONAL|.|E_OPERATIONAL|fictional schema read failure\n"
    )
    assert "Traceback" not in captured.err


def test_validation_does_not_mutate_target_fixture() -> None:
    project = FIXTURES / "multiple-diagnostics"
    before = file_snapshot(project)

    result = run_validator(project)

    assert result.returncode == 1
    assert file_snapshot(project) == before


def test_validation_performs_no_network_access(monkeypatch: pytest.MonkeyPatch) -> None:
    def forbidden_socket(*args: object, **kwargs: object) -> None:
        raise AssertionError("network access attempted")

    monkeypatch.setattr(socket, "socket", forbidden_socket)

    diagnostics, operational = validator.validate_project(FIXTURES / "valid")

    assert diagnostics == []
    assert operational is False


def test_documented_command_line_invocation() -> None:
    documentation = (REPOSITORY_ROOT / "docs" / "validation.md").read_text(
        encoding="utf-8"
    )
    result = subprocess.run(
        ["python", "tools/validate_afef.py", "--project", "tests/fixtures/valid"],
        cwd=REPOSITORY_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert "python tools/validate_afef.py --project <adopter-project-root>" in documentation
    assert result.returncode == 0
    assert result.stdout == ""
    assert result.stderr == ""
