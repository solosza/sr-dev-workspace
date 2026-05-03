# Task 001: Build — Sync Kernel Commands

## Objective
Copy all 15 kernel commands from sr_dev_workspace to isagawa-kernel, replacing outdated versions.

## Instructions

1. Copy all files from sr_dev `.claude/commands/kernel/` to master `.claude/commands/kernel/`:
   ```bash
   cp "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/commands/kernel/"*.md "D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/"
   ```
2. Verify 15 files exist in master after copy

## Acceptance Criteria
- 15 .md files in `D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/`
- All match sr_dev versions (zero diff)

## Gate
BUILD-01
