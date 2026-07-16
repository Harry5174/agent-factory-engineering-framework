# Safety Boundary Protocol

Reusable safety rules for all Agent Factory artifacts, sessions, and sprints.

---

## 1. Universal Safety Rules

These rules apply to every session, sprint, and artifact:

| Rule | Description |
|------|-------------|
| **Do not print secrets** | Never print, log, or expose tokens, API keys, passwords, or credentials |
| **Do not read `.env` unless explicitly approved** | `.env` files may contain credentials; do not read them without Product Owner approval |
| **Do not paste tokens into model contexts** | Never paste tokens, keys, or credentials into any model or agent interface |
| **Do not run live external side effects without explicit approval** | Any operation that writes to an external service requires explicit Product Owner approval |
| **Fake/default first** | All new functionality defaults to fake/mock execution; real execution is opt-in |
| **Real mode explicit only** | Real execution requires explicit configuration, not accidental enablement |
| **CI must not run live side effects** | CI/CD pipelines must use fake/mock clients only |
| **Approval before side effects** | Every side effect must pass through an approval gate before execution |
| **Proposals do not grant authority** | Generated proposals remain non-executable until the adopting project's authorized controls permit a bounded action |

---

## 2. Session-Level Safety

At the start of every session:

1. Verify `.env` is gitignored (`git check-ignore -v .env || true`)
2. Verify `.env` is not tracked (`git ls-files .env`)
3. Run token scans against new content before committing
4. Do not require external-service credentials unless the sprint explicitly authorizes that service and operation
5. Do not push or tag without Product Owner approval

---

## 3. Sprint-Level Safety

Every sprint prompt must include:

- Explicit list of allowed external interactions (if any)
- Explicit list of forbidden actions
- Block conditions that stop the sprint if safety is threatened

---

## 4. Reusable Safety Boundaries

### Proposal and Validation Boundary

- Generated proposals do not grant execution authority.
- Arguments and target scope are validated before execution.
- Unsafe or ambiguous requests fail closed.

### External-Read Boundary

- External reads are explicit and limited to approved resources.
- Read results are treated as untrusted input and recorded when they affect decisions.

### External-Write Boundary

- External writes require specific Product Owner authorization.
- Target allowlists, approval binding, idempotency, and audit requirements belong to the adopting project's approved design.
- Local or fake-mode evidence does not establish live-write readiness.

### Release Boundary

- Release review requires complete, independently verifiable evidence.
- A review recommendation does not publish, tag, or release.
- CI and unattended automation must not perform live side effects unless separately designed and authorized.

---

## 5. Evidence of Safety Compliance

Every completion report must include:

- [ ] Confirmation no runtime behavior was changed (if docs-only sprint)
- [ ] Confirmation no artifact code was modified (if docs-only sprint)
- [ ] Confirmation no live external-service execution occurred (unless explicitly approved)
- [ ] Confirmation no credentials were required or read
- [ ] Confirmation `.env` remained ignored/untracked
- [ ] Token/local path scan results for new content

---

## 6. Escalation

If a safety boundary is unclear or a sprint requires an exception:

1. Stop the sprint
2. Document the specific safety question
3. Request Product Owner decision
4. Record the decision in the decision log
5. Proceed only with explicit approval
