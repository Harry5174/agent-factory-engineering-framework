# AFEF Session Bootstrap

**Framework version:** `0.1.0`

## Purpose

Provide a verification-first entry point for any Product Owner, Design Supervisor, Implementation Supervisor, IDE Agent, or Independent Reviewer using the Agent Factory Engineering Framework (AFEF).

## Required Start

1. Identify the repository and session role.
2. Verify repository root, current branch, HEAD, working tree, remotes, and tags.
3. Load the explicitly authorized sprint or review prompt.
4. Load relevant AFEF specifications, protocols, and templates.
5. Load adopter-owned `.afef/` records only after comparing them with repository evidence.
6. State scope, prohibited work, required evidence, and stop conditions before changing state.

Repository evidence wins when an operational record is stale or contradictory. Correcting `.afef/` is itself a repository change and requires authorization.

## Minimum Repository Checks

```bash
git rev-parse --show-toplevel
git branch --show-current
git status -sb
git status --short
git rev-parse HEAD
git remote -v
git tag --list
git diff --check
```

Do not read `.env` contents. Confirm only whether environment files are ignored or tracked when that check is relevant.

## Role Boundaries

- Product Owner decisions define authorization; they do not substitute for evidence.
- Design Supervisors define architecture and issue final sprint gates.
- Implementation Supervisors translate approved scope and review evidence.
- IDE Agents implement bounded work and return raw evidence without self-approval.
- Independent Reviewers assess release readiness without modifying or publishing the candidate.

## Stop Conditions

Stop and report when:

- Repository state conflicts with the required starting state.
- Explicit sprint authorization is missing or ambiguous.
- Required context is missing, empty, or contradicted by repository evidence.
- Sensitive material may be exposed.
- An external write, publication, tag, or release lacks separate authorization.
- Completion would require scope expansion or redesign.
- Required evidence cannot be produced.

## Framework and Operational Records

AFEF owns the source templates under `docs/memory/`. Adopting repositories instantiate and maintain operational records under `.afef/`; this framework repository does not contain an adopter's live project memory.

## Role Templates

- [Design Supervisor Bootstrap](docs/templates/design-supervisor-bootstrap-template.md)
- [Implementation Supervisor Bootstrap](docs/templates/implementation-supervisor-bootstrap-template.md)
- [IDE Agent Bootstrap](docs/templates/ide-agent-bootstrap-template.md)
- [Green Gate Review](docs/templates/green-gate-review-template.md)

Using a template does not authorize implementation, publication, or release. Verify publication and release state using the [central release-verification guidance](README.md#version-publication-and-release-verification).
