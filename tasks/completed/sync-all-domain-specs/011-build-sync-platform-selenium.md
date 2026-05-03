# Task 011: Sync platform-selenium

## Objective
Sync kernel infrastructure from master to platform-selenium repo.

## Instructions

```bash
bash tasks/sync-all-domain-specs/sync-kernel.sh "D:/my_ai_projects/project_test_repos/platform-selenium"
```

## Acceptance Criteria
- platform-selenium has 15 kernel commands in `.claude/commands/kernel/`
- platform-selenium has 7 kernel skill folders in `.claude/skills/`
- platform-selenium has 6 kernel hooks in `.claude/hooks/`
- Domain commands preserved (pr, qa-on-failure, etc.)
- Domain skill preserved (qa-management-layer/)

## Gate
BUILD-11
