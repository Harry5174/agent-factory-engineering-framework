# Agent Factory Engineering Framework (AFEF)

**Repository:** `agent-factory-engineering-framework`

**Framework version:** `0.2.0`

The Agent Factory Engineering Framework (AFEF) is a human-operated development and engineering-governance framework for planning, implementing, reviewing, and handing off bounded work. It provides specifications, protocols, templates, memory templates, exactly three minimum-adoption schemas, and a narrow deterministic offline conformance validator.

AFEF is not an agent runtime, product runtime, workflow engine, project generator, general CLI, or automatic authorization system. It does not execute adopter work or replace human review.

## Version, Publication, and Release Verification

The `VERSION` file identifies the documented framework version. Determine the currently published revision, if any, from the designated repository's default branch. Determine release availability by verifying the applicable annotated Git tag and GitHub Release metadata. A version declaration alone does not prove publication or release.

The `agent-factory-engineering-framework` repository is the designated canonical repository for AFEF. Verify the currently published canonical revision, if any, from its default branch and release metadata.

These sources answer distinct questions:

- **Documented version:** the `VERSION` file and framework documentation.
- **Published revision:** the designated repository's remote default branch.
- **Released revision:** the applicable annotated Git tag and GitHub Release metadata.
- **Historical provenance:** the provenance record and commit map in [AFDF extraction provenance](docs/provenance/afdf-extraction.md).

Framework version `0.2.0` identifies the documented baseline. It is not by itself evidence of a Git tag, GitHub Release, published revision, adopter approval, or production maturity.

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

GitHub Steward is a possible adopter, not an AFEF runtime dependency. Neither an AFEF version declaration nor framework publication constitutes GitHub Steward adoption.

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
- [Validation guide](docs/validation.md)
- [Changelog](CHANGELOG.md)
- [v0.2.0 release notes](docs/releases/v0.2.0.md)
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

## v0.2.0 Scope and Limitations

- AFEF remains human-operated and provides exactly three minimum-adoption schemas: project manifest, specification, and work record.
- Its narrow deterministic offline validator checks represented record conformance only. It does not approve, authorize, execute, publish, repair, or create or modify adopter records.
- Repository-local CI validates AFEF's own suite. Deterministic valid/invalid tests and a synthetic clean-room adoption test prove the bounded validator behavior, not real-adopter operation.
- Validation cannot prove factual truth, real-world or cryptographic human identity, separation of control, approval authenticity, continuing authority, real-world execution, production readiness, publication, or deployment.
- AFEF does not provide a project generator, workflow engine, agent or product runtime, reusable GitHub Action, production deployment, or real-adopter proof.
- Publication and release availability require verification from the applicable Git refs and GitHub Release metadata.

## Claims Boundary

This documentation baseline supports publication and release review. It does not by itself establish a published or released revision, freeze AFDF, establish GitHub Steward adoption, authorize adopter work, or demonstrate a production deployment.
