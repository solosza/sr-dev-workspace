# Build Prompt: Tiered + Cross-Reference

## Context
Combine the tiered corpus with the cross-reference task prompt.

## Type
BUILD

## Execution
inline

## Dependencies
- 004-build-assemble-tiered-corpus
- 008-build-write-crossref-task

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/corpus-tiered.md` exists
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/task-crossref.md` exists

## Requirements
- Concatenate: corpus-tiered.md + "\n\n---\n\n# YOUR TASK\n\n" + task-crossref.md
- Write to `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/prompt-tiered-crossref.md`

## Acceptance Criteria
- [ ] `prompt-tiered-crossref.md` exists at the specified path

## Gates Satisfied
- BUILD-10 (partial — 6 of 6 prompts)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
