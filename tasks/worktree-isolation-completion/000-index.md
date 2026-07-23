# Worktree Isolation Completion (271) — Task Index

Backlog: [[../../docs/backlog/271-kernel-fix-worktree-isolation-completion.md]]
Gate contract: [[gate-contract.md]]

| # | Task | Type |
|---|------|------|
| 001 | [[001-build-fresh-base-worktree.md]] | BUILD |
| 002 | [[002-build-state-containment.md]] | BUILD |
| 003 | [[003-test-l2-routed-state-isolation.md]] | TEST |
| 004 | [[004-test-l3-live-worktree-isolation.md]] | TEST |

Completes backlog 244 per-agent isolation. Target: D:/my_ai_projects/project_test_repos/sr_dev_workspace/run-task.sh (spawn + state pre-init) + anchor path.
CORE FIX: a routed agent (KERNEL_AGENT_ID set) must NEVER write the PARENT sr_dev_workflow.json / session_state.json —
especially the `anchored` flag (background agents flipping it blocked the interactive session repeatedly this session).
Runs in an isolated worktree, block-to-completion; merged after orchestrator L3 re-run. State writes Python/Write only.
