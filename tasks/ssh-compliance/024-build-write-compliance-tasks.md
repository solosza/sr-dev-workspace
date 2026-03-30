# Write Compliance Tasks

## Context
Write L3 compliance tasks that chain validator calls into domain operations. This composes the individual compliance validators into higher-level framework-specific audits.

## Type
BUILD

## Execution
inline

## Dependencies
- 020
- 021
- 022
- 023

## Phase Gate
- [ ] 020 completed (STIG validator exists)
- [ ] 021 completed (CIS validator exists)
- [ ] 022 completed (NIST validator exists)
- [ ] 023 completed (FIPS validator exists)

## Requirements
- Write `framework/_reference/tasks/compliance_tasks.py`
- ComplianceTasks class that composes compliance validators
- Runs framework-specific audits by delegating to the appropriate validator(s)
- Aggregates results across validators

## Acceptance Criteria
- [ ] `grep -q 'class ComplianceTasks' framework/_reference/tasks/compliance_tasks.py` exits 0

## Gates Satisfied
STRUCT-18, BUILD-13

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
