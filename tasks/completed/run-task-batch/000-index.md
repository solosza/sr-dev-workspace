# Run Task Batch — Task Index

## Goal
Build run-task-batch.sh — a batch mode script for headless task execution where the agent runs all tasks in one session with a timeout guard.

## Tasks

| # | Task | Dependencies | Status |
|---|------|-------------|--------|
| 001 | [[001-script-build-batch-runner]] | none | pending |
| 002 | [[002-test-run-batch-happy-path]] | 001 | pending |
| 003 | [[003-test-run-batch-failure-skip]] | 001 | pending |

## Deliverables
- `run-task-batch.sh` in `C:/Users/solos/my_ai_projects/run-task-resume-master/`
- Updated `README.md` with batch usage
- Happy path test passing (3/3 tasks)
- Failure+skip test passing (3 completed, 1 skipped)
