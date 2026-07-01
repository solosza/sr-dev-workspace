# Write step-02/kernel-file-list.md

## Context
Layer 4 reference payload for Step 2 (Compile Harness). Lists the exact files and directories to copy from the kernel into the test repo. The step file reads this reference before copying.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/skills/eval/references/step-02/kernel-file-list.md`
- Must list the exact files/directories to copy from the kernel (workspace or golden master):
  - `.claude/commands/kernel/` — all kernel commands
  - `.claude/protocols/` — protocol template
  - `.claude/hooks/` — universal-gate-enforcer.py, domain enforcer, auto-approve, actions-log-appender, test-failure-detector
  - `.claude/state/` — fresh state files (session_state.json, workflow.json)
  - `.claude/skills/kernel-domain-setup/` — so domain-setup can run
  - `.claude/skills/autonomous-cycling/` — for task execution
  - `.claude/lessons/` — lessons.md (RULE ZERO template)
  - `.claude/settings.local.json` — hook registrations
  - `run-task.sh` — task execution script
  - `CLAUDE.md` — kernel CLAUDE.md
- Source material: `docs/backlog/157-kernel-build-deepeval-command-testing/harness-compilation.md` (What Gets Copied section)
- Must be under 200 lines

## Acceptance Criteria
- [ ] File exists at `.claude/skills/eval/references/step-02/kernel-file-list.md`
- [ ] `grep -q "universal-gate-enforcer" .claude/skills/eval/references/step-02/kernel-file-list.md` passes
- [ ] `grep -q "CLAUDE.md" .claude/skills/eval/references/step-02/kernel-file-list.md` passes
- [ ] `grep -q "run-task.sh" .claude/skills/eval/references/step-02/kernel-file-list.md` passes
- [ ] File is under 200 lines

## Gates Satisfied
BUILD-12

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
