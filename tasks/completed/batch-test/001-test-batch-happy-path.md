# Test Batch Runner — Happy Path

## Context
Verify run-task-batch.sh completes all tasks in a single agent session. Uses test-run-task-resume repo with 3 simple tasks.

## Dependencies
- None

## Requirements
- Ensure test repo has exactly 3 task files: 001-create-hello.md, 002-create-config.md, 003-create-summary.md (remove 003-impossible-task.md and rename 004-create-summary.md to 003 if needed)
- Reset test repo state via python script: completed_tasks=[], skipped_tasks=[], session_started=false, clean output files and logs
- Copy run-task-batch.sh from `C:/Users/solos/my_ai_projects/run-task-resume-master/run-task-batch.sh` to test repo
- Run `bash C:/Users/solos/my_ai_projects/test-run-task-resume/run-task-batch.sh C:/Users/solos/my_ai_projects/test-run-task-resume` in background
- Wait for completion
- Read and verify all output files and state

## Acceptance Criteria
- [ ] Test repo `tasks/` has exactly 3 .md files (verify with ls)
- [ ] Workflow state before run: completed_tasks empty, skipped_tasks empty (verify by reading JSON)
- [ ] Batch script exits 0 (verify from task output)
- [ ] `C:/Users/solos/my_ai_projects/test-run-task-resume/hello.txt` contains "Hello from task 1" (verify by reading file)
- [ ] `C:/Users/solos/my_ai_projects/test-run-task-resume/config.json` is valid JSON with version "1.0" (verify by reading file)
- [ ] `C:/Users/solos/my_ai_projects/test-run-task-resume/summary.md` mentions hello.txt and config.json (verify by reading file)
- [ ] Workflow state after run: completed_tasks has all 3 filenames (verify by reading JSON)
- [ ] Workflow state after run: skipped_tasks is empty (verify by reading JSON)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
