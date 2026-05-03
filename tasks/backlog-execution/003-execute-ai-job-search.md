# 003 — Execute AI Job Search Tasks

## Type
BUILD

## Depends On
001

## Goal
Execute all tasks in `tasks/ai-job-search/` via `run-task.sh`, producing a curated job listing with match scores.

## Instructions

1. Verify `tasks/ai-job-search/000-index.md` exists (created by task 001)
2. Run: `bash run-task.sh tasks/ai-job-search/`
3. run-task.sh will cycle through each task file autonomously, spawning one-shot agents per task
4. Wait for completion

## Acceptance Criteria

- [ ] All tasks in `tasks/ai-job-search/` are marked complete in workflow state
- [ ] Structured job listing output exists (JSON or markdown)
- [ ] Each job entry has: URL, company, title, location, remote status, match score
