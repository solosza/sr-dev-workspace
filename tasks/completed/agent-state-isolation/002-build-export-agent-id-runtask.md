# Export KERNEL_AGENT_ID in run-task.sh

## Type
BUILD
## Execution
inline
## Dependencies
- 001

## Requirements
- READ run-task.sh fully first; find where claude -p is invoked and where TASK_SUBFOLDER/agent_id is derived
- Export KERNEL_AGENT_ID={worker-id} (the subfolder) into the claude -p subprocess environment
- No other behavior change

## Acceptance Criteria
- [ ] Export present in the claude -p invocation path
- [ ] Existing arg handling unchanged

## Gates Satisfied
- SI-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
