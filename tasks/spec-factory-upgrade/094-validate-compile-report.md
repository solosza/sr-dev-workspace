# Compile validation-report.json

## Context
Final artifact with per-gate results and aggregate.

## Type
TEST

## Dependencies
- 093

## Phase Gate
- [ ] Coverage calculated (task 093)

## Requirements
- Write `$WORKSPACE/_test/validation-report.json`
- Per-gate and aggregate fields
- Must be valid JSON

## Acceptance Criteria
- [ ] validation-report.json exists and valid (verify: file_exists + json_valid)

## Gates Satisfied
VAL-14

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
