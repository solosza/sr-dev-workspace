# Gate Contract — HMSA Healthcare QA Workspace

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Workspace dir exists | file_exists | `test -d D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa` | Create dir |
| BUILD-02 | Git repo initialized | file_exists | `test -d D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.git` | Git init |
| BUILD-03 | Kernel .claude/ exists | file_exists | `test -d D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\commands\kernel` | Copy kernel |
| BUILD-04 | CLAUDE.md exists | file_exists | `test -f D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\CLAUDE.md` | Copy CLAUDE.md |
| BUILD-05 | run-task.sh exists | file_exists | `test -f D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\run-task.sh` | Copy scripts |
| BUILD-06 | Spec copied | file_exists | `test -f D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\README.md` | Copy spec |
| BUILD-07 | Initial commit | run_code | `git -C D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa log --oneline -1` exits 0 | Commit |
| FUNC-01 | Domain-setup complete | file_exists | `test -f D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\state\session_state.json` | Run domain-setup |
| FUNC-02 | Protocol created | grep | Protocol file exists in .claude/protocols/ | Run domain-setup |
| FUNC-03 | Hooks registered | grep | `grep -q 'hooks' D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\settings.local.json` | Fix settings |
| BUILD-08 | lessons/ package exists | file_exists | `test -f D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\lessons\__init__.py` | Copy package |
| BUILD-09 | delegation/ package exists | file_exists | `test -f D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\delegation\__init__.py` | Copy package |
| BUILD-10 | scanner/ package exists | file_exists | `test -f D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\scanner\__init__.py` | Copy package |
| BUILD-11 | Test packages exist | file_exists | `test -d D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\tests\test_recurrence` | Copy tests |
| BUILD-12 | Updated learn.md | grep | `grep -q 'Recurrence' D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\commands\kernel\learn.md` | Copy command |
| TEST-01 | All tests pass | run_test | `python -m pytest tests/ -v` exits 0 in target workspace | Fix tests |
| TEST-02 | Features verified | run_code | All 3 packages import cleanly | Fix imports |
| BUILD-13 | Features committed | run_code | `git -C ... log --oneline -1` shows feature commit | Commit |
