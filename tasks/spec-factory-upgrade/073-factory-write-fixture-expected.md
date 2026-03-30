# Write Test Fixture Expected Files

## Context
Expected output JSON files for mock_data gates. One file per gate.

## Type
BUILD

## Dependencies
- 072

## Phase Gate
- [ ] All reference code files exist (tasks 055-069 complete)

## Requirements
- For each mock_data gate in gate-contract.md:
  - Write `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/_test/expected/GATE-ID-expected.json`

## Acceptance Criteria
- [ ] At least 1 expected fixture exists (verify: ls _test/expected/*.json)

## Gates Satisfied
FAC-20

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
