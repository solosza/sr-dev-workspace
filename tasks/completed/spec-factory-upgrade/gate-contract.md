# Gate Contract — Spec Factory Upgrade

→ [[.claude/skills/task-builder/references/verification-methods.md]]

## Phase 1: Kernel Sync (26 gates)

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| SYNC-01 | auto-approve hook copied | file_exists | `test -f .../hooks/auto-approve-claude-writes.py` | Copy file |
| SYNC-02 | actions-log hook copied | file_exists | `test -f .../hooks/actions-log-appender.py` | Copy file |
| SYNC-03 | gate-enforcer copied | file_exists | `test -f .../hooks/universal-gate-enforcer.py` | Copy file |
| SYNC-04 | test-failure hook copied | file_exists | `test -f .../hooks/test-failure-detector.py` | Copy file |
| SYNC-05 | anchor.md copied | file_exists | `test -f .../commands/kernel/anchor.md` | Copy file |
| SYNC-06 | complete.md copied | file_exists | `test -f .../commands/kernel/complete.md` | Copy file |
| SYNC-07 | session-start.md copied | file_exists | `test -f .../commands/kernel/session-start.md` | Copy file |
| SYNC-08 | domain-setup.md copied | file_exists | `test -f .../commands/kernel/domain-setup.md` | Copy file |
| SYNC-09 | fix.md copied | file_exists | `test -f .../commands/kernel/fix.md` | Copy file |
| SYNC-10 | learn.md copied | file_exists | `test -f .../commands/kernel/learn.md` | Copy file |
| SYNC-11 | reset.md copied | file_exists | `test -f .../commands/kernel/reset.md` | Copy file |
| SYNC-12 | task-builder.md copied | file_exists | `test -f .../commands/kernel/task-builder.md` | Copy file |
| SYNC-13 | audit-workflow.md copied | file_exists | `test -f .../commands/kernel/audit-workflow.md` | Copy file |
| SYNC-14 | backlog.md copied | file_exists | `test -f .../commands/kernel/backlog.md` | Copy file |
| SYNC-15 | autonomous-cycle.md copied | file_exists | `test -f .../commands/kernel/autonomous-cycle.md` | Copy file |
| SYNC-16 | task-builder skill copied | file_exists | `test -f .../skills/task-builder/SKILL.md` | Copy dir |
| SYNC-17 | audit-workflow skill copied | file_exists | `test -f .../skills/audit-workflow/SKILL.md` | Copy dir |
| SYNC-18 | autonomous-cycling skill copied | file_exists | `test -f .../skills/autonomous-cycling/SKILL.md` | Copy dir |
| SYNC-19 | domain-setup skill copied | file_exists | `test -f .../skills/kernel-domain-setup/SKILL.md` | Copy dir |
| SYNC-20 | run-task.sh copied | file_exists | `test -f .../run-task.sh` | Copy file |
| SYNC-21 | run-task-batch.sh copied | file_exists | `test -f .../run-task-batch.sh` | Copy file |
| SYNC-22 | settings has PermissionRequest | grep | `grep -q 'PermissionRequest' settings.local.json` | Update |
| SYNC-23 | settings has actions-log | grep | `grep -q 'actions-log-appender' settings.local.json` | Update |
| SYNC-24 | CLAUDE.md has task-builder | grep | `grep -q 'task-builder' CLAUDE.md` | Update |
| SYNC-25 | CLAUDE.md has audit-workflow | grep | `grep -q 'audit-workflow' CLAUDE.md` | Update |
| SYNC-26 | CLAUDE.md has backlog | grep | `grep -q 'backlog.md' CLAUDE.md` | Update |

## Phase 2: Step-11 Rebuild (13 gates)

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| S11-01 | validation dir exists | file_exists | `test -d .../references/validation/` | Create dir |
| S11-02 | setup-workspace.md exists | file_exists | `test -f .../validation/setup-workspace.md` | Create file |
| S11-03 | run-domain-setup.md exists | file_exists | `test -f .../validation/run-domain-setup.md` | Create file |
| S11-04 | install-dependencies.md exists | file_exists | `test -f .../validation/install-dependencies.md` | Create file |
| S11-05 | generate-gate-tasks.md exists | file_exists | `test -f .../validation/generate-gate-tasks.md` | Create file |
| S11-06 | run-gate-cycling.md exists | file_exists | `test -f .../validation/run-gate-cycling.md` | Create file |
| S11-07 | verify-gates.md exists | file_exists | `test -f .../validation/verify-gates.md` | Create file |
| S11-08 | mock-data-comparison.md exists | file_exists | `test -f .../validation/mock-data-comparison.md` | Create file |
| S11-09 | coverage-report.md exists | file_exists | `test -f .../validation/coverage-report.md` | Create file |
| S11-10 | validation-report-schema.md exists | file_exists | `test -f .../validation/validation-report-schema.md` | Create file |
| S11-11 | retry-cleanup.md exists | file_exists | `test -f .../validation/retry-cleanup.md` | Create file |
| S11-12 | step-11.md is thin index | run_code | `wc -l < step-11.md` < 60 | Rewrite |
| S11-13 | step-11 references run-task.sh | grep | `grep -q 'run-task.sh' step-11.md` | Add ref |

## Phase 3: Functional Tests (8 gates)

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| FUNC-01 | gate-enforcer runs | run_code | Pipe test JSON, exits 0 | Fix hook |
| FUNC-02 | actions-log runs | run_code | Pipe test JSON, appends entry | Fix hook |
| FUNC-03 | auto-approve runs | run_code | Pipe JSON, outputs approval | Fix hook |
| FUNC-04 | test-failure runs | run_code | Pipe test JSON, exits 0 | Fix hook |
| FUNC-05 | 11 command files | run_code | `ls *.md \| wc -l` = 11 | Fix missing |
| FUNC-06 | 4 SKILL.md files | run_code | glob count = 4 | Fix missing |
| FUNC-07 | run-task.sh executable | run_code | `test -x` exits 0 | chmod +x |
| FUNC-08 | run-task-batch.sh executable | run_code | `test -x` exits 0 | chmod +x |

