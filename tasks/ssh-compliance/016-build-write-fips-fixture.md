# Write FIPS 140-3 Fixture JSON

## Context
Write FIPS 140-3 fixture JSON. This fixture drives automated FIPS cryptographic compliance scanning against Linux targets via SSH.

## Type
BUILD

## Execution
inline

## Dependencies
- 015

## Phase Gate
- [ ] Task 015 research notes with at least 10 FIPS checks mapped to commands

## Requirements
- Write tests/data/compliance/fips-140-3.json in target repo isagawa-qa/platform-ssh (cross-repo)
- File must contain a checks array

## Acceptance Criteria
- [ ] `grep -q '"checks"' tests/data/compliance/fips-140-3.json` exits 0

## Gates Satisfied
STRUCT-11, BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
