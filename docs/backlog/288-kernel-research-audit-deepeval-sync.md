# Audit platform-deepeval Uncommitted Changes Before GitHub Sync

## Status
Open

## Priority
High — the active deepeval work (62 uncommitted, Jul 7 5-layer implementation) needs a clean commit, not a blind `git add -A`. Gates the platform-deepeval → GitHub re-sync.

## Summary
The working copy at `D:/my_ai_projects/project_test_repos/platform-deepeval` is the latest/active deepeval platform (last commit 2026-07-07 `d394fb2` "5-layer reference implementation", branch `feature/harness-eval-5-layer`, remote `isagawa-qa/platform-deepeval`), with 62 uncommitted files. Before syncing to GitHub, audit those 62 files so we commit the real work and leave out noise/secrets. READ-ONLY: produce a report only — no `git add`, `commit`, or `push`.

## Requirements
- Enumerate all 62 uncommitted paths (`git -C <repo> status --porcelain`).
- Classify each as **kernel-state noise** (`.claude/state/*`, `*.log`, `__pycache__/`, `*.pyc`, `actions.jsonl`, `*_workflow.json`, `session_state.json`, `anchor-logs/`) vs **real work** (source, tests, docs, config).
- Flag any file that must **NOT** be committed (secrets, API keys, `.env`, large binaries, local absolute paths).
- Produce a recommended clean commit set (the real-work files) + a concrete commit message.
- Note whether a `.gitignore` addition would stop the noise recurring.
- Do NOT mutate the repo in any way.

## References
- Repo: `D:/my_ai_projects/project_test_repos/platform-deepeval` (remote `isagawa-qa/platform-deepeval`, branch `feature/harness-eval-5-layer`)
- Sibling context: the deepeval trio was triaged during kernel consolidation; this is the kept active copy.

## Task Builder Input
- **Deliverable:** A written audit report at `projects/deepeval-sync-audit/audit-report.md`: full file classification (noise vs real vs do-not-commit), recommended commit set + message, `.gitignore` suggestion. Repo untouched.
- **Location:** subproject:deepeval-sync-audit
- **Scope:** RESEARCH
- **Constraints:** READ-ONLY on `platform-deepeval` — no add/commit/push/mutation. Analysis + report only.
