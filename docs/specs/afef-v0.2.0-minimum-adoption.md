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

The minimal adopter control plane is `.afef/` containing three active records:

1. A **project manifest** that identifies the project, pins the immutable AFEF
   version and commit, records the constitution, and maps project paths.
2. An **active specification** with a stable identity such as `SPEC-0001` that
   defines approved intended behavior.
3. An **active work record** that scopes authorized delivery and records evidence,
   review recommendation, human checkpoint, and final gate.

Records may use adopter-selected locations declared in the manifest. A project
does not have to create numerous top-level documentation directories or split one
specification into a directory of supporting documents.

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

## 5. Configurable Project Paths

The project manifest can point to existing repository-relative locations for:

- documentation
- source
- tests
- architecture
- decisions
- specifications
- work records
- evidence

Paths describe where adopter-owned material already lives or will be maintained.
They do not require a prescribed repository layout.

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

## 7. Context Budget

AFEF records should link to central protocols instead of copying boilerplate.
Decisions should be recorded once, stable identifiers should replace repeated
prose, and optional fields should be omitted when they add no safety or clarity.

A normal implementation session should normally load only:

1. the project manifest;
2. the active specification;
3. the active work record; and
4. one directly relevant AFEF protocol.

Additional context is loaded only to resolve an identified question or
contradiction.

## 8. Contract Set

The three records are represented by:

| Record | Schema | Compact starting template |
|---|---|---|
| Project manifest | [`project-manifest.schema.json`](../../schemas/v0.2/project-manifest.schema.json) | [Project manifest template](../templates/project-manifest-template.yaml) |
| Specification | [`specification.schema.json`](../../schemas/v0.2/specification.schema.json) | [Specification template](../templates/specification-template.md) |
| Work record | [`work-record.schema.json`](../../schemas/v0.2/work-record.schema.json) | [Work record template](../templates/work-record-template.yaml) |

Schemas define record shape but do not validate themselves, prove approval, grant
authority, or establish factual accuracy.

## 9. Deferred Capabilities

- **I2:** behavioral schema validation and any separately authorized conformance
  work.
- **I3:** separately authorized adoption or integration work.
- **Post-v0.2.0:** generators, validators, automation, fixtures, and broader
  tooling, if designed and authorized.
- **v0.3.0:** any runtime or automated governance capabilities accepted through a
  future architecture and release process.

No deferred capability is implied, implemented, or authorized by this candidate.
