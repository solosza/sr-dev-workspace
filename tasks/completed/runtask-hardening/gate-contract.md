# Gate Contract - 262 run-task.sh Hardening

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| RH-01 | Task resolution: NEXT incomplete task computed from tasks/{subfolder}/ listing minus completed_tasks (routed agent workflow file, utf-8-sig tolerant); CURRENT_TASK and TASK_FILE_PATH set from it; [MODEL] line shows the real filename | bash -n + grep + run_test | 001 | resolution independent of state current_task |
| RH-02 | Empty-output retry: 0-byte-at-timeout iteration retried once WITHOUT consuming the iteration counter; second consecutive empty consumes normally; distinct log line ([EMPTY-RETRY]) | grep + run_test | 002 | bounded retry visible |
| RH-03 | Heartbeat: .claude/state/{subfolder}_runner-heartbeat.json written each loop pass (pid, iteration, ISO ts), UTF-8 no BOM | run_test | 003 | file updates per iteration |
| RH-04 | L1: bash -n clean; no regressions to lock handling, KERNEL_AGENT_ID export, worktree detection, move_to_done | run_test | 004 | greps confirm all preserved |
| RH-05 | L2: with a fixture folder (one haiku-keyword task 001-copy-simple-file.md, one sonnet-keyword task) + seeded workflow state, the resolution function returns the right file and route_model returns haiku/sonnet ids per config | run_test | 005 | non-default routing proven offline |
| RH-06 | L3 GATE: nested mini-batch in a scratch kernel repo (copy minimal kernel bits + patched run-task.sh): run 1 haiku-keyword dummy task via env -u CLAUDECODE; assert [MODEL] Selected line shows the task FILENAME and claude-haiku model id; heartbeat file updated; task completes | run_test | 006 | live proof |

## Rules
- READ run-task.sh + lib/model-router.sh + lib/common.sh FULLY before editing (RULE ZERO)
- The resolution must use the SAME routed workflow file the pre-check uses (agent-{id}-workflow.json when scoped)
- Preserve retry_upgrade_order behavior on failures
- Any red: fix then /kernel/learn
