# Update Metric Catalog

## Context
Add ReadComplianceMetric to the DeepEval domain spec's metric catalog so future eval suite generation can include it for agent pipeline evaluations.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-build-write-read-compliance-metric

## Phase Gate
- [ ] `framework/_reference/metrics/read_compliance_metrics.py` exists

## Requirements
- Edit: `D:/my_ai_projects/project_test_repos/test-platform-deepeval/.claude/skills/deepeval-management-layer/references/metric-catalog.md`
- Add new section "## Procedure Compliance Metrics" after "## Agentic Metrics" with:

| Metric | What It Measures | Required Params | Default Threshold |
|--------|-----------------|-----------------|-------------------|
| ReadComplianceMetric | Did the agent read all required files? | required_reads, actual_reads | 1.0 (all required) |

- Add `required_reads` and `actual_reads` to the Parameter Reference table

## Acceptance Criteria
- [ ] `grep -q "ReadComplianceMetric" .claude/skills/deepeval-management-layer/references/metric-catalog.md` passes
- [ ] `grep -q "Procedure Compliance" .claude/skills/deepeval-management-layer/references/metric-catalog.md` passes

## Gates Satisfied
- BUILD-11

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
