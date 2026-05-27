# Initial Commit

## Type
BUILD

## Execution
inline

## Dependencies
- 002, 003, 004, 005, 006

## Phase Gate
- [ ] Git repo initialized
- [ ] Kernel .claude/ copied
- [ ] CLAUDE.md copied
- [ ] run-task scripts copied
- [ ] Spec copied

## Requirements
- Stage and commit all files in the workspace:
  ```bash
  git -C "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa" add -A
  git -C "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa" commit -m "feat: scaffold hmsa-healthcare-qa workspace with kernel + spec"
  ```

## Acceptance Criteria
- [ ] `git -C "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa" log --oneline -1` exits 0 and shows commit message

## Gates Satisfied
- BUILD-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
