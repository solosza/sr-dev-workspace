# Task 002: Sync cognitive-agent

## Objective
Sync kernel infrastructure from master to cognitive-agent repo.

## Instructions

```bash
bash tasks/sync-all-domain-specs/sync-kernel.sh "D:/my_ai_projects/project_test_repos/cognitive-agent"
```

Verify output shows all categories synced successfully.

## Acceptance Criteria
- cognitive-agent has 15 kernel commands in `.claude/commands/kernel/`
- cognitive-agent has 7 kernel skill folders in `.claude/skills/`
- cognitive-agent has 6 kernel hooks in `.claude/hooks/`
- Domain commands preserved (image-on-failure, image-pre-construction, etc.)

## Gate
BUILD-02
