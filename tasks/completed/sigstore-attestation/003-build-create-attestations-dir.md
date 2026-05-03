# Create attestations directory

## Context
Create the directory where attestation bundles will be stored locally.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- Create `.claude/state/attestations/` directory
- Create `lib/attestation/` directory (for Python modules)
- Create `lib/attestation/__init__.py` (empty, makes it a package)

## Acceptance Criteria
- [ ] `.claude/state/attestations/` directory exists
- [ ] `lib/attestation/` directory exists
- [ ] `lib/attestation/__init__.py` exists

## Gates Satisfied
BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
