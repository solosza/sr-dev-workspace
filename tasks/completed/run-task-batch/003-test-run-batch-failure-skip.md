# Test Batch Runner — Failure + Skip

## Context
Verify run-task-batch.sh handles an impossible task correctly. The agent should skip the impossible task after 3 internal attempts and complete the remaining tasks. Uses test-run-task-resume repo with 4 tasks (001-hello, 002-config, 003-impossible, 004-summary).

## Dependencies
- 001-script-build-batch-runner

## Requirements
- Reset test repo state: `completed_tasks: []`, `skipped_tasks: []`, clean output files
- Ensure `tasks/003-impossible-task.md` exists (requires reading nonexistent file)
- Ensure `tasks/004-create-summary.md` exists (the task after the impossible one)
- Copy `run-task-batch.sh` from run-task-resume-master to test-run-task-resume
- Run `bash run-task-batch.sh` against the test repo
- Verify 3 tasks completed and 1 skipped
- Report results

## Acceptance Criteria
- [ ] Test repo has 4 task files (001, 002, 003-impossible, 004-summary)
- [ ] Test repo state reset before run (0 completed, 0 skipped)
- [ ] Script completes (exits 0 or reports completion)
- [ ] `hello.txt` exists with correct content
- [ ] `config.json` exists with valid JSON
- [ ] `summary.md` exists and mentions hello.txt and config.json
- [ ] Workflow state `completed_tasks` contains 001, 002, and 004
- [ ] Workflow state `skipped_tasks` contains 003

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
