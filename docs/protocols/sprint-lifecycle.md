# Sprint Lifecycle Protocol

A sprint is a bounded unit of work within an artifact. Every sprint follows this lifecycle.

---

## 1. Sprint Identity

Every sprint has:

| Field | Description |
|-------|-------------|
| **Sprint name** | e.g., `AFDF.0`, `A7.1` |
| **Sprint goal** | One-sentence description of what this sprint achieves |
| **Parent artifact** | The artifact this sprint belongs to |
| **Scope boundaries** | What is in scope and what is explicitly out of scope |

---

## 2. Pre-Implementation Review

Before implementation begins:

1. The **Design Supervisor** reviews the sprint scope
2. The **Implementation Supervisor** prepares the sprint prompt
3. The sprint prompt defines:
   - Deliverables
   - Allowed and forbidden edits
   - Tests required
   - Evidence required
   - Block conditions
   - Completion report requirements

---

## 3. Product Owner Approval

The **Product Owner** approves the sprint scope before implementation begins.

- For docs-only sprints, approval may be implicit
- For runtime changes, approval must be explicit
- For live side effects, approval must be explicit and recorded

---

## 4. Implementation

The **IDE Agent** or implementer executes the sprint prompt:

1. Create branch
2. Follow the implementation plan
3. Respect scope boundaries
4. Collect evidence during execution

---

## 5. Evidence Collection

During and after implementation, collect:

| Evidence Type | Description |
|---------------|-------------|
| Branch and commit | Git branch name and commit hash |
| Files created | List of new files |
| Files modified | List of changed files |
| Commands run | All commands executed |
| Test results | pytest, unit tests, integration tests |
| Lint results | ruff, eslint, etc. |
| Safety checks | Token scans, secret checks, `.env` verification |
| Scope confirmations | Explicit statements about what was not changed |

---

## 6. Completion Report

Fill in the [Completion Report Template](../templates/completion-report-template.md) with:

- All evidence from Step 5
- Known limitations
- Recommended next step

---

## 7. Green/Yellow/Red Gate

The **Design Supervisor** or **Reviewer** evaluates the completion report:

| Gate | Meaning |
|------|---------|
| **Green** | Accepted. Next sprint may begin. |
| **Yellow** | Accepted with minor follow-up. Next sprint may begin carefully. |
| **Red** | Blocked or rejected. Fix required before next sprint. |

### Gate Criteria

- **Scope:** Did the sprint deliver what was promised and only what was promised?
- **Evidence:** Is the evidence strong enough to support the claims?
- **Tests:** Did tests pass? Are there missing tests?
- **Safety:** Were safety boundaries respected? No secrets, no unauthorized side effects?
- **Quality:** Is the work clean, documented, and maintainable?

---

## 8. Next Sprint Recommendation

After the gate decision:

1. State the recommended next sprint (name and goal)
2. State any prerequisites or blockers
3. Update project memory
4. Prepare the next-session handoff
