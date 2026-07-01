# Completion Report Template

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
For AFDF/framework docs-only sprints, also run:
```bash
find 03-agent-factory/development-framework -maxdepth 6 -type f | sort
wc -l 03-agent-factory/development-framework/docs/templates/*-template.md
rg -n "ghp_|github_pat_|gho_|ghu_|ghs_|ghr_|Bearer |GITHUB_ACCESS_TOKEN=|AGENT_FACTORY_GITHUB_TOKEN=" 03-agent-factory/development-framework || true
rg -n "/home/harry|/home/|Desktop/prcx|xx_github|/Users/" 03-agent-factory/development-framework || true
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
