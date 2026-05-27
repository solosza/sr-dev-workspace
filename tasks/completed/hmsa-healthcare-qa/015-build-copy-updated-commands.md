# Copy Updated Kernel Commands

## Type
BUILD

## Execution
inline

## Dependencies
- 007

## Requirements
- Copy the updated learn.md (with recurrence check Step 5) from sr_dev_workspace:
  ```bash
  cp "D:\my_ai_projects\project_test_repos\sr_dev_workspace\.claude\commands\kernel\learn.md" "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\commands\kernel\learn.md"
  ```
- Copy scan-bookmarks.md:
  ```bash
  cp "D:\my_ai_projects\project_test_repos\sr_dev_workspace\.claude\commands\kernel\scan-bookmarks.md" "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\commands\kernel\scan-bookmarks.md"
  ```
- Copy execute-pipeline.md:
  ```bash
  cp "D:\my_ai_projects\project_test_repos\sr_dev_workspace\.claude\commands\kernel\execute-pipeline.md" "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\commands\kernel\execute-pipeline.md"
  ```
- Copy execute-pipeline skill:
  ```bash
  cp -r "D:\my_ai_projects\project_test_repos\sr_dev_workspace\.claude\skills\execute-pipeline" "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\skills\execute-pipeline"
  ```

## Acceptance Criteria
- [ ] `grep -q 'Recurrence' "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\commands\kernel\learn.md"` exits 0
- [ ] `test -f "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\commands\kernel\scan-bookmarks.md"` exits 0
- [ ] `test -f "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\commands\kernel\execute-pipeline.md"` exits 0

## Gates Satisfied
- BUILD-12

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
