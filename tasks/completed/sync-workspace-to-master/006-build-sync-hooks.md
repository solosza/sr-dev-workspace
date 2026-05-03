# Task 006: Build — Sync All Hooks

## Objective
Replace 2 differing hooks and copy 4 missing hooks to master.

## Instructions

1. Copy all kernel hooks (replaces existing, adds missing):
   ```bash
   cp "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/hooks/universal-gate-enforcer.py" "D:/my_ai_projects/isagawa-kernel/.claude/hooks/"
   cp "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/hooks/test-failure-detector.py" "D:/my_ai_projects/isagawa-kernel/.claude/hooks/"
   cp "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/hooks/actions-log-appender.py" "D:/my_ai_projects/isagawa-kernel/.claude/hooks/"
   cp "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/hooks/agent-inline-execution-blocker.py" "D:/my_ai_projects/isagawa-kernel/.claude/hooks/"
   cp "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/hooks/auto-approve-claude-writes.py" "D:/my_ai_projects/isagawa-kernel/.claude/hooks/"
   ```
2. Copy domain gate enforcer as template:
   ```bash
   cp "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/hooks/sr_dev-gate-enforcer.py" "D:/my_ai_projects/isagawa-kernel/.claude/hooks/domain-gate-enforcer.template.py"
   ```
3. Verify 6+ .py files in master hooks directory

## Acceptance Criteria
- 5 kernel hooks + 1 template = 6 .py files in master hooks
- universal-gate-enforcer.py and test-failure-detector.py match sr_dev

## Gate
BUILD-06
