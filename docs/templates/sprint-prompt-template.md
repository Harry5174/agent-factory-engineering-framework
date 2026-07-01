# Sprint Prompt Template

## Purpose
To outline a specific unit of work (a sprint) for an agent, defining scope, context, safety, and exact deliverables.

## When to Use
Use this to instruct the IDE agent at the start of a new sprint.

## Required Inputs
- Approved Implementation Plan
- Baseline repository state

## Required Outputs
All deliverables, plus a completion report with evidence.

## Required Context Sources
- `03-agent-factory/development-framework/README.md`
- `03-agent-factory/development-framework/docs/README.md`
- `03-agent-factory/development-framework/project-memory/README.md`
- `03-agent-factory/development-framework/project-memory/agent-factory/README.md`
- `03-agent-factory/development-framework/project-memory/agent-factory/project-memory.md`
- `03-agent-factory/development-framework/project-memory/agent-factory/phase-map.md`
- `03-agent-factory/development-framework/project-memory/agent-factory/artifact-map.md`
- `03-agent-factory/development-framework/project-memory/agent-factory/decision-log.md`
- `03-agent-factory/development-framework/project-memory/agent-factory/open-decisions.md`
- `03-agent-factory/development-framework/project-memory/agent-factory/safety-invariants.md`
- `03-agent-factory/development-framework/project-memory/agent-factory/evidence-index.md`
- `03-agent-factory/development-framework/project-memory/agent-factory/next-artifact-readiness.md`
- `docs/protocols/repository-inspection-protocol.md`

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
For AFDF/framework docs-only sprints, also run:
```bash
find 03-agent-factory/development-framework -maxdepth 6 -type f | sort
wc -l 03-agent-factory/development-framework/docs/templates/*-template.md
rg -n "ghp_|github_pat_|gho_|ghu_|ghs_|ghr_|Bearer |GITHUB_ACCESS_TOKEN=|AGENT_FACTORY_GITHUB_TOKEN=" 03-agent-factory/development-framework || true
rg -n "/home/harry|/home/|Desktop/prcx|xx_github|/Users/" 03-agent-factory/development-framework || true
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
- Do not let an LLM execute tools directly.
- LLM proposes; harness decides; operator approves.
- Record evidence before claiming completion.
- Do not overclaim mocked, fake/default, local demo, unpublished, or untagged work as production-ready.

Inherited safety boundaries:
- Artifact 04: real GitHub runtime safety boundary.
- Artifact 05: release-gate evidence boundary.
- Artifact 06: local/demo operator workbench boundary.
- AFDF: workflow memory/protocol boundary.
- Artifact 07 future: vertical-agent proposal boundary.

## Scope Boundaries
- Project: <PROJECT_NAME> (<PROJECT_SLUG>)
- Phase: <PHASE_NAME>
- Artifact: <ARTIFACT_NAME>
- Sprint: <SPRINT_NAME>

## Deliverables
- <DELIVERABLE_1>
- <DELIVERABLE_2>

## Implementation Plan Requirement
Review the required scope and state any assumptions or queries before modifying code.

## Evidence Expectations
Execute test commands and include their outputs in your completion report.

## Commit Instructions
Commit as directed. Do not push. Do not tag.

## Block Conditions
Halt session if:
- Validation tests fail repeatedly.
- Safety boundaries would be violated by the implementation.

## Handoff Expectations
Produce a formal Completion Report.

## Known Limitations
<KNOWN_LIMITATIONS>

## Next Step
<NEXT_STEP>
