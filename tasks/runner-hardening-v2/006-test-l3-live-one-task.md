# Task 006: L3 — Live One-Task Run
**Type:** TEST | **Gates:** RH-06
## Action
Run the hardened run-task.sh end-to-end on a real minimal 1-task folder (a trivial deliverable, e.g. write one file). Assert live: (a) the task is recorded complete in the routed state, (b) the deliverable is committed on the branch, (c) `git status --porcelain` is clean at complete.
## Spec
This is a LIVE run, not a simulation (lessons #39/#49). Use a disposable task folder + throwaway routed state. Capture the actual command + non-empty output as re-runnable evidence. Verify all three asserts from artifacts/state, not the runner's self-report alone.
## Acceptance
Live 1-task run: completion-in-state + deliverable-committed + clean-tree all verified from artifacts. Evidence captured.
