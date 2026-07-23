# platform-deepeval — Uncommitted File Classification

**Repo:** `D:/my_ai_projects/project_test_repos/platform-deepeval`
**Method:** `git status --porcelain` (62 paths) + `git diff` / `git diff --stat` on tracked changes + content scan (secrets, keys, hardcoded local paths, binary size) on all 50 untracked files.
**Read-only:** no `git add/commit/push/checkout` run against this repo.

## Summary counts

| Category | Count | Notes |
|---|---|---|
| REAL WORK | 62 | 100% — every uncommitted path is real work |
| NOISE | 0 | No `.claude/state`, logs, `__pycache__`, `.pyc`, `actions.jsonl`, `*_workflow.json`, `session_state.json`, or `anchor-logs` paths present in the status at all |
| DO-NOT-COMMIT | 0 | No secrets, `.env` files, private keys, or large binaries found in any modified/untracked file (largest untracked file: 18.6KB, plain text) |

The 62 paths split into two distinct logical groups (relevant for the commit recommendation in task 002):

- **Group A — kernel infra sync (33 paths):** `.claude/commands/kernel/*`, `.claude/hooks/*`, `.claude/skills/*` (autonomous-cycling, kernel-domain-setup, prod-test, task-builder, execute-pipeline, website-cloner). This is a kernel version bump — old task-builder step files deleted/renumbered, new commands/hooks/skills added — consistent with the kernel-consolidation work recorded in the current session's memory (285/286/canonical-kernel).
- **Group B — deepeval framework work (29 paths):** `framework/interfaces/deepeval_interface.py`, `framework/metrics/harness_metrics.py`, `framework/ab_testing/*` (6 files), `framework/metrics/ab_metrics.py`, `framework/metrics/criteria_changelog.md`, `framework/roles/*` (3 files), `framework/tasks/*` (3 files), `framework/tests/test_ab_eval.py`, `framework/tests/test_harness_eval.py`, `lib/common.sh`, `lib/attestation/*` (7 files), `requirements.txt`, `run-task.sh`.

## Group A — Kernel infra sync (REAL WORK)

| Path | Status | Classification |
|---|---|---|
| `.claude/commands/kernel/anchor.md` | M | REAL WORK — kernel sync |
| `.claude/commands/kernel/backlog.md` | M | REAL WORK — kernel sync |
| `.claude/commands/kernel/complete.md` | M | REAL WORK — kernel sync |
| `.claude/commands/kernel/domain-setup.md` | M | REAL WORK — kernel sync |
| `.claude/commands/kernel/fix.md` | M | REAL WORK — kernel sync |
| `.claude/commands/kernel/learn.md` | M | REAL WORK — kernel sync |
| `.claude/commands/kernel/prod-test.md` | M | REAL WORK — kernel sync (diff swaps a placeholder path for `C:/Users/solos/my_ai_projects/platform-ssh-verify` in the usage example — not a secret, but a stale/personal example path worth a follow-up cleanup, see task 002 notes) |
| `.claude/commands/kernel/reset.md` | M | REAL WORK — kernel sync |
| `.claude/commands/kernel/session-start.md` | M | REAL WORK — kernel sync |
| `.claude/commands/kernel/task-builder.md` | M | REAL WORK — kernel sync |
| `.claude/commands/kernel/attest.md` | ?? | REAL WORK — new kernel command |
| `.claude/commands/kernel/execute-pipeline.md` | ?? | REAL WORK — new kernel command |
| `.claude/commands/kernel/scan-bookmarks.md` | ?? | REAL WORK — new kernel command |
| `.claude/hooks/actions-log-appender.py` | M | REAL WORK — kernel sync |
| `.claude/hooks/test-failure-detector.py` | M | REAL WORK — kernel sync |
| `.claude/hooks/universal-gate-enforcer.py` | M | REAL WORK — kernel sync |
| `.claude/hooks/agent-inline-execution-blocker.py` | ?? | REAL WORK — new hook |
| `.claude/hooks/domain-gate-enforcer.template.py` | ?? | REAL WORK — new hook template |
| `.claude/skills/autonomous-cycling/workflow.md` | M | REAL WORK — kernel sync |
| `.claude/skills/kernel-domain-setup/references/step-02-discover.md` | M | REAL WORK — kernel sync |
| `.claude/skills/kernel-domain-setup/references/step-04-extract.md` | M | REAL WORK — kernel sync |
| `.claude/skills/kernel-domain-setup/references/step-05-enforcement.md` | M | REAL WORK — kernel sync |
| `.claude/skills/kernel-domain-setup/references/step-08-protocol.md` | M | REAL WORK — kernel sync |
| `.claude/skills/kernel-domain-setup/references/step-09-commands.md` | M | REAL WORK — kernel sync |
| `.claude/skills/kernel-domain-setup/references/step-10-state.md` | M | REAL WORK — kernel sync |
| `.claude/skills/kernel-domain-setup/references/step-11-report.md` | M | REAL WORK — kernel sync |
| `.claude/skills/prod-test/SKILL.md` | M | REAL WORK — kernel sync (same stale example-path diff as the command file above) |
| `.claude/skills/prod-test/references/step-02-master.md` | M | REAL WORK — kernel sync |
| `.claude/skills/prod-test/references/step-07-execute.md` | M | REAL WORK — kernel sync |
| `.claude/skills/task-builder/SKILL.md` | M | REAL WORK — kernel sync |
| `.claude/skills/task-builder/references/step-01-parse-goal.md` | M | REAL WORK — kernel sync |
| `.claude/skills/task-builder/references/step-02-research.md` | M | REAL WORK — kernel sync |
| `.claude/skills/task-builder/references/step-03-resolve-template.md` | D | REAL WORK — superseded, renumbered to `step-04-resolve-template.md` |
| `.claude/skills/task-builder/references/step-04-decompose.md` | D | REAL WORK — superseded, renumbered to `step-05-decompose.md` |
| `.claude/skills/task-builder/references/step-05-atomize.md` | D | REAL WORK — superseded, renumbered to `step-06-atomize.md` |
| `.claude/skills/task-builder/references/step-06-write-tasks.md` | D | REAL WORK — superseded, renumbered to `step-08-write-tasks.md` |
| `.claude/skills/task-builder/references/step-07-execute.md` | D | REAL WORK — superseded, renumbered to `step-09-execute.md` |
| `.claude/skills/task-builder/references/step-08-structural-audit.md` | D | REAL WORK — superseded, renumbered to `step-10-structural-audit.md` |
| `.claude/skills/task-builder/references/granularity-reference.md` | ?? | REAL WORK — new task-builder reference |
| `.claude/skills/task-builder/references/step-03-convention-check.md` | ?? | REAL WORK — new (inserted) step |
| `.claude/skills/task-builder/references/step-04-resolve-template.md` | ?? | REAL WORK — renumbered replacement |
| `.claude/skills/task-builder/references/step-05-decompose.md` | ?? | REAL WORK — renumbered replacement |
| `.claude/skills/task-builder/references/step-06-atomize.md` | ?? | REAL WORK — renumbered replacement |
| `.claude/skills/task-builder/references/step-07-plan-review.md` | ?? | REAL WORK — new (inserted) step |
| `.claude/skills/task-builder/references/step-08-write-tasks.md` | ?? | REAL WORK — renumbered replacement |
| `.claude/skills/task-builder/references/step-09-execute.md` | ?? | REAL WORK — renumbered replacement |
| `.claude/skills/task-builder/references/step-10-structural-audit.md` | ?? | REAL WORK — renumbered replacement |
| `.claude/skills/execute-pipeline/` (6 files) | ?? | REAL WORK — new skill directory (SKILL.md + references) |
| `.claude/skills/website-cloner/` (7 files) | ?? | REAL WORK — new skill directory (SKILL.md + references + research) |

