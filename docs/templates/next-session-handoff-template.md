# Next Session Handoff Template

> **Framework version:** `0.2.0`. This framework-owned template does not authorize work; adopters own instantiated operational records under `.afef/`.

## Purpose
To explicitly pass context from a completed sprint to the next IDE agent session, preserving project state and ensuring continuity without drift.

## When to Use
Use this template at the end of a sprint (often after a Green Gate Review) to set up the next task.

## Required Inputs
- Completed sprint results and Green Gate Review
- Open decisions and roadmap

## Required Outputs
A Next Session Handoff document.

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
- `docs/protocols/memory-update-protocol.md`

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

## Handoff Sections
1. What the next session must know
2. What it must not assume
3. Repo state
4. Branch/commit state
5. Completed work
6. Approved decisions
7. Open decisions
8. Safety boundaries
9. Required first files to read
10. Required first commands
11. Expected first response

## Evidence Expectations
N/A - this is a handover document.

## Block Conditions
Do not issue handoff if there is unclarity on what the next step should be; consult Product Owner instead.

## Known Limitations
<KNOWN_LIMITATIONS>

## Next Step
<NEXT_STEP>
