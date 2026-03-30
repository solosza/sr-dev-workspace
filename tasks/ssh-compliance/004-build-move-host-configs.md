# Move Host Configs to Tests Data

## Context
Move host_configs.json from framework/_reference/fixtures/ to tests/data/ to match convention.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-build-create-tests-dir

## Phase Gate
- [ ] tests/data/ directory exists (`test -d tests/data/`)

## Requirements
- Copy framework/_reference/fixtures/host_configs.json to tests/data/host_configs.json

## Acceptance Criteria
- [ ] tests/data/host_configs.json exists with rlc_pro key (`grep -q "rlc_pro" tests/data/host_configs.json`)

## Gates Satisfied
STRUCT-06

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
