# Write CIS Level 1 Fixture JSON

## Context
Write CIS Level 1 fixture JSON for Rocky Linux 9. This fixture drives automated CIS benchmark compliance scanning against targets via SSH.

## Type
BUILD

## Execution
inline

## Dependencies
- 011

## Phase Gate
- [ ] Task 011 research notes captured with at least 15 CIS benchmark IDs

## Requirements
- Write tests/data/compliance/cis-rocky9-l1.json in target repo isagawa-qa/platform-ssh (cross-repo)
- File must contain a benchmarks array

## Acceptance Criteria
- [ ] `grep -q '"benchmarks"' tests/data/compliance/cis-rocky9-l1.json` exits 0

## Gates Satisfied
STRUCT-09, BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
