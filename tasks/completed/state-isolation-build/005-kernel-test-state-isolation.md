# Test State Isolation

## Context
Verify that per-agent state isolation works correctly: agent logs route to per-agent files, parent state is protected, backward compatibility maintained.

## Type
TEST

## Execution
agent

## Dependencies
- 001-kernel-build-actions-log-routing
- 002-kernel-build-agent-state-write-guard
- 003-kernel-build-run-task-agent-id
- 004-kernel-build-anchor-per-agent-cleanup

## Phase Gate
- [ ] All BUILD tasks (001-004) complete

## Requirements
- Test 1 (agent_id routing): Create a mock session_state.json with `agent_id: "test-agent"`. Run a simulated PostToolUse hook input through actions-log-appender.py. Verify output goes to `agent-test-agent-actions.jsonl`, NOT `actions.jsonl`.
- Test 2 (backward compat): Create a mock session_state.json WITHOUT agent_id. Run same simulated input. Verify output goes to `actions.jsonl` as before.
- Test 3 (session_state guard): With agent_id set, verify actions-log-appender does NOT update session_state.json actions_log array.
- Test 4 (run-task.sh pre_init_state): Grep run-task.sh for agent_id in pre_init_state. Verify it uses TASK_SUBFOLDER.
- Test 5 (anchor cleanup): Grep anchor.md for agent-*-actions.jsonl reference.
- Report pass/fail for each test.

## Acceptance Criteria
- [ ] Test 1: Agent log routing works
- [ ] Test 2: Backward compatibility maintained
- [ ] Test 3: Parent state protected
- [ ] Test 4: run-task.sh passes agent_id
- [ ] Test 5: Anchor handles per-agent cleanup

## Gates Satisfied
- TEST-01, TEST-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
