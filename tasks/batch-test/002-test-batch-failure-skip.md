# Test Batch Runner — Failure + Skip

## Context
Verify run-task-batch.sh handles an impossible task correctly. Agent should skip it after 3 internal attempts and complete remaining tasks.

## Dependencies
- None

## Phase Gate
- [ ] `C:/Users/solos/my_ai_projects/run-task-resume-master/run-task-batch.sh` exists

## Requirements
- Ensure test repo has exactly 4 task files: 001-create-hello.md, 002-create-config.md, 003-impossible-task.md, 004-create-summary.md
- Create 003-impossible-task.md if it doesn't exist (requires reading nonexistent-api-response.json, writing output/secret.txt)
- Rename create-summary to 004 if needed
- Reset test repo state via python script: completed_tasks=[], skipped_tasks=[], total_tasks=4, session_started=false, clean output files and logs
- Run `bash C:/Users/solos/my_ai_projects/test-run-task-resume/run-task-batch.sh C:/Users/solos/my_ai_projects/test-run-task-resume` in background
- Wait for completion
- Read and verify all output files and state

## Acceptance Criteria
- [ ] Test repo `tasks/` has exactly 4 .md files (verify with ls)
- [ ] Workflow state before run: completed_tasks empty, skipped_tasks empty (verify by reading JSON)
- [ ] Batch script completes (verify from task output)
- [ ] `C:/Users/solos/my_ai_projects/test-run-task-resume/hello.txt` contains "Hello from task 1" (verify by reading file)
- [ ] `C:/Users/solos/my_ai_projects/test-run-task-resume/config.json` is valid JSON (verify by reading file)
- [ ] `C:/Users/solos/my_ai_projects/test-run-task-resume/summary.md` mentions hello.txt and config.json (verify by reading file)
- [ ] `C:/Users/solos/my_ai_projects/test-run-task-resume/output/secret.txt` does NOT exist (verify — impossible task was skipped)
- [ ] Workflow state after run: completed_tasks contains 001, 002, 004 (verify by reading JSON)
- [ ] Workflow state after run: skipped_tasks contains 003 (verify by reading JSON)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
