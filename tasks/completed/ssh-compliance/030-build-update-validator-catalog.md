# Update Validator Catalog

## Context
Add compliance validators to the existing validator catalog so they are discoverable and documented alongside the base validators.

## Type
BUILD

## Execution
inline

## Dependencies
- 029

## Phase Gate
- [ ] 029 completed (compliance imports verified)

## Requirements
- Update `references/validator-catalog.md` with entries for STIGValidator, CISValidator, NIST800171Validator, FIPSValidator
- Each entry should document the class, constructor signature, return format, and compliance framework reference

## Acceptance Criteria
- [ ] `grep -q 'STIGValidator' references/validator-catalog.md` exits 0

## Gates Satisfied
DOC-01

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
