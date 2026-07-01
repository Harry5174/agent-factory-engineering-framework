# Templates Index

This directory contains reusable, fill-in-the-blank templates for every stage of the Agent Factory development lifecycle.

---

## Lifecycle Map

Templates follow this lifecycle flow:

```text
Design Supervisor Bootstrap
        ↓
Implementation Supervisor Bootstrap / Sprint Prompt
        ↓
IDE Agent Bootstrap
        ↓
Completion Report
        ↓
Green Gate Review
        ↓
Next Session Handoff
        ↓
(back to Design Supervisor Bootstrap for the next session)
```

---

## Template Summary

| Template | Role | When Used | Inputs | Output |
|----------|------|-----------|--------|--------|
| [Design Supervisor Bootstrap](design-supervisor-bootstrap-template.md) | Design Supervisor | Start of a design session | Project memory, completion reports, repo state | Scope decisions, gate decisions, updated memory |
| [Implementation Supervisor Bootstrap](implementation-supervisor-bootstrap-template.md) | Implementation Supervisor | After design approval, before handoff to IDE Agent | Approved scope, repo state | Sprint prompt or IDE Agent bootstrap |
| [IDE Agent Bootstrap](ide-agent-bootstrap-template.md) | IDE Agent | Start of an implementation session | Sprint prompt, repo state | Deliverables + completion report |
| [Sprint Prompt](sprint-prompt-template.md) | Implementation Supervisor → IDE Agent | When preparing a sprint | Approved scope, safety boundaries | Self-contained sprint instructions |
| [Completion Report](completion-report-template.md) | IDE Agent / Implementer | End of a sprint | All evidence from the sprint | Structured evidence report |
| [Green Gate Review](green-gate-review-template.md) | Design Supervisor / Reviewer | After receiving a completion report | Sprint prompt, completion report, evidence | GREEN / YELLOW / RED gate decision |
| [Next Session Handoff](next-session-handoff-template.md) | Any role | End of a sprint, after gate review | Gate outcome, repo state | Context for the next session |

---

## Relationship to Living Memory

These templates are designed to be filled using data from the [Living Project Memory](../../project-memory/). While templates provide the empty structure, the living memory provides the factual content (status, decisions, evidence). Every filled template must link back to the living memory to ensure context continuity.

---

## How Templates Relate

1. The **Design Supervisor Bootstrap** sets scope and decisions
2. The **Implementation Supervisor Bootstrap** translates scope into actionable sprint instructions
3. The **Sprint Prompt** is the self-contained instruction set handed to the IDE Agent
4. The **IDE Agent Bootstrap** gives the IDE Agent everything it needs to start
5. The **Completion Report** captures all evidence from the sprint
6. The **Green Gate Review** evaluates the completion report
7. The **Next Session Handoff** prepares context for whoever works next

---

## Minimum Required Fields

Any template derivative or customized prompt must include at minimum:

| Field | Reason |
|-------|--------|
| Sprint identity (project, artifact, sprint, goal) | Prevents confusion about what is being worked on |
| Product Owner approval status | Prevents unauthorized work |
| Scope boundaries (in scope, out of scope) | Prevents drift |
| Safety invariants | Prevents safety violations |
| Anti-drift guard | Prevents hallucinated state |
| Evidence expectations | Ensures completion reports are reviewable |
| Block conditions | Defines when to stop |

---

## Placeholder Syntax

All templates use `<PLACEHOLDER>` syntax for fields that must be filled in:

```text
<PROJECT_NAME>         — Project name
<ARTIFACT_NAME>        — Artifact name with number
<SPRINT_NAME>          — Sprint identifier (e.g., A7.1)
<SPRINT_GOAL>          — One-sentence sprint goal
<BRANCH_NAME>          — Git branch name
<COMMIT_HASH>          — Git commit hash
<BASE_COMMIT>          — Base branch or commit
<REPO_PATH>            — Repository or workspace path
<APPROVAL_STATUS>      — Approved / Pending / Not yet requested
<APPROVED_BY>          — Who approved
<APPROVAL_SCOPE>       — What was approved
<APPROVAL_LIMITATIONS> — What was NOT approved
<SCAN_PATH>            — Path to scan for tokens/paths
```

---

## Supporting Documents

- [Template Quality Checklist](template-quality-checklist.md) — Evaluate whether a prompt/template is good enough before use
- [Session Lifecycle Protocol](../protocols/session-lifecycle.md) — Full session flow
- [Sprint Lifecycle Protocol](../protocols/sprint-lifecycle.md) — Full sprint flow
- [Evidence Review Protocol](../protocols/evidence-review-protocol.md) — How to evaluate evidence
- [Safety Boundary Protocol](../protocols/safety-boundary-protocol.md) — Safety rules
