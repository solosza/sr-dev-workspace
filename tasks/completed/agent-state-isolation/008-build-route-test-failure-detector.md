# Route Session State in test-failure-detector.py

## Type
BUILD
## Execution
inline
## Dependencies
- 004

## Requirements
- READ .claude/hooks/test-failure-detector.py fully first
- Where it resolves session_state.json: if env KERNEL_AGENT_ID is set, use agent-{id}-session-state.json (same dir); else unchanged
- All writes to state files in this hook go through the atomic helper from task 004

## Acceptance Criteria
- [ ] Routing added at every session-state resolution point in this hook
- [ ] Writes use atomic helper
- [ ] No behavior change when env var unset

## Gates Satisfied
- SI-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
