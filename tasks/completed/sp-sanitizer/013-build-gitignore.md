# Create .gitignore with Mapping Store Patterns

## Context
The mapping store is the skeleton key — it maps synthetic names back to real names. Must never be committed.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-build-project-structure

## Phase Gate
- [ ] `D:/my_ai_projects/sp-sanitizer/.git` exists

## Requirements
- Add to `.gitignore`:
  - `*.mapping.json` — mapping store files
  - `output/` — sanitized output directory
  - `*.leak-report.json` — leak reports
  - Standard Python ignores: `__pycache__/`, `*.pyc`, `.venv/`, `dist/`, `*.egg-info/`

## Acceptance Criteria
- [ ] `D:/my_ai_projects/sp-sanitizer/.gitignore` exists
- [ ] Contains `mapping.json` pattern
- [ ] Contains `output/` pattern
- [ ] Contains `__pycache__/` pattern

## Gates Satisfied
- BUILD-13

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
