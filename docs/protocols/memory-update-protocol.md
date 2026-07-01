# Memory Update Protocol

> **Purpose:** Ensure that the living project memory remains accurate and reflects reality after every sprint.

---

## When Memory is Updated
Memory must be updated at the end of every sprint, **after** a completion report has been submitted and reviewed.

## Who Updates It
- The **Design Supervisor** or **Product Owner** updates memory during a green-gate review.
- Or, the **IDE Agent** updates memory as the final step of a green-gated sprint, under explicit instruction from the Implementation Supervisor.

## Required Evidence
Memory updates must be grounded in facts. 
- You cannot claim an artifact is "complete" without a submitted completion report.
- You cannot claim an artifact is "published" without evidence of a git tag and merge to main.

## Files to Touch After a GREEN Gate
1. `project-memory.md` (Update current sprint/status).
2. `decision-log.md` (Record any new decisions made during the sprint).
3. `evidence-index.md` (Link to the new completion report and evidence artifacts).
4. `artifact-map.md` (Update the status of the current artifact).

## Files to Touch After a YELLOW Gate
1. `technical-debt-register.md` (Log the required follow-ups that caused the yellow gate).
2. `known-limitations-register.md` (If the sprint succeeded but revealed a new limitation).

## What NOT to Update After a RED Gate
- Do not update the `artifact-map.md` to "Complete".
- Do not update `project-memory.md` to claim success.
- The sprint must be retried or rescoped.

## Handling Unknowns
If a status is unknown (e.g., "Did the operator tag this release?"), mark it explicitly as **"Unknown — requires verification"**. Do not assume success.

## Avoiding Stale Claims
Do not make forward-looking claims in memory. 
- **Incorrect:** "Artifact 07 is built and uses a fake LLM." (If A7 hasn't started).
- **Correct:** "Artifact 07 is planned to use a fake LLM."
