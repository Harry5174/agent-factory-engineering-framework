# Risk-Scaled Delivery Protocol

## Purpose

Select governance effort, evidence, and review in proportion to risk while
preserving bounded authorization and independent gates.

## Profiles

### Lean

Suitable for documentation, small local refactoring, low-risk configuration, and
reversible internal changes.

Minimum flow:

```text
Supervisor designs and authorizes bounded work
→ IDE Agent implements
→ compact evidence returned
→ Supervisor gates
```

### Standard

Suitable for normal features, new dependencies, material architecture changes,
persistent data-model changes, and broader integration work.

Minimum flow:

```text
Design
→ bounded authorization
→ implementation
→ evidence review
→ final gate
```

Evidence should cover affected interfaces, validation appropriate to the change,
known limitations, and reconciliation with the active specification.

### High Assurance

Required for authentication and authorization, secrets and sensitive data,
material database migrations, Git-history rewriting, releases, production
changes, destructive actions, and externally effectful operations.

Preserve full role separation and independent review. Require explicit human
checkpoints before sensitive or irreversible steps and evidence adequate to
review both safety and outcome.

## Selection and Role Separation

Not every role requires a separate agent session for Lean or Standard work. Roles
and responsibilities must still be identifiable, and the IDE Agent never
self-approves. Independent review is mandatory whenever the selected profile or
operation requires it.

Every validator-relevant actor is recorded as a structured value:

```yaml
actor_id: "<STABLE_OPAQUE_PROJECT_IDENTITY>"
role: "<CANONICAL_ROLE>"
display_name: "<OPTIONAL_NON_NORMATIVE_LABEL>"
```

The canonical roles are `product_owner`, `design_supervisor`,
`implementation_supervisor`, `ide_agent`, and `independent_reviewer`.
`display_name` is optional and must never determine separation.

An implementer is required when `implementation_state` is `in_progress`,
`implemented`, or `verified`, but is not prematurely required for `not_started`,
`deferred`, or other records that have not reached implementation. A completed
review identifies its structured reviewer, recommendation, and local evidence
reference. A completed `accept_with_conditions` review records its conditions.

High Assurance work explicitly records `independent_review`. Its reviewer has
role `independent_reviewer`; an accepted or rejected completed independent review
includes its reviewer, completion timestamp, and repository-local review or
evidence reference. A pending review need not claim completed-review evidence.

A completed final gate identifies its structured owner and timestamp. An IDE
Agent cannot own the final gate, and `accepted_with_conditions` records its
conditions. For High Assurance work, `accepted` or
`accepted_with_conditions` cannot coexist with an absent, pending, or rejected
independent review.

JSON Schema represents these actors and lifecycle conditions but cannot compare
two actor IDs. Future I2 must enforce these cross-record identity invariants:

- independent reviewer `actor_id` differs from implementer `actor_id`;
- final-gate owner `actor_id` differs from implementer `actor_id`; and
- a reviewer does not approve their own implementation.

Do not substitute display-name or role-label keyword matching for actor-ID
comparison. Validation confirms only the identities and roles represented by the
record. It cannot prove real-world identity, distinct human control of two IDs,
cryptographic identity, or approval authenticity.

Operation characteristics override labels: work with High Assurance
characteristics uses High Assurance controls even if a lower profile was selected
or configured by default. Uncertainty that could conceal a higher-risk operation
must be resolved or escalated before proceeding.

## Authorization Envelopes

An authorization envelope records structured decisions for the bounded related
work an implementer may perform. Its normative source is `operations`; free-form
descriptions are optional, non-normative explanation and do not grant authority.
Do not maintain `permitted_actions` or `prohibited_actions` as parallel
authorization sources.

Each operation records:

```yaml
- operation_id: "OP-001"
  effect_class: local-reversible-write
  decision: permitted
  authorization_requirement: separate_reference
  description: "<OPTIONAL_NON_NORMATIVE_DESCRIPTION>"
```

Effect classes are exactly:

- `local-read`
- `local-reversible-write`
- `local-destructive`
- `external-read`
- `external-write`
- `external-destructive`
- `identity-permission-change`
- `publication-release`

Decisions are exactly `permitted` or `prohibited`. The structured authorization
requirement is `bounded_work_envelope`, `separate_reference`, or
`not_applicable`. A prohibited operation uses `not_applicable` and remains
prohibited even if an unrelated authorization reference exists.

A permitted operation classified as `local-destructive`, `external-write`,
`external-destructive`, `identity-permission-change`, or `publication-release`
requires `separate_reference` and an exact separate authorization bound to its
operation ID:

```yaml
- authorization_id: "AUTH-001"
  reference: "<EXACT_SEPARATE_APPROVAL_OR_EVIDENCE_REFERENCE>"
  operation_ids:
    - "OP-001"
```

Every external read must be explicitly represented. Public, credential-free
reading may use `bounded_work_envelope`; credentialed, private-resource,
protected-data, or otherwise sensitive reading uses `separate_reference` with an
operation-bound authorization. The selected requirement must be structured and
unambiguous.

Operation IDs and authorization IDs are stable and unique within one work record.
Future I2 must enforce property-level uniqueness, reject contradictory decisions
for one operation ID, reject unknown operation bindings, and verify that every
protected permitted operation has a reference bound to that exact operation ID.
This prevents an unrelated approval from being used for protected work; array
`uniqueItems` alone cannot enforce these keyed relationships.

The envelope does not expand the active specification, override the project
constitution, authorize unknown side effects, or convert a placeholder into
approval. Validation confirms the consistency and completeness of recorded
authorization. It cannot prove approval authenticity, truthful effect
classification, that an external action stayed within its classification, or
continuing validity outside the recorded scope.

## Evidence and Gates

Lean evidence may be compact: changed paths, diff summary, relevant validation,
commit or working-tree state, limitations, and an explicit non-claim of approval.
Standard evidence additionally covers material behavior and integration impact.
High Assurance evidence preserves the required independent reviews, checkpoints,
and operation-specific audit trail.

Every work record identifies the selected profile, implementation state,
validation summaries, evidence references, reviews, final gate, and next action
as applicable. A recommendation is not a final gate, and a final gate does not
retroactively authorize implementation or external effects.
