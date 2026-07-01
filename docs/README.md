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

---

## Templates

| Template | Used By |
|----------|---------|
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

---

## Status

| Document | Purpose |
|----------|---------|
| [Project Status](status/project-status.md) | Current AFDF and project state |
| [Roadmap](status/roadmap.md) | AFDF sprint roadmap |
| [Known Limitations](status/known-limitations.md) | What AFDF cannot do yet |
| [Interview Notes](status/interview-notes.md) | How to describe AFDF in interviews |
