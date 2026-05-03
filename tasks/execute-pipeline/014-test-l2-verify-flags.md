# L2 Test — Verify Task-Builder Flag Mechanism

## Context
Level 2 functional verification: confirm the skip_plan_review and no_execute flags are properly documented in the task-builder step files and the execute-pipeline skill correctly references them.

## Type
TEST

## Execution
inline

## Dependencies
- 001, 002 (flag edits must be complete)

## Phase Gate
- [ ] 001-build-edit-step07-flag.md in completed_tasks
- [ ] 002-build-edit-step09-flag.md in completed_tasks

## Requirements
1. Read step-07-plan-review.md — verify flag check section exists BEFORE existing content
2. Read step-09-execute.md — verify flag check section exists BEFORE existing content
3. Verify step-07 references `pipeline_mode.skip_plan_review` in session_state.json
4. Verify step-09 references `pipeline_mode.no_execute` in session_state.json
5. Read step-03-run-task-builder.md — verify it sets these flags before invoking task-builder
6. Verify step-03 clears flags after task-builder completes

## Acceptance Criteria
- [ ] step-07 has flag check before existing "When This Step Applies" section
- [ ] step-09 has flag check before existing "Process" section
- [ ] step-03 documents setting `pipeline_mode` before task-builder invocation
- [ ] step-03 documents clearing `pipeline_mode` after task-builder completion
- [ ] Flag field names are consistent across all three files

## Gates Satisfied
- FUNC-01, FUNC-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
