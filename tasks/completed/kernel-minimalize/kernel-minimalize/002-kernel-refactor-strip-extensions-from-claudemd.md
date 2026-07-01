# Strip Extensions from CLAUDE.md

## Context
CLAUDE.md currently lists 12+ commands including execute-pipeline, task-builder, prod-test, audit-workflow, backlog, attest, scan-bookmarks. These are extensions, not kernel. Strip the Commands section to core governance only.

## Type
REFACTOR

## Execution
inline

## Dependencies
- 001-kernel-build-feature-freeze-policy

## Phase Gate
- [ ] `docs/kernel-feature-freeze-policy.md` exists

## Requirements
- Read `CLAUDE.md`
- In the Commands section, keep ONLY: session-start, domain-setup, anchor, learn, fix, complete, reset
- Move removed commands to a new "Extensions" subsection below Commands with a note: "These are workspace extensions, not kernel core. They are installed per-workspace."
- Do NOT remove the skills section entries for domain-setup and autonomous-cycling (these are core)
- Keep all other CLAUDE.md content unchanged (The Loop, Smart Gates, Principles, etc.)

## Acceptance Criteria
- [ ] Commands section lists only 7 core commands
- [ ] Extensions subsection lists removed commands
- [ ] Skills section unchanged for core skills

## Gates Satisfied
- REFACTOR-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
