# Verify Research Deliverables

## Context
Final verification that all deliverables exist and meet gate contract requirements.

## Type
TEST

## Execution
inline

## Dependencies
- 007

## Phase Gate
- [ ] Research report written (task 007)

## Requirements
- Verify `projects/kernel-architecture/` directory exists
- Verify `projects/kernel-architecture/skill-as-app-research.md` exists
- Verify document contains all required sections (grep for each heading)
- Verify both test subjects are analyzed (grep for website-cloner and fraud)
- Verify trade-offs are documented
- Report pass/fail for each gate in gate-contract.md

## Acceptance Criteria
- [ ] All 7 gates in gate-contract.md pass
- [ ] Research document is complete and self-contained

## Gates Satisfied
BUILD-01 through BUILD-07 (verification)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
