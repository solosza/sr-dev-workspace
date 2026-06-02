# Gate Contract — Claude Agents Integration Research

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| DOC-01 | Project dir exists | file_exists | `test -d projects/claude-agents-research/` | Create dir |
| DOC-02 | agents-spec-summary exists | file_exists | `test -f projects/claude-agents-research/agents-spec-summary.md` | Write file |
| DOC-03 | Spec covers YAML frontmatter | grep | `grep -qi "frontmatter\|model:\|tools:" projects/claude-agents-research/agents-spec-summary.md` | Expand doc |
| DOC-04 | Spec covers auto-delegation | grep | `grep -qi "auto.del\|@-mention\|delegation" projects/claude-agents-research/agents-spec-summary.md` | Expand doc |
| DOC-05 | kernel-integration-assessment exists | file_exists | `test -f projects/claude-agents-research/kernel-integration-assessment.md` | Write file |
| DOC-06 | Integration covers hook inheritance | grep | `grep -qi "hook\|inherit\|PreToolUse\|PostToolUse" projects/claude-agents-research/kernel-integration-assessment.md` | Expand doc |
| DOC-07 | execute-pipeline-assessment exists | file_exists | `test -f projects/claude-agents-research/execute-pipeline-assessment.md` | Write file |
| DOC-08 | Pipeline assessment covers third route | grep | `grep -qi "third route\|third.route\|named agent route\|route.*agent" projects/claude-agents-research/execute-pipeline-assessment.md` | Expand doc |
| DOC-09 | design-decisions-resolved exists | file_exists | `test -f projects/claude-agents-research/design-decisions-resolved.md` | Write file |
| DOC-10 | All 5 decisions answered | grep | `grep -c "YES\|NO\|ENABLE\|DISABLE\|SELECTIVE\|global\|project" projects/claude-agents-research/design-decisions-resolved.md` | Answer questions |
| DOC-11 | research-report exists | file_exists | `test -f projects/claude-agents-research/research-report.md` | Write file |
| DOC-12 | Report has adoption recommendation | grep | `grep -qi "recommend\|adopt\|skip\|integrate" projects/claude-agents-research/research-report.md` | Expand doc |
| DOC-13 | Report is substantive | run_code | `test $(wc -l < "D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/claude-agents-research/research-report.md") -gt 100` | Expand doc |

## Requirements Coverage
- DOC-01 → task 001
- DOC-02, DOC-03, DOC-04 → task 002
- DOC-05, DOC-06 → task 003
- DOC-07, DOC-08 → task 004
- DOC-09, DOC-10 → task 005
- DOC-11, DOC-12, DOC-13 → task 006
