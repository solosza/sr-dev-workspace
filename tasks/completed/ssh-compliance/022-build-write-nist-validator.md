# Write NIST 800-171 Validator

## Context
Write NIST 800-171 validator following the same delegation pattern as STIG and CIS validators. Loads NIST rules from fixture JSON and delegates to existing validators.

## Type
BUILD

## Execution
inline

## Dependencies
- 019

## Phase Gate
- [ ] 019 completed (compliance fixture data exists)

## Requirements
- Write `framework/_reference/validators/nist_800_171_validator.py`
- NIST800171Validator class with `__init__(self, ssh, rules)` and `validate()` method
- Loads NIST 800-171 rules, delegates to ConfigValidator/PackageValidator/ServiceValidator based on `check_type`
- Returns `[{check, passed, evidence, refs: {nist: control_id, family}}]`

## Acceptance Criteria
- [ ] `grep -q 'def validate' framework/_reference/validators/nist_800_171_validator.py` exits 0

## Gates Satisfied
STRUCT-16, BUILD-08

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
