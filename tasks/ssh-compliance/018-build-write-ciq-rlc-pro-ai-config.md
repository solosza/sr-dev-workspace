# Write CIQ Rocky Linux Pro AI/HPC Client Config

## Context
Write CIQ Rocky Linux Pro AI/HPC client config variant. This config defines an AI/HPC-specific target host with FIPS and CIS L1 compliance framework selection.

## Type
BUILD

## Execution
inline

## Dependencies
- 008

## Phase Gate
- [ ] Task 008 completed successfully

## Requirements
- Write tests/data/clients/ciq-rlc-pro-ai.json in target repo isagawa-qa/platform-ssh (cross-repo)
- File must contain AI/HPC variant host config
- File must contain compliance_frameworks array selecting FIPS + CIS L1

## Acceptance Criteria
- [ ] `grep -q '"compliance_frameworks"' tests/data/clients/ciq-rlc-pro-ai.json` exits 0

## Gates Satisfied
STRUCT-13, BUILD-12

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
