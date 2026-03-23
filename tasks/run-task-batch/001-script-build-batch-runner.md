# Build Batch Runner Script

## Context
Create `run-task-batch.sh` — the batch counterpart to `run-task.sh`. One-shot runs one task per `claude -p` invocation. Batch runs all tasks in a single `claude -p` session. The agent handles task-to-task flow internally via kernel cycling. The outer script's job: start, timeout guard, resume on crash, report.

## Dependencies
- None

## Requirements
- Create `run-task-batch.sh` in `C:/Users/solos/my_ai_projects/run-task-resume-master/`
- Script accepts arguments: `repo_path` (default: `.`), `task_folder` (default: none), `timeout_seconds` (default: 600)
- Validate repo: check CLAUDE.md exists
- Windows compatibility: cygpath conversion for state paths
- Build a batch prompt that tells the agent to:
  - Follow kernel workflow (session-start, anchor)
  - Cycle through ALL tasks in the folder (not one-shot)
  - Skip after 3 failed attempts per task
  - Output `ALL_TASKS_COMPLETE` when done
- Run `claude -p --dangerously-skip-permissions --output-format json` with the prompt
- Apply timeout via `timeout` command (or platform equivalent)
- Capture `session_id` from JSON output
- If no completion signal (crash/timeout): resume once with `claude -p --resume <session_id>`
- If resume also fails: exit with error and log location
- Log output to `.claude/state/batch_run.log`
- Report final status: tasks completed, tasks skipped, total time
- Update `README.md` in run-task-resume-master with batch usage section

## Acceptance Criteria
- [ ] `C:/Users/solos/my_ai_projects/run-task-resume-master/run-task-batch.sh` exists
- [ ] Script accepts `repo_path`, `task_folder`, and `timeout_seconds` arguments
- [ ] `grep -q 'CLAUDE.md' C:/Users/solos/my_ai_projects/run-task-resume-master/run-task-batch.sh` (validates repo)
- [ ] `grep -q 'output-format.*json' C:/Users/solos/my_ai_projects/run-task-resume-master/run-task-batch.sh` (JSON output)
- [ ] `grep -q 'resume' C:/Users/solos/my_ai_projects/run-task-resume-master/run-task-batch.sh` (resume logic)
- [ ] `grep -q 'ALL_TASKS_COMPLETE' C:/Users/solos/my_ai_projects/run-task-resume-master/run-task-batch.sh` (completion detection)
- [ ] `grep -q 'timeout' C:/Users/solos/my_ai_projects/run-task-resume-master/run-task-batch.sh` (timeout guard)
- [ ] `grep -q 'batch' C:/Users/solos/my_ai_projects/run-task-resume-master/README.md` (docs updated)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
