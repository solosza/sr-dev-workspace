# Write step-05-contract.json

## Context
Layer 5 contract for Step 5 (Generate Tests). Validates that the test suite was generated correctly — conftest.py exists, fixtures load, metrics selected, at least one test case exists.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/skills/eval/contracts/step-05-contract.json`
- Must be valid JSON
- Must contain:
  - `step`: "05-generate-tests"
  - `success_criteria`: ["conftest.py exists in test repo", "At least one test file exists", "Fixtures load without import error", "At least one metric selected with threshold"]
  - `expected_artifacts`: ["conftest.py", "test_*.py file(s)", "metric instances", "golden dataset fixtures (when contracts exist)"]
  - `soft_validation_rules`: rules for test quality (e.g., "Tests are parametrized", "Thresholds match contract severity", "Metrics match pipeline type")
  - `verification_commands`: bash commands to verify conftest.py existence and fixture loading
- Must parse as valid JSON

## Acceptance Criteria
- [ ] File exists at `.claude/skills/eval/contracts/step-05-contract.json`
- [ ] `python -c "import json; json.load(open('.claude/skills/eval/contracts/step-05-contract.json'))"` exits 0
- [ ] `grep -q "conftest" .claude/skills/eval/contracts/step-05-contract.json` passes

## Gates Satisfied
BUILD-21, FUNC-01 (partial)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
