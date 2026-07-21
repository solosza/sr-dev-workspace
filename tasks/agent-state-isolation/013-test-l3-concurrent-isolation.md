# L3: Concurrent Isolation Proof

## Type
TEST
## Execution
inline
## Dependencies
- 012

## Requirements
- Snapshot parent session_state.json bytes
- Spawn TWO concurrent run-task.sh runs (tiny 1-task throwaway folders created by this test, unique subfolders) via env -u CLAUDECODE, wait for both
- Assert parent session_state.json byte-identical to snapshot; assert each agent produced its own agent-{id}-session-state.json
- Clean up throwaway folders/state; report honestly — any clobber = RED, fix -> /kernel/learn

## Acceptance Criteria
- [ ] Byte-identical parent state; per-agent files present; cleanup done

## Gates Satisfied
- SI-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
