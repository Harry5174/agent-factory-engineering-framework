#!/usr/bin/env python3
"""Deterministic, offline validation for AFEF v0.2.0 adopter records."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable
from urllib.parse import quote

import yaml
from jsonschema import Draft202012Validator, FormatChecker


MANIFEST_PATH = ".afef/project-manifest.yaml"
SCHEMA_DIRECTORY = Path(__file__).resolve().parents[1] / "schemas" / "v0.2"
SCHEMA_FILES = {
    "project-manifest": "project-manifest.schema.json",
    "specification": "specification.schema.json",
    "work-record": "work-record.schema.json",
}
EXPECTED_EXTENSIONS = {"specification": ".md", "work-record": ".yaml"}
PROTECTED_EFFECT_CLASSES = {
    "local-destructive",
    "external-write",
    "external-destructive",
    "identity-permission-change",
    "publication-release",
}
REPOSITORY_PATH_PATTERN = re.compile(
    r"^(?!/)(?![A-Za-z]:)(?!~(?:/|$))(?!.*(?:^|/)(?:\.|\.\.)(?:/|$))"
    r"(?!.*\\)(?!.*//)[^/\\]+(?:/[^/\\]+)*$"
)


@dataclass(frozen=True, order=True)
class Diagnostic:
    """One stable machine-comparable diagnostic."""

    path: str
    code: str
    detail: str
    kind: str = "CONFORMANCE"

    def render(self) -> str:
        fields = (self.kind, self.path, self.code, self.detail)
        return "|".join(quote(field, safe="/") for field in fields)


class DuplicateKeyError(yaml.YAMLError):
    """Raised when YAML contains a duplicate mapping key."""


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects duplicate mapping keys."""


def _construct_mapping(
    loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False
) -> dict[Any, Any]:
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in mapping
        except TypeError:
            raise yaml.constructor.ConstructorError(
                None, None, "found unhashable mapping key", key_node.start_mark
            ) from None
        if duplicate:
            raise DuplicateKeyError(f"duplicate mapping key {key!r}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping
)


class UsageError(Exception):
    """A deterministic command-line usage failure."""


class StableArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise UsageError


class OperationalFailure(Exception):
    def __init__(self, path: str, detail: str) -> None:
        super().__init__(detail)
        self.path = path
        self.detail = detail


def _project_relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return "."


