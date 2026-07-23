---
target_version: 0.2.0
status: unreleased_design_candidate
release_authority: not_established_by_this_document
---

# AFEF v0.2.0 Minimum-Adoption Specification

This document is an unreleased design candidate. It does not establish that AFEF
v0.2.0 has been released, published, validated, or adopted.

## 1. Purpose and Boundary

AFEF v0.2.0 is intended to let a project adopt a small governance control plane,
conduct bounded discovery, record its constitution, approve authoritative intent,
authorize implementation in proportion to risk, and preserve implementation
evidence and a final gate.

This candidate defines documentation contracts only. It does not provide a
runtime, CLI, generator, validator, automated policy enforcement, CI integration,
or an adoption fixture. Adoption initializes governance; it does not initialize
product technology.

## 2. Ownership and Minimum Control Plane

AFEF owns reusable specifications, protocols, schemas, and templates. An adopter
owns instantiated records, project facts, approvals, and evidence.

The minimal adopter control plane under `.afef/` uses a three-record model. The
model defines exactly three record categories and exactly three schemas:

1. A **project manifest** that identifies the project, pins the immutable AFEF
   version and commit, records the constitution, and maps project paths.
2. A **specification** with a stable identity such as `SPEC-0001` that defines
   approved intended behavior.
3. A **work record** that scopes authorized delivery and records evidence, review
   recommendation, human checkpoint, and final gate.

An adopter maintains exactly one project manifest at the sole normative location
`<project-root>/.afef/project-manifest.yaml`. No alternate filename or configurable
manifest location is accepted, and manifest discovery is not recursive. It may
preserve multiple historical specifications and work records. Multiple concurrent active
specifications or work records are permitted when genuinely required by
concurrent project work. The model limits record categories and schemas; it does
not impose a project-wide maximum of one specification or one work record.

The manifest supplies required repository-relative directories for specifications
and work records. A project does not have to create optional top-level
documentation, design, prompt, source, test, or deployment directories or split
one specification into a directory of supporting documents.

Governance initialization may create authorized `.afef/` records. Technology
initialization—including dependency installation, runtime scaffolding, databases,
or deployment configuration—requires an applicable approved specification and
delivery authorization.

## 3. Discovery and Constitution

Discovery is interactive, bounded, and decision-oriented. It asks only unresolved
questions material to project goal, users, scope, constraints, technology,
architecture, deployment, security, privacy, non-functional requirements,
assumptions, risks, acceptance expectations, and the project constitution.

The constitution records durable project-specific principles and safety
boundaries. It may be inline in the manifest or referenced by a repository-relative
path. A reference does not transfer ownership to AFEF and must be verified against
repository state.

Discovery follows the
[Project Discovery Protocol](../protocols/project-discovery-protocol.md) and ends
in exactly one of its defined outcomes.

## 4. Authority and Factual Reality

- Specifications define approved intended behavior.
- Code and configuration represent implemented state.
- Tests and evidence establish verified behavior.
- Repository and deployed state establish current factual reality.

When these disagree, the conflict must be reported and reconciled. Neither
documentation nor code should be trusted blindly. An approved specification can
describe intent not yet implemented, and implementation can precede its
documentation; both cases are explicit drift requiring lifecycle action rather
than silent reinterpretation.

Specifications use stable sequential identities such as `SPEC-0001` and
`SPEC-0002`. Timestamps belong in metadata and are not primary identities. The
[Specification Lifecycle Protocol](../protocols/specification-lifecycle-protocol.md)
defines approval, activation, amendment, supersession, retirement, and drift
reconciliation.

## 5. Record Locations and Formats

The validator begins at exactly `.afef/project-manifest.yaml`, relative to the
adopting project root. No `.yml`, JSON, TOML, alternate manifest name, or
configurable manifest location is accepted. The manifest's `paths.specifications`
and `paths.work_records` fields are required and identify directories relative to
that same root.

All configured paths use deterministic repository-style `/` semantics. They must
not be absolute, drive-qualified, home-relative, contain `.` or `..` traversal
segments, or resolve outside the project root. Resolution must not follow a
symlink outside the project root.

