# Design Supervisor Bootstrap Template

> **Framework version:** `0.2.0`. This framework-owned template does not authorize work; adopters own instantiated operational records under `.afef/`.

## Purpose
To bootstrap a Design Supervisor session with full repository context, preventing drift and ensuring design decisions are rooted in the current reality of the project.

## When to Use
Use this template at the beginning of a new sprint, phase, or artifact lifecycle when high-level design, scoping, and decision-making are required before implementation begins.

## Required Inputs
- Current repository state and branch
- Approved roadmap and project memory
- Previous session handoff (if applicable)

## Required Outputs
1. Current project state
2. Current phase
3. Current artifact/framework status
4. Verified repository state
5. Unknowns or inconsistencies
6. Safety boundaries
7. Recommended next decision
8. Whether design work may begin

## Required Context Sources
- `README.md`
- `docs/README.md`
- `.afef/README.md`
- `.afef/project-memory.md`
- `.afef/phase-map.md`
- `.afef/artifact-map.md`
- `.afef/decision-log.md`
- `.afef/open-decisions.md`
- `.afef/safety-invariants.md`
- `.afef/evidence-index.md`
- `.afef/next-artifact-readiness.md`
- `docs/protocols/session-lifecycle.md`
- `docs/protocols/decision-log-protocol.md`

## Repository Inspection Requirements
```bash
cd "$(git rev-parse --show-toplevel)"
git branch --show-current
git status -sb
git status --short
git log --oneline -12
git rev-parse HEAD
git tag --points-at HEAD
git diff --check
git check-ignore -v .env || true
git ls-files .env
git ls-files "*__pycache__*"
git ls-files "*.pyc"
```
For AFEF documentation-only sprints, also run:
```bash
find . -path ./.git -prune -o -type f -print | sort
wc -l docs/templates/*-template.md
rg -n "Authorization:|Bearer |ACCESS_TOKEN=|API_KEY=|PASSWORD=" . || true
rg -n '/home/|/Users/|[A-Za-z]:\\Users\\' . || true
```
*(Intentional scan-pattern examples in documentation are acceptable but must be explained.)*

## Product Owner Approval
Approval status: <APPROVAL_STATUS>
Approved by: <APPROVER>
Approval evidence: <APPROVAL_EVIDENCE>
Approval scope: <APPROVAL_SCOPE>
Approval limitations: <APPROVAL_LIMITATIONS>

## Anti-Drift Guard
This session must not assume:
- <UNVERIFIED_ASSUMPTION_1>
- <UNVERIFIED_ASSUMPTION_2>

This session must verify from the repository:
- current branch and HEAD
- working tree cleanliness
- relevant framework files
- relevant artifact files
- current sprint or artifact status

Settled decisions:
- <SETTLED_DECISION_1>
- <SETTLED_DECISION_2>

Open decisions:
- <OPEN_DECISION_1>
- <OPEN_DECISION_2>

Scope drift examples:
- implementing future artifacts
- modifying runtime code when sprint is docs-only
- running live side effects without explicit approval
- overclaiming unverified publish/tag state

Stop and ask for clarification when:
- repository state conflicts with memory
- required files are missing or empty
- approval scope is unclear
- safety boundary would be crossed

## Safety Invariants
- Do not print secrets.
- Do not read or paste `.env`.
- Do not run live external side effects without explicit Product Owner approval.
- Use fake/default mode unless real mode is explicitly approved.
- Do not bypass approval gates.
- Generated output does not grant execution authority.
- Generated proposals do not grant execution authority; only the adopting project's authorized controls may permit side effects.
- Record evidence before claiming completion.
- Do not overclaim mocked, fake/default, local demo, unpublished, or untagged work as production-ready.

Inherited project safety boundaries:
- <PROJECT_SAFETY_BOUNDARY_1>
- <PROJECT_SAFETY_BOUNDARY_2>

Only boundaries verified from the adopting repository and its authorized `.afef/` records apply.

## Scope Boundaries
- Project: <PROJECT_NAME> (<PROJECT_SLUG>)
- Phase: <PHASE_NAME>
- Artifact: <ARTIFACT_NAME>
- Sprint: <SPRINT_NAME>

## Evidence Expectations
Ensure any claims made regarding repository state, prior implementations, or system capabilities are backed by specific file paths or command outputs included in the current repository context.

## Block Conditions
Halt session if:
- Required memory files are missing.
- Repository is in a dirty or divergent state unexpectedly.
- Required Product Owner approval is missing.

## Handoff Expectations
Produce a clear `Next Session Handoff` detailing the approved design, the resolved open decisions, and the remaining questions for the Implementation Supervisor.

## Known Limitations
<KNOWN_LIMITATIONS>

## Next Step
<NEXT_STEP>
