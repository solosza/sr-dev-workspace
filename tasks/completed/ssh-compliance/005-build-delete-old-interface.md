# Delete Old SSH Interface from _reference

## Context
Remove old ssh_interface.py from _reference/ after move to interfaces/.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-build-move-interface

## Phase Gate
- [ ] framework/interfaces/ssh_interface.py exists (`test -f framework/interfaces/ssh_interface.py`)

## Requirements
- Delete framework/_reference/ssh_interface.py

## Acceptance Criteria
- [ ] framework/_reference/ssh_interface.py does NOT exist (`test ! -f framework/_reference/ssh_interface.py`)

## Gates Satisfied
STRUCT-02

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
