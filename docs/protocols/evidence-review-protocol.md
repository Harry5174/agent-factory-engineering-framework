# Evidence Review Protocol

How to evaluate the evidence in a completion report.

---

## 1. Required Evidence Categories

Every completion report should include evidence in these categories:

| Category | Description |
|----------|-------------|
| **Branch and commit** | The branch name and commit hash |
| **Files created** | List of new files with brief descriptions |
| **Files modified** | List of changed files with brief descriptions |
| **Commands run** | All commands executed during the sprint |
| **Test results** | Output of test runs (pytest, etc.) |
| **Lint results** | Output of linting tools (ruff, etc.) |
| **Safety checks** | Token scans, secret checks, `.env` verification |
| **Secret scans** | Results of scanning for hardcoded credentials |
| **Scope confirmations** | Explicit statements about what was not changed |
| **Known limitations** | Honest description of what is not covered |
| **Next step** | Recommended next sprint or action |

---

## 2. Evidence Quality Levels

### Strong Evidence

- Command output is included verbatim or summarized with key details
- Test results show pass counts and any failures
- Safety scans show no unexpected matches (or matches are explained)
- Scope confirmations are explicit and specific
- Known limitations are honest and not minimized

### Acceptable Evidence

- Evidence is present but abbreviated
- Test results are summarized without full output
- Safety scans were run but output is paraphrased
- Some scope confirmations are implicit rather than explicit

### Weak Evidence

- Evidence is claimed but not shown
- "Tests passed" without output or pass counts
- Safety scans mentioned but not shown
- Scope boundaries are vague

### Missing Evidence

- A required category has no entry
- A claim is made without any supporting evidence
- A required check was not run and no explanation is given

---

## 3. Evaluation Checklist

When reviewing a completion report, check:

- [ ] Does every claim have supporting evidence?
- [ ] Are test results included and do they pass?
- [ ] Were safety scans run and are results clean (or explained)?
- [ ] Is `.env` confirmed as gitignored/untracked?
- [ ] Are no real tokens, credentials, or local paths in committed content?
- [ ] Is the scope confirmation explicit (what was not changed)?
- [ ] Are known limitations stated honestly?
- [ ] Does the completion report match the sprint prompt deliverables?
- [ ] Is there any overclaim (claiming more than what was actually done)?
- [ ] Is the recommended next step reasonable?

---

## 4. Overclaim Detection

Watch for these patterns:

| Pattern | Example |
|---------|---------|
| **Scope inflation** | Sprint was docs-only but report claims "runtime improvements" |
| **Evidence-free claims** | "All tests pass" without test output |
| **Minimized limitations** | Omitting known gaps or stating them vaguely |
| **Assumed state** | "Artifact X is published" without verifying tag state |
| **Forward claims** | Claiming future work is done or will definitely happen |

---

## 5. Review Outcome

After evaluation, the reviewer provides:

1. **Evidence quality assessment** (strong / acceptable / weak / missing per category)
2. **Overclaim flags** (if any)
3. **Recommended corrections** (if any)
4. **Gate recommendation** (green / yellow / red)

This feeds into the [Green Gate Review Protocol](green-gate-review-protocol.md).
