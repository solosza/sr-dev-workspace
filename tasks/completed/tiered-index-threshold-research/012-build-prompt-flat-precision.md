# Build Prompt: Flat + Precision

## Context
Combine the flat corpus with the precision-recall task prompt.

## Type
BUILD

## Execution
inline

## Dependencies
- 003-build-assemble-flat-corpus
- 007-build-write-precision-task

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/corpus-flat.md` exists
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/task-precision.md` exists

## Requirements
- Concatenate: corpus-flat.md + "\n\n---\n\n# YOUR TASK\n\n" + task-precision.md
- Write to `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/prompt-flat-precision.md`

## Acceptance Criteria
- [ ] `prompt-flat-precision.md` exists at the specified path

## Gates Satisfied
- BUILD-10 (partial — 3 of 6 prompts)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
