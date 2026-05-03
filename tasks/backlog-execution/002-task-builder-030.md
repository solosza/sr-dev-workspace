# 002 — Run Task Builder on Backlog 030 (Portfolio Site)

## Type
BUILD

## Depends On
None

## Goal
Invoke `/kernel/task-builder 030` to decompose the portfolio site build (backlog 030) into atomic tasks.

## Instructions

1. Read `docs/backlog/030-market-build-portfolio-site.md`
2. Invoke `/kernel/task-builder` with backlog 030 as input
3. **STOP after step 8** — write task files only, do NOT auto-execute (step 9)
4. The task-builder will create `tasks/portfolio-site/` with numbered task files

## CRITICAL: Stop After Step 8

The task-builder skill normally auto-executes after writing tasks (step 9). For this task, you MUST stop after step 8 (write tasks + fixtures). Execution will be handled separately by task 004.

When reaching step 9 in the task-builder skill, skip it and invoke `/kernel/complete` instead.

## Acceptance Criteria

- [ ] `tasks/portfolio-site/000-index.md` exists
- [ ] At least 5 numbered task files exist in `tasks/portfolio-site/`
- [ ] Task files cover: research, tech stack, build, deploy, review phases
- [ ] No tasks were executed — only written
