# Test Batch Runner — Happy Path

## Context
Verify run-task-batch.sh completes all tasks in a single agent session. Uses the test-run-task-resume repo with 3 simple tasks (create hello.txt, create config.json, create summary.md).

## Dependencies
- 001-script-build-batch-runner

## Requirements
- Reset test repo state: `completed_tasks: []`, `skipped_tasks: []`, clean output files
- Copy `run-task-batch.sh` from run-task-resume-master to test-run-task-resume
- Run `bash run-task-batch.sh` against the test repo
- Verify all 3 tasks completed
- Check iteration log for permission_denials count
- Report results

## Acceptance Criteria
- [ ] Test repo state reset before run (0 completed, 0 skipped)
- [ ] `run-task-batch.sh` copied to test repo
- [ ] Script exits 0
- [ ] `C:/Users/solos/my_ai_projects/test-run-task-resume/hello.txt` exists with "Hello from task 1"
- [ ] `C:/Users/solos/my_ai_projects/test-run-task-resume/config.json` exists with valid JSON
- [ ] `C:/Users/solos/my_ai_projects/test-run-task-resume/summary.md` exists and mentions hello.txt and config.json
- [ ] Workflow state shows `completed_tasks` has all 3 task filenames
- [ ] Workflow state shows `skipped_tasks` is empty

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
