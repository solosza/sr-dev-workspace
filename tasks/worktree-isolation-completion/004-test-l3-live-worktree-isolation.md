# Task 004: L3 — Live Worktree Isolation
**Type:** TEST | **Gates:** WI-04
## Action
Run run-task.sh on a real minimal 1-task folder in an isolated worktree and assert isolation holds live.
## Spec
This is a LIVE run, not a simulation (lessons #39/#49). Before the run, record the parent sr_dev_workflow.json `anchored` value + its hash. Spawn/execute the worktree runner (KERNEL_AGENT_ID set). Assert: (a) the worktree branched from current main HEAD (merge-base == main HEAD), (b) the parent sr_dev_workflow.json `anchored` is UNCHANGED during and after the run (hash matches), (c) no stray test/state artifacts (agent-* files, test outputs) landed in the MAIN working tree. Capture the actual command + non-empty output as evidence.
## Acceptance
Live run: fresh base + parent anchored unchanged + no main-tree pollution, all verified from artifacts. Evidence captured.
