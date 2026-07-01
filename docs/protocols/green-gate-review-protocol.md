# Green Gate Review Protocol

How Design Supervisors and Reviewers conduct gate reviews at the end of a sprint.

---

## 1. Gate Outcomes

| Gate | Meaning | Next Action |
|------|---------|-------------|
| **Green** | Accepted. All criteria met. | Next sprint may begin. Update project memory. |
| **Yellow** | Accepted with minor follow-up. | Next sprint may begin carefully. Follow-up items must be tracked. |
| **Red** | Blocked or rejected. | Fix required before next sprint. Do not proceed. |

---

## 2. Review Inputs

The reviewer needs:

1. The **sprint prompt** (what was requested)
2. The **completion report** (what was delivered)
3. The **evidence** (proof of delivery)
4. Access to the **repository** (to verify claims if needed)

---

## 3. Review Criteria

### 3.1 Scope Assessment

- Did the sprint deliver everything in the scope?
- Did the sprint deliver only what was in scope (no scope creep)?
- Are out-of-scope items correctly listed as not done?

### 3.2 Evidence Assessment

Use the [Evidence Review Protocol](evidence-review-protocol.md) to evaluate:

- Is evidence present for all required categories?
- What is the evidence quality level (strong / acceptable / weak / missing)?
- Are there overclaims?

### 3.3 Tests Assessment

- Were required tests run?
- Did tests pass?
- Are there missing test scenarios?
- If tests were skipped, is the reason documented and valid?

### 3.4 Safety Assessment

- Were safety boundaries respected?
- Were safety scans run and clean?
- Is `.env` confirmed as untracked?
- Were no secrets committed or exposed?
- Were no unauthorized live side effects executed?

### 3.5 Quality Assessment

- Is the work clean and maintainable?
- Is documentation clear and honest?
- Are known limitations stated?

---

## 4. Gate Decision Process

1. Review each criterion (scope, evidence, tests, safety, quality)
2. Assign a per-criterion status:
   - ✅ Pass
   - ⚠️ Minor issue (acceptable for yellow gate)
   - ❌ Blocking issue (requires red gate)
3. Determine overall gate:
   - **Green:** All criteria pass
   - **Yellow:** All criteria pass or have only minor issues; follow-up items are tracked
   - **Red:** Any criterion has a blocking issue

---

## 5. Gate Report

Fill in the [Green Gate Review Template](../templates/green-gate-review-template.md) with:

- Decision (green / yellow / red)
- Per-criterion assessments
- Risks and concerns
- Known limitations
- Required follow-up (for yellow)
- Required fixes (for red)
- Recommended next sprint

---

## 6. After the Gate

| Gate | Actions |
|------|---------|
| **Green** | Update project memory. Prepare next-session handoff. Merge/tag if Product Owner approves. |
| **Yellow** | Update project memory. Track follow-up items. Prepare next-session handoff with caveats. |
| **Red** | Document required fixes. Do not update project memory. Do not merge. Re-sprint or fix before retrying gate. |
