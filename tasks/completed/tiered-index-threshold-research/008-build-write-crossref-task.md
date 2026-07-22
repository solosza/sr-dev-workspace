# Write Cross-Reference Task Prompt

## Context
Task type 3: Cross-reference retrieval. The answer requires linking information from TWO distant sections of the corpus — a rule defined early in one skill and a constraint defined later in a different skill. This tests the model's ability to hold and connect widely separated context.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-build-create-experiment-dir

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/` exists

## Requirements
- Write a task prompt requiring cross-reference between two different skills
- The answer must combine information from:
  1. A rule or constraint from check-data-engine (e.g., the date registry mechanism, Step 3)
  2. A validation rule from verify-sit-xlsx or create-sit-xlsx (e.g., field format requirements)
- Example: "You are setting up TC-003 for a readmission claim. You have already assigned dates for TC-001 and TC-002 in the date registry. Now you need to create a SIT spreadsheet entry for TC-003. Using the check-data-engine date registry rules AND the create-sit-xlsx field format requirements, explain: (a) how to pick non-conflicting dates, (b) what format each date field must use in the SIT spreadsheet, and (c) which columns map to which claim fields."
- The answer requires synthesizing rules from distant parts of the corpus
- Write to `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/task-crossref.md`

## Acceptance Criteria
- [ ] `task-crossref.md` exists at the specified path
- [ ] References at least 2 different skills' content
- [ ] Requires synthesizing rules from distant corpus sections
- [ ] Has verifiable correct answer components

## Gates Satisfied
- BUILD-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
