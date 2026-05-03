# Gap 5: Add Gate Contract Verification to /kernel/complete

## Status
NEW

## Location
`.claude/commands/kernel/complete.md`

## Problem
When tasks run via run-task.sh → `claude -p`, each one-shot agent does session-start → anchor → pick task → implement → complete. But `/kernel/complete` doesn't mechanically verify the gate contract. It trusts the agent's self-report. The gate contract is written but never enforced by the execution path.

This means a task can be marked "complete" without actually passing its gates. The agent says "I did it" and complete believes it.

## Fix
Add a gate verification step to `/kernel/complete`:

1. When completing a task, read `gate-contract.md` from the task folder
2. Find all gates that map to the current task (by task number or BUILD/TEST prefix)
3. For each gate, run the verification method:
   - `file_exists` → check file exists
   - `grep` → run grep command
   - `run_code` → execute command, check exit 0
   - `run_test` → execute test, check exit 0
4. If any gate fails:
   - Report which gate failed and why
   - Do NOT mark task complete
   - Set `needs_learn: true` (same as test failure)
5. If all gates pass (or no gates map to this task):
   - Proceed with normal complete flow

This makes gate contracts enforceable, not advisory.

### Scope consideration
Not every task has gates in the contract. Simple tasks (create directory, write config) may not have explicit gates. The verification only runs for tasks that have matching gate IDs. Tasks with no matching gates complete normally.

## Dependencies
- Gate contract format (already defined in step-06-atomize.md)
- `/kernel/complete` command (already exists)
