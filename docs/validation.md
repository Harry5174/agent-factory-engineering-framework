# AFEF v0.2.0 Minimum Adoption and Validation

This repository contains the schemas, templates, protocols, and one narrow,
offline validator for the three AFEF v0.2.0 adopter record categories. The
adopter owns every instantiated `.afef/` record, project fact, approval, and
evidence item. Framework templates are starting points only: copying and filling
one does not establish factual truth, approval, authorization, or completed
evidence.

## Minimum Adopter Records

A minimum adopter has exactly these integrated record instances:

1. one YAML project manifest at the sole normative location
   `.afef/project-manifest.yaml`;
2. one direct `.md` specification in the repository-relative directory named by
   `paths.specifications`; and
3. one direct `.yaml` work record in the repository-relative directory named by
   `paths.work_records`.

Discovery in both configured record directories is non-recursive. Start from the
three compact files in `docs/templates/`, replace every placeholder with
adopter-owned facts, and remove optional fields that do not add needed context.
Do not treat template prose or placeholder identities as approval or evidence.

The manifest records both the adopted version and immutable framework revision:

```yaml
afef:
  version: "0.2.0"
  commit: "<FULL_40_CHARACTER_AFEF_COMMIT>"
```

The validator requires a non-empty `afef.version` and a full 40-character
hexadecimal `afef.commit`. It checks the recorded pin's presence and shape; it
does not authenticate the pin or compare it with the currently checked-out AFEF
commit. The adopter must obtain and preserve the intended immutable revision
through its separately authorized provenance process.

## Running from Outside the Framework Repository

The already selected Python environment must contain the bounded packages in
`requirements-validation.txt`. Install or environment changes are a separate
setup action; do not perform them during a controlled evidence run.

Use the active Python interpreter, validator script, and adopter root as absolute
paths. Set the working directory to a location outside the AFEF repository. This
shell form also demonstrates that the validator subprocess does not require
`PATH`:

```text
cd /tmp
/usr/bin/env -i PYTHONDONTWRITEBYTECODE=1 \
  /absolute/path/to/python \
  /absolute/path/to/agent-factory-engineering-framework/tools/validate_afef.py \
  --project /absolute/path/to/adopter-project
```

The supported validator entry point is:

```text
<ABSOLUTE_PYTHON> <ABSOLUTE_AFEF_ROOT>/tools/validate_afef.py \
  --project <ABSOLUTE_ADOPTER_ROOT>
```

The validator begins only at
`<adopter-project-root>/.afef/project-manifest.yaml`. It does not search for an
alternate manifest. The manifest supplies the non-recursive specification and
work-record directories. Validation performs no network access and makes no
writes to the adopter project or this repository.

Configured manifest paths, constitution references, specification
`affected_paths`, and work-record authorization-envelope `affected_paths` must
use repository-style project-relative syntax and resolve within the supplied
project root. Affected paths need not exist. Permitted protected-effect
operations require a `high_assurance` risk profile as well as any exact
authorization binding. Specification supersession references must exist, be
reciprocal, mark predecessors as `superseded`, and form an acyclic graph.

## Diagnostics

Every diagnostic is one UTF-8 line:

```text
KIND|PROJECT_RELATIVE_PATH|CODE|DETAIL
```

`KIND` is `CONFORMANCE` for invalid adopter content and `OPERATIONAL` for a
validator failure. Paths always use project-relative `/` syntax; `.` identifies
the supplied root and `-` identifies command usage. `CODE` is a stable
machine-comparable identifier. `DETAIL` is a compact explanation. Before joining
the four fields with `|`, each field is UTF-8 percent-encoded using RFC 3986
unreserved characters plus `/` as the only unescaped characters. Delimiters,
percent signs, control characters, whitespace, and other characters are
therefore unambiguous and cannot create extra fields or lines.

Diagnostics are sorted by the unencoded tuple `(project-relative path, code,
detail, kind)`, which is the field order of the validator's immutable diagnostic
record, and then encoded. Repeated runs against unchanged input therefore
produce byte-identical output.
Conformance diagnostics are written to standard output. Usage and operational
diagnostics are written to standard error. Usage failures emit only the stable
detail `invalid command usage`; they do not echo supplied arguments. The
validator emits no timestamps, random values, workstation-absolute paths,
environment prefixes, or tracebacks.

## Exit Codes

| Code | Meaning |
|---:|---|
| `0` | The supplied adopter project conforms. |
| `1` | The project root or its AFEF records are invalid or nonconforming. |
| `2` | Command usage failed or the validator had an operational/internal failure. |

Schema validity and recorded relationships do not prove approval authenticity,
factual truth, production readiness, publication, or authorization outside the
records. Validation reports conformance only. It does not approve, authorize,
repair, rewrite, execute, publish, or release adopter work. Publication and every
external operation require separate authority.

This guide describes a minimum unreleased v0.2.0 design-candidate baseline and a
local clean-room conformance flow. It is not production-readiness evidence,
publication or release evidence, or proof of adoption by an actual project.
