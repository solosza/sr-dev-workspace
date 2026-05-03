# Copy scanner/ Package

## Type
BUILD

## Execution
inline

## Dependencies
- 007

## Requirements
- Copy the entire scanner/ package from sr_dev_workspace to target:
  ```bash
  cp -r "D:\my_ai_projects\project_test_repos\sr_dev_workspace\scanner" "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\scanner"
  rm -rf "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\scanner\__pycache__"
  ```

## Acceptance Criteria
- [ ] `test -f "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\scanner\__init__.py"` exits 0
- [ ] `test -f "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\scanner\analyzer.py"` exits 0

## Gates Satisfied
- BUILD-10

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
