# Harness Observability Layer (276) — Task Index

Backlog: [[../../docs/backlog/276-kernel-build-harness-observability-layer.md]]
Gate contract: [[gate-contract.md]]

| # | Task | Type |
|---|------|------|
| 001 | [[001-build-completion-truth-oracle.md]] | BUILD |
| 002 | [[002-build-banner-vs-reality.md]] | BUILD |
| 003 | [[003-build-liveness-and-stranded-deliverable.md]] | BUILD |
| 004 | [[004-build-run-status-view.md]] | BUILD |
| 005 | [[005-test-reproduce-session-failures.md]] | TEST |

Target: D:/my_ai_projects/project_test_repos/sr_dev_workspace/lib/ (observability helpers) + a status command. Composes with 270 (completion persistence, verify_completion_write)
+ 271 (state routing) — detects what they prevent; do NOT duplicate them.
Structural detection of false-completion / silent-death / STRANDED-DELIVERABLE without orchestrator vigilance.
State writes Python/Write only. Runs isolated worktree, block-to-completion; merged after orchestrator L3 re-run.
