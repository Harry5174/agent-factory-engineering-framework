# Green Gate Review Template

> **Purpose:** Evaluate a sprint's completion report and issue a GREEN / YELLOW / RED gate decision.
>
> **When to use:** After receiving a completion report, before approving the next sprint.
>
> **Required inputs:** Sprint prompt, completion report, evidence, repository access.
>
> **Required outputs:** Gate decision with per-criterion assessments.
>
> **Instructions:** Replace all `<PLACEHOLDER>` fields with review findings.

---

## Review Identity

| Field | Value |
|-------|-------|
| **Artifact** | `<ARTIFACT_NAME>` |
| **Sprint** | `<SPRINT_NAME>` |
| **Reviewer** | `<REVIEWER>` |
| **Date** | `<DATE>` |

---

## Decision

> **Gate outcome: `<GREEN / YELLOW / RED>`**

`<ONE_SENTENCE_SUMMARY>`

---

## Product Owner Approval Verification

| Field | Status |
|-------|--------|
| Approval was obtained before implementation | `<✅ / ⚠️ / ❌>` |
| Implementation stayed within approval scope | `<✅ / ⚠️ / ❌>` |
| Approval limitations were respected | `<✅ / ⚠️ / ❌>` |

---

## Scope Assessment

| Criterion | Status | Notes |
|-----------|--------|-------|
| All deliverables completed | `<✅ / ⚠️ / ❌>` | `<NOTES>` |
| No scope creep | `<✅ / ⚠️ / ❌>` | `<NOTES>` |
| Out-of-scope items correctly excluded | `<✅ / ⚠️ / ❌>` | `<NOTES>` |

---

## Evidence Assessment

| Category | Quality | Notes |
|----------|---------|-------|
| Branch and commit | `<strong / acceptable / weak / missing>` | `<NOTES>` |
| Base commit | `<strong / acceptable / weak / missing>` | `<NOTES>` |
| Files created/modified | `<strong / acceptable / weak / missing>` | `<NOTES>` |
| Commands run | `<strong / acceptable / weak / missing>` | `<NOTES>` |
| Test results | `<strong / acceptable / weak / missing>` | `<NOTES>` |
| Lint results | `<strong / acceptable / weak / missing>` | `<NOTES>` |
| Secret scans | `<strong / acceptable / weak / missing>` | `<NOTES>` |
| Local path scans | `<strong / acceptable / weak / missing>` | `<NOTES>` |
| `.env` verification | `<strong / acceptable / weak / missing>` | `<NOTES>` |
| Scope confirmations | `<strong / acceptable / weak / missing>` | `<NOTES>` |
| Safety confirmations | `<strong / acceptable / weak / missing>` | `<NOTES>` |

---

## Tests Assessment

| Criterion | Status | Notes |
|-----------|--------|-------|
| Required tests run | `<✅ / ⚠️ / ❌>` | `<NOTES>` |
| Tests pass | `<✅ / ⚠️ / ❌>` | `<NOTES>` |
| Skip reason valid (if skipped) | `<✅ / ⚠️ / ❌ / N/A>` | `<NOTES>` |

---

## Safety Assessment

| Criterion | Status | Notes |
|-----------|--------|-------|
| No secrets committed | `<✅ / ⚠️ / ❌>` | `<NOTES>` |
| `.env` untracked | `<✅ / ⚠️ / ❌>` | `<NOTES>` |
| No unauthorized side effects | `<✅ / ⚠️ / ❌>` | `<NOTES>` |
| Safety scans clean or explained | `<✅ / ⚠️ / ❌>` | `<NOTES>` |
| No real local paths in content | `<✅ / ⚠️ / ❌>` | `<NOTES>` |

---

## Overclaim Check

| Check | Status | Notes |
|-------|--------|-------|
| No evidence-free claims | `<✅ / ⚠️ / ❌>` | `<NOTES>` |
| No stale artifact status claims | `<✅ / ⚠️ / ❌>` | `<NOTES>` |
| Limitations stated honestly | `<✅ / ⚠️ / ❌>` | `<NOTES>` |

---

## Acceptance Criteria

- [ ] Sprint goal met
- [ ] Evidence quality is acceptable or better for all categories
- [ ] Safety boundaries respected
- [ ] Known limitations documented
- [ ] No overclaims detected
- [ ] Product Owner approval scope respected

---

## Risks

- `<RISK_1>`
- `<RISK_2>`

---

## Known Limitations

- `<LIMITATION_1>`
- `<LIMITATION_2>`

---

## Gate Outcome

| Field | Value |
|-------|-------|
| **Decision** | `<GREEN / YELLOW / RED>` |
| **Rationale** | `<WHY_THIS_OUTCOME>` |
| **Follow-up required** | `<FOR_YELLOW_WHAT_ITEMS>` (or "N/A") |
| **Fixes required** | `<FOR_RED_WHAT_MUST_BE_FIXED>` (or "N/A") |

---

## Next Sprint

| Field | Value |
|-------|-------|
| **Recommended next sprint** | `<SPRINT_NAME>` |
| **Next sprint goal** | `<GOAL>` |
| **Prerequisites** | `<PREREQUISITES>` |
