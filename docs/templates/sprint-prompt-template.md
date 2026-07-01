# Sprint Prompt Template

> **Purpose:** Define a complete, self-contained sprint for an IDE Agent or implementer — including all context, scope, safety, evidence, and handoff requirements.
>
> **When to use:** When the Implementation Supervisor prepares a sprint for execution. This is the primary input to an IDE Agent session.
>
> **Required inputs:** Approved sprint scope, repository state, safety boundaries, evidence requirements.
>
> **Required outputs:** All deliverables, plus a completion report with evidence.
>
> **Instructions:** Copy this template and replace all `<PLACEHOLDER>` fields with current values.

---

## Role

You are the **`<ROLE>`** (e.g., IDE Agent) working in the `<WORKSPACE>` repository.

---

## Sprint Identity

| Field | Value |
|-------|-------|
| **Project** | `<PROJECT_NAME>` |
| **Artifact** | `<ARTIFACT_NAME>` (e.g., Artifact 07 — GitHub Repo Steward Agent) |
| **Sprint** | `<SPRINT_NAME>` (e.g., A7.1 — Foundation Scaffold) |
| **Sprint goal** | `<SPRINT_GOAL>` |

---

## Product Owner Approval

| Field | Value |
|-------|-------|
| **Approval status** | `<APPROVAL_STATUS>` |
| **Approved by** | `<APPROVED_BY>` |
| **Approval scope** | `<APPROVAL_SCOPE>` |
| **Approval limitations** | `<APPROVAL_LIMITATIONS>` |

---

## Context

> Provide the context the implementer needs. Include relevant project state, previous sprint outcomes, and bootstrap information.

`<CONTEXT_BLOCK>`

---

## Scope Boundaries

### In Scope

- `<DELIVERABLE_1>`
- `<DELIVERABLE_2>`

### Out of Scope

- `<EXCLUDED_1>`
- `<EXCLUDED_2>`

### Hard Constraints

- `<CONSTRAINT_1>` (e.g., "No runtime code changes")
- `<CONSTRAINT_2>` (e.g., "No GitHub API calls")

---

## Anti-Drift Guard

### What this session must NOT assume

- `<ASSUMPTION_TO_AVOID_1>`
- `<ASSUMPTION_TO_AVOID_2>`

### What must be verified from the repository

- Branch and commit match expected starting state
- Required input files exist and are current

### What decisions are already settled

- `<SETTLED_DECISION_1>`

### What decisions are still open

- `<OPEN_DECISION_1>` (resolve during implementation or stop and escalate)

### What would count as scope drift

- Implementing features beyond the deliverables listed above
- Modifying files outside the sprint's scope
- Adding unapproved dependencies or infrastructure

### When to stop and ask for clarification

- Scope is ambiguous or contradictory
- A required input is missing
- A safety boundary would need to be relaxed

---

## Deliverables

| # | Deliverable | Description |
|---|-------------|-------------|
| 1 | `<DELIVERABLE_NAME_1>` | `<WHAT_IT_IS_AND_CONTAINS>` |
| 2 | `<DELIVERABLE_NAME_2>` | `<WHAT_IT_IS_AND_CONTAINS>` |

---

## Tests

| Test | Command | Expected Result |
|------|---------|-----------------|
| `<TEST_NAME>` | `<COMMAND>` | `<EXPECTED_OUTCOME>` |

For docs-only sprints, minimum validation:

```bash
git diff --check
```

---

## Safety Invariants

- Do not print secrets
- Do not read or paste `.env`
- Do not run live external side effects without explicit Product Owner approval
- Use fake/default mode unless real mode is explicitly approved
- Do not bypass approval gates
- Do not let an LLM execute tools directly — LLM proposes; harness decides; operator approves
- Record evidence before claiming completion

### Inherited Safety Boundaries

- Artifact 04: real GitHub runtime safety (server-side token, allowlisted repos)
- Artifact 05: release-gate evidence safety (evidence required before claims)
- Artifact 06: local/demo operator workbench safety (no live GitHub for demo)

---

## Validation Commands

Run after implementation:

```bash
git status -sb
git diff --check
```

Safety scans:

```bash
rg -n "ghp_|github_pat_|gho_|ghu_|ghs_|ghr_|Bearer |GITHUB_ACCESS_TOKEN=|AGENT_FACTORY_GITHUB_TOKEN=" \
  <SCAN_PATH> || true

rg -n "/home/|Desktop/|/Users/" \
  <SCAN_PATH> || true

git check-ignore -v .env || true
git ls-files .env
git ls-files "*__pycache__*"
git ls-files "*.pyc"
```

> Matches that are intentional scan-pattern examples in documentation must be explained in the completion report.

---

## Commit Instructions

```text
Branch: <BRANCH_NAME>
Commit message: <COMMIT_MESSAGE>
Stage: <STAGE_COMMAND>
Push: no (unless Product Owner approves)
Tag: no (unless Product Owner approves)
```

---

## Completion Report Requirements

Return a completion report with:

1. Sprint goal
2. Branch and commit (with base commit)
3. Files reviewed before implementation
4. Files created (with descriptions)
5. Files modified (with descriptions)
6. Commands run (with relevant output)
7. Test/lint results (or documented reason for skipping)
8. Secret scan results
9. Local path scan results
10. `.env` verification results
11. Scope confirmations (what was NOT changed)
12. Safety confirmations checklist
13. Known limitations
14. Recommended next step

---

## Block Conditions

Stop and report blocked if:

- `<BLOCK_CONDITION_1>`
- `<BLOCK_CONDITION_2>`
- Scope expansion beyond approved boundaries is needed
- Safety boundary exception is needed without Product Owner approval
- Required files or state are missing from the repository
- Secret scans reveal actual credentials
- Local path scans reveal real machine-specific paths
