# Copy lessons/ Package

## Type
BUILD

## Execution
inline

## Dependencies
- 007

## Requirements
- Copy the entire lessons/ package from sr_dev_workspace to target:
  ```bash
  cp -r "D:\my_ai_projects\project_test_repos\sr_dev_workspace\lessons" "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\lessons"
  ```
- Remove __pycache__ if copied:
  ```bash
  rm -rf "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\lessons\__pycache__"
  ```

## Acceptance Criteria
- [ ] `test -f "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\lessons\__init__.py"` exits 0
- [ ] `test -f "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\lessons\recurrence.py"` exits 0
- [ ] `test -f "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\lessons\integrations.py"` exits 0

## Gates Satisfied
- BUILD-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
