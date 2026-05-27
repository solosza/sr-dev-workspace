# Copy Healthcare-QA Spec

## Type
BUILD

## Execution
inline

## Dependencies
- 001

## Phase Gate
- [ ] Workspace directory exists

## Requirements
- Copy spec contents (NOT the .git or .claude dirs) from healthcare-qa-spec:
  ```bash
  cp "D:\my_ai_projects\project_test_repos\specs\health-insurance\healthcare-qa-spec\README.md" "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\README.md"
  cp -r "D:\my_ai_projects\project_test_repos\specs\health-insurance\healthcare-qa-spec\_test" "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\_test"
  ```
- Copy any other spec files (check for additional files beyond README.md and _test/)
- Do NOT copy the spec's .git/ or .claude/ — the workspace has its own kernel

## Acceptance Criteria
- [ ] `test -f "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\README.md"` exits 0
- [ ] Spec content is present in workspace

## Gates Satisfied
- BUILD-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
