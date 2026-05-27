# Copy Test Packages

## Type
BUILD

## Execution
inline

## Dependencies
- 010, 011, 012

## Phase Gate
- [ ] lessons/, delegation/, scanner/ packages exist in target

## Requirements
- Create tests/ directory and copy all 5 test packages:
  ```bash
  mkdir -p "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\tests"
  cp -r "D:\my_ai_projects\project_test_repos\sr_dev_workspace\tests\test_recurrence" "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\tests\test_recurrence"
  cp -r "D:\my_ai_projects\project_test_repos\sr_dev_workspace\tests\test_decay" "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\tests\test_decay"
  cp -r "D:\my_ai_projects\project_test_repos\sr_dev_workspace\tests\test_extraction" "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\tests\test_extraction"
  cp -r "D:\my_ai_projects\project_test_repos\sr_dev_workspace\tests\test_delegation" "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\tests\test_delegation"
  cp -r "D:\my_ai_projects\project_test_repos\sr_dev_workspace\tests\test_scanner" "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\tests\test_scanner"
  ```
- Remove __pycache__ from all copied dirs

## Acceptance Criteria
- [ ] `test -d "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\tests\test_recurrence"` exits 0
- [ ] `test -d "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\tests\test_decay"` exits 0
- [ ] `test -d "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\tests\test_extraction"` exits 0
- [ ] `test -d "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\tests\test_delegation"` exits 0
- [ ] `test -d "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\tests\test_scanner"` exits 0

## Gates Satisfied
- BUILD-11

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
