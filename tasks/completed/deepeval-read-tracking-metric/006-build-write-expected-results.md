# Write Expected Results Fixture

## Context
Expected results JSON for the golden dataset. Maps each test_id to its expected metric output (score, pass/fail, missed reads, extra reads). Used by pytest to validate the metric against known outcomes.

## Type
BUILD

## Execution
inline

## Dependencies
- 005-build-write-golden-dataset

## Phase Gate
- [ ] `tests/fixtures/read-compliance/golden-dataset.json` exists

## Requirements
- File: `D:/my_ai_projects/project_test_repos/test-platform-deepeval/tests/fixtures/read-compliance/expected-results.json`
- JSON object keyed by test_id, each value containing:
  - `compliance_score`: float
  - `coverage_score`: float
  - `passed`: boolean
  - `missed_reads`: list of file paths (required but not read)
  - `extra_reads`: list of file paths (read but not required)
- Must match every test_id in golden-dataset.json

## Acceptance Criteria
- [ ] File exists at `tests/fixtures/read-compliance/expected-results.json`
- [ ] File is valid JSON
- [ ] Every test_id from golden-dataset.json has a corresponding entry

## Gates Satisfied
- BUILD-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
