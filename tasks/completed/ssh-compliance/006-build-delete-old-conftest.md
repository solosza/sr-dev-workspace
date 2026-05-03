# Delete Old conftest.py from _reference/tests

## Context
Remove old conftest.py from _reference/tests/ after move to tests/.

## Type
BUILD

## Execution
inline

## Dependencies
- 003-build-move-conftest

## Phase Gate
- [ ] tests/conftest.py exists (`test -f tests/conftest.py`)

## Requirements
- Delete framework/_reference/tests/conftest.py

## Acceptance Criteria
- [ ] framework/_reference/tests/conftest.py does NOT exist (`test ! -f framework/_reference/tests/conftest.py`)

## Gates Satisfied
STRUCT-05

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
