# Completion Report Template

> **Purpose:** Document what was done in a sprint with structured evidence so reviewers can evaluate claims, verify safety, and make gate decisions.
>
> **When to use:** At the end of every sprint, before requesting a green-gate review.
>
> **Required inputs:** All evidence collected during the sprint.
>
> **Required outputs:** A filled report that covers every evidence category below.
>
> **Instructions:** Replace all `<PLACEHOLDER>` fields with actual values and evidence.

---

## Sprint Summary

| Field | Value |
|-------|-------|
| **Project** | `<PROJECT_NAME>` |
| **Artifact** | `<ARTIFACT_NAME>` |
| **Sprint** | `<SPRINT_NAME>` |
| **Sprint goal** | `<SPRINT_GOAL>` |
| **Date** | `<DATE>` |
| **Author** | `<AUTHOR>` |

---

## Product Owner Approval

| Field | Value |
|-------|-------|
| **Approval status** | `<APPROVAL_STATUS>` |
| **Approved by** | `<APPROVED_BY>` |
| **Approval scope** | `<APPROVAL_SCOPE>` |
| **Approval limitations** | `<APPROVAL_LIMITATIONS>` |

---

## Decision Summary

`<DECISION_SUMMARY>`

---

## Branch and Commit

```text
Branch: <BRANCH_NAME>
Commit: <COMMIT_HASH>
Base: <BASE_COMMIT>
```

---

## Files Reviewed

- `<FILE_PATH_1>`
- `<FILE_PATH_2>`

---

## Files Created

| File | Description |
|------|-------------|
| `<FILE_PATH>` | `<DESCRIPTION>` |

---

## Files Modified

| File | Change |
|------|--------|
| `<FILE_PATH>` | `<WHAT_CHANGED_AND_WHY>` |

---

## Commands Run

```bash
<COMMAND_AND_OUTPUT>
```

---

## Test and Lint Results

### Tests

```text
<TEST_OUTPUT_OR_SUMMARY>
```

### Lint

```text
<LINT_OUTPUT_OR_SUMMARY>
```

### If Tests/Lint Were Skipped

**Reason:** `<REASON>` (e.g., "docs-only sprint with no code changes")

---

## Safety Scans

### Secret Scans

```text
<TOKEN_SCAN_OUTPUT>
```

> If matches appear, explain whether they are intentional scan-pattern examples or real credentials.

### Local Path Scans

```text
<LOCAL_PATH_SCAN_OUTPUT>
```

> If matches appear, explain whether they are scan-pattern examples or real paths.

### `.env` Verification

```text
<GIT_CHECK_IGNORE_OUTPUT>
<GIT_LS_FILES_ENV_OUTPUT>
```

---

## Safety Confirmations

- [ ] No runtime behavior was changed
- [ ] No artifact code was modified
- [ ] No live GitHub execution occurred
- [ ] No credentials were required or read
- [ ] `.env` remained ignored/untracked
- [ ] No real tokens in committed content
- [ ] No real local paths in committed content
- [ ] Product Owner approval scope was respected

---

## Scope Confirmations

- `<SCOPE_CONFIRMATION_1>` (e.g., "No changes to Artifact 04/05/06 runtime code")
- `<SCOPE_CONFIRMATION_2>` (e.g., "Artifact 07 was not created")

---

## Known Limitations

- `<LIMITATION_1>`
- `<LIMITATION_2>`

---

## Recommended Next Step

| Field | Value |
|-------|-------|
| **Next sprint** | `<NEXT_SPRINT_NAME>` |
| **Next sprint goal** | `<NEXT_SPRINT_GOAL>` |
| **Prerequisites** | `<PREREQUISITES>` |
