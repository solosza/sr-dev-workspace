# Gate Contract — Fix Execute-Pipeline Cycling

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | MAX_CONSECUTIVE_FAILS=4 | grep | `grep -q 'MAX_CONSECUTIVE_FAILS=4' run-task.sh` | Edit value |
| BUILD-02 | Empty output backoff logic | grep | `grep -q 'EMPTY_OUTPUT_BACKOFF' run-task.sh` | Add backoff |
| BUILD-03 | Pre-check dedup uses set() | grep | `grep -q 'set(' run-task.sh` | Fix dedup |
| BUILD-04 | complete.md dedup check | grep | `grep -qi 'already in.*completed_tasks\|duplicate\|not already' .claude/commands/kernel/complete.md` | Add check |
| BUILD-05 | step-03 atomic enforcement | grep | `grep -qi 'ATOMIC\|MECHANICAL\|MUST NOT STOP' .claude/skills/execute-pipeline/references/step-03-run-task-builder.md` | Strengthen |
| BUILD-06 | step-04 pipeline_mode guard | grep | `grep -q 'pipeline_mode' .claude/skills/execute-pipeline/references/step-04-execute-tasks.md` | Add guard |
| BUILD-07 | step-08 total_tasks pre-write | grep | `grep -q 'total_tasks' .claude/skills/task-builder/references/step-08-write-tasks.md` | Add pre-write |
| TEST-01 | All BUILD gates pass | run_code | All BUILD-01 through BUILD-07 pass | Fix remaining |
