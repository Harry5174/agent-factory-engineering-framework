# Decision Log Protocol

> **Purpose:** Standardize how decisions are recorded so future sessions understand *why* the project is built the way it is.

---

## What Counts as a Decision?
- Architectural choices (e.g., "Use SQLite for the ledger").
- Safety rules (e.g., "Real GitHub execution must be explicit").
- Process boundaries (e.g., "AFDF is Markdown-first").
- Scope reductions (e.g., "Drop Next.js from Artifact 06").

## What Does NOT Count as a Decision?
- Routine implementation details (e.g., "Named the variable `x` instead of `y`").
- Uncontroversial bug fixes.
- Temporary debugging steps.

## Required Fields
Every decision in the log must include:
1. **Decision ID** (e.g., AF-DEC-0012)
2. **Date or Sprint** (e.g., Artifact 04, or AFDF.1)
3. **Context** (The problem being solved)
4. **Decision** (The actual choice made)
5. **Rationale** (Why it was chosen)
6. **Alternatives Considered** (What else was an option, and why it was rejected)
7. **Impact** (How this affects the project going forward)
8. **Status** (Active, Superseded, Deprecated)
9. **Superseded By** (If applicable, link to the new decision)

## Status Lifecycle
- **Active:** The decision is currently in effect.
- **Superseded:** A newer decision overrides this one.
- **Deprecated:** The feature or context no longer exists.

## Superseding a Decision
To change a past decision, do not delete the old record.
1. Create a new decision record (e.g., AF-DEC-0020).
2. Change the old record's status to `Superseded`.
3. Fill in the `Superseded By` field on the old record pointing to the new ID.

## Linking to Artifacts/Evidence
If a decision was heavily debated or proven via a specific artifact, mention the artifact in the `Context` or `Rationale` field (e.g., "Proven necessary by Artifact 05 release gate failures").
