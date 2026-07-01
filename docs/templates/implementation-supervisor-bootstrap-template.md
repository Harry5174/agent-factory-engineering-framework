# Implementation Supervisor Bootstrap Template

> **Purpose:** Prepare a sprint for an IDE Agent or implementer by translating an approved design into actionable instructions with clear scope, safety, and evidence requirements.
>
> **When to use:** After the Design Supervisor has approved a sprint scope — before handing off to the IDE Agent.
>
> **Required inputs:** Approved sprint scope from Design Supervisor, project memory, repository state.
>
> **Required outputs:** Sprint prompt or IDE Agent bootstrap with all context needed to execute without scope drift.
>
> **Instructions:** Copy this template and replace all `<PLACEHOLDER>` fields with current values.

---

## Approved Design Summary

| Field | Value |
|-------|-------|
| **Artifact** | `<ARTIFACT_NAME>` (e.g., Artifact 07 — GitHub Repo Steward Agent) |
| **Sprint** | `<SPRINT_NAME>` (e.g., A7.1 — Foundation Scaffold) |
| **Sprint goal** | `<SPRINT_GOAL>` |

---

## Product Owner Approval

| Field | Value |
|-------|-------|
| **Approval status** | `<APPROVAL_STATUS>` (e.g., Approved / Pending) |
| **Approved by** | `<APPROVED_BY>` |
| **Approval evidence** | `<APPROVAL_EVIDENCE>` (e.g., link to approval, or "sprint prompt delivery implies approval") |
| **Approval scope** | `<APPROVAL_SCOPE>` (e.g., "docs-only sprint" / "code sprint, no live execution") |
| **Approval limitations** | `<APPROVAL_LIMITATIONS>` (e.g., "No real GitHub execution approved") |

---

## Repository Verification

Run before preparing the sprint prompt:

```bash
git branch --show-current
git status -sb
git log --oneline -8
git check-ignore -v .env || true
git ls-files .env
```

**Expected state:**

```text
Branch: <EXPECTED_BRANCH>
Clean: <yes/no>
Latest commit: <EXPECTED_COMMIT>
```

---

## Scope Boundaries

### In Scope

- `<DELIVERABLE_1>`
- `<DELIVERABLE_2>`

### Out of Scope

- `<EXCLUDED_1>`
- `<EXCLUDED_2>`

### Block Conditions

Stop and report blocked if:

- `<BLOCK_CONDITION_1>`
- `<BLOCK_CONDITION_2>`
- Scope expansion beyond approved boundaries is requested
- Safety boundary exception is needed without Product Owner approval
- Required files or state are missing from the repository

---

## Anti-Drift Guard

### What the implementer must NOT assume

- `<ASSUMPTION_TO_AVOID_1>`
- `<ASSUMPTION_TO_AVOID_2>`
- Do not assume prior sprint work is merged unless verified
- Do not assume approval for actions not explicitly listed in scope

### What must be verified from the repository

- Branch and commit match the expected starting state
- Required input files exist and are current
- No unexpected changes in the working tree

### What decisions are already settled

- `<SETTLED_DECISION_1>`
- `<SETTLED_DECISION_2>`

### What decisions are still open

- `<OPEN_DECISION_1>` (resolve during implementation or escalate)

### What would count as scope drift

- Implementing features beyond the sprint deliverables
- Modifying files outside the sprint's scope
- Adding dependencies not approved in the sprint scope
- Making safety boundary exceptions

---

## Files to Inspect

> Files the implementer should read before starting work.

| File | Purpose |
|------|---------|
| `<FILE_PATH_1>` | `<WHY_THIS_FILE_MATTERS>` |
| `<FILE_PATH_2>` | `<WHY_THIS_FILE_MATTERS>` |

---

## Implementation Expectations

### Files to Create

| File | Description |
|------|-------------|
| `<FILE_PATH>` | `<WHAT_THIS_FILE_DOES>` |

### Files to Modify

| File | Change |
|------|--------|
| `<FILE_PATH>` | `<WHAT_CHANGES_AND_WHY>` |

### Implementation Notes

`<SPECIFIC_GUIDANCE_PATTERNS_CONSTRAINTS>`

---

## Tests Required

| Test | Command | Expected Result |
|------|---------|-----------------|
| `<TEST_NAME>` | `<COMMAND>` | `<EXPECTED_OUTCOME>` |

For docs-only sprints, minimum validation:

```bash
git diff --check
```

---

## Safety Invariants

> These safety rules apply to this sprint. See [Safety Boundary Protocol](../protocols/safety-boundary-protocol.md).

- Do not print secrets
- Do not read or paste `.env`
- Do not run live external side effects without explicit Product Owner approval
- Use fake/default mode unless real mode is explicitly approved
- Do not bypass approval gates
- LLM proposes; harness decides; operator approves
- Record evidence before claiming completion

### Inherited Safety Boundaries

- Artifact 04: real GitHub runtime safety (server-side token, allowlisted repos)
- Artifact 05: release-gate evidence safety (evidence required before claims)
- Artifact 06: local/demo operator workbench safety (no live GitHub for demo)

---

## Completion Report Requirements

The completion report must include:

- [ ] Branch and commit (with base commit)
- [ ] Files reviewed before implementation
- [ ] Files created (with descriptions)
- [ ] Files modified (with descriptions)
- [ ] Commands run (with relevant output)
- [ ] Test results (or reason for skipping)
- [ ] Lint results (or reason for skipping)
- [ ] Secret scan results
- [ ] Local path scan results
- [ ] `.env` verification results
- [ ] Scope confirmations (what was NOT changed)
- [ ] Safety confirmations checklist
- [ ] Known limitations
- [ ] Recommended next step
- [ ] `<ADDITIONAL_SPRINT_SPECIFIC_REQUIREMENTS>`

---

## Validation Commands

After implementation, the implementer must run:

```bash
git status -sb
git diff --check
git check-ignore -v .env || true
git ls-files .env
git ls-files "*__pycache__*"
git ls-files "*.pyc"
```

For content with potential secrets or local paths:

```bash
rg -n "ghp_|github_pat_|gho_|ghu_|ghs_|ghr_|Bearer |GITHUB_ACCESS_TOKEN=|AGENT_FACTORY_GITHUB_TOKEN=" \
  <SCAN_PATH> || true

rg -n "/home/|Desktop/|/Users/" \
  <SCAN_PATH> || true
```

> Matches that are intentional scan-pattern examples in documentation must be explained in the completion report.
