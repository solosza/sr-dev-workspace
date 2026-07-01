# Gate Contract

| Gate ID | Task | Method | Check | Expected |
|---------|------|--------|-------|----------|
| BUILD-01 | 001 | run_code | `test -d D:/my_ai_projects/project_test_repos/kernel-minimal/.git` | exit 0 |
| BUILD-01b | 001 | file_exists | `D:/my_ai_projects/project_test_repos/kernel-minimal/CLAUDE.md` | exists |
| BUILD-02 | 002 | run_code | `ls D:/my_ai_projects/project_test_repos/kernel-minimal/.claude/commands/kernel/ \| wc -l` | 7 (session-start, anchor, learn, complete, fix, domain-setup, reset) |
| BUILD-03 | 003 | run_code | `ls -d D:/my_ai_projects/project_test_repos/kernel-minimal/.claude/skills/*/` | exactly 2 dirs (kernel-domain-setup, autonomous-cycling) |
| BUILD-04 | 004 | run_code | `test ! -d D:/my_ai_projects/project_test_repos/kernel-minimal/delegation && test ! -d D:/my_ai_projects/project_test_repos/kernel-minimal/scanner` | exit 0 |
| BUILD-05 | 005 | run_code | `test ! -d D:/my_ai_projects/project_test_repos/kernel-minimal/lib/attestation && test ! -d D:/my_ai_projects/project_test_repos/kernel-minimal/lib/validators` | exit 0 |
| BUILD-06 | 006 | run_code | `ls D:/my_ai_projects/project_test_repos/kernel-minimal/.claude/lessons/ \| wc -l` | 1 (lessons.md only) |
| BUILD-07 | 007 | grep | `grep -c "session-start\|anchor\|learn\|complete\|fix\|domain-setup\|reset" D:/my_ai_projects/project_test_repos/kernel-minimal/CLAUDE.md` | >= 7 |
| BUILD-08 | 008 | file_exists | `D:/my_ai_projects/project_test_repos/kernel-minimal/docs/kernel-feature-freeze-policy.md` | exists |
| TEST-09 | 009 | run_code | `test -f D:/my_ai_projects/project_test_repos/kernel-minimal/CLAUDE.md && test -f D:/my_ai_projects/project_test_repos/kernel-minimal/run-task.sh` | exit 0 |
