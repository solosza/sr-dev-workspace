# Task 007: Sync hmsa-healthcare-qa

## Objective
Sync kernel infrastructure from master to hmsa-healthcare-qa repo.

## Instructions

```bash
bash tasks/sync-all-domain-specs/sync-kernel.sh "D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa"
```

## Acceptance Criteria
- hmsa-healthcare-qa has 15 kernel commands in `.claude/commands/kernel/`
- hmsa-healthcare-qa has 7 kernel skill folders in `.claude/skills/`
- hmsa-healthcare-qa has 6 kernel hooks in `.claude/hooks/`
- Domain commands preserved (create-ado-test-cases, create-sql-dump, qa-onboard, qa-review, qa-test)
- Domain skill preserved (healthcare-qa/)

## Gate
BUILD-07
