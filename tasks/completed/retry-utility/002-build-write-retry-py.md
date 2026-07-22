# Write retry.py

## Context
Backlog 200 (V-BASE): the canonical implementation is fully specified in the design doc — this is transcription, not invention.

## Type
BUILD

## Execution
inline

## Dependencies
- 001

## Phase Gate
- [ ] Current branch is build/200-qa-build-retry-utility (RTY-01)

## Requirements
- READ the design doc first: `D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/hmsa-qa-platform/02-reference-patterns/retry-utility.md`
- Write `D:/my_ai_projects/project_test_repos/hmsa-qa-platform/framework/resources/utilities/retry.py` implementing `retry_operation` EXACTLY as the doc's Canonical Implementation section
- Module docstring must state the two-retries boundary (transient retry here; subject-selection retry is Task-loop logic, never this utility)

## Acceptance Criteria
- [ ] File exists with `def retry_operation` (RTY-02, RTY-03)
- [ ] Docstring covers the two-retries boundary

## Gates Satisfied
- RTY-02, RTY-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
