# Task 010: Sync platform-playwright

## Objective
Sync kernel infrastructure from master to platform-playwright repo.

## Instructions

```bash
bash tasks/sync-all-domain-specs/sync-kernel.sh "D:/my_ai_projects/project_test_repos/platform-playwright"
```

## Acceptance Criteria
- platform-playwright has 15 kernel commands in `.claude/commands/kernel/`
- platform-playwright has 7 kernel skill folders in `.claude/skills/`
- platform-playwright has 6 kernel hooks in `.claude/hooks/`
- Domain commands preserved (pr, qa-on-failure, qa-pre-construction, qa-propose-fix, qa-reuse-check, qa-workflow, qa-workflow-dev, run-test)
- Domain skill preserved (qa-management-layer/)

## Gate
BUILD-10
