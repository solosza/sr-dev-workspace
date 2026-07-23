# Model Router Keyword Tuning (272) — Task Index

Backlog: [[../../docs/backlog/272-kernel-fix-model-routing-tuning.md]]
Gate contract: [[gate-contract.md]]

| # | Task | Type |
|---|------|------|
| 001 | [[001-build-reweight-keywords.md]] | BUILD |
| 002 | [[002-build-precedence-and-default.md]] | BUILD |
| 003 | [[003-test-routing-assertions.md]] | TEST |

Target: D:/my_ai_projects/project_test_repos/sr_dev_workspace/lib/model-routing-config.json + D:/my_ai_projects/project_test_repos/sr_dev_workspace/lib/model-router.sh.
FIX: build/authoring tasks under-tier to Haiku (247/001, 257/001). Re-weight so build/write/implement -> SONNET;
Haiku only for mechanical (copy/scaffold/rename/move/stub/register/index); Opus for architecture/gate/verify.
Do NOT change the resolved model IDs (opus-4-8 / sonnet-5 / haiku-4.5) — only the keyword->tier mapping.
run-task.sh sources the router — runs isolated worktree, block-to-completion; merged after orchestrator re-run.
