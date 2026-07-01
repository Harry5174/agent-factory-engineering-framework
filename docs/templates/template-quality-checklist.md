# Template Quality Checklist

Use this checklist to evaluate whether a prompt, bootstrap, or template is ready for use. A template that fails multiple checks is likely to cause drift, overclaims, or safety issues.

---

## Context Completeness

- [ ] Sprint identity is specified (project, artifact, sprint name, sprint goal)
- [ ] Current phase and artifact status are stated
- [ ] Previous sprint outcome is referenced (or "first sprint" is stated)
- [ ] Completed work is summarized with evidence references, not vague claims

## Repository Grounding

- [ ] Repository path and workspace are specified
- [ ] Expected branch and commit state are stated
- [ ] Repository verification commands are included
- [ ] Expected file tree or key files are listed

## Scope Clarity

- [ ] In-scope deliverables are listed explicitly
- [ ] Out-of-scope items are listed explicitly
- [ ] Hard constraints are stated (e.g., "no runtime code changes")
- [ ] Block conditions define when to stop

## Role Clarity

- [ ] The role of the session participant is stated (Design Supervisor / Implementation Supervisor / IDE Agent / Reviewer)
- [ ] What the role must produce is stated
- [ ] What the role must NOT do is stated

## Approval Clarity

- [ ] Product Owner approval status is stated (Approved / Pending / Not yet requested)
- [ ] Who approved is specified
- [ ] Approval scope is clear (what was approved)
- [ ] Approval limitations are clear (what was NOT approved)
- [ ] No "implicit approval" language without explanation

## Safety Boundaries

- [ ] Standard safety block is present (no secrets, no `.env`, no live side effects without approval)
- [ ] Inherited safety boundaries from prior artifacts are listed
- [ ] Fake/default mode is explicitly the default
- [ ] Real mode requires explicit approval

## Evidence Requirements

- [ ] Evidence categories are listed (branch, commit, files, tests, scans, etc.)
- [ ] Evidence quality expectations are clear
- [ ] Completion report template or format is referenced
- [ ] Scope confirmations (what was NOT changed) are required

## Test and Validation Requirements

- [ ] Test commands are specified (or skip reason is required)
- [ ] Lint commands are specified (or skip reason is required)
- [ ] Safety scan commands are included
- [ ] `git diff --check` is included
- [ ] `.env` verification commands are included

## Block Conditions

- [ ] Block conditions are listed
- [ ] Scope drift is defined as a block condition
- [ ] Safety boundary violations are defined as block conditions
- [ ] Missing required files/state is a block condition

## Handoff Quality

- [ ] Expected output is listed
- [ ] Next-session handoff expectations are stated
- [ ] Commit instructions are specified (branch, message, push/tag rules)

## No Secret Exposure

- [ ] No real tokens, API keys, or credentials appear in the template
- [ ] No real `.env` values are included
- [ ] Scan patterns use token-type prefixes only (e.g., `ghp_`), not real values

## No Local Absolute Paths

- [ ] No real machine-specific paths (e.g., `/home/username/...`)
- [ ] Path examples use relative or placeholder syntax
- [ ] Scan patterns reference path patterns, not real paths

## No Stale Artifact Claims

- [ ] Artifact status claims match known/verified state
- [ ] No forward claims about future artifact completion
- [ ] Cautious wording for unverified states (e.g., "verify publish/tag state")
