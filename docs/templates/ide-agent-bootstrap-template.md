# IDE Agent Bootstrap Template

> **Instructions:** Copy this template and fill in the bracketed fields to bootstrap an IDE Agent session.

---

## Repository Path

```text
[e.g., 03-agent-factory/xx-projects/07-github-repo-steward-agent]
```

---

## Branch Instructions

```text
Branch name: [e.g., artifact-7.1-foundation-scaffold]
Base branch: [e.g., main]
Create from: [e.g., latest main]
```

---

## Files to Review

Read these files before starting implementation:

- [ ] [file path 1] — [why]
- [ ] [file path 2] — [why]

---

## Pre-Implementation Plan

Before writing any code or docs, confirm this plan:

1. [step 1]
2. [step 2]
3. [step 3]

---

## Allowed Edits

You may:

- [allowed edit 1]
- [allowed edit 2]

---

## Forbidden Edits

You must not:

- [forbidden edit 1]
- [forbidden edit 2]
- Modify any file outside the sprint scope
- Read or print `.env` contents
- Print tokens or credentials
- Run live external side effects without explicit approval

---

## Commands to Run

### Before Implementation

```bash
[pre-implementation command 1]
[pre-implementation command 2]
```

### After Implementation

```bash
[post-implementation command 1, e.g., pytest]
[post-implementation command 2, e.g., ruff check .]
[safety scan command]
```

---

## Evidence to Collect

During and after implementation, collect:

- [ ] Branch name and commit hash
- [ ] List of files created
- [ ] List of files modified
- [ ] Command output for all commands run
- [ ] Test results
- [ ] Lint results
- [ ] Safety scan results (token scan, `.env` check)
- [ ] [additional sprint-specific evidence]

---

## Commit Instructions

```text
Commit message: [e.g., "feat: scaffold Artifact 7 foundation"]
Files to stage: [e.g., "git add xx-projects/07-github-repo-steward-agent"]
Do not push: [true/false]
Do not tag: [true/false]
```

---

## Completion Report Format

Return a completion report using the [Completion Report Template](completion-report-template.md) with all evidence collected above.
