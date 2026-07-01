# Safety Boundary Protocol

Reusable safety rules for all Agent Factory artifacts, sessions, and sprints.

---

## 1. Universal Safety Rules

These rules apply to every session, sprint, and artifact:

| Rule | Description |
|------|-------------|
| **Do not print secrets** | Never print, log, or expose tokens, API keys, passwords, or credentials |
| **Do not read `.env` unless explicitly approved** | `.env` files may contain credentials; do not read them without Product Owner approval |
| **Do not paste tokens into LLM contexts** | Never paste tokens, keys, or credentials into ChatGPT, Claude, or other LLM interfaces |
| **Do not run live external side effects without explicit approval** | Any operation that writes to an external service requires explicit Product Owner approval |
| **Fake/default first** | All new functionality defaults to fake/mock execution; real execution is opt-in |
| **Real mode explicit only** | Real execution requires explicit configuration, not accidental enablement |
| **CI must not run live side effects** | CI/CD pipelines must use fake/mock clients only |
| **Approval before side effects** | Every side effect must pass through an approval gate before execution |
| **LLM proposes, harness decides, operator approves** | The model proposes actions; the harness validates them; the operator makes the final decision |

---

## 2. Session-Level Safety

At the start of every session:

1. Verify `.env` is gitignored (`git check-ignore -v .env || true`)
2. Verify `.env` is not tracked (`git ls-files .env`)
3. Run token scans against new content before committing
4. Do not require GitHub credentials unless the sprint explicitly involves real GitHub execution
5. Do not push or tag without Product Owner approval

---

## 3. Sprint-Level Safety

Every sprint prompt must include:

- Explicit list of allowed external interactions (if any)
- Explicit list of forbidden actions
- Block conditions that stop the sprint if safety is threatened

---

## 4. Artifact-Specific Safety Boundaries

Each artifact adds specific safety rules that subsequent artifacts inherit:

### Artifact 00–01 — Foundation and Skill Runner

- Identity is server-derived, never client-claimed
- Proposals are validated before execution
- Unsafe arguments are rejected

### Artifact 02 — Approval-Gated GitHub Tool Harness

- Side effects require explicit approval
- In-memory idempotency ledger prevents duplicate execution
- Fake-client execution is the default

### Artifact 03 — Durable Side-Effect Ledger

- SQLite-backed persistence for side-effect records
- Restart/replay duplicate suppression
- Durable approval bindings

### Artifact 04 — Real GitHub Comment Adapter

- Real execution is explicitly configured, not default
- Repository allowlisting limits which repos can be targeted
- Server-side token loading (tokens are never client-supplied)
- Remote idempotency marker lookup and reconciliation
- Durable audit recording for all execution attempts

### Artifact 05 — Real-Mode Smoke Evidence and Release Gate

- Evidence artifact only — does not own runtime
- Release gate requires documented evidence
- Offline replay and no-duplicate proofs
- Negative/zero-network proof for CI safety

### Artifact 06 — Operator Approval Console / Workbench

- Local/demo execution boundary
- Operator inspects risk, scopes, context, and execution mode before decision
- Server-controlled approval routes (not client-bypass)
- No live GitHub execution, no `.env`, no OAuth required for demo

### Artifact 07 (Future) — Vertical Agent Boundary

- Will inherit all prior safety boundaries
- Specific safety rules to be defined in Artifact 07 design

---

## 5. Evidence of Safety Compliance

Every completion report must include:

- [ ] Confirmation no runtime behavior was changed (if docs-only sprint)
- [ ] Confirmation no artifact code was modified (if docs-only sprint)
- [ ] Confirmation no live GitHub execution occurred (unless explicitly approved)
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
