# Commit All Features

## Type
BUILD

## Execution
inline

## Dependencies
- 017

## Phase Gate
- [ ] All tests passing
- [ ] All imports verified

## Requirements
- Stage and commit all feature files:
  ```bash
  git -C "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa" add -A
  git -C "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa" commit -m "feat: install kernel features (lessons, delegation, scanner) + tests"
  ```

## Acceptance Criteria
- [ ] `git -C "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa" log --oneline -1` shows feature commit
- [ ] `git -C "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa" status --porcelain` is empty (clean working tree)

## Gates Satisfied
- BUILD-13

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
