# Completion Report Template

> **Instructions:** Fill in this template at the end of a sprint to document what was done and provide evidence.

---

## Sprint Summary

| Field | Value |
|-------|-------|
| **Artifact** | [e.g., Artifact 07 — GitHub Repo Steward Agent] |
| **Sprint** | [e.g., A7.1 — Foundation Scaffold] |
| **Sprint goal** | [one-sentence goal] |
| **Date** | [date] |
| **Author** | [who completed the sprint] |

---

## Decision Summary

[Summarize key decisions made during the sprint. Reference decision log entries if applicable.]

---

## Branch and Commit

```text
Branch: [branch name]
Commit: [commit hash]
Base: [base branch, e.g., main]
```

---

## Files Reviewed

[List files that were reviewed/inspected before implementation.]

- [file path 1]
- [file path 2]

---

## Files Created

| File | Description |
|------|-------------|
| [file path] | [what this file is] |

---

## Files Modified

| File | Change |
|------|--------|
| [file path] | [what changed and why] |

---

## Commands Run

```bash
[command 1 and relevant output]
[command 2 and relevant output]
```

---

## Test and Lint Results

### Tests

```text
[test output or summary]
```

### Lint

```text
[lint output or summary]
```

### If Tests/Lint Were Skipped

**Reason:** [why tests or lint were not run, e.g., "docs-only sprint with no code changes"]

---

## Safety Scans

### Secret Scans

```text
[output of token/credential scan]
```

### Local Path Scans

```text
[output of local path scan]
```

### `.env` Verification

```text
[output of git check-ignore and git ls-files for .env]
```

---

## Safety Confirmations

- [ ] No runtime behavior was changed
- [ ] No artifact code was modified
- [ ] No live GitHub execution occurred
- [ ] No credentials were required or read
- [ ] `.env` remained ignored/untracked
- [ ] No real tokens or local paths in committed content

---

## Known Limitations

[Honest description of what is not covered, not complete, or not ideal.]

- [limitation 1]
- [limitation 2]

---

## Recommended Next Step

**Next sprint:** [e.g., A7.2 — Core Agent Implementation]
**Next sprint goal:** [one-sentence goal]
**Prerequisites:** [any prerequisites for the next sprint]
