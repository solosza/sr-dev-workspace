# Task 003: Liveness + Stranded-Deliverable Detection
**Type:** BUILD | **Gates:** OBS-03
## Action
Add detection for (a) silent death/stall via the heartbeat, and (b) completed-but-unmerged worktree deliverables.
## Spec
(a) LIVENESS: read the 262 HEARTBEAT_FILE; if older than a threshold while tasks remain, classify the run as stalled/dead and produce a VISIBLE signal (not just a file) — the factory-died-at-step-6 class. (b) STRANDED-DELIVERABLE: detect a worktree/branch whose routed state shows complete=true and has a committed deliverable, but the branch was never merged/ported to main (the 275 owner-facing plan + 269 research both sat un-ported this session). Scan agent worktrees + branches, cross-check merge state, list the stranded ones. Both are read-only detectors.
## Acceptance
Stall/death detected with a visible signal; completed-but-unmerged worktree deliverables enumerated.
