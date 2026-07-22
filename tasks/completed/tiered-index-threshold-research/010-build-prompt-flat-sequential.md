# Build Prompt: Flat + Sequential

## Context
Combine the flat corpus with the sequential task prompt into a single prompt file for piping to `claude -p`.

## Type
BUILD

## Execution
inline

## Dependencies
- 003-build-assemble-flat-corpus
- 006-build-write-sequential-task

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/corpus-flat.md` exists
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/task-sequential.md` exists

## Requirements
- Concatenate: corpus-flat.md + "\n\n---\n\n# YOUR TASK\n\n" + task-sequential.md
- Write to `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/prompt-flat-sequential.md`

## Acceptance Criteria
- [ ] `prompt-flat-sequential.md` exists at the specified path
- [ ] Contains flat corpus content at the start
- [ ] Contains "YOUR TASK" separator
- [ ] Contains sequential task prompt at the end

## Gates Satisfied
- BUILD-10 (partial — 1 of 6 prompts)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
