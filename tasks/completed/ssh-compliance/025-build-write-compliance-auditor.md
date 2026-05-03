# Write Compliance Auditor Role

## Context
Write L4 compliance auditor role that orchestrates compliance tasks. This is the top-level entry point that loads client config, selects frameworks, runs tasks, and aggregates results.

## Type
BUILD

## Execution
inline

## Dependencies
- 024

## Phase Gate
- [ ] 024 completed (compliance tasks exist)

## Requirements
- Write `framework/_reference/roles/compliance_auditor.py`
- ComplianceAuditor class that loads client config, selects compliance frameworks, runs tasks, aggregates results
- Client config specifies which frameworks apply (e.g., STIG + FIPS for DoD, CIS for commercial)
- Produces unified compliance report with per-framework results

## Acceptance Criteria
- [ ] `grep -q 'class ComplianceAuditor' framework/_reference/roles/compliance_auditor.py` exits 0

## Gates Satisfied
STRUCT-19, BUILD-14

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
