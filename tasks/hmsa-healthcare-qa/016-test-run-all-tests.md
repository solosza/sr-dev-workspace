# Run All Tests in Target Workspace

## Type
TEST

## Execution
inline

## Dependencies
- 010, 011, 012, 013, 014, 015

## Phase Gate
- [ ] All feature packages copied
- [ ] All test packages copied
- [ ] Updated commands copied

## Requirements
- Run pytest against all test packages in the target workspace:
  ```bash
  python -m pytest "D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\tests" -v --tb=short
  ```
- All tests should pass (88 tests across 5 packages)
- If tests fail, diagnose and fix before proceeding

## Acceptance Criteria
- [ ] pytest exits 0
- [ ] All test packages run (test_recurrence, test_decay, test_extraction, test_delegation, test_scanner)

## Gates Satisfied
- TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
