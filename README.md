# Agent Factory Engineering Framework (AFEF)

**Repository:** `agent-factory-engineering-framework`

**Target version:** `0.1.0`
**Release status: Unreleased**

The Agent Factory Engineering Framework (AFEF) is a documentation-first development and engineering-governance framework for planning, implementing, reviewing, and handing off bounded work. It provides human-operated specifications, protocols, templates, and memory templates.

AFEF is not an agent runtime, product runtime, workflow engine, CLI, validator, or automated policy-enforcement system. It does not execute tools or replace human review.

## Repository Status

This repository is intended to become the canonical home of AFEF only after a separate publication and release gate. The local history in this candidate has not been published, tagged, or released, and the empty public namespace is not yet the canonical source of truth.

Target version `0.1.0` identifies the baseline being prepared. It is not evidence of a Git tag, GitHub release, public repository initialization, adopter approval, or production maturity.

## Historical Provenance

The first five commits were selectively extracted from the historical Agent Factory Development Framework (AFDF) directory in `learn-agentic-ai`. Their rewritten hashes preserve selected content provenance while excluding project memory, status documents, examples, and evidence packages. The later canonicalization commit establishes active AFEF identity and is deliberately distinguishable from those historical extraction commits.

See [AFDF extraction provenance](docs/provenance/afdf-extraction.md) for the source pin, extraction boundary, commit mapping, and rewrite limitations.

## Operating Model

AFEF separates reusable framework guidance from adopter-owned operational state:

- This repository owns specifications, protocols, templates, memory templates, governance, and provenance.
- An adopting repository owns its instantiated operational records under `.afef/`.
- An adopter must verify its repository state before relying on `.afef/` records.
- Every implementation sprint requires explicit authorization and bounded evidence.
- Publication, tags, and releases require separate authorization.

GitHub Steward is a possible future adopter. It is not an AFEF runtime dependency, is not initialized by this baseline, and has not adopted AFEF.

## Roles

| Role | Responsibility |
|---|---|
| Product Owner | Owns scope, policy, licensing, adoption, publication, tag, and release decisions. |
| Design Supervisor | Owns architecture, sprint boundaries, and final sprint-gate decisions. |
| Implementation Supervisor | Translates approved scope into executable prompts and reviews implementation evidence. |
| IDE Agent | Performs explicitly authorized bounded changes and returns raw evidence without self-approval. |
| Independent Reviewer | Independently evaluates release readiness; review does not itself publish or release. |

See [Governance](GOVERNANCE.md) for the authority boundaries.

## Documentation Map

- [Documentation index](docs/README.md)
- [Active AFEF specification](docs/specs/agent-factory-engineering-framework.md)
- [Protocols](docs/protocols/)
- [Templates](docs/templates/README.md)
- [Memory templates](docs/memory/project-memory-template.md)
- [Session bootstrap](session-bootstrap.md)
- [Governance](GOVERNANCE.md)
- [Extraction provenance](docs/provenance/afdf-extraction.md)
- [License](LICENSE)
- [Version declaration](VERSION)

## Starting a Session

1. Verify the repository path, branch, HEAD, remotes, tags, and working-tree state.
2. Load the authorized sprint prompt and relevant AFEF protocols.
3. Load adopter-owned `.afef/` records only after checking them against repository evidence.
4. State scope, prohibited work, evidence requirements, and stop conditions before editing.
5. Stop when authorization is missing or repository state contradicts the supplied context.

Use [session-bootstrap.md](session-bootstrap.md) and the relevant role template for a structured start.

## Completing a Sprint

1. Validate the implementation against the approved scope.
2. Preserve raw command output and the complete intended diff outside the working tree when required.
3. Produce a completion report with supported claims and explicit non-claims.
4. Submit evidence for independent review without issuing a self-approval decision.
5. Update adopter-owned `.afef/` records only when the sprint explicitly authorizes that update.

## v0.1.0 Limitations

- AFEF is documentation-first and manually operated.
- It has no schemas, validators, CLI, CI integration, or reusable Actions.
- It does not define a machine-readable governance contract.
- It includes no adopter fixture and performs no automatic adoption.
- Gate vocabulary and lifecycle automation remain candidates for a future, separately authorized version.
- The target baseline is unreleased and has not passed an independent release gate.

## Claims Boundary

This local baseline may support a future publication review. It does not claim that AFEF v0.1.0 is released, the public AFEF repository is initialized, AFDF is frozen, AFEF v0.2.0 exists, GitHub Steward has adopted AFEF, or any production deployment has occurred.
