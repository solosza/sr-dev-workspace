# Gate Contract — MCP Server Builder Research

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| DOC-01 | Project dir exists | file_exists | `test -d projects/mcp-server-research/` | Create dir |
| DOC-02 | mcp-frameworks-summary exists | file_exists | `test -f projects/mcp-server-research/mcp-frameworks-summary.md` | Write file |
| DOC-03 | Summary covers FastMCP | grep | `grep -qi "fastmcp\|fast.mcp\|SDK\|framework" projects/mcp-server-research/mcp-frameworks-summary.md` | Expand doc |
| DOC-04 | capabilities-assessment exists | file_exists | `test -f projects/mcp-server-research/capabilities-assessment.md` | Write file |
| DOC-05 | Assessment covers attestation | grep | `grep -qi "attest\|attestation\|pipeline" projects/mcp-server-research/capabilities-assessment.md` | Expand doc |
| DOC-06 | research-report exists | file_exists | `test -f projects/mcp-server-research/research-report.md` | Write file |
| DOC-07 | Report has recommendation | grep | `grep -qi "recommend\|build\|skip\|prototype" projects/mcp-server-research/research-report.md` | Expand doc |
| DOC-08 | Report is substantive | run_code | `test $(wc -l < "D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/mcp-server-research/research-report.md") -gt 60` | Expand doc |
