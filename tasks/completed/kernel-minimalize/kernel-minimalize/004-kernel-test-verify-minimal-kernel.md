# Verify Minimal Kernel

## Context
Verify that CLAUDE.md reflects the minimal kernel, the feature freeze policy is complete, and core governance components are all present.

## Type
TEST

## Execution
agent

## Dependencies
- 002-kernel-refactor-strip-extensions-from-claudemd
- 003-kernel-refactor-document-core-vs-extension

## Phase Gate
- [ ] CLAUDE.md has been updated
- [ ] `docs/kernel-core-vs-extension.md` exists

## Requirements
- Grep CLAUDE.md Commands section for non-core commands (execute-pipeline, task-builder, prod-test, audit-workflow, backlog, attest, scan-bookmarks). Should NOT appear in Commands section.
- Grep CLAUDE.md for core commands (session-start, anchor, learn, complete, fix, domain-setup, reset). All should be present.
- Verify `docs/kernel-feature-freeze-policy.md` exists and lists freeze rule
- Verify `docs/kernel-core-vs-extension.md` exists and has classification table
- Report pass/fail for each check

## Acceptance Criteria
- [ ] No extension commands in CLAUDE.md Commands section
- [ ] All 7 core commands present in CLAUDE.md
- [ ] Feature freeze policy file exists
- [ ] Core vs extension doc exists

## Gates Satisfied
- TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
