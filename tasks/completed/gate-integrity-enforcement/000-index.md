# Gate Integrity Enforcement (273) — Task Index

Backlog: [[../../docs/backlog/273-kernel-fix-gate-integrity.md]]
Gate contract: [[gate-contract.md]]

| # | Task | Type |
|---|------|------|
| 001 | [[001-build-gate-evidence-classifier.md]] | BUILD |
| 002 | [[002-build-fixture-portability-linter.md]] | BUILD |
| 003 | [[003-build-strip-markup-grep-helper.md]] | BUILD |
| 004 | [[004-test-gate-integrity-regression.md]] | TEST |

Target: D:/my_ai_projects/project_test_repos/sr_dev_workspace/lib/ (helpers) + gate-contract verification path. Last item of the kernel-fix chain (categories 1-4).
Fixes: gate-pass-on-stub/simulation (247 L3 sim, 216 L3 never ran); non-portable fixtures (222 relative DATABASE_URL/PYTHONPATH, #47);
grep false-positives (CSS max-width:100% matched absolute-claims grep, 255/256/258). COMPOSE with 276 observability (don't duplicate).
Runs isolated worktree, block-to-completion; merged after orchestrator re-run.
