# Task 014: Test L2 — Verify Content Match

## Objective
Diff sr_dev vs master for all synced categories — expect zero differences.

## Instructions

1. Diff kernel commands:
   ```bash
   diff -rq "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/commands/kernel/" "D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/"
   ```
2. Diff hooks (5 kernel hooks, exclude template):
   ```bash
   for h in universal-gate-enforcer.py test-failure-detector.py actions-log-appender.py agent-inline-execution-blocker.py auto-approve-claude-writes.py; do
     diff "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/hooks/$h" "D:/my_ai_projects/isagawa-kernel/.claude/hooks/$h"
   done
   ```
3. Diff skill SKILL.md files:
   ```bash
   for skill in audit-workflow autonomous-cycling execute-pipeline kernel-domain-setup prod-test task-builder website-cloner; do
     diff "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/$skill/SKILL.md" "D:/my_ai_projects/isagawa-kernel/.claude/skills/$skill/SKILL.md"
   done
   ```

## Acceptance Criteria
- Zero differences in all diffs

## Gate
TEST-14
