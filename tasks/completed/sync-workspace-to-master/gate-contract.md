# Gate Contract — Sync Workspace to Master

## Gates

| ID | Check | Method | Path/Command |
|----|-------|--------|--------------|
| BUILD-01 | 15 kernel commands exist in master | run_code | `test $(ls D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/*.md \| wc -l) -eq 15` |
| BUILD-02 | 3 top-level commands exist | run_code | `test -f D:/my_ai_projects/isagawa-kernel/.claude/commands/clone.md && test -f D:/my_ai_projects/isagawa-kernel/.claude/commands/elegant.md && test -f D:/my_ai_projects/isagawa-kernel/.claude/commands/grill.md` |
| BUILD-03 | autonomous-cycling SKILL.md matches sr_dev | run_code | `diff D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/autonomous-cycling/SKILL.md D:/my_ai_projects/isagawa-kernel/.claude/skills/autonomous-cycling/SKILL.md` |
| BUILD-04 | kernel-domain-setup step-10 matches sr_dev | run_code | `diff D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/kernel-domain-setup/references/step-10-state.md D:/my_ai_projects/isagawa-kernel/.claude/skills/kernel-domain-setup/references/step-10-state.md` |
| BUILD-05 | 7 skill folders exist in master | run_code | `test $(ls -d D:/my_ai_projects/isagawa-kernel/.claude/skills/*/ \| wc -l) -ge 7` |
| BUILD-06 | 6 hooks exist in master | run_code | `test $(ls D:/my_ai_projects/isagawa-kernel/.claude/hooks/*.py \| wc -l) -ge 6` |
| BUILD-07 | settings.local.json has 5+ hook entries | grep | `grep -c "command.*python.*hooks" D:/my_ai_projects/isagawa-kernel/.claude/settings.local.json` >= 5 |
| BUILD-08 | lib/attestation/intent.py exists | file_exists | `D:/my_ai_projects/isagawa-kernel/lib/attestation/intent.py` |
| BUILD-09 | run-task.sh exists | file_exists | `D:/my_ai_projects/isagawa-kernel/run-task.sh` |
| BUILD-10 | .claude/lessons/lessons.md exists | file_exists | `D:/my_ai_projects/isagawa-kernel/.claude/lessons/lessons.md` |
| BUILD-11 | CLAUDE.md has task-builder section | grep | `grep -q "task-builder" D:/my_ai_projects/isagawa-kernel/CLAUDE.md` |
| BUILD-12 | kernel-manifest.json exists | file_exists | `D:/my_ai_projects/isagawa-kernel/kernel-manifest.json` |
| TEST-13 | All synced files match sr_dev | run_code | `diff -rq D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/commands/kernel/ D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/` |
| TEST-14 | Zero diff on hooks | run_code | `for h in universal-gate-enforcer.py test-failure-detector.py actions-log-appender.py agent-inline-execution-blocker.py auto-approve-claude-writes.py; do diff D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/hooks/$h D:/my_ai_projects/isagawa-kernel/.claude/hooks/$h; done` |
| TEST-15 | Master-only content preserved | run_code | `test -d D:/my_ai_projects/isagawa-kernel/scanner && test -d D:/my_ai_projects/isagawa-kernel/tests && test -f D:/my_ai_projects/isagawa-kernel/README.md && test -f D:/my_ai_projects/isagawa-kernel/LICENSE` |
