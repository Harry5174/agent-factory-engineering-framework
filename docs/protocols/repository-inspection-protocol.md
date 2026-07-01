# Repository Inspection Protocol

Standard commands for verifying repository state at the start of a session or before/after implementation.

---

## 1. Branch and Status

Run these at the start of every session:

```bash
git branch --show-current
git status -sb
git status --short
git log --oneline -8
```

**What to check:**

- Are you on the expected branch?
- Is the working tree clean?
- Do recent commits match the expected state from the bootstrap?

---

## 2. File Tree Inspection

Get a high-level view of the repository structure:

```bash
find . -maxdepth 3 -type f | sort | sed -n '1,200p'
```

**What to check:**

- Are the expected directories and files present?
- Are there unexpected files (e.g., `.env` tracked, `__pycache__` committed)?

---

## 3. Safety Scans

Scan for tokens, secrets, and sensitive patterns:

```bash
rg -n "TODO|FIXME|token|Authorization|Bearer|GITHUB_ACCESS_TOKEN|AGENT_FACTORY_GITHUB_TOKEN" . || true
```

**What to check:**

- Are there hardcoded tokens or credentials?
- If matches appear, are they in documentation/examples as pattern references (acceptable) or in code as real values (not acceptable)?

---

## 4. Tracked File Hygiene

Verify that sensitive and generated files are not tracked:

```bash
git check-ignore -v .env || true
git ls-files .env
git ls-files "*__pycache__*"
git ls-files "*.pyc"
```

**What to check:**

- `.env` should be gitignored, not tracked
- `__pycache__` and `.pyc` files should not be tracked
- If any of these return results, flag for cleanup

---

## 5. Tests and Lint (When Applicable)

If the sprint involves code changes or the artifact has a test suite:

```bash
pytest
ruff check .
```

If the sprint is docs-only, these may be skipped. Document why if skipped.

---

## 6. Diff Hygiene

Check for whitespace issues in staged changes:

```bash
git diff --check
```

---

## 7. Token and Local Path Scans (For New Content)

After creating new files, scan them for accidental secret or local path leaks:

```bash
rg -n "ghp_|github_pat_|gho_|ghu_|ghs_|ghr_|Bearer |GITHUB_ACCESS_TOKEN=|AGENT_FACTORY_GITHUB_TOKEN=" \
  <path-to-new-content> || true

rg -n "/home/|Desktop/|/Users/" \
  <path-to-new-content> || true
```

**What to check:**

- If matches appear, are they in safety-pattern documentation (acceptable) or real values/paths (not acceptable)?
- Real tokens, real local paths, and real credentials must never appear in committed content

---

## 8. Tag Inspection (For Closeout/Publish)

When verifying publish/tag state:

```bash
git tag --points-at HEAD
git rev-parse HEAD
```

---

## When to Run

| Situation | Run Sections |
|-----------|--------------|
| Start of any session | 1, 2, 3, 4 |
| Before implementation | 1, 2, 3, 4, 6 |
| After implementation | 1, 3, 4, 5, 6, 7 |
| Closeout/publish verification | 1, 4, 8 |
| Docs-only sprint | 1, 3, 4, 6, 7 (skip 5) |
