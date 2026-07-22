# Task 003: Runner Heartbeat

**Type:** BUILD | **Gates:** RH-03

## Action
ONE edit to run-task.sh: at the top of each loop pass, write .claude/state/${TASK_SUBFOLDER:-default}_runner-heartbeat.json with {pid: $$, iteration: N, ts: ISO-8601} via python json.dump (UTF-8 no BOM, lesson #49). Remove it in cleanup_lock.

## Acceptance
bash -n clean; heartbeat written per pass and removed on exit.
