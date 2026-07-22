# Task 007: L3 - Live Dependent Swarm (GATE)
**Type:** TEST (L3) - GATE TASK: skip never waives (lesson #39).
**Gates:** DW-07
## Action
ONE script: assemble 3 trivial throwaway backlogs/task-folders in a scratch area (2 independent research-style one-task jobs + 1 that depends_on both). Run them through the wave engine. Assert (via manifest/timestamps) the dependent agent SPAWNS ONLY AFTER both independents complete. Then run a cyclic set and assert it is rejected pre-spawn. Clean up scratch artifacts.
## Acceptance
Dependent ordering proven live + cycle rejected live, exit 0. Red: fix then /kernel/learn.
