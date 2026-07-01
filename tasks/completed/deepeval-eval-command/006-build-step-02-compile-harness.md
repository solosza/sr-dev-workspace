# Write step-02-compile-harness.md

## Context
Layer 3 step file for harness compilation. This is the critical step that transforms a folder of files into a live, governed agent harness. It copies kernel + platform-deepeval spec, then runs domain-setup for full initialization (protocol, hooks, state).

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/skills/eval/steps/step-02-compile-harness.md`
- Must contain:
  - **What to do**: copy kernel files, copy platform-deepeval spec, run domain-setup
  - **Pre-generation checkpoint**: read reference files `step-02/kernel-file-list.md` and `step-02/deepeval-file-list.md` before copying
  - **What to produce**: compiled harness — protocol exists, hooks wired, state initialized
  - **Verification**: protocol file exists, settings.local.json has hook entries, session_state.json exists
  - **Error handling**: if domain-setup fails, capture error, check missing files, retry once after fixing
  - **Critical distinction**: this is compilation, not file copy — the repo must be a live agent harness
- References: `references/step-02/kernel-file-list.md`, `references/step-02/deepeval-file-list.md`
- Source material: `docs/backlog/157-kernel-build-deepeval-command-testing/harness-compilation.md`
- Must be under 200 lines

## Acceptance Criteria
- [ ] File exists at `.claude/skills/eval/steps/step-02-compile-harness.md`
- [ ] `grep -q "domain-setup" .claude/skills/eval/steps/step-02-compile-harness.md` passes
- [ ] `grep -q "kernel-file-list" .claude/skills/eval/steps/step-02-compile-harness.md` passes
- [ ] `grep -q "deepeval-file-list" .claude/skills/eval/steps/step-02-compile-harness.md` passes
- [ ] File is under 200 lines

## Gates Satisfied
BUILD-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
