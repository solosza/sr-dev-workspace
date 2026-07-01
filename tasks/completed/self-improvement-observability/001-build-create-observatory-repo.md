# Create kernel-observatory repo

## Context
Creates the new kernel-observatory repo at D:/my_ai_projects/kernel-observatory. This is the Tier 3 infrastructure repo that houses metrics aggregation, experiment tracking, and extension commands.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- Create directory at `D:/my_ai_projects/kernel-observatory`
- Initialize git repo
- Create directory structure:
  ```
  kernel-observatory/
  ├── lib/
  ├── schemas/
  ├── commands/kernel/
  └── docs/
  ```
- Create `.gitignore` (Python defaults + .jsonl data files in root)

## Acceptance Criteria
- [ ] `D:/my_ai_projects/kernel-observatory` exists
- [ ] `git -C D:/my_ai_projects/kernel-observatory status` exits 0
- [ ] `lib/`, `schemas/`, `commands/kernel/`, `docs/` directories exist

## Gates Satisfied
- BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
