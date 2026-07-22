# Remove Campaign Python Files

## Context
The D&D game engine is 100% agent-orchestrated — no Python code. The campaign loop has 3 legacy Python files and a tests/ directory with Python tests that must be removed.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- Remove `arc-transition.py` from `D:/my_ai_projects/project_test_repos/dnd-game-engine-test/.claude/skills/campaign/`
- Remove `campaign-loop.py` from the same directory
- Remove `state-manager.py` from the same directory
- Remove Python test files from `tests/` subdirectory (`test_campaign.py`, `test_integration.py`)
- Preserve non-Python files: SKILL.md, contracts/, tests/ directory structure

## Acceptance Criteria
- [x] No `.py` files exist in `D:/my_ai_projects/project_test_repos/dnd-game-engine-test/.claude/skills/campaign/`
- [x] No `.py` files exist in `D:/my_ai_projects/project_test_repos/dnd-game-engine-test/.claude/skills/campaign/tests/`
- [x] SKILL.md still exists
- [x] contracts/ directory still exists

## Gates Satisfied
- BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