def _json_location(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_diagnostics(
    record: Any,
    schema: dict[str, Any],
    record_path: str,
) -> list[Diagnostic]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    diagnostics: list[Diagnostic] = []
    for error in validator.iter_errors(record):
        location = _json_location(error.absolute_path)
        code = f"E_SCHEMA_{error.validator.upper()}"
        if error.validator == "required" and isinstance(error.instance, dict):
            missing = sorted(set(error.validator_value) - set(error.instance))
            detail = f"{location}: missing required properties {missing!r}"
        elif error.validator == "type":
            detail = f"{location}: value must have type {error.validator_value!r}"
        elif error.validator == "format":
            detail = f"{location}: value must satisfy format {error.validator_value!r}"
        else:
            detail = f"{location}: schema constraint {error.validator!r} failed"
        diagnostics.append(Diagnostic(record_path, code, detail))
    return diagnostics


def _load_yaml(path: Path, root: Path) -> tuple[Any | None, list[Diagnostic]]:
    display_path = _project_relative(path, root)
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise OperationalFailure(
            display_path, f"unable to read UTF-8 file ({type(error).__name__})"
        ) from None
    try:
        return yaml.load(text, Loader=UniqueKeyLoader), []
    except DuplicateKeyError:
        return None, [
            Diagnostic(display_path, "E_YAML_DUPLICATE_KEY", "duplicate mapping key")
        ]
    except yaml.YAMLError:
        return None, [
            Diagnostic(display_path, "E_YAML_PARSE", "malformed YAML content")
        ]


def _load_specification(
    path: Path, root: Path
) -> tuple[Any | None, list[Diagnostic]]:
    display_path = _project_relative(path, root)
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise OperationalFailure(
            display_path, f"unable to read UTF-8 file ({type(error).__name__})"
        ) from None
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return None, [
            Diagnostic(
                display_path,
                "E_FRONT_MATTER",
                "Markdown specification must begin with YAML front matter",
            )
        ]
    try:
        closing_index = lines[1:].index("---") + 1
    except ValueError:
        return None, [
            Diagnostic(
                display_path,
                "E_FRONT_MATTER",
                "Markdown specification front matter is not closed",
            )
        ]
    front_matter = "\n".join(lines[1:closing_index])
    try:
        return yaml.load(front_matter, Loader=UniqueKeyLoader), []
    except DuplicateKeyError:
        return None, [
            Diagnostic(display_path, "E_YAML_DUPLICATE_KEY", "duplicate mapping key")
        ]
    except yaml.YAMLError:
        return None, [
            Diagnostic(display_path, "E_YAML_PARSE", "malformed YAML front matter")
        ]


def _load_schemas() -> dict[str, dict[str, Any]]:
    schemas: dict[str, dict[str, Any]] = {}
    for category, filename in SCHEMA_FILES.items():
        path = SCHEMA_DIRECTORY / filename
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
        except Exception as error:
            raise OperationalFailure(
                ".",
                f"unable to load bundled {category} schema ({type(error).__name__})",
            ) from None
        schemas[category] = schema
    return schemas


def _is_repository_path(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    try:
        value.encode("utf-8", errors="strict")
    except UnicodeEncodeError:
        return False
    return "\x00" not in value and REPOSITORY_PATH_PATTERN.fullmatch(value) is not None


def _resolve_declared_path(
    root: Path, declared: Any, affected_path: str, field_name: str
) -> tuple[Path | None, list[Diagnostic]]:
    if not _is_repository_path(declared):
        return None, [
            Diagnostic(
                affected_path,
                "E_PATH_INVALID",
                f"{field_name} must use project-relative repository-style syntax",
            )
        ]
    candidate = root.joinpath(*PurePosixPath(declared).parts)
    try:
        resolved = candidate.resolve(strict=False)
    except OSError as error:
        raise OperationalFailure(
            affected_path, f"unable to resolve path ({type(error).__name__})"
        ) from None
    if not resolved.is_relative_to(root):
        return None, [
            Diagnostic(
                affected_path,
                "E_PATH_ESCAPE",
                f"{field_name} resolves outside the supplied project root",
            )
        ]
    return candidate, []


def _discover_records(
    root: Path,
    directory: Path,
    category: str,
) -> tuple[list[Path], list[Diagnostic]]:
    directory_path = _project_relative(directory, root)
    try:
        if not directory.exists() or not directory.is_dir():
            return [], [
                Diagnostic(
                    directory_path,
                    "E_RECORD_DIRECTORY_MISSING",
                    f"{category} directory does not exist",
                )
            ]
        entries = sorted(directory.iterdir(), key=lambda item: item.name)
    except OSError as error:
        raise OperationalFailure(
            directory_path,
            f"unable to inspect record directory ({type(error).__name__})",
        ) from None

    expected_extension = EXPECTED_EXTENSIONS[category]
    records: list[Path] = []
    diagnostics: list[Diagnostic] = []
    for entry in entries:
        try:
            if entry.is_dir():
                continue
            if not entry.is_file():
                continue
            resolved = entry.resolve(strict=False)
        except OSError as error:
            raise OperationalFailure(
                _project_relative(entry, root),
                f"unable to inspect record path ({type(error).__name__})",
            ) from None
        display_path = _project_relative(entry, root)
        if not resolved.is_relative_to(root):
            diagnostics.append(
                Diagnostic(
                    display_path,
                    "E_PATH_ESCAPE",
                    "record path resolves outside the supplied project root",
                )
            )
            continue
        if entry.suffix != expected_extension:
            diagnostics.append(
                Diagnostic(
                    display_path,
                    "E_RECORD_EXTENSION",
                    f"{category} records require {expected_extension}",
                )
            )
            continue
        records.append(entry)
    if not records:
        diagnostics.append(
            Diagnostic(
                directory_path,
                "E_RECORD_DIRECTORY_EMPTY",
                f"{category} directory contains no direct {expected_extension} records",
            )
        )
    return records, diagnostics


def _duplicates(
    records: list[tuple[str, dict[str, Any]]],
    field: str,
    code: str,
) -> list[Diagnostic]:
    by_value: dict[Any, list[str]] = {}
    for path, record in records:
        value = record.get(field)
        if isinstance(value, str):
            by_value.setdefault(value, []).append(path)
    diagnostics: list[Diagnostic] = []
    for value, paths in by_value.items():
        if len(paths) > 1:
            for path in paths:
                diagnostics.append(
                    Diagnostic(path, code, f"{field} {value!r} is not unique")
                )
    return diagnostics


def _validate_specification_relationships(
    specifications: list[tuple[str, dict[str, Any]]],
) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    by_id = {
        record["specification_id"]: (path, record)
        for path, record in specifications
        if isinstance(record.get("specification_id"), str)
    }
    graph: dict[str, set[str]] = {
        specification_id: set() for specification_id in sorted(by_id)
    }
    for path, record in specifications:
        current_id = record.get("specification_id")
        dependencies = record.get("dependencies", [])
        if isinstance(dependencies, list):
            for referenced_id in dependencies:
                if isinstance(referenced_id, str) and referenced_id not in by_id:
                    diagnostics.append(
                        Diagnostic(
                            path,
                            "E_SPECIFICATION_REFERENCE",
                            f"dependencies references unknown specification {referenced_id!r}",
                        )
                    )
        successor_id = record.get("superseded_by")
        if isinstance(successor_id, str) and successor_id not in by_id:
            diagnostics.append(
                Diagnostic(
                    path,
                    "E_SPECIFICATION_REFERENCE",
                    f"superseded_by references unknown specification {successor_id!r}",
                )
            )
        if (
            isinstance(successor_id, str)
            and isinstance(current_id, str)
            and successor_id in by_id
        ):
            graph[current_id].add(successor_id)
        if (
            isinstance(successor_id, str)
            and record.get("specification_status") != "superseded"
        ):
            diagnostics.append(
                Diagnostic(
                    path,
                    "E_SUPERSESSION",
                    "a specification naming superseded_by must have status 'superseded'",
                )
            )
        if record.get("specification_status") == "superseded" and not successor_id:
            diagnostics.append(
                Diagnostic(
                    path,
                    "E_SUPERSESSION",
                    "a superseded specification must name superseded_by",
                )
            )
        if isinstance(successor_id, str) and successor_id in by_id:
            successor = by_id[successor_id][1]
            if current_id not in successor.get("supersedes", []):
                diagnostics.append(
                    Diagnostic(
                        path,
                        "E_SUPERSESSION",
                        f"{successor_id!r} does not reciprocally name {current_id!r}",
                    )
                )
        predecessors = record.get("supersedes", [])
        if not isinstance(predecessors, list):
            continue
        for predecessor_id in predecessors:
            if not isinstance(predecessor_id, str):
                continue
            if predecessor_id not in by_id:
                diagnostics.append(
                    Diagnostic(
                        path,
                        "E_SPECIFICATION_REFERENCE",
                        f"supersedes references unknown specification {predecessor_id!r}",
                    )
                )
                continue
            if isinstance(current_id, str):
                graph[predecessor_id].add(current_id)
            predecessor = by_id[predecessor_id][1]
            if predecessor.get("specification_status") != "superseded":
                diagnostics.append(
                    Diagnostic(
                        path,
                        "E_SUPERSESSION",
                        f"predecessor {predecessor_id!r} must have status 'superseded'",
                    )
                )
            if predecessor.get("superseded_by") != current_id:
                diagnostics.append(
                    Diagnostic(
                        path,
                        "E_SUPERSESSION",
                        f"{predecessor_id!r} does not reciprocally name {current_id!r}",
                    )
                )

    visited: set[str] = set()
    finish_order: list[str] = []
    for starting_id in sorted(graph):
        if starting_id in visited:
            continue
        stack: list[tuple[str, bool]] = [(starting_id, False)]
        while stack:
            specification_id, expanded = stack.pop()
            if expanded:
                finish_order.append(specification_id)
                continue
            if specification_id in visited:
                continue
            visited.add(specification_id)
            stack.append((specification_id, True))
            for successor_id in reversed(sorted(graph[specification_id])):
                if successor_id not in visited:
                    stack.append((successor_id, False))

    reverse_graph: dict[str, set[str]] = {
        specification_id: set() for specification_id in graph
    }
    for predecessor_id in sorted(graph):
        for successor_id in sorted(graph[predecessor_id]):
            reverse_graph[successor_id].add(predecessor_id)

    assigned: set[str] = set()
    components: list[tuple[str, ...]] = []
    for starting_id in reversed(finish_order):
        if starting_id in assigned:
            continue
        component: list[str] = []
        stack = [starting_id]
        assigned.add(starting_id)
        while stack:
            specification_id = stack.pop()
            component.append(specification_id)
            for predecessor_id in reversed(sorted(reverse_graph[specification_id])):
                if predecessor_id not in assigned:
                    assigned.add(predecessor_id)
                    stack.append(predecessor_id)
        components.append(tuple(sorted(component)))
    for component in sorted(components):
        cyclic = len(component) > 1 or component[0] in graph[component[0]]
        if cyclic:
            path = by_id[component[0]][0]
            diagnostics.append(
                Diagnostic(
                    path,
                    "E_SUPERSESSION_CYCLE",
                    f"supersession cycle contains {list(component)!r}",
                )
            )
    return diagnostics


def _validate_actor_separation(path: str, record: dict[str, Any]) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    implementer = record.get("implementer")
    implementer_id = implementer.get("actor_id") if isinstance(implementer, dict) else None
    if not implementer_id:
        return diagnostics

    independent_review = record.get("independent_review")
    if isinstance(independent_review, dict):
        reviewer = independent_review.get("reviewer")
        reviewer_id = reviewer.get("actor_id") if isinstance(reviewer, dict) else None
        if reviewer_id == implementer_id:
            diagnostics.append(
                Diagnostic(
                    path,
                    "E_ACTOR_SEPARATION",
                    "independent reviewer actor_id equals implementer actor_id",
                )
            )

    final_gate = record.get("final_gate")
    if isinstance(final_gate, dict):
        owner = final_gate.get("owner")
        owner_id = owner.get("actor_id") if isinstance(owner, dict) else None
        if owner_id == implementer_id:
            diagnostics.append(
                Diagnostic(
                    path,
                    "E_ACTOR_SEPARATION",
                    "final-gate owner actor_id equals implementer actor_id",
                )
            )

    for review in record.get("reviews", []):
        if not isinstance(review, dict):
            continue
        if review.get("status") != "completed":
            continue
        reviewer = review.get("reviewer")
        reviewer_id = reviewer.get("actor_id") if isinstance(reviewer, dict) else None
        if reviewer_id == implementer_id:
            review_id = review.get("review_id", "<unknown>")
            diagnostics.append(
                Diagnostic(
                    path,
                    "E_ACTOR_SEPARATION",
                    f"review {review_id!r} reviewer actor_id equals implementer actor_id",
                )
            )
    return diagnostics


def _validate_authorization(path: str, record: dict[str, Any]) -> list[Diagnostic]:
    envelope = record.get("authorization_envelope")
    if not isinstance(envelope, dict):
        return []
    operations = envelope.get("operations")
    references = envelope.get("authorization_references", [])
    if not isinstance(operations, list) or not isinstance(references, list):
        return []

    diagnostics: list[Diagnostic] = []
    if record.get("risk_profile") != "high_assurance" and any(
        isinstance(operation, dict)
        and operation.get("decision") == "permitted"
        and operation.get("effect_class") in PROTECTED_EFFECT_CLASSES
        for operation in operations
    ):
        diagnostics.append(
            Diagnostic(
                path,
                "E_RISK_PROFILE_ESCALATION",
                "permitted protected operations require risk_profile 'high_assurance'",
            )
        )
    operation_ids: dict[Any, list[dict[str, Any]]] = {}
    for operation in operations:
        operation_id = operation.get("operation_id") if isinstance(operation, dict) else None
        if isinstance(operation_id, str):
            operation_ids.setdefault(operation_id, []).append(operation)
    for operation_id, matching in operation_ids.items():
        if operation_id is not None and len(matching) > 1:
            decisions = sorted(
                {
                    operation.get("decision")
                    for operation in matching
                    if isinstance(operation.get("decision"), str)
                }
            )
            detail = f"operation_id {operation_id!r} is not unique"
            if len(decisions) > 1:
                detail += " and has contradictory decisions"
            diagnostics.append(Diagnostic(path, "E_OPERATION_ID", detail))

    authorization_ids: dict[Any, int] = {}
    bound_operation_ids: set[Any] = set()
    known_operation_ids = set(operation_ids)
    for reference in references:
        if not isinstance(reference, dict):
            continue
        authorization_id = reference.get("authorization_id")
        if isinstance(authorization_id, str):
            authorization_ids[authorization_id] = (
                authorization_ids.get(authorization_id, 0) + 1
            )
        bound_ids = reference.get("operation_ids", [])
        if not isinstance(bound_ids, list):
            continue
        for operation_id in bound_ids:
            if not isinstance(operation_id, str):
                continue
            if operation_id not in known_operation_ids:
                diagnostics.append(
                    Diagnostic(
                        path,
                        "E_AUTHORIZATION_BINDING",
                        f"authorization {authorization_id!r} binds unknown operation {operation_id!r}",
                    )
                )
            else:
                bound_operation_ids.add(operation_id)
    for authorization_id, count in authorization_ids.items():
        if authorization_id is not None and count > 1:
            diagnostics.append(
                Diagnostic(
                    path,
                    "E_AUTHORIZATION_ID",
                    f"authorization_id {authorization_id!r} is not unique",
                )
            )

    for operation_id, matching in operation_ids.items():
        if operation_id is None:
            continue
        for operation in matching:
            requires_reference = (
                operation.get("decision") == "permitted"
                and (
                    operation.get("authorization_requirement") == "separate_reference"
                    or operation.get("effect_class") in PROTECTED_EFFECT_CLASSES
                )
            )
            if requires_reference and operation_id not in bound_operation_ids:
                diagnostics.append(
                    Diagnostic(
                        path,
                        "E_AUTHORIZATION_BINDING",
                        f"permitted operation {operation_id!r} requires an exact authorization binding",
                    )
                )
                break
    return diagnostics


def _validate_work_relationships(
    work_records: list[tuple[str, dict[str, Any]]],
    specification_ids: set[str],
) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    for path, record in work_records:
        related = record.get("related_specifications", [])
        if isinstance(related, list):
            for specification_id in related:
                if (
                    isinstance(specification_id, str)
                    and specification_id not in specification_ids
                ):
                    diagnostics.append(
                        Diagnostic(
                            path,
                            "E_WORK_SPECIFICATION_REFERENCE",
                            f"related_specifications references unknown specification {specification_id!r}",
                        )
                    )
        diagnostics.extend(_validate_authorization(path, record))
        diagnostics.extend(_validate_actor_separation(path, record))
    return diagnostics


def _validate_affected_paths(
    root: Path,
    record_path: str,
    values: Any,
    field_name: str,
) -> list[Diagnostic]:
    if not isinstance(values, list):
        return []
    diagnostics: list[Diagnostic] = []
    for index, declared in enumerate(values):
        _, path_diagnostics = _resolve_declared_path(
            root,
            declared,
            record_path,
            f"{field_name}[{index}]",
        )
        diagnostics.extend(path_diagnostics)
    return diagnostics


def validate_project(project_root: Path) -> tuple[list[Diagnostic], bool]:
    """Return diagnostics and whether an operational failure occurred."""

    diagnostics: list[Diagnostic] = []
    try:
        root = project_root.resolve(strict=False)
        if not root.exists() or not root.is_dir():
            return [
                Diagnostic(
                    ".",
                    "E_PROJECT_ROOT",
                    "supplied project root does not exist or is not a directory",
                )
            ], False

        schemas = _load_schemas()
        manifest_file = root / MANIFEST_PATH
        if not manifest_file.exists() or not manifest_file.is_file():
            return [
                Diagnostic(
                    MANIFEST_PATH,
                    "E_MANIFEST_MISSING",
                    "normative project manifest is missing",
                )
            ], False
        try:
            manifest_resolved = manifest_file.resolve(strict=True)
        except OSError as error:
            raise OperationalFailure(
                MANIFEST_PATH,
                f"unable to resolve normative manifest ({type(error).__name__})",
            ) from None
        if not manifest_resolved.is_relative_to(root):
            return [
                Diagnostic(
                    MANIFEST_PATH,
                    "E_PATH_ESCAPE",
                    "normative manifest resolves outside the supplied project root",
                )
            ], False

        manifest, parse_diagnostics = _load_yaml(manifest_file, root)
        diagnostics.extend(parse_diagnostics)
        if not isinstance(manifest, dict):
            if manifest is not None:
                diagnostics.extend(
                    _schema_diagnostics(manifest, schemas["project-manifest"], MANIFEST_PATH)
                )
            return sorted(diagnostics), False

        diagnostics.extend(
            _schema_diagnostics(manifest, schemas["project-manifest"], MANIFEST_PATH)
        )

        constitution = manifest.get("constitution")
        if isinstance(constitution, dict) and "reference" in constitution:
            constitution_path, path_diagnostics = _resolve_declared_path(
                root,
                constitution["reference"],
                MANIFEST_PATH,
                "constitution.reference",
            )
            diagnostics.extend(path_diagnostics)
            if constitution_path is not None and (
                not constitution_path.exists() or not constitution_path.is_file()
            ):
                diagnostics.append(
                    Diagnostic(
                        constitution["reference"],
                        "E_CONSTITUTION_MISSING",
                        "declared constitution reference does not exist",
                    )
                )

        paths = manifest.get("paths")
        if not isinstance(paths, dict):
            return sorted(diagnostics), False

        resolved_directories: dict[str, Path] = {}
        record_fields = {
            "specifications": "specification",
            "work_records": "work-record",
        }
        configured_path_fields = (
            "architecture",
            "decisions",
            "documentation",
            "evidence",
            "source",
            "specifications",
            "tests",
            "work_records",
        )
        for field in configured_path_fields:
            if field not in paths:
                continue
            directory, path_diagnostics = _resolve_declared_path(
                root, paths[field], MANIFEST_PATH, f"paths.{field}"
            )
            diagnostics.extend(path_diagnostics)
            category = record_fields.get(field)
            if category is not None and directory is not None:
                resolved_directories[category] = directory

        if len(resolved_directories) == 2:
            spec_dir = resolved_directories["specification"].resolve(strict=False)
            work_dir = resolved_directories["work-record"].resolve(strict=False)
            if spec_dir == work_dir:
                diagnostics.append(
                    Diagnostic(
                        MANIFEST_PATH,
                        "E_RECORD_DIRECTORY_DUPLICATE",
                        "specification and work-record directories resolve to the same location",
                    )
                )
            elif spec_dir.is_relative_to(work_dir) or work_dir.is_relative_to(spec_dir):
                diagnostics.append(
                    Diagnostic(
                        MANIFEST_PATH,
                        "E_RECORD_DIRECTORY_OVERLAP",
                        "specification and work-record directories overlap",
                    )
                )

        loaded_records: dict[str, list[tuple[str, dict[str, Any]]]] = {
            "specification": [],
            "work-record": [],
        }
        for category in ("specification", "work-record"):
            directory = resolved_directories.get(category)
            if directory is None:
                continue
            record_paths, discovery_diagnostics = _discover_records(
                root, directory, category
            )
            diagnostics.extend(discovery_diagnostics)
            for record_file in record_paths:
                if category == "specification":
                    record, record_diagnostics = _load_specification(record_file, root)
                else:
                    record, record_diagnostics = _load_yaml(record_file, root)
                diagnostics.extend(record_diagnostics)
                if record is None:
                    continue
                display_path = _project_relative(record_file, root)
                diagnostics.extend(
                    _schema_diagnostics(record, schemas[category], display_path)
                )
                if isinstance(record, dict):
                    loaded_records[category].append((display_path, record))

        specifications = loaded_records["specification"]
        work_records = loaded_records["work-record"]
        diagnostics.extend(
            _duplicates(
                specifications,
                "specification_id",
                "E_DUPLICATE_SPECIFICATION_ID",
            )
        )
        diagnostics.extend(_duplicates(work_records, "work_id", "E_DUPLICATE_WORK_ID"))
        for path, record in specifications:
            diagnostics.extend(
                _validate_affected_paths(
                    root,
                    path,
                    record.get("affected_paths", []),
                    "affected_paths",
                )
            )
        for path, record in work_records:
            envelope = record.get("authorization_envelope")
            if isinstance(envelope, dict):
                diagnostics.extend(
                    _validate_affected_paths(
                        root,
                        path,
                        envelope.get("affected_paths", []),
                        "authorization_envelope.affected_paths",
                    )
                )
        diagnostics.extend(_validate_specification_relationships(specifications))
        specification_ids = {
            record["specification_id"]
            for _, record in specifications
            if isinstance(record.get("specification_id"), str)
        }
        diagnostics.extend(
            _validate_work_relationships(work_records, specification_ids)
        )
        return sorted(set(diagnostics)), False
    except OperationalFailure as error:
        return [
            Diagnostic(error.path, "E_OPERATIONAL", error.detail, kind="OPERATIONAL")
        ], True
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception as error:
        return [
            Diagnostic(
                ".",
                "E_INTERNAL",
                f"unexpected validator failure ({type(error).__name__})",
                kind="OPERATIONAL",
            )
        ], True


def _parser() -> StableArgumentParser:
    parser = StableArgumentParser(
        prog="afef-validate",
        description="Validate AFEF v0.2.0 adopter records offline.",
        add_help=True,
    )
    parser.add_argument("--project", required=True, type=Path, help="adopter project root")
    return parser


def main(argv: list[str] | None = None) -> int:
    try:
        arguments = _parser().parse_args(argv)
    except UsageError:
        print(
            Diagnostic(
                "-", "E_USAGE", "invalid command usage", kind="OPERATIONAL"
            ).render(),
            file=sys.stderr,
        )
        return 2

    diagnostics, operational_failure = validate_project(arguments.project)
    output = sys.stderr if operational_failure else sys.stdout
    for diagnostic in diagnostics:
        print(diagnostic.render(), file=output)
    if operational_failure:
        return 2
    return 1 if diagnostics else 0


if __name__ == "__main__":
    sys.exit(main())
