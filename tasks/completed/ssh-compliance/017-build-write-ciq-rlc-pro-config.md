# Write CIQ Rocky Linux Pro Client Config

## Context
Write CIQ Rocky Linux Pro client config with host info and compliance framework selection. This config defines the target host and which compliance frameworks to scan against.

## Type
BUILD

## Execution
inline

## Dependencies
- 008

## Phase Gate
- [ ] Task 008 completed successfully

## Requirements
- Write tests/data/clients/ciq-rlc-pro.json in target repo isagawa-qa/platform-ssh (cross-repo)
- File must contain host config (connection details)
- File must contain compliance_frameworks array selecting STIG + CIS L1 + NIST 800-171

## Acceptance Criteria
- [ ] `grep -q '"compliance_frameworks"' tests/data/clients/ciq-rlc-pro.json` exits 0

## Gates Satisfied
STRUCT-12, BUILD-05

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
