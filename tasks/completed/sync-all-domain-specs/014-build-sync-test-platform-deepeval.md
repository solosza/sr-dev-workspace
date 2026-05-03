# Task 014: Sync test-platform-deepeval

## Objective
Sync kernel infrastructure from master to test-platform-deepeval repo.

## Instructions

```bash
bash tasks/sync-all-domain-specs/sync-kernel.sh "D:/my_ai_projects/project_test_repos/test-platform-deepeval"
```

## Acceptance Criteria
- test-platform-deepeval has 15 kernel commands in `.claude/commands/kernel/`
- test-platform-deepeval has 7 kernel skill folders in `.claude/skills/`
- test-platform-deepeval has 6 kernel hooks in `.claude/hooks/`
- Domain skill preserved (deepeval-management-layer/)

## Gate
BUILD-14
