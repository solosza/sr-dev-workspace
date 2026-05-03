# Task 004: Sync game-dev

## Objective
Sync kernel infrastructure from master to game-dev repo.

## Instructions

```bash
bash tasks/sync-all-domain-specs/sync-kernel.sh "D:/my_ai_projects/project_test_repos/game-dev"
```

## Acceptance Criteria
- game-dev has 15 kernel commands in `.claude/commands/kernel/`
- game-dev has 7 kernel skill folders in `.claude/skills/`
- game-dev has 6 kernel hooks in `.claude/hooks/`
- Domain commands preserved (game-build, game-create)
- Domain skill preserved (game-engine/)

## Gate
BUILD-04
