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

Operation characteristics override labels: work with High Assurance
characteristics uses High Assurance controls even if a lower profile was selected
or configured by default. Uncertainty that could conceal a higher-risk operation
must be resolved or escalated before proceeding.

## Authorization Envelopes

An authorization envelope records the bounded related work an implementer may
perform without seeking approval for each routine, reversible step. It should
identify:

- permitted actions;
- affected repositories, modules, or paths;
- prohibited actions;
- constraints and stop conditions; and
- validity or checkpoint boundaries.

The envelope does not expand the active specification, override the project
constitution, or authorize unknown side effects. It must never silently grant
side-effect authority.

Exact separate authorization remains required for:

- pushes not already approved;
- tags and releases;
- production changes;
- credential access;
- destructive operations;
- external writes; and
- security-sensitive exceptions.

If a step crosses one of these boundaries, stop at the human checkpoint and obtain
authorization naming that operation.

## Evidence and Gates

Lean evidence may be compact: changed paths, diff summary, relevant validation,
commit or working-tree state, limitations, and an explicit non-claim of approval.
Standard evidence additionally covers material behavior and integration impact.
High Assurance evidence preserves the required independent reviews, checkpoints,
and operation-specific audit trail.

Every work record identifies the selected profile, implementation state,
validation summaries, evidence references, review recommendation, final gate, and
next action as applicable. A recommendation is not a final gate, and a final gate
does not retroactively authorize implementation or external effects.
