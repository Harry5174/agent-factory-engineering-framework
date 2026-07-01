# Agent Factory Development Framework (AFDF)

The Agent Factory Development Framework is a reusable, living Markdown framework that supports the design, implementation, review, and handoff of all future Agent Factory artifacts.

---

## What AFDF Is

AFDF is a lightweight process infrastructure layer for the Agent Factory project. It provides:

- **Bootstrap templates** that give new sessions the context they need to start without recreating knowledge from scratch
- **Sprint and session lifecycle protocols** that define how work flows from design through green-gate review
- **Memory templates** that preserve decisions, lessons, rejected ideas, and technical debt across sessions
- **Evidence and review protocols** that define how completion reports are evaluated
- **Safety boundary protocols** that carry forward the Agent Factory's core safety invariants
- **Role definitions** that clarify who does what in the design–implement–review cycle

---

## What AFDF Is Not

- AFDF **does not run agents**. It is advisory and process-level only.
- AFDF **does not enforce workflow automatically**. There is no CLI, database, or automation engine.
- AFDF **does not modify artifact runtime behavior**. Artifacts 00–06 are unchanged.
- AFDF **does not replace human review**. A Design Supervisor or Product Owner still makes decisions.
- AFDF **does not generate prompts programmatically**. Templates are filled in manually.

---

## Where It Lives

```text
03-agent-factory/development-framework/
```

This directory lives alongside the coursework folders and `xx-projects/`. It is not a numbered artifact — it is shared infrastructure that all future artifacts consume.

---

## How It Supports Future Artifacts

Every future artifact follows a reusable lifecycle:

```text
design session → sprint prompt → IDE/implementation session → completion report → green-gate review → living memory update → next-session bootstrap
```

AFDF provides templates and protocols for each stage. Instead of recreating context from scratch, new sessions start from a bootstrap document that carries forward project state, approved decisions, and safety invariants.

**Core principle:** Context changes. Workflow does not.

---

## Who Uses It

| Role | Uses AFDF For |
|------|---------------|
| **Product Owner** | Scope approval, publish/tag decisions, safety boundary review |
| **Design Supervisor** | Design sessions, scope definition, green-gate reviews |
| **Implementation Supervisor** | Sprint prompts, scope boundaries, completion report requirements |
| **IDE Agent** | Bootstrap context, allowed/forbidden edits, evidence collection |
| **Reviewer/Evaluator** | Evidence review, overclaim detection, safety verification |

---

## What Files Matter First

If you are starting a new session, read these first:

1. **This README** — understand what AFDF is
2. **[Session Lifecycle Protocol](docs/protocols/session-lifecycle.md)** — understand the full session flow
3. **The appropriate bootstrap template** for your role:
   - Design Supervisor → [design-supervisor-bootstrap-template.md](docs/templates/design-supervisor-bootstrap-template.md)
   - Implementation Supervisor → [implementation-supervisor-bootstrap-template.md](docs/templates/implementation-supervisor-bootstrap-template.md)
   - IDE Agent → [ide-agent-bootstrap-template.md](docs/templates/ide-agent-bootstrap-template.md)
4. **[Project Memory Template](docs/memory/project-memory-template.md)** — understand what living memory looks like

---

## How to Use AFDF at the Start of a Session

1. Identify your role (Design Supervisor, Implementation Supervisor, IDE Agent, etc.)
2. Copy the appropriate bootstrap template
3. Fill in the current project state from the latest project memory and status docs
4. Use the filled bootstrap as the opening context for the new session
5. Verify the repository state using the [Repository Inspection Protocol](docs/protocols/repository-inspection-protocol.md)

---

## How to Use AFDF at the End of a Sprint

1. Fill in the [Completion Report Template](docs/templates/completion-report-template.md)
2. Request a green-gate review using the [Green Gate Review Template](docs/templates/green-gate-review-template.md)
3. If approved, update project memory using the [Project Memory Template](docs/memory/project-memory-template.md)
4. Fill in the [Next Session Handoff Template](docs/templates/next-session-handoff-template.md)
5. Commit, but do not push/tag without Product Owner approval

---

## What AFDF Does Not Do Yet

- No CLI or validation tooling
- No automated schema enforcement
- No multi-project synchronization
- No prompt generation code
- No database or persistence layer
- Templates are manually filled, not auto-populated

See [Roadmap](docs/status/roadmap.md) for planned future sprints.

---

## Framework Version

| Sprint | Description | Status |
|--------|-------------|--------|
| AFDF.0 | Framework Scaffold and Operating Model | Current |
| AFDF.1 | Core Bootstrap Templates Hardening | Planned |
| AFDF.2 | Project Memory, Decision Log, and Evidence Protocols | Planned |
| AFDF.3 | Agent Factory Bootstrap Example | Planned |
| AFDF.4 | Next-Session Prompt Generation Protocol | Planned |

---

## Directory Structure

```text
development-framework/
├── README.md                          # This file
└── docs/
    ├── README.md                      # Docs index
    ├── specs/
    │   └── agent-factory-development-framework.md
    ├── protocols/
    │   ├── session-lifecycle.md
    │   ├── sprint-lifecycle.md
    │   ├── repository-inspection-protocol.md
    │   ├── evidence-review-protocol.md
    │   ├── safety-boundary-protocol.md
    │   └── green-gate-review-protocol.md
    ├── templates/
    │   ├── design-supervisor-bootstrap-template.md
    │   ├── implementation-supervisor-bootstrap-template.md
    │   ├── ide-agent-bootstrap-template.md
    │   ├── sprint-prompt-template.md
    │   ├── completion-report-template.md
    │   ├── green-gate-review-template.md
    │   └── next-session-handoff-template.md
    ├── memory/
    │   ├── project-memory-template.md
    │   ├── decision-log-template.md
    │   ├── rejected-ideas-template.md
    │   ├── known-limitations-template.md
    │   ├── technical-debt-template.md
    │   └── lessons-learned-template.md
    ├── examples/
    │   ├── agent-factory-project-bootstrap-example.md
    │   └── artifact-06-closeout-bootstrap-example.md
    └── status/
        ├── project-status.md
        ├── roadmap.md
        ├── known-limitations.md
        └── interview-notes.md
```
