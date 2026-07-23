# Gate Contract — 276 Harness Observability Layer

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| OBS-01 | Completion-truth oracle: a helper reconciles claimed completion (routed workflow.json completed_tasks) against GROUND-TRUTH (git commits touching the deliverable path + non-empty artifacts). Returns divergence (claimed-done-but-no-evidence) automatically, no human diff | grep + read code; unit sim | 001 | oracle flags claim-vs-evidence divergence |
| OBS-02 | Banner-vs-reality: a helper computes a run's TRUE outcome from authoritative signals (routed state + artifacts + iteration logs) and surfaces DISAGREEMENT between the wrapper banner and reality as a first-class alert (the 261 false-'3 failed' + empty-stdout class) | grep + read code; unit sim | 002 | banner/reality disagreement surfaced |
| OBS-03 | Liveness + STRANDED-DELIVERABLE: consumes the 262 heartbeat to detect silent death/stall (visible signal, not just a file), AND detects a completed-but-unmerged worktree deliverable (routed state complete=true + committed branch that was never merged/ported — the 275/269 failure this session) | grep + read code; unit sim | 003 | stall + stranded-deliverable both detected |
| OBS-04 | Run-status view: a single queryable command/script that reads all agent-*-workflow.json + heartbeats + branch/merge state and prints per-agent/per-pipeline status (running / stalled / complete-unmerged / dead) — an operator reads it without tailing raw JSONL | live run | 004 | status readout across agents, live |
| OBS-05 | L2/L3: reproduce this session's failure cases as fixtures — (a) claimed-done-no-artifact, (b) banner-says-failed-but-completed, (c) complete-but-unmerged worktree, (d) stale-heartbeat stall — and assert each is caught | live pytest/bash | 005 | 4/4 session-failure cases caught live |

## Rules
- READ run-task.sh (262 heartbeat, 270 verify_completion_write, 271 routing) + this session's failure evidence FIRST (RULE ZERO)
- COMPOSE with 270/271 — observability DETECTS what they PREVENT; do not re-implement their logic
- Observability is PASSIVE/automatic — never another gate the operator must satisfy or routes around (lesson: right gate, not more gates / backlog 279)
- Authoritative evidence over banners (lessons #39/#49). State writes Python/Write only.
- L3 (005) reproduces REAL session failures, not simulations. Any RED -> fix -> /kernel/learn.
