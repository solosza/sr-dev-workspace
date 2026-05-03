# Task 009: Sync platform-deepeval

## Objective
Sync kernel infrastructure from master to platform-deepeval repo.

## Instructions

```bash
bash tasks/sync-all-domain-specs/sync-kernel.sh "D:/my_ai_projects/project_test_repos/platform-deepeval"
```

## Acceptance Criteria
- platform-deepeval has 15 kernel commands in `.claude/commands/kernel/`
- platform-deepeval has 7 kernel skill folders in `.claude/skills/`
- platform-deepeval has 6 kernel hooks in `.claude/hooks/`
- Domain commands preserved (eval-dev, eval-workflow)
- Domain skill preserved (deepeval-management-layer/)

## Gate
BUILD-09
