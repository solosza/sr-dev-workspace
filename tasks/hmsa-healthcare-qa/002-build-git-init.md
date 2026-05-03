# Initialize Git Repo

## Type
BUILD

## Execution
inline

## Dependencies
- 001

## Phase Gate
- [ ] Directory exists at `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa`

## Requirements
- Run `git init "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa"`
- Do NOT use cd — use the path argument to git init

## Acceptance Criteria
- [ ] `test -d "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.git"` exits 0

## Gates Satisfied
- BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
