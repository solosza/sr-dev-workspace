# L1: Routing Present Everywhere

## Type
TEST
## Execution
inline
## Dependencies
- 010

## Requirements
- Grep all 4 hooks for KERNEL_AGENT_ID routing + atomic helper usage; grep run-task.sh for export + seed; grep both command docs
- Script exits 0 only if every site present

## Acceptance Criteria
- [ ] L1 script exit 0

## Gates Satisfied
- SI-05, SI-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
