# Write Test Fixture Input Files

## Context
Input JSON files for mock_data gates. One file per gate. Realistic CIQ data from audit.

## Type
BUILD

## Dependencies
- 071

## Phase Gate
- [ ] All reference code files exist (tasks 055-069 complete)

## Requirements
- For each mock_data gate in gate-contract.md:
  - Write `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/_test/fixtures/GATE-ID-input.json`
- Use realistic CIQ data from audit (task 045)

## Acceptance Criteria
- [ ] At least 1 input fixture exists (verify: ls _test/fixtures/*.json)

## Gates Satisfied
FAC-20

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
