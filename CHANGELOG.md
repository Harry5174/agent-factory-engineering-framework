# Changelog

## v0.2.0

AFEF v0.2.0 adds a minimum-adoption control plane with exactly three integrated
record contracts and schemas:

- a project manifest at `.afef/project-manifest.yaml`;
- Markdown specifications with YAML front matter; and
- YAML work records for bounded delivery, evidence, review, and final gates.

The baseline includes compact adopter-owned starting templates, a narrow
deterministic offline conformance validator, repository-local CI, deterministic
valid and invalid fixture checks, and a synthetic clean-room adoption proof.
Controlled implementation and review chains accepted I1, I2, I3, and the I3-CR1
strengthening of clean-room non-mutation evidence.

Compared with v0.1.0, adopters can represent the minimum contracts in
machine-checkable records and validate their shape and cross-record
relationships. Existing human authority, repository verification, evidence,
review, and nonauthorization boundaries remain in force. Adopters own all
instantiated `.afef/` records and must explicitly select and pin the intended
immutable AFEF revision.

AFEF remains a human-operated engineering and governance framework. It is not an
agent or product runtime, workflow engine, project generator, general CLI,
reusable GitHub Action, automatic authorization system, or production
deployment. Validation confirms represented record conformance only; it cannot
prove identity, factual truth, approval authenticity, separation of control,
continuing authority, real-world execution, production readiness, publication,
deployment, or real-project adoption.

See the [validation guide](docs/validation.md) and
[v0.2.0 release notes](docs/releases/v0.2.0.md). Verify actual publication and
release state from the designated repository's default branch, applicable
annotated Git refs, and GitHub Release metadata.

## v0.1.0

The initial documentation-first baseline established human roles, authority and
safety boundaries, session and sprint lifecycle protocols, evidence review,
templates, adopter-owned memory conventions, governance, licensing, and
extraction provenance.
