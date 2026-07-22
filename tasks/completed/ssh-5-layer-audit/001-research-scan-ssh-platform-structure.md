# Scan SSH Platform Structure

## Context
Map all Python files in the SSH platform to understand the current directory layout.

## Type
RESEARCH

## Execution
inline

## Dependencies
- None

## Requirements
- List all Python files in `D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/`
- Identify which files are in `framework/` subdirectories (interfaces, metrics, tasks, roles, tests)
- Identify which files are in `_reference/` subdirectories
- Write results to `tasks/ssh-5-layer-audit/ssh-platform-file-map.md`

## Acceptance Criteria
- [ ] File map exists at `tasks/ssh-5-layer-audit/ssh-platform-file-map.md`
- [ ] Lists all Python files with their directory paths
- [ ] Identifies layer assignment for each file (L1-L5 or unknown)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
