# Write STIG Validator

## Context
Write STIG validator that loads rules from fixture JSON and delegates to existing validators. This is the first compliance framework validator, establishing the pattern for CIS, NIST, and FIPS.

## Type
BUILD

## Execution
inline

## Dependencies
- 019

## Phase Gate
- [ ] 019 completed (compliance fixture data exists)

## Requirements
- Write `framework/_reference/validators/stig_validator.py`
- STIGValidator class with `__init__(self, ssh, rules)` and `validate()` method
- Loads rules from fixture JSON, delegates to ConfigValidator/PackageValidator/ServiceValidator based on `check_type`
- Returns `[{check, passed, evidence, refs: {stig: rule_id, severity}}]`

## Acceptance Criteria
- [ ] `grep -q 'def validate' framework/_reference/validators/stig_validator.py` exits 0

## Gates Satisfied
STRUCT-14, BUILD-06

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
