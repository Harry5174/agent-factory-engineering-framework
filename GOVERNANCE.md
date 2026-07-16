# AFEF Governance

## Repository Authority

The dedicated `agent-factory-engineering-framework` repository is the intended canonical home of AFEF after a separately authorized publication gate. Until publication occurs, this local candidate is unreleased and the public namespace is not the canonical source of truth.

`learn-agentic-ai` is the historical extraction source. It is not the future source of truth for active AFEF guidance.

## Decision Roles

- **Product Owner:** owns product direction, scope authorization, licensing, adoption, publication, tags, and releases.
- **Design Supervisor:** owns architecture, defines bounded sprint scope, and issues final sprint-gate decisions.
- **Implementation Supervisor:** translates approved designs into implementation prompts and evaluates whether raw implementation evidence satisfies the prompt. It does not issue the final sprint gate.
- **IDE Agent:** performs only explicitly authorized bounded implementation, preserves raw evidence, and reports blockers. It does not self-approve.
- **Independent Reviewer:** independently assesses release readiness and reports findings. Publication or release still requires the authorized release process.

Every implementation sprint requires explicit authorization. Remote publication, tags, and releases require separate authorization even when local implementation is approved.

## Framework and Adopter Ownership

AFEF owns reusable specifications, protocols, templates, memory templates, governance, and provenance. Each adopting repository owns its instantiated operational records under `.afef/`, including its decisions, evidence indexes, limitations, and handoffs.

Adopter records do not override repository evidence. Adopters must define who may update `.afef/` and when those updates are authorized.

Examples supplied by AFEF are non-authoritative fixtures unless a governing document explicitly declares otherwise. A project name in historical provenance or a future-adopter statement does not create runtime coupling or adoption authority.

## Change and Release Boundaries

Architecture changes, machine-readable governance, schemas, validators, automation, and lifecycle redesign require separately authorized work. A local commit, version file, or favorable review is not a release. Publication must use the exact history approved by the release gate.
