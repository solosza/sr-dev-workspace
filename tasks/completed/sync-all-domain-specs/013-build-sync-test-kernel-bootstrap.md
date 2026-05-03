# Task 013: Sync test-kernel-bootstrap

## Objective
Sync kernel infrastructure from master to test-kernel-bootstrap repo.

## Instructions

```bash
bash tasks/sync-all-domain-specs/sync-kernel.sh "D:/my_ai_projects/project_test_repos/test-kernel-bootstrap"
```

## Acceptance Criteria
- test-kernel-bootstrap has 15 kernel commands in `.claude/commands/kernel/`
- test-kernel-bootstrap has 7 kernel skill folders in `.claude/skills/`
- test-kernel-bootstrap has 6 kernel hooks in `.claude/hooks/`
- Domain commands preserved (kernel-build, kernel-build-dev, etc.)
- Domain skills preserved (kernel-governance/, qa-management-layer/)

## Gate
BUILD-13
