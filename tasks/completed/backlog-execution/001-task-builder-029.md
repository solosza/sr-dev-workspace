# 001 — Run Task Builder on Backlog 029 (Job Search)

## Type
BUILD

## Depends On
None

## Goal
Invoke `/kernel/task-builder 029` to decompose the AI harness engineering job search (backlog 029) into atomic tasks.

## Instructions

1. Read `docs/backlog/029-market-research-ai-harness-engineering-jobs.md`
2. Invoke `/kernel/task-builder` with backlog 029 as input
3. **STOP after step 8** — write task files only, do NOT auto-execute (step 9)
4. The task-builder will create `tasks/ai-job-search/` with numbered task files

## CRITICAL: Stop After Step 8

The task-builder skill normally auto-executes after writing tasks (step 9). For this task, you MUST stop after step 8 (write tasks + fixtures). Execution will be handled separately by task 003.

When reaching step 9 in the task-builder skill, skip it and invoke `/kernel/complete` instead.

## Acceptance Criteria

- [ ] `tasks/ai-job-search/000-index.md` exists
- [ ] At least 5 numbered task files exist in `tasks/ai-job-search/`
- [ ] Task files cover: resume read, company searches, result compilation, scoring
- [ ] No tasks were executed — only written