## Phase 4: Factory Execution (22 gates)

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| FAC-01 | Decomposition doc | file_exists | step-01-decomposition.md exists | Run step |
| FAC-02 | Audit doc | file_exists | step-02-audit.md exists | Run step |
| FAC-03 | Score doc | file_exists | step-03-score.md exists | Run step |
| FAC-04 | Design doc | file_exists | step-04-design.md exists | Run step |
| FAC-05 | SKILL.md | file_exists | SKILL.md exists in spec output | Create |
| FAC-06 | workflow.md | file_exists | workflow.md exists | Create |
| FAC-07 | 5 step files | run_code | `ls references/step-*.md \| wc -l` = 5 | Create |
| FAC-08 | ssh_interface.py | file_exists | File exists | Create |
| FAC-09 | SSHInterface class | grep | `grep -q 'class SSHInterface'` | Add class |
| FAC-10 | 4 validators | run_code | `ls validators/*.py \| wc -l` = 4 | Create |
| FAC-11 | run_ssh_command.py | file_exists | File exists | Create |
| FAC-12 | ssh_batch_executor.py | file_exists | File exists | Create |
| FAC-13 | test_ssh_batch.py | file_exists | File exists | Create |
| FAC-14 | conftest.py | file_exists | File exists | Create |
| FAC-15 | host_configs.json | file_exists | File exists | Create |
| FAC-16 | requirements.txt has paramiko | grep | `grep -q 'paramiko'` | Add dep |
| FAC-17 | FRAMEWORK.md | file_exists | File exists | Create |
| FAC-18 | SSH gate-contract.md | file_exists | File exists | Create |
| FAC-19 | 20+ gates in contract | run_code | `grep -c '|'` >= 20 | Add gates |
| FAC-20 | Test fixtures exist | file_exists | `_test/fixtures/` exists | Create |
| FAC-21 | README.md | file_exists | File exists | Create |
| FAC-22 | Audit clean | run_code | Re-audit 0 gaps | Fix gaps |

## Phase 5: Validation + Package + E2E (20 gates)

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| VAL-01 | Workspace created | file_exists | Test dir exists | Create |
| VAL-02 | Spec files copied | file_exists | SKILL.md in workspace | Copy |
| VAL-03 | Kernel installed | file_exists | CLAUDE.md in workspace | Copy |
| VAL-04 | Deps installed | run_code | `pip list \| grep paramiko` | Install |
| VAL-05 | Domain-setup task written | file_exists | Task file exists | Write |
| VAL-06 | Domain-setup spawned | run_code | run-task.sh exited | Fix |
| VAL-07 | Protocol created | file_exists | Protocol file exists | Fix spec |
| VAL-08 | Gates parsed | run_code | Gate count > 0 | Fix parser |
| VAL-09 | Gate tasks generated | run_code | Task count matches gates | Fix gen |
| VAL-10 | Cycling completed | run_code | run-task.sh exited | Fix cycling |
| VAL-11 | Structural gates pass | run_code | All pass | Fix files |
| VAL-12 | Functional gates pass | run_code | All pass | Fix code |
| VAL-13 | Coverage >= 90% | run_code | Percentage >= 90 | Fix coverage |
| VAL-14 | Report compiled | json_valid | validation-report.json valid | Fix format |
| PKG-01 | Frontmatter added | grep | `head -1` is `---` | Add |
| PKG-02 | No absolute paths | grep | `grep -rq 'C:/Users'` returns 1 | Fix |
| PKG-03 | README complete | grep | `grep -q 'install'` | Fix |
| PKG-04 | Git initialized | file_exists | `.git/` exists | Init |
| PKG-05 | Remote created | run_code | `git remote -v` shows origin | Add |
| PKG-06 | Pushed | run_code | `git push` exits 0 | Push |

## E2E Integration (3 gates)

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| INT-01 | Protocol references SSH | run_code | grep 'ssh-management-layer' in protocol | Fix spec |
| INT-02 | Hooks fire | run_code | actions_since_anchor > 0 | Fix hooks |
| INT-03 | Task completes under enforcement | run_code | completed_tasks has entry | Fix cycling |

## Production Tests (7 gates)

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| PROD-01 | Kernel session works in spec factory | run_code | session_started + anchored = true | Fix state |
| PROD-02 | run-task.sh completes task | run_code | Task in completed_tasks | Fix script |
| PROD-03 | Hooks fire during real work | run_code | actions_since_anchor > 0 | Fix hooks |
| PROD-04 | All Python modules import | run_code | All imports exit 0 | Fix code |
| PROD-05 | Pytest suite passes | run_test | `pytest` exits 0 | Fix tests |
| PROD-06 | Gate contract parseable | run_code | 20+ gates with 5 columns | Fix contract |
| PROD-07 | Step-11 validation produces report | run_code | validation-report.json valid | Fix flow |

## Requirements Coverage
Each gate maps to task acceptance criteria. All acceptance criteria have corresponding gates.

## Summary
- Phase 1 (Sync): 26 gates
- Phase 2 (Step-11): 13 gates
- Phase 3 (Functional): 8 gates
- Phase 4 (Factory): 22 gates
- Phase 5 (Validation + Package): 20 gates
- E2E Integration: 3 gates
- Production Tests: 7 gates
- **Total: 99 gates**
