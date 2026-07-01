# Write Golden Dataset Fixtures

## Context
JSON fixture file with 10+ test cases for the ReadComplianceMetric. Each test case specifies required_reads, actual_reads, and the expected compliance score. Covers: perfect compliance, partial reads, missing reads, extra reads, empty reads, single-file reads.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-build-create-feature-branch

## Phase Gate
- [ ] `tests/fixtures/read-compliance/` directory exists

## Requirements
- File: `D:/my_ai_projects/project_test_repos/test-platform-deepeval/tests/fixtures/read-compliance/golden-dataset.json`
- JSON array of test case objects, each with:
  - `test_id`: string (e.g., "perfect-compliance-001")
  - `description`: string (what the test validates)
  - `required_reads`: list of file paths
  - `actual_reads`: list of file paths
  - `expected_compliance_score`: float (0.0-1.0)
  - `expected_coverage_score`: float (0.0-1.0)
  - `expected_pass`: boolean
- Minimum 12 test cases covering:
  - Perfect compliance (all required read, no extras) — 2 cases
  - Partial compliance (some required read) — 2 cases
  - Zero compliance (none required read) — 1 case
  - Extra reads (all required plus irrelevant) — 2 cases
  - Empty required (nothing required, should pass) — 1 case
  - Empty actual (required files but nothing read) — 1 case
  - Single file (one required, one read) — 1 case
  - Large set (10+ required files) — 1 case
  - Overlapping paths (partial overlap between required and actual) — 1 case

## Acceptance Criteria
- [ ] File exists at `tests/fixtures/read-compliance/golden-dataset.json`
- [ ] File is valid JSON (python -c "import json; json.load(open('tests/fixtures/read-compliance/golden-dataset.json'))")
- [ ] Contains 12+ test cases

## Gates Satisfied
- BUILD-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