## Group B — deepeval framework work (REAL WORK)

| Path | Status | Classification |
|---|---|---|
| `framework/interfaces/deepeval_interface.py` | M | REAL WORK — 2-line change |
| `framework/metrics/harness_metrics.py` | M | REAL WORK — 3-line change |
| `framework/ab_testing/` (6 files: reporter.py, variant_generator.py, runner.py, scorer.py, experiment_config.py, + 1 more) | ?? | REAL WORK — new A/B testing subsystem |
| `framework/metrics/ab_metrics.py` | ?? | REAL WORK — new metrics module |
| `framework/metrics/criteria_changelog.md` | ?? | REAL WORK — new changelog doc |
| `framework/roles/` (3 files: harness_evaluator.py, ab_evaluator.py, + 1 more) | ?? | REAL WORK — new roles |
| `framework/tasks/` (3 files) | ?? | REAL WORK — new tasks |
| `framework/tests/test_ab_eval.py` | ?? | REAL WORK — new test |
| `framework/tests/test_harness_eval.py` | ?? | REAL WORK — new test |
| `lib/common.sh` | M | REAL WORK — 40-line change |
| `lib/attestation/` (7 files: attest.py, rekor.py, sign.py, schema.py, intent.py, collect.py, + 1 more) | ?? | REAL WORK — new attestation subsystem (matches kernel's `lib/attestation/intent.py` pattern seen in sr_dev_workspace) |
| `requirements.txt` | M | REAL WORK — 1-line addition |
| `run-task.sh` | M | REAL WORK — 172-line change (significant runner update) |

## Content-scan findings (DO-NOT-COMMIT check)

- Grepped all 50 untracked files for API-key patterns (`sk-...`, `AKIA...`), private-key headers, and hardcoded absolute local paths (`D:\my_ai_projects`, `C:\Users\solos`, `/d/my_ai_projects`): **no matches**.
- Grepped all modified tracked files' diffs for the same patterns: **2 matches**, both in Group A (`prod-test.md`, `prod-test/SKILL.md`) — both are a documentation usage-example path (`C:/Users/solos/my_ai_projects/platform-ssh-verify`), not a secret. Flagged above, not classified DO-NOT-COMMIT.
- Largest untracked file is 18.6KB (`website-cloner/references/extraction.md`), plain text — no binaries found.
