# Task 005: Sync game-engine-master

## Objective
Sync kernel infrastructure from master to game-engine-master repo.

## Instructions

```bash
bash tasks/sync-all-domain-specs/sync-kernel.sh "D:/my_ai_projects/project_test_repos/game-engine-master"
```

## Acceptance Criteria
- game-engine-master has 15 kernel commands in `.claude/commands/kernel/`
- game-engine-master has 7 kernel skill folders in `.claude/skills/`
- game-engine-master has 6 kernel hooks in `.claude/hooks/`
- Domain commands preserved (game-build, game-create)
- Domain skill preserved (game-engine/)

## Gate
BUILD-05
