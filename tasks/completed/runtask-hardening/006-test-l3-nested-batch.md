# Task 006: L3 - Nested Mini-Batch (GATE)

**Type:** TEST (L3) - GATE TASK: skip never waives (lesson #39).
**Gates:** RH-06

## Action
ONE script: assemble a scratch kernel repo in the system temp dir (copy: patched run-task.sh, lib/, minimal .claude/state seed, CLAUDE.md stub, tasks/rh-live/ with ONE trivial haiku-keyword task: 'copy the file a.txt to b.txt in this repo, then output ONE_SHOT_COMPLETE'). Run env -u CLAUDECODE bash run-task.sh <scratch> 3 rh-live. Assert from the runner output: [MODEL] Selected line contains the task filename AND 'haiku'; heartbeat json existed during the run; the task completed (b.txt exists, ALL_TASKS_COMPLETE or task_done signal).

## Acceptance
Live proof of non-default routing + heartbeat; exit 0. Red: fix then /kernel/learn.
