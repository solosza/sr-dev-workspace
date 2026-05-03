# Create pyproject.toml

## Context
Project configuration with dependencies (pydantic) and dev dependencies (pytest). CLI entry point for the runner.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-build-project-structure

## Phase Gate
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/__init__.py` exists

## Requirements
- Python 3.10+ required
- pydantic as runtime dependency
- pytest as dev dependency
- CLI entry point: `sp-sanitizer = "sp_sanitizer.runner:main"`
- Package name: `sp-sanitizer`

## Acceptance Criteria
- [ ] `D:/my_ai_projects/sp-sanitizer/pyproject.toml` exists
- [ ] Contains `[project]` section with name `sp-sanitizer`
- [ ] Contains pydantic in dependencies
- [ ] Contains pytest in optional/dev dependencies

## Gates Satisfied
- BUILD-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
