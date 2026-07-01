# Next Session Handoff Template

> **Purpose:** Prepare all context the next session needs to start without drift or hallucinated state.
>
> **When to use:** At the end of a sprint, after the green-gate review, before closing the session.
>
> **Required inputs:** Completion report, gate outcome, current repository state.
>
> **Required outputs:** A document the next session can use as its bootstrap context.
>
> **Instructions:** Replace all `<PLACEHOLDER>` fields with current values.

---

## Handoff Identity

| Field | Value |
|-------|-------|
| **From sprint** | `<CURRENT_SPRINT_NAME>` |
| **Gate outcome** | `<GREEN / YELLOW / RED>` |
| **To sprint** | `<NEXT_SPRINT_NAME>` |
| **Date** | `<DATE>` |

---

## What the Next Session Knows

> Facts the next session can rely on.

- `<FACT_1>` (e.g., "AFDF.1 templates are hardened and committed")
- `<FACT_2>` (e.g., "Framework lives at `03-agent-factory/development-framework/`")
- `<FACT_3>`

---

## What the Next Session Must NOT Assume

> The next session must verify these rather than assume them.

- `<ASSUMPTION_TO_AVOID_1>` (e.g., "Do not assume the branch has been merged to main")
- `<ASSUMPTION_TO_AVOID_2>` (e.g., "Do not assume Artifact 06 is fully published/tagged")
- Do not assume prior session context is available — start from this handoff

---

## Repository State

```text
Branch: <BRANCH_NAME>
Commit: <COMMIT_HASH>
Base: <BASE_COMMIT>
Tag: <TAG_OR_NONE>
Clean: <yes/no>
```

---

## Artifact State

| Artifact | Status |
|----------|--------|
| `<ARTIFACT_NAME_1>` | `<STATUS>` |
| `<ARTIFACT_NAME_2>` | `<STATUS>` |

---

## Product Owner Approval State

| Field | Value |
|-------|-------|
| **Current approval scope** | `<WHAT_IS_APPROVED>` |
| **Pending approvals** | `<WHAT_NEEDS_APPROVAL>` (or "none") |
| **Expired/consumed approvals** | `<WHAT_WAS_USED>` (or "none") |

---

## Approved Decisions

> Decisions the next session must honor.

| Decision | Date | Reference |
|----------|------|-----------|
| `<DECISION>` | `<DATE>` | `<REFERENCE>` |

---

## Current Blockers

- `<BLOCKER_1>` (or "None")

---

## Follow-Up Items (Yellow Gate Only)

- `<FOLLOW_UP_1>` (or "N/A — gate was GREEN")

---

## Required First Commands

The next session should run these commands first to verify state:

```bash
git branch --show-current
git status -sb
git log --oneline -8
git check-ignore -v .env || true
git ls-files .env
```

---

## Safety Reminders

- Do not print secrets
- Do not read or paste `.env`
- Do not run live external side effects without explicit Product Owner approval
- Use fake/default mode unless real mode is explicitly approved
- Record evidence before claiming completion

---

## Next Expected Output

The next session is expected to produce:

- [ ] `<EXPECTED_OUTPUT_1>`
- [ ] `<EXPECTED_OUTPUT_2>`
