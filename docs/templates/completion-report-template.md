# Completion Report Template

> **Framework version:** `0.2.0`. This framework-owned template does not authorize work; adopters own instantiated operational records under `.afef/`.

## Purpose
To officially close a sprint by documenting exactly what was done, providing verifiable evidence of completion, and confirming safety and scope adherence.

## When to Use
Use this template at the very end of an implementation sprint, before asking for a Green Gate Review.

## Required Inputs
- Original sprint prompt
- Terminal outputs, git logs, and test results from the sprint
- Evidence packages

## Required Outputs
A detailed Markdown report containing the sections below.

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
- `docs/protocols/evidence-review-protocol.md`

## Repository Inspection Requirements
(Run and include in completion report)
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

## Report Sections
1. Sprint goal
2. Branch
3. Commit
4. Base commit
5. Working directory
6. Files reviewed
7. Files created
8. Files modified
9. Commands run
10. Test/lint/check results
11. Token scan
12. Local path scan
13. .env status
14. Scope confirmations
15. Safety confirmations
16. Known limitations
17. Recommended next step

## Evidence Expectations
Include exact command outputs, file paths, or screenshots if applicable.

## Block Conditions
Report is blocked if:
- Any tests fail.
- Any secrets or absolute paths are exposed in scans (except intentional docs examples).
- Required sections are omitted.

## Handoff Expectations
Deliver the completed report.

## Known Limitations
<KNOWN_LIMITATIONS>

## Next Step
<NEXT_STEP>
