# Copy Kernel .claude/ Directory

## Type
BUILD

## Execution
inline

## Dependencies
- 001

## Phase Gate
- [ ] Workspace directory exists

## Requirements
- Copy the entire `.claude/` directory from kernel repo to target workspace:
  ```bash
  cp -r "D:\my_ai_projects\isagawa-kernel\.claude" "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude"
  ```
- This copies: commands/kernel/, skills/, hooks/, settings.json, lessons/
- Do NOT copy .claude/state/ (fresh workspace starts with no state)
- Remove any state files that were copied: `rm -rf "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\state"`

## Acceptance Criteria
- [ ] `test -d "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\commands\kernel"` exits 0
- [ ] `test -d "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\skills"` exits 0
- [ ] `test -d "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\hooks"` exits 0
- [ ] No stale state files: `test ! -d "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\state"` OR state dir is empty

## Gates Satisfied
- BUILD-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
