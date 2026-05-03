# Task 003: Sync domain-spec-factory

## Objective
Sync kernel infrastructure from master to domain-spec-factory repo.

## Instructions

```bash
bash tasks/sync-all-domain-specs/sync-kernel.sh "D:/my_ai_projects/project_test_repos/domain-spec-factory"
```

## Acceptance Criteria
- domain-spec-factory has 15 kernel commands in `.claude/commands/kernel/`
- domain-spec-factory has 7 kernel skill folders in `.claude/skills/`
- domain-spec-factory has 6 kernel hooks in `.claude/hooks/`
- Domain commands preserved (spec-factory-build, spec-factory-run, spec-factory-score)
- Domain skill preserved (spec-factory/)

## Gate
BUILD-03
