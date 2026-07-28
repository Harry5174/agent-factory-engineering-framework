# AFEF Documentation

This directory contains active documentation for Agent Factory Engineering Framework (AFEF) version `0.2.0`. The designated canonical repository and the sources used to verify publication and release state are described in the [central release-verification guidance](../README.md#version-publication-and-release-verification).

## Specification

- [Agent Factory Engineering Framework specification](specs/agent-factory-engineering-framework.md)

### Minimum Adoption

- [Minimum-adoption specification](specs/afef-v0.2.0-minimum-adoption.md)

## Protocols

- [Session lifecycle](protocols/session-lifecycle.md)
- [Sprint lifecycle](protocols/sprint-lifecycle.md)
- [Repository inspection](protocols/repository-inspection-protocol.md)
- [Evidence review](protocols/evidence-review-protocol.md)
- [Evidence packaging](protocols/evidence-package-protocol.md)
- [Safety boundaries](protocols/safety-boundary-protocol.md)
- [Green gate review](protocols/green-gate-review-protocol.md)
- [Memory updates](protocols/memory-update-protocol.md)
- [Decision logging](protocols/decision-log-protocol.md)
- [Overclaim prevention](protocols/overclaim-prevention-protocol.md)

### Discovery and Delivery Protocols

- [Project discovery](protocols/project-discovery-protocol.md)
- [Specification lifecycle](protocols/specification-lifecycle-protocol.md)
- [Risk-scaled delivery](protocols/risk-scaled-delivery-protocol.md)

## Templates

- [Template index](templates/README.md)
- [Design Supervisor bootstrap](templates/design-supervisor-bootstrap-template.md)
- [Implementation Supervisor bootstrap](templates/implementation-supervisor-bootstrap-template.md)
- [IDE Agent bootstrap](templates/ide-agent-bootstrap-template.md)
- [Sprint prompt](templates/sprint-prompt-template.md)
- [Completion report](templates/completion-report-template.md)
- [Green gate review](templates/green-gate-review-template.md)
- [Next-session handoff](templates/next-session-handoff-template.md)
- [Template quality checklist](templates/template-quality-checklist.md)

### Minimum-Adoption Contracts and Templates

- [Deterministic adopter validation](validation.md)
- [`project-manifest.schema.json`](../schemas/v0.2/project-manifest.schema.json)
  and [project manifest template](templates/project-manifest-template.yaml)
- [`specification.schema.json`](../schemas/v0.2/specification.schema.json)
  and [specification template](templates/specification-template.md)
- [`work-record.schema.json`](../schemas/v0.2/work-record.schema.json)
  and [work record template](templates/work-record-template.yaml)

## Memory Templates

These are reusable source templates. Adopters instantiate operational copies under their own `.afef/` directory.

- [Project memory](memory/project-memory-template.md)
- [Decision log](memory/decision-log-template.md)
- [Rejected ideas](memory/rejected-ideas-template.md)
- [Known limitations](memory/known-limitations-template.md)
- [Technical debt](memory/technical-debt-template.md)
- [Lessons learned](memory/lessons-learned-template.md)

## Repository Records

- [Repository overview and current limitations](../README.md)
- [Version declaration](../VERSION)
- [Changelog](../CHANGELOG.md)
- [v0.2.0 release notes](releases/v0.2.0.md)
- [Validation guide](validation.md)
- [Governance](../GOVERNANCE.md)
- [AFDF extraction provenance](provenance/afdf-extraction.md)

Operational project status, evidence, examples, and project memory are intentionally not stored in this framework documentation tree. An adopting repository owns those records and must maintain them under its authorized `.afef/` convention.
