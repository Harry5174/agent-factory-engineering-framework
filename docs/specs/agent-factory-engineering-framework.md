# Agent Factory Engineering Framework — Specification

**Framework version:** `0.1.0`

**Implementation model:** Documentation-first and human-operated

## 1. Purpose

The Agent Factory Engineering Framework (AFEF) provides reusable engineering-governance material for bounded, evidence-driven work:

- Session and sprint lifecycle protocols
- Human role and authority boundaries
- Repository-grounded bootstrap templates
- Evidence, review, and overclaim-prevention protocols
- Safety boundaries for local and externally effectful work
- Memory templates for adopter-owned operational records

AFEF is not an agent runtime, product runtime, workflow engine, or automated enforcement layer.

## 2. Ownership Model

The AFEF repository owns reusable framework material. Each adopting repository owns its instantiated operational records under `.afef/`. Operational records must be checked against current repository state and cannot grant authority beyond an approved sprint.

The `agent-factory-engineering-framework` repository is the designated canonical repository for AFEF. Determine its currently published revision, if any, from the default branch, and determine release availability from the applicable annotated Git tag and GitHub Release metadata. See the [central release-verification guidance](../../README.md#version-publication-and-release-verification).

## 3. Framework Invariants

1. Repository state is verified before operational records are trusted.
2. Every implementation sprint has explicit, bounded authorization.
3. Every sprint defines scope, prohibited work, evidence, and stop conditions.
4. Every completion claim is backed by raw evidence.
5. Implementation agents do not self-approve.
6. Remote publication, tags, and releases require separate authorization.
7. Framework templates and adopter-owned `.afef/` records remain distinct.

## 4. Session Lifecycle

```text
bootstrap and role identification
    ↓
repository and context verification
    ↓
authorization and scope confirmation
    ↓
bounded implementation or review
    ↓
validation and raw evidence collection
    ↓
completion report
    ↓
independent review and final sprint gate
    ↓
authorized operational-record update and handoff
```

See the [Session Lifecycle Protocol](../protocols/session-lifecycle.md).

## 5. Sprint Lifecycle

```text
sprint definition
    ↓
design review
    ↓
Product Owner authorization
    ↓
implementation prompt
    ↓
bounded implementation
    ↓
evidence and completion report
    ↓
Implementation Supervisor evidence review
    ↓
Design Supervisor final sprint gate
```

Publication and release follow a separate authorization and independent-review path. See the [Sprint Lifecycle Protocol](../protocols/sprint-lifecycle.md).

## 6. Role Model

### Product Owner

- Owns scope, policy, licensing, adoption, publication, tag, and release decisions.
- Authorizes every implementation sprint and any external side effect.
- Does not bypass evidence or review requirements.

### Design Supervisor

- Owns architecture and bounded sprint design.
- Issues the final sprint-gate decision after reviewing implementation evidence and recommendations.
- Does not publish or release without separate Product Owner authorization.

### Implementation Supervisor

- Translates approved design into a complete implementation prompt.
- Defines validation, evidence, and block conditions.
- Reviews implementation evidence and recommends corrections but does not issue the final sprint gate.

### IDE Agent

- Performs only the implementation authorized by the sprint prompt.
- Verifies repository state, preserves raw evidence, and reports blockers.
- Does not expand scope, expose secrets, publish, tag, release, or self-approve.

### Independent Reviewer

- Independently validates release readiness, evidence integrity, and claim boundaries.
- Does not modify the candidate or perform publication.
- Returns findings to the authorized release process.

See [Governance](../../GOVERNANCE.md) for authority details.

## 7. Safety Model

- Local/dry-run behavior is preferred when it can establish the required evidence.
- External reads and writes must be distinguished explicitly.
- External writes require specific authorization and an auditable boundary.
- Secrets and `.env` values are never printed or placed into model context.
- Generated proposals do not grant execution authority.
- Evidence is redacted without suppressing material failures.
- Automation must not silently broaden authorization.

See the [Safety Boundary Protocol](../protocols/safety-boundary-protocol.md).

## 8. Evidence Model

Evidence must record the relevant repository state, exact validation commands, exit codes, raw or safely redacted output, supported claims, non-claims, and known limitations. Evidence stored by an adopter belongs under that repository's `.afef/` convention or another explicitly approved external location.

Evidence review produces findings and recommendations. It does not by itself grant implementation, publication, or release authority.

## 9. v0.1.0 Limitations

Version `0.1.0` is documentation-first. It does not provide schemas, validators, a CLI, CI integration, reusable Actions, automatic prompt generation, machine-readable governance, or adoption fixtures. Gate-vocabulary normalization and lifecycle automation require separately authorized future work.

The documented version is not by itself evidence of a published revision, annotated tag, GitHub Release, adoption, or production maturity.
