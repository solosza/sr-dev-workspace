# Delete Old Fixtures Directory from _reference

## Context
Remove old fixtures/ directory from _reference/ after move to tests/data/.

## Type
BUILD

## Execution
inline

## Dependencies
- 004-build-move-host-configs

## Phase Gate
- [ ] tests/data/host_configs.json exists (`test -f tests/data/host_configs.json`)

## Requirements
- Delete framework/_reference/fixtures/ directory

## Acceptance Criteria
- [ ] framework/_reference/fixtures/ does NOT exist (`test ! -d framework/_reference/fixtures/`)

## Gates Satisfied
STRUCT-07

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
