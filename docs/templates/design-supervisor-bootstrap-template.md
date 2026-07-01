# Design Supervisor Bootstrap Template

> **Purpose:** Bootstrap a Design Supervisor session with full project context so the session can make scope, design, and gate decisions without recreating knowledge from scratch.
>
> **When to use:** At the start of any design session — artifact scoping, sprint planning, green-gate review, or design review.
>
> **Required inputs:** Latest project memory, latest completion report, current repository state.
>
> **Required outputs:** Scope decisions, gate decisions, updated project memory, next-session handoff.
>
> **Instructions:** Copy this template and replace all `<PLACEHOLDER>` fields with current values.

---

## Project Context

| Field | Value |
|-------|-------|
| **Project** | `<PROJECT_NAME>` |
| **Repository** | `<REPO_URL>` |
| **Workspace** | `<WORKSPACE_PATH>` (e.g., `03-agent-factory`) |

---

## Current Phase

| Field | Value |
|-------|-------|
| **Phase** | `<PHASE_NAME>` (e.g., Phase 03 — Vertical Agents) |
| **Phase goal** | `<PHASE_GOAL>` |

---

## Current Artifact

| Field | Value |
|-------|-------|
| **Artifact** | `<ARTIFACT_NAME>` (e.g., Artifact 07 — GitHub Repo Steward Agent) |
| **Artifact status** | `<ARTIFACT_STATUS>` (e.g., Design phase / Sprint X complete / Published) |

---

## Current Sprint

| Field | Value |
|-------|-------|
| **Sprint** | `<SPRINT_NAME>` (e.g., A7.0 — Foundation Design) |
| **Sprint goal** | `<SPRINT_GOAL>` |
| **Sprint status** | `<SPRINT_STATUS>` (e.g., Not started / In progress / Complete) |

---

## Product Owner Approval

| Field | Value |
|-------|-------|
| **Approval status** | `<APPROVAL_STATUS>` (e.g., Approved / Pending / Not yet requested) |
| **Approved by** | `<APPROVED_BY>` (e.g., Product Owner name or "pending") |
| **Approval evidence** | `<APPROVAL_EVIDENCE>` (e.g., link to approval message, or "verbal") |
| **Approval scope** | `<APPROVAL_SCOPE>` (e.g., "Design session for Artifact 07 scoping") |
| **Approval limitations** | `<APPROVAL_LIMITATIONS>` (e.g., "No live GitHub execution approved") |

---

## Repository Links

| Resource | Path |
|----------|------|
| Artifact folder | `<ARTIFACT_FOLDER_PATH>` |
| Artifact spec | `<ARTIFACT_SPEC_PATH>` |
| Latest completion report | `<LATEST_COMPLETION_REPORT_PATH>` (or "none yet") |
| Project memory | `<PROJECT_MEMORY_PATH>` (or "not yet instantiated") |
| Decision log | `<DECISION_LOG_PATH>` (or "not yet instantiated") |
| Development framework | `<DEV_FRAMEWORK_PATH>` |

---

## Repository Verification

Run these commands at session start to confirm repository state:

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

## Completed Work

> Be specific about what was **proven**, not just what was attempted. Reference evidence.

`<COMPLETED_WORK_SUMMARY>`

---

## Approved Decisions

> These decisions are settled and should not be revisited unless explicitly reopened by the Product Owner.

| Decision | Date | Reference |
|----------|------|-----------|
| `<DECISION_1>` | `<DATE>` | `<REFERENCE>` |
| `<DECISION_2>` | `<DATE>` | `<REFERENCE>` |

---

## Open Decisions

> These decisions need to be made in this session.

| Decision Needed | Context | Options |
|-----------------|---------|---------|
| `<DECISION_NEEDED_1>` | `<CONTEXT>` | `<OPTIONS>` |
| `<DECISION_NEEDED_2>` | `<CONTEXT>` | `<OPTIONS>` |

---

## Non-Goals

> What this session explicitly will NOT do.

- `<NON_GOAL_1>`
- `<NON_GOAL_2>`
- Do not implement runtime code
- Do not modify existing artifact behavior
- Do not start the next artifact unless explicitly approved

---

## Anti-Drift Guard

> Prevent this session from hallucinating project state.

### What this session must NOT assume

- `<ASSUMPTION_TO_AVOID_1>` (e.g., "Do not assume Artifact 06 is published/tagged")
- `<ASSUMPTION_TO_AVOID_2>` (e.g., "Do not assume the previous branch was merged to main")

### What must be verified from the repository

- Current branch and commit match expectations
- Artifact status claims match actual git tag/merge state
- Previous sprint's completion report exists and was green-gated

### What decisions are already settled

> Reference the Approved Decisions section above.

### What decisions are still open

> Reference the Open Decisions section above.

### What would count as scope drift

- Expanding into artifact implementation
- Adding runtime features not in the sprint scope
- Designing beyond the current artifact's boundaries
- Making safety boundary exceptions without Product Owner approval

### When to stop and ask for clarification

- Scope is ambiguous or contradictory
- A required input is missing or stale
- A safety boundary would need to be relaxed
- A prior decision needs to be reversed

---

## Safety Invariants

> These safety rules apply to this session. See [Safety Boundary Protocol](../protocols/safety-boundary-protocol.md).

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

## Files to Review

> List specific files the Design Supervisor should review before making decisions.

- [ ] `<FILE_PATH_1>` — `<REASON>`
- [ ] `<FILE_PATH_2>` — `<REASON>`

---

## Questions to Answer

> List specific questions this session must answer.

1. `<QUESTION_1>`
2. `<QUESTION_2>`

---

## Expected Output

> What the Design Supervisor must produce at the end of this session.

- [ ] `<OUTPUT_1>` (e.g., "Approved sprint scope for A7.1")
- [ ] `<OUTPUT_2>` (e.g., "Green-gate decision for A7.0")
- [ ] `<OUTPUT_3>` (e.g., "Updated project memory")
- [ ] Next-session handoff document (if applicable)
