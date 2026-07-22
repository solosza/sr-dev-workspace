# Runner Hardening v2 (270) — Task Index

Backlog: [[../../docs/backlog/270-kernel-fix-runner-hardening-v2.md]]
Gate contract: [[gate-contract.md]]

| # | Task | Type |
|---|------|------|
| 001 | [[001-build-completion-write-verify.md]] | BUILD |
| 002 | [[002-build-stall-detection.md]] | BUILD |
| 003 | [[003-build-commit-on-complete.md]] | BUILD |
| 004 | [[004-build-empty-output-rootcause.md]] | BUILD |
| 005 | [[005-test-l2-completion-persistence.md]] | TEST |
| 006 | [[006-test-l3-live-one-task.md]] | TEST |

Target: D:/my_ai_projects/project_test_repos/sr_dev_workspace/run-task.sh (+ optional D:/my_ai_projects/project_test_repos/sr_dev_workspace/lib/ helper). Category-1 runner reliability.
Runs in an isolated worktree; merged to main after orchestrator live gate re-run.
State writes are Python/Write only (no PowerShell). Backward-compatible with KERNEL_AGENT_ID routing.
