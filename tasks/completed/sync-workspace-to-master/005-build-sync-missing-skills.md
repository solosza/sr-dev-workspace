# Task 005: Build — Copy 5 Missing Skill Folders

## Objective
Copy 5 skill folders that don't exist in master: audit-workflow, execute-pipeline, prod-test, task-builder, website-cloner.

## Instructions

1. Copy each folder recursively:
   ```bash
   for skill in audit-workflow execute-pipeline prod-test task-builder website-cloner; do
     cp -r "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/$skill" "D:/my_ai_projects/isagawa-kernel/.claude/skills/"
   done
   ```
2. Verify all 5 folders exist with SKILL.md in each

## Acceptance Criteria
- 7 total skill folders in master (2 existing + 5 new)
- Each new folder has SKILL.md

## Gate
BUILD-05
