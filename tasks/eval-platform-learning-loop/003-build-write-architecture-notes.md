# Write architecture_notes.py

## Context
Per-harness architecture notes that are passed via LLMTestCase.context to GEval judges. Notes explain valid design patterns (tiered indexing, implicit WORK state) so the judge can make informed evaluations without polluting universal criteria.

## Type
BUILD

## Execution
inline

## Dependencies
- 001 (metrics dir exists)

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/` directory exists

## Requirements
- Copy from `D:/my_ai_projects/project_test_repos/eval-kernel-minimal-test/framework/metrics/architecture_notes.py`
- Write to `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/architecture_notes.py`
- Preserve `ARCHITECTURE_NOTES` dict and `get_notes()` function
- Do NOT modify the content — this is a direct copy

## Acceptance Criteria
- [ ] `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/architecture_notes.py` exists
- [ ] File contains `def get_notes` function
- [ ] File contains `ARCHITECTURE_NOTES` dict

## Gates Satisfied
- BUILD-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
