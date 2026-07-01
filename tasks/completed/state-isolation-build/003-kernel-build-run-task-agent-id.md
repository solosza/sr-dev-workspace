# Pass agent_id in run-task.sh pre_init_state

## Context
run-task.sh spawns one-shot agents via `claude -p`. These agents need an identity so hooks can route their state to per-agent files. Pass `agent_id` derived from the task subfolder name.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Phase Gate
- [ ] `run-task.sh` exists and has been read

## Requirements
- Read `run-task.sh`
- Find the `pre_init_state` call (line ~289): `pre_init_state "session_started=True,one_shot=True"`
- Change to: `pre_init_state "session_started=True,one_shot=True,agent_id=${TASK_SUBFOLDER:-default}"`
- The agent_id uses the task subfolder name (e.g., "state-isolation-build", "resume-loops-agent-systems")
- If no subfolder, use "default" as agent_id
- Also support AGENT_ID environment variable override: `agent_id=${AGENT_ID:-${TASK_SUBFOLDER:-default}}`

## Acceptance Criteria
- [ ] pre_init_state line includes agent_id
- [ ] agent_id defaults to TASK_SUBFOLDER name
- [ ] AGENT_ID env var overrides if set
- [ ] No other changes to run-task.sh

## Gates Satisfied
- BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
