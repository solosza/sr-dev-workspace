# Verify All Structural Corrections

## Context
Verify all structural corrections are complete before proceeding to compliance work.

## Type
TEST

## Execution
agent

## Dependencies
- 001-build-move-interface
- 002-build-create-tests-dir
- 003-build-move-conftest
- 004-build-move-host-configs
- 005-build-delete-old-interface
- 006-build-delete-old-conftest
- 007-build-delete-old-fixtures-dir

## Requirements
- Verify interface in correct location
- Verify conftest in correct location
- Verify host configs in correct location
- Verify old files deleted

## Acceptance Criteria
- [ ] framework/interfaces/ssh_interface.py exists with SSHInterface class (`grep -q "class SSHInterface" framework/interfaces/ssh_interface.py`)
- [ ] tests/data/compliance/ directory exists (`test -d tests/data/compliance`)
- [ ] tests/data/clients/ directory exists (`test -d tests/data/clients`)
- [ ] tests/conftest.py exists with mock_ssh_interface fixture (`grep -q "mock_ssh_interface" tests/conftest.py`)
- [ ] tests/data/host_configs.json exists with rlc_pro key (`grep -q "rlc_pro" tests/data/host_configs.json`)
- [ ] framework/_reference/ssh_interface.py does NOT exist (`test ! -f framework/_reference/ssh_interface.py`)
- [ ] framework/_reference/tests/conftest.py does NOT exist (`test ! -f framework/_reference/tests/conftest.py`)
- [ ] framework/_reference/fixtures/ does NOT exist (`test ! -d framework/_reference/fixtures/`)

## Gates Satisfied
STRUCT-01, STRUCT-02, STRUCT-03, STRUCT-04, STRUCT-05, STRUCT-06, STRUCT-07

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
