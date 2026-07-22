# Gate Contract — Contract Deliverable Copy

Target: `D:/my_ai_projects/project_test_repos/hmsa-qa-platform` on branch build/201-qa-build-contract-deliverable
Source of truth: `D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md`

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| CON-01 | Feature branch current | run_code | branch --show-current → build/201-qa-build-contract-deliverable | Re-run 001 |
| CON-02 | Contract file exists in target | file_exists | `framework/docs/5-layer-contract.md` | Re-run 002 |
| CON-03 | Byte-identical to workspace source | run_code | python sha256 of both files matches — exit 0 | Re-run 002 |
| CON-04 | Committed, clean, main untouched | run_code | commit on branch; porcelain empty; main log unchanged | Re-run 004 |
