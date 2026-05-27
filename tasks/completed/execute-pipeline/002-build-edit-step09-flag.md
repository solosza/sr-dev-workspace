# Edit step-09-execute.md — Add no_execute Flag

## Context
Task-builder step 9 (execute) currently auto-starts cycling. The execute-pipeline command needs task-builder to stop after step 8 (write tasks) so run-task.sh takes over execution. Adding a flag check at the top of step 9.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- Add a flag check section at the TOP of `.claude/skills/task-builder/references/step-09-execute.md`, before the existing "Process" section
- Check: read `session_state.json`, if `pipeline_mode.no_execute` is `true`, skip this step — report the task folder path and return
- The skip output should include: project name, task folder path, task count, so the caller knows what to pass to run-task.sh
- Do NOT modify any other content in the file
- Standalone task-builder usage is unchanged (flag is not set by default)

## Acceptance Criteria
- [ ] `grep -q 'no_execute' .claude/skills/task-builder/references/step-09-execute.md` exits 0
- [ ] The flag check section appears BEFORE the existing "Process" section
- [ ] Existing execute logic is unchanged

## Gates Satisfied
- BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
