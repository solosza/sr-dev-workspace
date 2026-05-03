# Write step-03-run-task-builder.md

## Context
Step 3 of execute-pipeline: invoke task-builder with flags to skip plan review and stop before execution. The task-builder reads the backlog file and decomposes into tasks.

## Type
BUILD

## Execution
inline

## Dependencies
- 003 (references directory must exist)

## Requirements
- Write `.claude/skills/execute-pipeline/references/step-03-run-task-builder.md`
- Before invoking task-builder, set flags in session_state.json:
  ```json
  {
    "pipeline_mode": {
      "skip_plan_review": true,
      "no_execute": true
    }
  }
  ```
- Invoke `/kernel/task-builder` with `pipeline_state.backlog_path` as argument
- Task-builder reads flags → skips step 7 (plan review) → stops after step 8 (write tasks)
- Capture task folder path and task count from task-builder output into `pipeline_state`
- After task-builder completes, clear `pipeline_mode` from session_state.json
- Document the flag mechanism clearly so future readers understand the handoff

## Acceptance Criteria
- [ ] `test -f .claude/skills/execute-pipeline/references/step-03-run-task-builder.md` exits 0
- [ ] File documents flag setting before task-builder invocation
- [ ] File documents flag clearing after task-builder completion
- [ ] File documents what pipeline_state fields get captured

## Gates Satisfied
- BUILD-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
