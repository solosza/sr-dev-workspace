# Copy Research Docs

## Type
BUILD

## Execution
inline

## Dependencies
- 007

## Requirements
- Create docs/research/ directory and copy zep cloud analysis:
  ```bash
  mkdir -p "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\docs\research"
  cp "D:\my_ai_projects\project_test_repos\sr_dev_workspace\docs\research\zep-cloud-memory-analysis.md" "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\docs\research\zep-cloud-memory-analysis.md"
  ```
- If the source file doesn't exist, skip this task (it's optional)

## Acceptance Criteria
- [ ] docs/research/ directory exists in target, OR source file doesn't exist (skip)

## Gates Satisfied
- (no gate — optional)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
