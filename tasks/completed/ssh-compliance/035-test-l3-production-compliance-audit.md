# L3 Production Test — Compliance Audit Against Live Target

## Context
L3 production test running the compliance auditor against a real Docker+SSH Rocky Linux target. Validates end-to-end compliance audit flow.

## Type
TEST

## Execution
agent

## Dependencies
- 034

## Phase Gate
- [ ] 034 completed (L2 pytest suite passes)

## Requirements
- Spin up Docker+SSH Rocky Linux target (use prod-test infra)
- Run ComplianceAuditor against the live target
- Verify results have passed/failed counts
- Verify results contain compliance refs metadata (stig/cis/nist/fips fields)
- Clean up Docker target after test

## Acceptance Criteria
- [ ] Compliance audit completes with structured results containing check/passed/evidence/refs fields

## Gates Satisfied
TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
