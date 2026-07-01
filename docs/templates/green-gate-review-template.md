# Green Gate Review Template

> **Instructions:** Fill in this template when reviewing a sprint's completion report.

---

## Review Identity

| Field | Value |
|-------|-------|
| **Artifact** | [e.g., Artifact 07 — GitHub Repo Steward Agent] |
| **Sprint** | [e.g., A7.1 — Foundation Scaffold] |
| **Reviewer** | [who is reviewing] |
| **Date** | [date] |

---

## Decision

> **Gate outcome: [GREEN / YELLOW / RED]**

[One-sentence summary of the decision.]

---

## Scope Assessment

| Criterion | Status | Notes |
|-----------|--------|-------|
| All deliverables completed | [✅ / ⚠️ / ❌] | [notes] |
| No scope creep | [✅ / ⚠️ / ❌] | [notes] |
| Out-of-scope items correctly excluded | [✅ / ⚠️ / ❌] | [notes] |

---

## Evidence Assessment

| Category | Quality | Notes |
|----------|---------|-------|
| Branch and commit | [strong / acceptable / weak / missing] | [notes] |
| Files created/modified | [strong / acceptable / weak / missing] | [notes] |
| Commands run | [strong / acceptable / weak / missing] | [notes] |
| Test results | [strong / acceptable / weak / missing] | [notes] |
| Lint results | [strong / acceptable / weak / missing] | [notes] |
| Safety scans | [strong / acceptable / weak / missing] | [notes] |
| Scope confirmations | [strong / acceptable / weak / missing] | [notes] |

---

## Tests Assessment

| Criterion | Status | Notes |
|-----------|--------|-------|
| Required tests run | [✅ / ⚠️ / ❌] | [notes] |
| Tests pass | [✅ / ⚠️ / ❌] | [notes] |
| No missing test scenarios | [✅ / ⚠️ / ❌] | [notes] |

---

## Safety Assessment

| Criterion | Status | Notes |
|-----------|--------|-------|
| No secrets committed | [✅ / ⚠️ / ❌] | [notes] |
| `.env` untracked | [✅ / ⚠️ / ❌] | [notes] |
| No unauthorized side effects | [✅ / ⚠️ / ❌] | [notes] |
| Safety scans clean | [✅ / ⚠️ / ❌] | [notes] |

---

## Acceptance Criteria

- [ ] Sprint goal met
- [ ] Evidence quality is acceptable or better
- [ ] Safety boundaries respected
- [ ] Known limitations are documented
- [ ] No overclaims detected

---

## Risks

[List any risks identified during review.]

- [risk 1]
- [risk 2]

---

## Known Limitations

[List known limitations acknowledged in this review.]

- [limitation 1]
- [limitation 2]

---

## Gate Outcome

| Outcome | Details |
|---------|---------|
| **Decision** | [GREEN / YELLOW / RED] |
| **Rationale** | [why this outcome] |
| **Follow-up required** | [for yellow: what follow-up items] |
| **Fixes required** | [for red: what must be fixed] |

---

## Next Sprint

**Recommended next sprint:** [sprint name]
**Next sprint goal:** [one-sentence goal]
**Prerequisites:** [any prerequisites]
