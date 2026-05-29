# Research SAM.gov LLC Requirements

## Context
Research SAM.gov registration requirements for an LLC pursuing government contracts. This directly supports backlog 092 (govcon AI app) — the LLC must be registered in SAM.gov to bid on federal contracts.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-build-create-project-dir

## Phase Gate
- [ ] `projects/ai-business-formation/` directory exists

## Requirements
- Document SAM.gov registration process for a new LLC
- Cover required information: DUNS/UEI number, NAICS codes, business type, size standards
- Address set-aside eligibility (small business, 8(a), HUBZone, SDVOSB)
- Document timeline from LLC formation to SAM.gov active registration
- Identify any blockers or prerequisites (e.g., EIN, bank account, physical address)
- Cross-reference with backlog 092 govcon requirements

## Acceptance Criteria
- [ ] `projects/ai-business-formation/04-sam-gov-requirements.md` exists
- [ ] File covers SAM.gov registration steps
- [ ] File addresses set-aside eligibility options

## Gates Satisfied
- DOC-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
