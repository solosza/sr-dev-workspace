# Task 008: Sync isagawa-qa-zentyant

## Objective
Sync kernel infrastructure from master to isagawa-qa-zentyant repo.

## Instructions

```bash
bash tasks/sync-all-domain-specs/sync-kernel.sh "D:/my_ai_projects/project_test_repos/isagawa-qa-zentyant"
```

## Acceptance Criteria
- isagawa-qa-zentyant has 15 kernel commands in `.claude/commands/kernel/`
- isagawa-qa-zentyant has 7 kernel skill folders in `.claude/skills/`
- isagawa-qa-zentyant has 6 kernel hooks in `.claude/hooks/`
- Domain commands preserved (pr, qa-on-failure, qa-pre-construction, qa-propose-fix, qa-reuse-check, qa-workflow, qa-workflow-dev, run-test)
- Domain skill preserved (qa-management-layer/)

## Gate
BUILD-08
