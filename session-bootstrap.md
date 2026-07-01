# Universal Session Bootstrap

**Purpose:** A universal entry point for any stateless Design Supervisor, Implementation Supervisor, IDE Agent, or Reviewer/Evaluator session.

## Who Should Use It
Any LLM-based agent assuming a role within the Agent Factory Development Framework (AFDF).

## Startup Sequence
1. Understand your role (Design, Implement, Execute, Review).
2. Do not assume prior chat memory exists. You are stateless.
3. Locate the `bootstrap-packages/` directory for your target artifact.
4. Read this `session-bootstrap.md` completely.
5. Follow the `context-load-order.md` for your specific artifact.
6. Run the repository inspection commands to verify the physical repository state.
7. Return your first response strictly matching the role's expected kickoff output.

## Required Context Loading Order
Your kickoff prompt will provide a `context-load-order.md`. Follow it explicitly to load framework documentation, project memory, and artifact context before making any decisions.

## Repository Inspection Sequence
**Inspect first, then trust.**
Always run the `pre-design-repository-inspection.md` or equivalent inspection script provided in your kickoff package. The file system is the ultimate source of truth. 

## Reconciling Memory vs Repository State
If `project-memory` claims a feature is complete, but the repository code or git history contradicts this claim, the repository state wins. Update the project memory to reflect reality (via the Memory Update Protocol) or halt and escalate to the Product Owner.

## Missing or Empty Files
If a required context file or template is missing or completely empty:
- Do not hallucinate its contents.
- Halt the session.
- Request clarification or a repair sprint (e.g., AFDF.1R) from the Product Owner.

## What Not to Assume
- Do not assume you are in the correct git branch; always verify.
- Do not assume tests pass just because code was written; always run them.
- Do not assume side effects are safe to run; always check safety invariants.
- Do not assume undocumented integrations exist.

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

## When to Stop and Ask for Clarification
- When repository state fundamentally conflicts with loaded context.
- When you encounter a missing, blocked, or unspecified dependency.
- When an action would violate a safety invariant.

## Role-Specific Templates
This file does not replace role-specific templates. Once you have bootstrapped, proceed to your specific template:
- [Design Supervisor Bootstrap](docs/templates/design-supervisor-bootstrap-template.md)
- [Implementation Supervisor Bootstrap](docs/templates/implementation-supervisor-bootstrap-template.md)
- [IDE Agent Bootstrap](docs/templates/ide-agent-bootstrap-template.md)
- [Green Gate Review](docs/templates/green-gate-review-template.md)
