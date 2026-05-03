# Task 012: Sync test-content-production

## Objective
Sync kernel infrastructure from master to test-content-production repo.

## Instructions

```bash
bash tasks/sync-all-domain-specs/sync-kernel.sh "D:/my_ai_projects/project_test_repos/test-content-production"
```

## Acceptance Criteria
- test-content-production has 15 kernel commands in `.claude/commands/kernel/`
- test-content-production has 7 kernel skill folders in `.claude/skills/`
- test-content-production has 6 kernel hooks in `.claude/hooks/`
- Domain commands preserved (content-calendar, content-produce, content-repurpose)
- Domain skill preserved (content-production/)

## Gate
BUILD-12
