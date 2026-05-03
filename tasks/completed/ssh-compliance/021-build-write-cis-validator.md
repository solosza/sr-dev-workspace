# Write CIS Validator

## Context
Write CIS benchmark validator following the same delegation pattern as STIG validator. Loads CIS rules from fixture JSON and delegates to existing validators.

## Type
BUILD

## Execution
inline

## Dependencies
- 019

## Phase Gate
- [ ] 019 completed (compliance fixture data exists)

## Requirements
- Write `framework/_reference/validators/cis_validator.py`
- CISValidator class with `__init__(self, ssh, rules)` and `validate()` method
- Loads CIS benchmark rules, delegates to ConfigValidator/PackageValidator/ServiceValidator based on `check_type`
- Returns `[{check, passed, evidence, refs: {cis: benchmark_id, level}}]`

## Acceptance Criteria
- [ ] `grep -q 'def validate' framework/_reference/validators/cis_validator.py` exits 0

## Gates Satisfied
STRUCT-15, BUILD-07

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
