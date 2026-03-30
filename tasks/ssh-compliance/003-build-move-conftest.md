# Move conftest.py to Tests Root

## Context
Move conftest.py from framework/_reference/tests/ to tests/ to match convention.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-build-create-tests-dir

## Phase Gate
- [ ] tests/ directory exists (`test -d tests/`)

## Requirements
- Copy framework/_reference/tests/conftest.py to tests/conftest.py
- Update import paths for new location

## Acceptance Criteria
- [ ] tests/conftest.py exists with mock_ssh_interface fixture (`grep -q "mock_ssh_interface" tests/conftest.py`)

## Gates Satisfied
STRUCT-04

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
