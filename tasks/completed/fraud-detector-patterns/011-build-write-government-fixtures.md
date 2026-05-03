# 011 — Write Test Fixtures for Government Finance Patterns (029-031)

## Type
BUILD

## Action
Create test fixture file `D:\my_ai_projects\fraud-detection-app\tests\fixtures\government_finance_fixtures.json` with mock input data for patterns 029-031.

## Fixtures to Write

For each of PATTERN-029, 030, 031:
- 1 fixture that SHOULD trigger a match (all indicators present)
- 1 fixture that should NOT trigger (missing key indicators)

Total: 6 fixtures (2 per pattern).

## Constraints
- Use realistic but fake data (no real PII)
- Field names must match what the check functions expect

## Target File
`D:\my_ai_projects\fraud-detection-app\tests\fixtures\government_finance_fixtures.json`

## Acceptance
- [ ] File exists and is valid JSON
- [ ] 6 fixtures (2 per pattern)
- [ ] Each fixture has pattern_id, input, expected_match, description

## Dependencies
007
