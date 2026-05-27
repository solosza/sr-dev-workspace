# Copy CLAUDE.md

## Type
BUILD

## Execution
inline

## Dependencies
- 001

## Phase Gate
- [ ] Workspace directory exists

## Requirements
- Copy CLAUDE.md from kernel repo:
  ```bash
  cp "D:\my_ai_projects\isagawa-kernel\CLAUDE.md" "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\CLAUDE.md"
  ```

## Acceptance Criteria
- [ ] `test -f "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\CLAUDE.md"` exits 0

## Gates Satisfied
- BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
