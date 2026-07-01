# Session Lifecycle Protocol

Every session — design, implementation, or review — follows this lifecycle. Sessions have **no reliable prior memory** unless a bootstrap document gives it to them.

---

## 1. Start-of-Session Bootstrap

**Purpose:** Give the new session all the context it needs to begin without recreating knowledge from scratch.

**Steps:**

1. Identify the session role (Design Supervisor, Implementation Supervisor, IDE Agent, Reviewer)
2. Select the appropriate bootstrap template from `docs/templates/`
3. Fill in the bootstrap with current project state from:
   - Latest `docs/memory/project-memory-template.md` (or the active project memory instance)
   - Latest `docs/status/project-status.md`
   - Latest completion report from the previous sprint
   - Latest next-session handoff document
4. Include the bootstrap as the opening context for the session

**Key rule:** New sessions have no reliable prior memory. If the bootstrap does not contain a fact, the session should not assume it.

---

## 2. Repository/Context Verification

**Purpose:** Confirm that the repository matches expected state before beginning work.

**Steps:**

1. Run the commands defined in the [Repository Inspection Protocol](repository-inspection-protocol.md)
2. Verify branch, commit, and file state match the bootstrap expectations
3. If state does not match, stop and report the discrepancy

---

## 3. Scope Confirmation

**Purpose:** Confirm what this session will and will not do.

**Steps:**

1. Read the sprint scope from the bootstrap or sprint prompt
2. Confirm the scope boundaries (allowed and forbidden actions)
3. Identify any block conditions
4. If scope is ambiguous, stop and request clarification

---

## 4. Implementation Plan

**Purpose:** Define the concrete steps before execution begins.

**Steps:**

1. List the files to create, modify, or review
2. List the commands to run
3. List the tests and checks required
4. Identify any dependencies or ordering constraints
5. Confirm the plan aligns with sprint scope

---

## 5. Work Execution

**Purpose:** Perform the approved work.

**Steps:**

1. Execute the implementation plan
2. Follow scope boundaries strictly
3. If a block condition is encountered, stop and report
4. If scope expansion is needed, stop and request approval

---

## 6. Evidence Collection

**Purpose:** Gather artifacts that prove the work was done correctly.

**Steps:**

1. Record commands run and their output
2. Record test results
3. Record lint/check results
4. Record safety scans (token scans, secret checks, `.env` verification)
5. Record files created and modified
6. Record any scope boundary confirmations

---

## 7. Completion Report

**Purpose:** Produce a structured summary of the sprint's work.

**Steps:**

1. Fill in the [Completion Report Template](../templates/completion-report-template.md)
2. Include all evidence from Step 6
3. State known limitations honestly
4. Recommend the next step

---

## 8. Green-Gate Review

**Purpose:** A Design Supervisor or Reviewer evaluates the completion report.

**Steps:**

1. Review the completion report using the [Green Gate Review Protocol](green-gate-review-protocol.md)
2. Evaluate evidence quality using the [Evidence Review Protocol](evidence-review-protocol.md)
3. Issue a green/yellow/red gate outcome

---

## 9. Memory Update

**Purpose:** Preserve decisions, lessons, and state for future sessions.

**Steps:**

1. Update the project memory document
2. Add entries to the decision log if decisions were made
3. Add entries to lessons learned if applicable
4. Update known limitations if boundaries changed
5. Update technical debt if cleanup items were identified

---

## 10. Next-Session Handoff

**Purpose:** Prepare the context for whoever works next.

**Steps:**

1. Fill in the [Next Session Handoff Template](../templates/next-session-handoff-template.md)
2. State what the next session should know
3. State what the next session must not assume
4. Include the current repo state (branch, commit, tag)
5. Include any blockers or required first commands