Only these I1 formats are recognized:

| Record | Format |
|---|---|
| Project manifest | YAML at `.afef/project-manifest.yaml` |
| Specification | Markdown with YAML front matter |
| Work record | YAML |

For discovery, YAML means the `.yaml` extension only and Markdown means `.md`
only; `.yml` and other variants are unsupported.

Record discovery within each configured directory is non-recursive: inspect
direct files only, reject unsupported extensions, and sort discovered
project-relative paths lexically. Missing, empty, duplicate, overlapping, or
escaping record directories and duplicate discovered records are contract
nonconformance. An unreadable directory or filesystem failure is an operational
failure for future I2. Nested directories are not traversed.

## 6. Risk Profiles and Authorization

The [Risk-Scaled Delivery Protocol](../protocols/risk-scaled-delivery-protocol.md)
defines three profiles:

- **Lean** for bounded, reversible, low-risk work.
- **Standard** for normal features and material engineering changes.
- **High Assurance** for sensitive, destructive, production, release, or
  externally effectful work.

Each work record selects a profile, defines an authorization envelope, and records
proportional evidence and human checkpoints. Higher-risk operation characteristics
override a lower selected profile. The IDE Agent never self-approves, and an
authorization envelope never silently grants side-effect authority.

Normative actors use a stable opaque `actor_id` and one canonical `role`:
`product_owner`, `design_supervisor`, `implementation_supervisor`, `ide_agent`, or
`independent_reviewer`. `display_name` is optional, non-normative, and never
determines separation. Manifest authority assignments and work-record
implementers, reviewers, independent reviewers, final-gate owners, and recorded
checkpoint owners use this actor structure.

The authorization envelope's normative source is its structured `operations`
collection, not free-form action prose. Every operation has a stable
`operation_id`, bounded `effect_class`, `permitted` or `prohibited` decision, and
structured authorization requirement. Separate authorization references bind an
exact reference to exact operation IDs. Optional descriptions are explanatory
only.

## 7. Context Budget

AFEF records should link to central protocols instead of copying boilerplate.
Decisions should be recorded once, stable identifiers should replace repeated
prose, and optional fields should be omitted when they add no safety or clarity.

A normal implementation session should normally load only:

1. one project manifest;
2. the directly relevant specification;
3. the active work record; and
4. one directly relevant AFEF protocol.

Additional context is loaded only to resolve an identified question or
contradiction. Agents must not load unrelated specifications or work records by
default.

## 8. Contract Set

The three record categories are represented by exactly three schemas:

| Record | Schema | Compact starting template |
|---|---|---|
| Project manifest | [`project-manifest.schema.json`](../../schemas/v0.2/project-manifest.schema.json) | [Project manifest template](../templates/project-manifest-template.yaml) |
| Specification | [`specification.schema.json`](../../schemas/v0.2/specification.schema.json) | [Specification template](../templates/specification-template.md) |
| Work record | [`work-record.schema.json`](../../schemas/v0.2/work-record.schema.json) | [Work record template](../templates/work-record-template.yaml) |

Schemas define record shape but do not validate themselves, prove approval, grant
authority, or establish factual accuracy. Validation can confirm only the
identities, roles, effect classifications, decisions, and authorization bindings
represented by records. It cannot prove real-world or cryptographic identity,
that two IDs are controlled by different people, approval authenticity, truthful
effect classification, actual external behavior, or continuing authority outside
the recorded scope.

## 9. Sequenced Capabilities

- **I2, if separately authorized:** deterministic offline validator; valid and
  invalid fixtures; schema and cross-record conformance tests; validator exit-code
  behavior; and repository-local CI.
- **I3, if separately authorized:** minimal clean-room adopter; non-authoritative
  GitHub Steward fixture; offline adoption test; independent release review; and
  AFEF v0.2.0 release preparation.
- **Post-v0.2.0:** project generators or initializers; agent runtime or
  orchestration; automated governance or policy enforcement; and broader tooling
  justified by adoption experience.

This sequence does not authorize I2, I3, release, publication, or remote mutation.
