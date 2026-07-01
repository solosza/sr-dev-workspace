# Update Anchor to Clean Per-Agent State Files

## Context
Per-agent state files (`agent-*-state.json`, `agent-*-actions.jsonl`) accumulate across pipeline runs. The anchor ceremony needs to archive and clean these alongside the main actions.jsonl.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-kernel-build-actions-log-routing

## Phase Gate
- [ ] `.claude/commands/kernel/anchor.md` exists and has been read

## Requirements
- Read `.claude/commands/kernel/anchor.md`
- In Part C, Step 11 (Archive and reset actions log), add:
  - After archiving `actions.jsonl`, also archive any `agent-*-actions.jsonl` files
  - Include per-agent logs in the archive JSON under an `agent_logs` key
  - Truncate all `agent-*-actions.jsonl` files to empty
  - Optionally clear `agent-*-state.json` files (these are per-pipeline, not per-anchor)
- Keep the existing archive format compatible (add fields, don't change existing ones)

## Acceptance Criteria
- [ ] Anchor Part C Step 11 mentions per-agent log files
- [ ] Archive includes agent-specific logs
- [ ] Per-agent log files truncated after archive
- [ ] Existing archive format preserved (additive changes only)

## Gates Satisfied
- BUILD-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
