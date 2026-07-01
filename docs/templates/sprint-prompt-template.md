# Sprint Prompt Template

> **Instructions:** Copy this template and fill in the bracketed fields to create a sprint prompt for an IDE Agent or implementer.

---

## Role

You are the **[role, e.g., IDE Agent]** working in the `[workspace]` repository.

---

## Sprint Identity

| Field | Value |
|-------|-------|
| **Artifact** | [e.g., Artifact 07 — GitHub Repo Steward Agent] |
| **Sprint** | [e.g., A7.1 — Foundation Scaffold] |
| **Sprint goal** | [one-sentence goal] |

---

## Context

[Provide the context the implementer needs. Include relevant project state, previous sprint outcomes, and any bootstrap information.]

---

## Scope Boundaries

### In Scope

- [deliverable 1]
- [deliverable 2]

### Out of Scope

- [excluded item 1]
- [excluded item 2]

### Hard Constraints

- [constraint 1, e.g., "No runtime code changes"]
- [constraint 2, e.g., "No GitHub API calls"]

---

## Deliverables

| # | Deliverable | Description |
|---|-------------|-------------|
| 1 | [deliverable name] | [what it is and what it contains] |
| 2 | [deliverable name] | [what it is and what it contains] |

---

## Tests

| Test | Command | Expected Result |
|------|---------|-----------------|
| [test name] | [command] | [expected outcome] |

---

## Validation Commands

Run after implementation:

```bash
[validation command 1]
[validation command 2]
[safety scan command]
```

---

## Commit Instructions

```text
Branch: [branch name]
Commit message: [message]
Stage: [files/patterns to stage]
Push: [yes/no]
Tag: [yes/no]
```

---

## Completion Report Requirements

Return a completion report with:

1. Sprint goal
2. Branch and commit
3. Files created
4. Files modified
5. Commands run
6. Test/lint results
7. Safety scan results
8. Scope confirmations
9. Known limitations
10. Recommended next step

---

## Block Conditions

Stop and report blocked if:

- [block condition 1]
- [block condition 2]
