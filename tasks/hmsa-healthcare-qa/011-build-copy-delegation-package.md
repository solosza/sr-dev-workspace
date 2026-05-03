# Copy delegation/ Package

## Type
BUILD

## Execution
inline

## Dependencies
- 007

## Requirements
- Copy the entire delegation/ package from sr_dev_workspace to target:
  ```bash
  cp -r "D:\my_ai_projects\project_test_repos\sr_dev_workspace\delegation" "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\delegation"
  rm -rf "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\delegation\__pycache__"
  ```

## Acceptance Criteria
- [ ] `test -f "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\delegation\__init__.py"` exits 0
- [ ] `test -f "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\delegation\engine.py"` exits 0

## Gates Satisfied
- BUILD-09

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
