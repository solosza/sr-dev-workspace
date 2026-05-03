# Task 006: Sync healthcare-qa-spec-master

## Objective
Sync kernel infrastructure from master to healthcare-qa-spec-master repo.

## Instructions

```bash
bash tasks/sync-all-domain-specs/sync-kernel.sh "D:/my_ai_projects/project_test_repos/healthcare-qa-spec-master"
```

## Acceptance Criteria
- healthcare-qa-spec-master has 15 kernel commands in `.claude/commands/kernel/`
- healthcare-qa-spec-master has 7 kernel skill folders in `.claude/skills/`
- healthcare-qa-spec-master has 6 kernel hooks in `.claude/hooks/`
- Domain commands preserved (qa-onboard, qa-review, qa-test)
- Domain skill preserved (healthcare-qa/)

## Gate
BUILD-06
