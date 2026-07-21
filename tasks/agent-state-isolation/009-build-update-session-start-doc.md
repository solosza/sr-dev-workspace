# Update session-start.md Routing Docs

## Type
BUILD
## Execution
inline
## Dependencies
- 005

## Requirements
- Extend the Workflow State Routing section in .claude/commands/kernel/session-start.md: session state routes per KERNEL_AGENT_ID exactly like workflow state
- Document that one-shot agents must NEVER write the parent session_state.json

## Acceptance Criteria
- [ ] Routing section covers session state

## Gates Satisfied
- SI-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
