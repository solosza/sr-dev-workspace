# Update conftest.py with Compliance Fixtures

## Context
Update tests/conftest.py to add compliance_config and client_config fixtures needed by the compliance test suite.

## Type
BUILD

## Execution
inline

## Dependencies
- 025

## Phase Gate
- [ ] 025 completed (compliance auditor role exists)

## Requirements
- Add `compliance_config` fixture that loads all compliance JSON from `tests/data/compliance/`
- Add `client_config` fixture that loads client JSON from `tests/data/clients/`
- Keep existing `mock_ssh_interface` fixture intact
- Fixtures should be session-scoped for performance

## Acceptance Criteria
- [ ] `grep -q 'compliance_config' tests/conftest.py` exits 0
- [ ] `grep -q 'client_config' tests/conftest.py` exits 0

## Gates Satisfied
BUILD-10, BUILD-11

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
