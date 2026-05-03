# Gate Contract — Sync All Domain Specs

## Gate Contract

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Sync script exists | file_exists | `test -f tasks/sync-all-domain-specs/sync-kernel.sh` | Create script |
| BUILD-02 | cognitive-agent synced | run_code | `test -d "D:/my_ai_projects/project_test_repos/cognitive-agent/.claude/commands/kernel" && test $(ls D:/my_ai_projects/project_test_repos/cognitive-agent/.claude/commands/kernel/*.md \| wc -l) -eq 15` | Re-run sync |
| BUILD-03 | domain-spec-factory synced | run_code | `test $(ls D:/my_ai_projects/project_test_repos/domain-spec-factory/.claude/commands/kernel/*.md \| wc -l) -eq 15` | Re-run sync |
| BUILD-04 | game-dev synced | run_code | `test $(ls D:/my_ai_projects/project_test_repos/game-dev/.claude/commands/kernel/*.md \| wc -l) -eq 15` | Re-run sync |
| BUILD-05 | game-engine-master synced | run_code | `test $(ls D:/my_ai_projects/project_test_repos/game-engine-master/.claude/commands/kernel/*.md \| wc -l) -eq 15` | Re-run sync |
| BUILD-06 | healthcare-qa-spec-master synced | run_code | `test $(ls D:/my_ai_projects/project_test_repos/healthcare-qa-spec-master/.claude/commands/kernel/*.md \| wc -l) -eq 15` | Re-run sync |
| BUILD-07 | hmsa-healthcare-qa synced | run_code | `test $(ls D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/commands/kernel/*.md \| wc -l) -eq 15` | Re-run sync |
| BUILD-08 | isagawa-qa-zentyant synced | run_code | `test $(ls D:/my_ai_projects/project_test_repos/isagawa-qa-zentyant/.claude/commands/kernel/*.md \| wc -l) -eq 15` | Re-run sync |
| BUILD-09 | platform-deepeval synced | run_code | `test $(ls D:/my_ai_projects/project_test_repos/platform-deepeval/.claude/commands/kernel/*.md \| wc -l) -eq 15` | Re-run sync |
| BUILD-10 | platform-playwright synced | run_code | `test $(ls D:/my_ai_projects/project_test_repos/platform-playwright/.claude/commands/kernel/*.md \| wc -l) -eq 15` | Re-run sync |
| BUILD-11 | platform-selenium synced | run_code | `test $(ls D:/my_ai_projects/project_test_repos/platform-selenium/.claude/commands/kernel/*.md \| wc -l) -eq 15` | Re-run sync |
| BUILD-12 | test-content-production synced | run_code | `test $(ls D:/my_ai_projects/project_test_repos/test-content-production/.claude/commands/kernel/*.md \| wc -l) -eq 15` | Re-run sync |
| BUILD-13 | test-kernel-bootstrap synced | run_code | `test $(ls D:/my_ai_projects/project_test_repos/test-kernel-bootstrap/.claude/commands/kernel/*.md \| wc -l) -eq 15` | Re-run sync |
| BUILD-14 | test-platform-deepeval synced | run_code | `test $(ls D:/my_ai_projects/project_test_repos/test-platform-deepeval/.claude/commands/kernel/*.md \| wc -l) -eq 15` | Re-run sync |
| BUILD-15 | isagawa-kernel-a synced | run_code | `test $(ls D:/my_ai_projects/isagawa-kernel-a/.claude/commands/kernel/*.md \| wc -l) -eq 15` | Re-run sync |
| BUILD-16 | isagawa-kernel-b synced | run_code | `test $(ls D:/my_ai_projects/isagawa-kernel-b/.claude/commands/kernel/*.md \| wc -l) -eq 15` | Re-run sync |
| BUILD-17 | py_sel_framework_mcp synced | run_code | `test $(ls D:/my_ai_projects/py_sel_framework_mcp/.claude/commands/kernel/*.md \| wc -l) -eq 15` | Re-run sync |
| BUILD-18 | qa_kernel_test synced | run_code | `test $(ls D:/my_ai_projects/qa_kernel_test/.claude/commands/kernel/*.md \| wc -l) -eq 15` | Re-run sync |
| TEST-19 | L1 file counts all repos | run_code | All 17 repos have 15 commands, 7 skill folders, 6 hooks | Fix missing |
| TEST-20 | L2 content match all repos | run_code | Zero diff on kernel files across all 17 repos | Re-sync |
| TEST-21 | L3 domain preservation | run_code | Domain commands, skills, protocols intact in all repos | Restore |
