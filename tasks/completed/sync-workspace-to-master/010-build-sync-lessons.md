# Task 010: Build — Copy Lessons

## Objective
Copy .claude/lessons/ directory (17 markdown files) to master.

## Instructions

1. Create directory:
   ```bash
   mkdir -p "D:/my_ai_projects/isagawa-kernel/.claude/lessons"
   ```
2. Copy all lesson files:
   ```bash
   cp "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/lessons/"*.md "D:/my_ai_projects/isagawa-kernel/.claude/lessons/"
   ```
3. Verify lessons.md exists in master

## Acceptance Criteria
- `.claude/lessons/lessons.md` exists in master
- 17 .md files in `.claude/lessons/`

## Gate
BUILD-10
