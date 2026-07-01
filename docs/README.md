# AFDF Documentation Index

This directory contains the specifications, protocols, templates, memory templates, examples, and status documents for the Agent Factory Development Framework.

---

## Specifications

| Document | Purpose |
|----------|---------|
| [Agent Factory Development Framework](specs/agent-factory-development-framework.md) | Core framework specification and role model |

---

## Protocols

| Protocol | Purpose |
|----------|---------|
| [Session Lifecycle](protocols/session-lifecycle.md) | How sessions start, execute, and hand off |
| [Sprint Lifecycle](protocols/sprint-lifecycle.md) | How sprints flow from goal to green gate |
| [Repository Inspection](protocols/repository-inspection-protocol.md) | Standard commands for verifying repo state |
| [Evidence Review](protocols/evidence-review-protocol.md) | How to evaluate completion report evidence |
| [Safety Boundary](protocols/safety-boundary-protocol.md) | Reusable safety rules and artifact boundaries |
| [Green Gate Review](protocols/green-gate-review-protocol.md) | How to conduct green/yellow/red gate reviews |
| [Memory Update](protocols/memory-update-protocol.md) | When and how to update living memory |
| [Decision Log](protocols/decision-log-protocol.md) | How to record decisions |
| [Evidence Package](protocols/evidence-package-protocol.md) | How to structure evidence packages |
| [Overclaim Prevention](protocols/overclaim-prevention-protocol.md) | How to prevent hallucinated completion states |

---

## Templates

See [Templates Index](templates/README.md) for the full lifecycle map and usage guide.

| Template | Used By |
|----------|---------|
| [Templates Index](templates/README.md) | All roles — lifecycle map and usage guide |
| [Template Quality Checklist](templates/template-quality-checklist.md) | All roles — validate templates before use |
| [Design Supervisor Bootstrap](templates/design-supervisor-bootstrap-template.md) | Design Supervisor at session start |
| [Implementation Supervisor Bootstrap](templates/implementation-supervisor-bootstrap-template.md) | Implementation Supervisor at sprint start |
| [IDE Agent Bootstrap](templates/ide-agent-bootstrap-template.md) | IDE Agent at implementation start |
| [Sprint Prompt](templates/sprint-prompt-template.md) | Implementation Supervisor preparing a sprint |
| [Completion Report](templates/completion-report-template.md) | IDE Agent / Implementer at sprint end |
| [Green Gate Review](templates/green-gate-review-template.md) | Design Supervisor / Reviewer at review time |
| [Next Session Handoff](templates/next-session-handoff-template.md) | Any role preparing the next session |

---

## Memory Templates

| Template | Purpose |
|----------|---------|
| [Project Memory](memory/project-memory-template.md) | Living project context and decisions |
| [Decision Log](memory/decision-log-template.md) | Why decisions were made |
| [Rejected Ideas](memory/rejected-ideas-template.md) | Ideas rejected and why |
| [Known Limitations](memory/known-limitations-template.md) | Current system boundaries |
| [Technical Debt](memory/technical-debt-template.md) | Cleanup and improvement backlog |
| [Lessons Learned](memory/lessons-learned-template.md) | Reusable lessons from past work |

---

## Examples

| Example | Shows |
|---------|-------|
| [Agent Factory Project Bootstrap](examples/agent-factory-project-bootstrap-example.md) | How to bootstrap a Design Supervisor session |
| [Artifact 06 Closeout Bootstrap](examples/artifact-06-closeout-bootstrap-example.md) | How to bootstrap a closeout verification session |
| [Artifact 07 Readiness Draft](examples/artifact-07-bootstrap-readiness-draft.md) | Framework readiness for the next vertical agent |

---

## Status

| Document | Purpose |
|----------|---------|
| [Project Status](status/project-status.md) | Current AFDF and project state |
| [Roadmap](status/roadmap.md) | AFDF sprint roadmap |
| [Known Limitations](status/known-limitations.md) | What AFDF cannot do yet |
| [Interview Notes](status/interview-notes.md) | How to describe AFDF in interviews |
