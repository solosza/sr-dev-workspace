# Create Tests Directory Structure

## Context
Create top-level tests/ and tests/data/ directories to match sibling conventions.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- Create tests/, tests/data/, tests/data/compliance/, tests/data/clients/ directories in platform-ssh

## Acceptance Criteria
- [ ] tests/data/compliance/ directory exists (`test -d tests/data/compliance`)
- [ ] tests/data/clients/ directory exists (`test -d tests/data/clients`)

## Gates Satisfied
STRUCT-03

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
