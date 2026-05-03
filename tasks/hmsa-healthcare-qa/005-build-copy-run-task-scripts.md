# Copy run-task Scripts + lib

## Type
BUILD

## Execution
inline

## Dependencies
- 001

## Phase Gate
- [ ] Workspace directory exists

## Requirements
- Copy run-task.sh, run-task-batch.sh, and lib/ from sr_dev_workspace:
  ```bash
  cp "D:\my_ai_projects\project_test_repos\sr_dev_workspace\run-task.sh" "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\run-task.sh"
  cp "D:\my_ai_projects\project_test_repos\sr_dev_workspace\run-task-batch.sh" "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\run-task-batch.sh"
  cp -r "D:\my_ai_projects\project_test_repos\sr_dev_workspace\lib" "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\lib"
  ```

## Acceptance Criteria
- [ ] `test -f "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\run-task.sh"` exits 0
- [ ] `test -f "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\run-task-batch.sh"` exits 0
- [ ] `test -d "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\lib"` exits 0

## Gates Satisfied
- BUILD-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
