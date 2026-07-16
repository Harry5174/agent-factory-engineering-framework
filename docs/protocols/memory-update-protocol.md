# Memory Update Protocol

> **Purpose:** Ensure that the living project memory remains accurate and reflects reality after every sprint.

---

## When Memory is Updated
Operational memory may be updated only after a completion report has been submitted and reviewed and when that update is explicitly authorized. AFEF source templates remain unchanged by adopter operations.

## Who Updates It
- The adopting repository defines who maintains its `.afef/` records.
- An **IDE Agent** may update those records only when the sprint prompt explicitly authorizes it.

## Required Evidence
Memory updates must be grounded in facts. 
- You cannot claim an artifact is "complete" without a submitted completion report.
- You cannot claim an artifact is "published" without evidence of a git tag and merge to main.

## Files to Touch After a GREEN Gate
1. `.afef/project-memory.md` (Update current sprint/status).
2. `.afef/decision-log.md` (Record approved decisions).
3. `.afef/evidence-index.md` (Link to completion evidence).
4. Other adopter-owned `.afef/` records explicitly named by the sprint.

## Files to Touch After a YELLOW Gate
1. `technical-debt-register.md` (Log the required follow-ups that caused the yellow gate).
2. `known-limitations-register.md` (If the sprint succeeded but revealed a new limitation).

## What NOT to Update After a RED Gate
- Do not update a status record to "Complete".
- Do not update `.afef/project-memory.md` to claim success.
- The sprint must be retried or rescoped.

## Handling Unknowns
If a status is unknown (e.g., "Did the authorized publisher tag this release?"), mark it explicitly as **"Unknown — requires verification"**. Do not assume success.

## Avoiding Stale Claims
Do not make forward-looking claims in memory. 
- **Incorrect:** "The capability is complete." (When only design evidence exists.)
- **Correct:** "The capability is planned; implementation evidence does not yet exist."
