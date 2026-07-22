# Write Precision-Recall Task Prompt

## Context
Task type 2: Mid-document precision recall. The answer is buried in the middle of the corpus. This task type tests the "lost-in-the-middle" failure mode — when important information is neither at the beginning nor end of the context. At 60K+ tokens, the model must retrieve a specific rule from mid-document among many similar rules.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-build-create-experiment-dir

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/` exists

## Requirements
- Write a task prompt that requires finding a SPECIFIC rule buried in the middle of the corpus
- The prompt should ask a question where the answer requires combining TWO conditions from the healthcare-qa rules:
  - Example: "A member has a readmission claim with DRG 470 (MDC 08) admitted 15 days after discharge. The history claim was in PAID status. DRG 470 is NOT on the exclusion list. Which processing path applies — PEND, DENY, or BYPASS? Cite the exact rule text and step number from the specification."
- The answer should require mid-document retrieval (rules about pend vs deny vs exclusion are spread across different sections)
- Must be unambiguous — only one correct answer
- Write to `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/task-precision.md`

## Acceptance Criteria
- [ ] `task-precision.md` exists at the specified path
- [ ] Contains a scenario requiring mid-document rule retrieval
- [ ] Asks for specific rule citation (not just the decision)
- [ ] Has one unambiguous correct answer

## Gates Satisfied
- BUILD-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
