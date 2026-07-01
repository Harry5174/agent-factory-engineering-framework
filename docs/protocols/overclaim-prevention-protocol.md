# Overclaim Prevention Protocol

> **Purpose:** Ensure that the project memory and documentation accurately reflect reality, preventing hallucinations about project completion.

---

## What is Overclaiming?
Overclaiming is stating that a feature, artifact, or integration is complete, published, or functional when it has not been verified or lacks evidence.

## Common Overclaim Patterns
1. **The "Done" Illusion:** Assuming that because code was written, the feature is "done" and "released."
2. **The "Live" Illusion:** Assuming that a passing local test with mocked data proves the live integration works.
3. **The "Merged" Illusion:** Assuming a local branch was merged to `main` and tagged just because a sprint ended.

## Distinguishing States
Always use precise language:
- **Implemented:** Code exists on a branch.
- **Tested:** Code passes automated tests (specify if mocked or real).
- **Demoed:** Code was run locally by a human and works.
- **Published/Released:** Code is merged to `main`, tagged, and pushed to the remote.

## Distinguishing Modes
- **Fake/Default:** Uses mock adapters and local SQLite.
- **Real/Live:** Hits external internet APIs (e.g., GitHub).
Never conflate the two in documentation.

## Handling Unknown Publish/Tag State
If an IDE Agent or Supervisor does not have access to run `git fetch` and verify the upstream remote tags, they MUST NOT claim an artifact is published.
- **Required Wording:** "Artifact 06 is complete at the sprint level. Final publish/tag state is unverified and requires operator confirmation."

## Review Checklist for Gate Reviews
Reviewers must check completion reports for overclaims:
- [ ] Did the sprint claim "live" execution but only provide "mock" evidence?
- [ ] Did the sprint claim it is "published" without providing `git log` or `git tag` output showing the main branch?
- [ ] Did the sprint claim it solved a future artifact's problem (e.g., A6 claiming it built a vertical agent)?
If any are true, issue a **YELLOW** or **RED** gate.
