# Remove Rest Python Files

## Context
The D&D game engine is 100% agent-orchestrated — no Python code. The rest loop has 4 legacy Python files and a tests/ directory with Python tests that must be removed.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- Remove `__init__.py` from `D:/my_ai_projects/project_test_repos/dnd-game-engine-test/.claude/skills/rest/`
- Remove `rest_operations.py` from the same directory
- Remove `condition_removal.py` from the same directory
- Remove `interruption.py` from the same directory
- Remove Python test files from `tests/` subdirectory (`__init__.py`, `test_rest.py`)
- Preserve non-Python files: SKILL.md, rest-loop-contract.json, tests/ directory structure

## Acceptance Criteria
- [ ] No `.py` files exist in `D:/my_ai_projects/project_test_repos/dnd-game-engine-test/.claude/skills/rest/`
- [ ] No `.py` files exist in `D:/my_ai_projects/project_test_repos/dnd-game-engine-test/.claude/skills/rest/tests/`
- [ ] SKILL.md still exists
- [ ] rest-loop-contract.json still exists

## Gates Satisfied
- BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
