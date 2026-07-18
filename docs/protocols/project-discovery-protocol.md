# Project Discovery Protocol

## Purpose

Use bounded discovery to turn unresolved, material project questions into an
authoritative specification handoff. Discovery initializes governance knowledge;
it is not permission to initialize product technology.

## Inputs

Inspect available project facts and ask only what remains unresolved and material:

- project goal and users;
- scope and explicit non-scope;
- constraints;
- technology decisions;
- architecture;
- deployment;
- security and privacy;
- non-functional requirements;
- assumptions and risks;
- acceptance expectations; and
- project constitution.

The constitution captures durable principles, safety boundaries, ownership, and
decision rules. Store it once, inline in the project manifest or at the manifest's
declared constitution reference.

## Conversation Rules

1. Prefer no more than three questions per round.
2. Normally converge in one or two rounds.
3. Offer a recommended default with a short rationale when a reasonable default
   exists.
4. Do not repeat settled questions.
5. Record each decision once and refer to it instead of restating it.
6. Escalate only decisions with material consequences for scope, safety,
   architecture, cost, reversibility, or authority.
7. Mark assumptions as assumptions; do not present them as repository facts.

If additional rounds are necessary, state the unresolved material issue that
justifies them.

## Governance and Technology Boundary

Authorized discovery may create governance records under `.afef/`, including a
project manifest and draft specification. It must not run technology initialization
or create product implementation merely to answer questions.

Actions such as `uv init`, dependency installation, runtime scaffolding, database
creation, and deployment configuration require the relevant approved
specification and delivery authorization.

## Specification Handoff

Consolidate settled decisions into one compact specification with:

- a stable `SPEC-0001`-style identity;
- an owner;
- explicit scope and non-scope;
- intended behavior or design;
- stable acceptance-criterion identifiers;
- dependencies and affected paths where known; and
- remaining assumptions or risks.

Do not duplicate manifest fields or create supporting documents unless the project
already uses them and the manifest points to them.

## Required Outcome

Discovery ends in exactly one of:

1. **approved specification** — the authorized approver has approved the
   specification and it is ready for activation or bounded delivery;
2. **blocked outcome with reason** — a material impediment prevents a safe,
   authoritative specification; or
3. **deferred outcome with required decision** — a named decision and its owner
   are required before discovery can conclude.

Do not describe a draft, silence, or agent recommendation as approval.
