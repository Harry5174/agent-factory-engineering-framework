# IDE Agent Bootstrap Template

> **Purpose:** Give an IDE Agent all the context, scope, commands, safety rules, and evidence expectations it needs to execute a sprint without drift.
>
> **When to use:** At the start of an IDE Agent implementation session, after the Implementation Supervisor has prepared the sprint.
>
> **Required inputs:** Sprint prompt or Implementation Supervisor bootstrap, repository state.
>
> **Required outputs:** All deliverables listed in the sprint scope, plus a completion report with evidence.
>
> **Instructions:** Copy this template and replace all `<PLACEHOLDER>` fields with current values.

---

## Sprint Identity

| Field | Value |
|-------|-------|
| **Project** | `<PROJECT_NAME>` |
| **Artifact** | `<ARTIFACT_NAME>` |
| **Sprint** | `<SPRINT_NAME>` |
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

## Repository Path

```text
<REPO_PATH> (e.g., 03-agent-factory/xx-projects/07-github-repo-steward-agent)
```

---

## Branch Instructions

```text
Branch name: <BRANCH_NAME> (e.g., artifact-7.1-foundation-scaffold)
Base branch: <BASE_BRANCH> (e.g., main)
Create from: <CREATE_FROM> (e.g., latest main)
```

---

## Repository Verification

Run these commands before starting any work:

```bash
git branch --show-current
git status -sb
git status --short
git log --oneline -8
git check-ignore -v .env || true
git ls-files .env
git ls-files "*__pycache__*"
git ls-files "*.pyc"
```

**Expected state:**

```text
Branch: <EXPECTED_BRANCH>
Clean: <yes/no>
Latest commit: <EXPECTED_COMMIT>
```

If state does not match expectations, **stop and report the discrepancy** before proceeding.

---

## Files to Review

Read these files before starting implementation:

- [ ] `<FILE_PATH_1>` — `<REASON>`
- [ ] `<FILE_PATH_2>` — `<REASON>`

---

## Pre-Implementation Plan

Before writing any code or docs, confirm this plan:

1. `<STEP_1>`
2. `<STEP_2>`
3. `<STEP_3>`

---

## Allowed Edits

You may:

- `<ALLOWED_EDIT_1>`
- `<ALLOWED_EDIT_2>`

---

## Forbidden Edits

You must not:

- `<FORBIDDEN_EDIT_1>`
- `<FORBIDDEN_EDIT_2>`
- Modify any file outside the sprint scope
- Read or print `.env` contents
- Print tokens or credentials
- Run live external side effects without explicit Product Owner approval
- Push or tag without Product Owner approval

---

## Anti-Drift Guard

### What this session must NOT assume

- `<ASSUMPTION_TO_AVOID_1>`
- `<ASSUMPTION_TO_AVOID_2>`
- Do not assume prior work is merged to main unless verified
- Do not assume approval for actions not explicitly listed

### What must be verified from the repository

- Branch, commit, and working tree cleanliness
- Required input files exist and match expectations
- No conflicting changes in the working tree

### What decisions are already settled

- `<SETTLED_DECISION_1>`
- `<SETTLED_DECISION_2>`

### What decisions are still open

- `<OPEN_DECISION_1>` (resolve during implementation or stop and escalate)

### What would count as scope drift

- Creating files outside the sprint's scope
- Modifying artifact runtime code when the sprint is docs-only
- Adding dependencies, APIs, or CLI tooling not in scope
- Expanding into a future artifact's work

### When to stop and ask for clarification

- Scope is ambiguous or contradictory
- A required input file is missing or stale
- A safety boundary would need to be relaxed
- An unexpected test failure suggests a broader issue

---

## Safety Invariants

> These safety rules apply to this session. See [Safety Boundary Protocol](../protocols/safety-boundary-protocol.md).

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

## Commands to Run

### Before Implementation

```bash
git branch --show-current
git status -sb
git log --oneline -8
```

### After Implementation

```bash
git status -sb
git diff --check
<TEST_COMMAND> (e.g., pytest, or skip with reason for docs-only sprints)
<LINT_COMMAND> (e.g., ruff check ., or skip with reason)
```

### Safety Scans

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

## Evidence to Collect

During and after implementation, collect:

- [ ] Branch name and commit hash (with base commit)
- [ ] List of files created (with descriptions)
- [ ] List of files modified (with descriptions)
- [ ] Command output for all commands run
- [ ] Test results (or documented reason for skipping)
- [ ] Lint results (or documented reason for skipping)
- [ ] Secret scan results
- [ ] Local path scan results
- [ ] `.env` verification results
- [ ] Scope confirmations (what was NOT changed)
- [ ] Safety confirmations checklist
- [ ] Known limitations
- [ ] `<ADDITIONAL_SPRINT_SPECIFIC_EVIDENCE>`

---

## Commit Instructions

```text
Commit message: <COMMIT_MESSAGE> (e.g., "feat: scaffold Artifact 7 foundation")
Files to stage: <STAGE_COMMAND> (e.g., "git add xx-projects/07-github-repo-steward-agent")
Do not push: true
Do not tag: true
```

---

## Completion Report Format

Return a completion report using the [Completion Report Template](completion-report-template.md) with all evidence collected above.

The completion report must demonstrate that:

1. Every deliverable was completed
2. Every safety boundary was respected
3. Evidence supports all claims
4. Known limitations are stated honestly
5. The recommended next step is actionable
