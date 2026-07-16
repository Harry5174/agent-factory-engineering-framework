# AFEF Documentation

This directory contains active documentation for the Agent Factory Engineering Framework (AFEF) target version `0.1.0`. The baseline is unreleased and the dedicated public repository has not yet been established as canonical.

## Specification

- [Agent Factory Engineering Framework specification](specs/agent-factory-engineering-framework.md)

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
- [Governance](../GOVERNANCE.md)
- [AFDF extraction provenance](provenance/afdf-extraction.md)

Operational project status, evidence, examples, and project memory are intentionally not stored in this framework documentation tree. An adopting repository owns those records and must maintain them under its authorized `.afef/` convention.
