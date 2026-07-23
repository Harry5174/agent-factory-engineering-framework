# AFEF v0.2.0 Adopter Validation

This repository contains one narrow, offline validator for the three AFEF v0.2.0
adopter record categories. Install the bounded dependencies and run it from the
AFEF repository root:

```text
python -m pip install -r requirements-validation.txt
python tools/validate_afef.py --project <adopter-project-root>
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
records.
