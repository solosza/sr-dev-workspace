# Build Prompt: Tiered + Sequential

## Context
Combine the tiered corpus with the sequential task prompt into a single prompt file.

## Type
BUILD

## Execution
inline

## Dependencies
- 004-build-assemble-tiered-corpus
- 006-build-write-sequential-task

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/corpus-tiered.md` exists
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/task-sequential.md` exists

## Requirements
- Concatenate: corpus-tiered.md + "\n\n---\n\n# YOUR TASK\n\n" + task-sequential.md
- Write to `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/prompt-tiered-sequential.md`

## Acceptance Criteria
- [ ] `prompt-tiered-sequential.md` exists at the specified path
- [ ] Contains tiered corpus content (with wikilinks) at the start
- [ ] Contains sequential task prompt at the end

## Gates Satisfied
- BUILD-10 (partial — 2 of 6 prompts)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
