# Write FIPS 140-3 Validator

## Context
Write FIPS 140-3 validator following the same delegation pattern as the other compliance validators. Loads FIPS rules from fixture JSON and delegates to existing validators.

## Type
BUILD

## Execution
inline

## Dependencies
- 019

## Phase Gate
- [ ] 019 completed (compliance fixture data exists)

## Requirements
- Write `framework/_reference/validators/fips_validator.py`
- FIPSValidator class with `__init__(self, ssh, rules)` and `validate()` method
- Loads FIPS 140-3 rules, delegates to ConfigValidator/PackageValidator/ServiceValidator based on `check_type`
- Returns `[{check, passed, evidence, refs: {fips: requirement_id, module}}]`

## Acceptance Criteria
- [ ] `grep -q 'def validate' framework/_reference/validators/fips_validator.py` exits 0

## Gates Satisfied
STRUCT-17, BUILD-09

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
