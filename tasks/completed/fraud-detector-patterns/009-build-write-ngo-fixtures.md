# 009 — Write Test Fixtures for NGO Grant Patterns (023-025)

## Type
BUILD

## Action
Create test fixture file `D:\my_ai_projects\fraud-detection-app\tests\fixtures\ngo_grant_fixtures.json` with mock input data for patterns 023-025.

## Fixture Format
Each fixture should be a JSON object with:
- `pattern_id`: which pattern this tests
- `input`: mock data dict matching what `check_pattern_NNN` expects
- `expected_match`: true/false
- `description`: what this fixture tests

## Fixtures to Write

For each of PATTERN-023, 024, 025:
- 1 fixture that SHOULD trigger a match (all indicators present)
- 1 fixture that should NOT trigger (missing key indicators)

Total: 6 fixtures (2 per pattern).

## Constraints
- Use realistic but fake data (no real PII, EINs, or org names)
- Dollar amounts should be realistic for the sector
- Field names must match what the check functions expect

## Target File
`D:\my_ai_projects\fraud-detection-app\tests\fixtures\ngo_grant_fixtures.json`

## Acceptance
- [ ] File exists and is valid JSON
- [ ] 6 fixtures (2 per pattern)
- [ ] Each fixture has pattern_id, input, expected_match, description

## Dependencies
005
