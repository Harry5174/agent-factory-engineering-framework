# Green Gate Review Template

> **AFEF template status:** Target version `0.1.0` is unreleased. This framework-owned template does not authorize work; adopters own instantiated operational records under `.afef/`.

## Purpose
To evaluate a completion report and decide whether the sprint's output is ready to merge or proceed to the next phase.

## When to Use
Use this template after a sprint concludes and a Completion Report is submitted, before moving to the next sprint.

## Required Inputs
- The submitted Completion Report
- Acceptance criteria from the sprint design

## Required Outputs
A formal Gate Result: Green (Pass), Yellow (Pass with conditions), or Red (Fail).

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
- `docs/protocols/green-gate-review-protocol.md`

## Repository Inspection Requirements
Ensure the completion report contains valid execution results of:
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

## Gate Review Sections
1. Decision
2. Scope assessment
3. Evidence assessment
4. Test assessment
5. Safety assessment
6. Overclaim assessment
7. Acceptance criteria checklist
8. Evidence quality classification (Strong / Acceptable / Weak / Missing)
9. Gate result (Green / Yellow / Red)
10. Risks
11. Required follow-up
12. Next sprint recommendation

## Evidence Expectations
Evaluate the evidence provided in the Completion Report against the sprint plan requirements. Ensure no overclaims are present.

## Block Conditions
Gate fails (Red) if:
- Completion Report is incomplete.
- Tests fail.
- Safety invariant is violated.
- Scope has drifted unacceptably.

## Handoff Expectations
Produce the Gate Review document and a recommendation for next steps.

## Known Limitations
<KNOWN_LIMITATIONS>

## Next Step
<NEXT_STEP>
