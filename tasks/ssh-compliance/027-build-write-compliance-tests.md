# Write Compliance Test Suite

## Context
Write actual compliance test suite at tests/test_compliance.py (NOT in _reference/). This validates all compliance validators, batch execution, and result format.

## Type
BUILD

## Execution
inline

## Dependencies
- 026

## Phase Gate
- [ ] 026 completed (conftest fixtures exist)

## Requirements
- Write `tests/test_compliance.py` with pytest tests
- Use `compliance_config` and `mock_ssh_interface` fixtures
- Test each validator individually (STIG, CIS, NIST, FIPS)
- Test batch execution through ComplianceTasks
- Test result format includes `refs` metadata with framework-specific fields
- Test ComplianceAuditor with client config selecting specific frameworks

## Acceptance Criteria
- [ ] `tests/test_compliance.py` exists with test functions

## Gates Satisfied
STRUCT-20, FUNC-04

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
