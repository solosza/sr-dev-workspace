# 001 — Inventory + classify uncommitted files

## Action
Run `git -C D:/my_ai_projects/project_test_repos/platform-deepeval status --porcelain` and classify every path as NOISE (.claude/state, *.log, __pycache__, *.pyc, actions.jsonl, *_workflow.json, session_state.json, anchor-logs) vs REAL WORK (source/tests/docs/config) vs DO-NOT-COMMIT (secrets, .env, keys, large binaries, local absolute paths).

## Acceptance
- A classification table of all uncommitted paths is produced (saved to projects/deepeval-sync-audit/classification.md).
- READ-ONLY: no git add/commit/push/checkout run against platform-deepeval.
