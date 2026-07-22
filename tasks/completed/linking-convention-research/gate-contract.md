# Gate Contract — Linking Convention Research

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | @import test results documented | file_exists | `test -f D:/my_ai_projects/project_test_repos/sr_dev_workspace/tasks/linking-convention-research/at-import-test-results.md` | Run tests |
| BUILD-02 | Wikilink vs codespan comparison documented | file_exists | `test -f D:/my_ai_projects/project_test_repos/sr_dev_workspace/tasks/linking-convention-research/wikilink-vs-codespan-results.md` | Run comparison |
| BUILD-03 | Current usage analysis documented | file_exists | `test -f D:/my_ai_projects/project_test_repos/sr_dev_workspace/tasks/linking-convention-research/current-usage-analysis.md` | Run analysis |
| BUILD-04 | Design decision document exists | file_exists | `test -f D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/docs/design/tiered-index-architecture/linking-convention.md` | Write doc |
| BUILD-05 | Migration checklist exists | file_exists | `test -f D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/docs/design/tiered-index-architecture/linking-migration-checklist.md` | Write checklist |
