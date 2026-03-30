# Write STIG Rules Fixture JSON

## Context
Write STIG rules fixture JSON with rule IDs, check types, and parameters. This fixture drives automated STIG compliance scanning against Rocky Linux 9 targets via SSH.

## Type
BUILD

## Execution
inline

## Dependencies
- 009

## Phase Gate
- [ ] Task 009 research notes captured with at least 20 STIG rule IDs

## Requirements
- Write tests/data/compliance/stig-rocky9.json in target repo isagawa-qa/platform-ssh (cross-repo)
- File must contain a rules array
- Each rule must have: id, title, severity, check_type (config/package/service), and params

## Acceptance Criteria
- [ ] `grep -q '"rules"' tests/data/compliance/stig-rocky9.json` exits 0

## Gates Satisfied
STRUCT-08, BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
