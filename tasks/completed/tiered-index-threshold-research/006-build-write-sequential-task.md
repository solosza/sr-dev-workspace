# Write Sequential Walkthrough Task Prompt

## Context
Task type 1: Sequential walkthrough. Same pattern as the prior N=3 test — walk through all steps of the check-data-engine workflow for a test case. This is the baseline task type where we expect NO difference between flat and tiered (confirmed at 12K tokens).

## Type
BUILD

## Execution
inline

## Dependencies
- 002-build-create-experiment-dir

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/` exists

## Requirements
- Write a task prompt that exercises the check-data-engine agent's TC-001 walkthrough
- Same pattern as existing `task-prompt.md` in eval-ab-check-data-engine root — walk Steps 0-6
- Test case: Same-MDC Readmission within 30 days, Expected PEND
- Given data: History CLM-H-9001, Member M12345, DRG 470, MDC 08, Enddate 2025-11-15
- Readmission CLM-R-5501, Microfilm X837BT2025110501, same member/DRG/MDC
- Instructions: "Execute steps 0-6 from the skill specification. Show full work for each step."
- Write to `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/task-sequential.md`

## Acceptance Criteria
- [ ] `task-sequential.md` exists at the specified path
- [ ] Contains TC-001 scenario data (CLM-H-9001, M12345, DRG 470)
- [ ] References Steps 0-6

## Gates Satisfied
- BUILD-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
