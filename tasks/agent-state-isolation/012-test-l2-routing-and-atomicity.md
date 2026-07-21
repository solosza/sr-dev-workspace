# L2: Routing + Atomicity Behavior

## Type
TEST
## Execution
inline
## Dependencies
- 011

## Requirements
- Invoke one hook as a subprocess with KERNEL_AGENT_ID=zztest and a synthetic tool-call payload: assert it reads/writes agent-zztest-session-state.json and NOT session_state.json
- Invoke without the env var: assert unchanged behavior
- Call the atomic helper with a near-empty dict: assert rejection; with valid payload: assert os.replace result is complete valid JSON
- Clean up zztest artifacts

## Acceptance Criteria
- [ ] All L2 assertions pass; artifacts cleaned

## Gates Satisfied
- SI-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
