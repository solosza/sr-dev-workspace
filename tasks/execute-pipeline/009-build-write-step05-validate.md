# Write step-05-validate-report.md

## Context
Step 5 of execute-pipeline: validate execution results and produce final report. Reads workflow state, checks for skipped/failed tasks, reports to user.

## Type
BUILD

## Execution
inline

## Dependencies
- 003 (references directory must exist)

## Requirements
- Write `.claude/skills/execute-pipeline/references/step-05-validate-report.md`
- Read workflow state to get completed_tasks, skipped_tasks
- Read validation report if one exists at `tasks/[folder]/_test/validation-report.json`
- Read run-task.sh logs if available
- Produce final report:
  ```
  PIPELINE COMPLETE

  Backlog: [backlog file path]
  Tasks: [folder] (N total, M completed, K skipped)
  Execution: [pass/fail]
  Time: [if available]

  [If skipped tasks:]
  Skipped:
  - [task] — [reason if available]

  [If validation report exists:]
  Gates: N/M passed

  Log: [log path]
  ```
- Clear `pipeline_state` from session_state.json

## Acceptance Criteria
- [ ] `test -f .claude/skills/execute-pipeline/references/step-05-validate-report.md` exits 0
- [ ] File documents report format
- [ ] File documents pipeline_state cleanup

## Gates Satisfied
- BUILD-09

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
