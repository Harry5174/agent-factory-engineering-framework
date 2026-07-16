# Evidence Package Protocol

> **Purpose:** Define how to collect and present proof that an artifact or sprint actually did what it claims to do, safely.

---

## What is an Evidence Package?
An evidence package is a collection of files (usually Markdown, JSON, or text) that proves a specific capability, test result, or safety guarantee. AFEF supplies the protocol; an adopting repository owns its operational evidence under `.afef/evidence/` or another explicitly authorized external location.

## Minimum Evidence Fields
Every evidence package must state:
1. **What is being proven** (e.g., "An authorized external write completed").
2. **The environment** (Local, CI, Live).
3. **The mode** (Fake/Default vs. Real).
4. **The result** (Success, Failure, Blocked).
5. **The raw output** (Logs, API responses, terminal output).

## Evidence Quality Levels
- **Strong:** Full audit logs, raw API JSON responses, idempotency markers, clean safety scans.
- **Acceptable:** Terminal output showing success, passing test suites, clean safety scans.
- **Weak:** "It works on my machine" text, missing logs, missing scans.
- **Missing:** No output provided.

## Redaction Requirements
**CRITICAL:** Evidence packages may be committed or transferred for review. They MUST be redacted before either action.
1. **Tokens:** Replace real tokens with `[REDACTED_ACCESS_TOKEN]`.
2. **Authorization Headers:** Replace header values with `Bearer [REDACTED]`.
3. **Passwords/Secrets:** Remove entirely.

## Secret and Local Path Scans
Before committing an evidence package, you must run:
- A token scan (e.g., searching for populated authorization headers and credential assignments).
- A local path scan (e.g., searching for `/home/username/`).
Include the clean results of these scans in the completion report.

## Offline vs Live Evidence Labeling
- **Offline / Mocked Evidence:** Must be labeled clearly as "Mocked", "Fake", or "Local SQLite Only".
- **Live / Real Evidence:** Must be labeled as "Live" or "Real External API" and must identify the authorized target without exposing credentials.

## Documenting What Evidence Does NOT Prove
Evidence is often narrow. If a smoke test proves the adapter works, it does not prove the UI works.
- Explicitly state: "This evidence does NOT prove [X]." This prevents overclaiming.
