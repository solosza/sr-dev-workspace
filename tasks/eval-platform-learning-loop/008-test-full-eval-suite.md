# Test: full eval suite — 17/17 from platform-deepeval

## Context
Run the complete eval suite from platform-deepeval pointing at isagawa-kernel as the target harness. This is the L3 production test — proves the entire system works end-to-end from the permanent home.

## Type
TEST

## Execution
agent

## Dependencies
- 006 (test file written)

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/platform-deepeval/tests/test_eval_kernel_minimal.py` exists
- [ ] `D:/my_ai_projects/project_test_repos/platform-deepeval/tests/conftest.py` exists
- [ ] OPENAI_API_KEY environment variable is set

## Requirements
- Run: `python -m pytest D:/my_ai_projects/project_test_repos/platform-deepeval/tests/test_eval_kernel_minimal.py --harness-root=D:/my_ai_projects/isagawa-kernel --rootdir=D:/my_ai_projects/project_test_repos/platform-deepeval -v`
- Must show 17 passed
- Segfault on teardown (exit code 139) is acceptable if all 17 tests show PASSED

## Acceptance Criteria
- [ ] pytest output shows `17 passed`
- [ ] No test failures (FAILED count = 0)

## Gates Satisfied
- FUNC-03, TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
