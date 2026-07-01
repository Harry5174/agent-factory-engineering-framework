# Agent Factory Development Framework — Specification

**Version:** AFDF.0
**Sprint:** Framework Scaffold and Operating Model
**Status:** Initial scaffold

---

## 1. Purpose

The Agent Factory Development Framework (AFDF) is a reusable, living Markdown framework that provides:

- Consistent session bootstrapping so new sessions start with full context
- Reusable sprint and session lifecycle protocols
- Living project memory that preserves decisions and lessons across sessions
- Evidence and review protocols that define quality standards
- Safety boundary protocols that inherit from the artifact sequence
- Role definitions that clarify responsibilities and handoffs

**Core invariant:** Context changes. Workflow does not.

---

## 2. Framework Invariants

1. Every new session starts from a bootstrap.
2. Every sprint ends with evidence.
3. Every green gate updates memory.
4. No context is recreated from scratch when it can be updated from a living document.

---

## 3. Session Lifecycle

Every session follows this lifecycle:

```text
start-of-session bootstrap
    ↓
repository/context verification
    ↓
scope confirmation
    ↓
implementation plan
    ↓
work execution
    ↓
evidence collection
    ↓
completion report
    ↓
green-gate review
    ↓
memory update
    ↓
next-session handoff
```

See [Session Lifecycle Protocol](../protocols/session-lifecycle.md) for details.

---

## 4. Sprint Lifecycle

Every sprint follows this lifecycle:

```text
sprint definition (name, goal, scope)
    ↓
pre-implementation review
    ↓
Product Owner approval
    ↓
implementation
    ↓
evidence collection
    ↓
completion report
    ↓
green/yellow/red gate
    ↓
next sprint recommendation
```

See [Sprint Lifecycle Protocol](../protocols/sprint-lifecycle.md) for details.

---

## 5. Role Model

### 5.1 Product Owner

| Aspect | Definition |
|--------|------------|
| **Responsibility** | Owns project scope, approves live actions, approves publish/tag decisions, approves safety boundary exceptions |
| **Inputs** | Design proposals, sprint plans, completion reports, green-gate reviews |
| **Outputs** | Scope approvals, publish/tag decisions, exception approvals |
| **Must not** | Write code, run tests, modify runtime behavior, bypass safety protocols |
| **Handoff** | Approved scope → Design Supervisor. Approved publish → merge/tag/push |

### 5.2 Design Supervisor

| Aspect | Definition |
|--------|------------|
| **Responsibility** | Finalizes artifact scope, defines sprint boundaries, conducts green-gate reviews, maintains design consistency |
| **Inputs** | Product Owner scope approval, project memory, previous completion reports |
| **Outputs** | Sprint scope documents, green-gate decisions, design review notes, updated project memory |
| **Must not** | Edit application code directly, run live side effects, approve publish/tag (that is the Product Owner) |
| **Handoff** | Approved sprint scope → Implementation Supervisor. Green-gate outcome → next session bootstrap |

### 5.3 Implementation Supervisor

| Aspect | Definition |
|--------|------------|
| **Responsibility** | Turns approved design into sprint prompts, defines implementation expectations, specifies tests and evidence requirements |
| **Inputs** | Approved sprint scope from Design Supervisor, project memory, repository state |
| **Outputs** | Sprint prompts, implementation plans, block conditions, completion report requirements |
| **Must not** | Override Design Supervisor scope, approve green gates, approve publish/tag decisions |
| **Handoff** | Sprint prompt → IDE Agent. Completion report requirements → IDE Agent |

### 5.4 IDE Agent

| Aspect | Definition |
|--------|------------|
| **Responsibility** | Edits the repository, runs tests/lint/checks, collects evidence, produces completion reports |
| **Inputs** | Sprint prompt, IDE agent bootstrap, repository state |
| **Outputs** | Code/docs changes, test results, lint results, safety scan results, completion report |
| **Must not** | Expand scope beyond sprint boundaries, run live side effects without explicit approval, read/print secrets, push/tag without Product Owner approval |
| **Handoff** | Completion report → Design Supervisor for green-gate review |

### 5.5 Reviewer/Evaluator

| Aspect | Definition |
|--------|------------|
| **Responsibility** | Checks integrity of completion reports, detects overclaims, verifies evidence quality, validates safety compliance |
| **Inputs** | Completion reports, evidence artifacts, repository state |
| **Outputs** | Review notes, evidence quality assessments, overclaim flags, recommended corrections |
| **Must not** | Approve scope changes, override Product Owner decisions, modify code |
| **Handoff** | Review notes → Design Supervisor for gate decision |

---

## 6. Safety Inheritance

The framework inherits safety principles from the artifact sequence:

| Principle | Source |
|-----------|--------|
| LLM proposes, harness decides, operator approves | Artifact 00 onwards |
| Fake/default first, real mode explicit only | Artifact 02 onwards |
| Approval before side effects | Artifact 02 onwards |
| Do not print/expose secrets | All artifacts |
| CI must not run live side effects | Artifact 04 onwards |

See [Safety Boundary Protocol](../protocols/safety-boundary-protocol.md) for the full reusable safety ruleset.

---

## 7. What AFDF Does Not Cover (Yet)

- Automated template validation
- CLI tooling
- Prompt generation code
- Multi-project synchronization
- Database or persistence
- Schema enforcement

See [Roadmap](../status/roadmap.md) for planned future sprints.
