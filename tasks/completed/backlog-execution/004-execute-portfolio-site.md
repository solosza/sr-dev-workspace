# 004 — Execute Portfolio Site Tasks

## Type
BUILD

## Depends On
002

## Goal
Execute all tasks in `tasks/portfolio-site/` via `run-task.sh`, producing a deployed portfolio site.

## Instructions

1. Verify `tasks/portfolio-site/000-index.md` exists (created by task 002)
2. Run: `bash run-task.sh tasks/portfolio-site/`
3. run-task.sh will cycle through each task file autonomously, spawning one-shot agents per task
4. Wait for completion

## Acceptance Criteria

- [ ] All tasks in `tasks/portfolio-site/` are marked complete in workflow state
- [ ] Portfolio site files exist and are deployable
- [ ] Site showcases AI management layer / Isagawa Kernel as centerpiece
