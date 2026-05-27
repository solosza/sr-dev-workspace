# Verify All Fixes

## Context
Verify that all 7 BUILD tasks produced correct fixes by running every gate in the gate contract.

## Type
TEST

## Execution
inline

## Dependencies
001, 002, 003, 004, 005, 006, 007

## Phase Gate
- [ ] All 7 BUILD tasks are in `completed_tasks`

## Requirements
- Run each gate from gate-contract.md (BUILD-01 through BUILD-07)
- Read each modified file and confirm the fix is semantically correct (not just grep-matching)
- Verify no unintended changes were introduced

## Acceptance Criteria
- [ ] BUILD-01: `grep -q 'MAX_CONSECUTIVE_FAILS=4' run-task.sh` exits 0
- [ ] BUILD-02: `grep -q 'EMPTY_OUTPUT_BACKOFF' run-task.sh` exits 0
- [ ] BUILD-03: `grep -q 'set(' run-task.sh` exits 0
- [ ] BUILD-04: `grep -qi 'not already\|already present' .claude/commands/kernel/complete.md` exits 0
- [ ] BUILD-05: `grep -qi 'MUST NOT STOP\|atomic' .claude/skills/execute-pipeline/references/step-03-run-task-builder.md` exits 0
- [ ] BUILD-06: `grep -q 'pipeline_mode' .claude/skills/execute-pipeline/references/step-04-execute-tasks.md` exits 0
- [ ] BUILD-07: `grep -q 'total_tasks' .claude/skills/task-builder/references/step-08-write-tasks.md` exits 0

## Gates Satisfied
TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
