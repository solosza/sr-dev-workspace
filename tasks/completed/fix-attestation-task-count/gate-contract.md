# Gate Contract — Fix Attestation Bundle Task Count

| Gate | Check | Method | Pass Condition | Fail Action |
|------|-------|--------|----------------|-------------|
| G1 | Diagnosis findings written | file_exists | `projects/fix-attestation-task-count/diagnosis.md` exists | Write task 001 incomplete |
| G2 | attest.py has fallback fix | grep | `_count_task_folder` or `task_file_count` in `lib/attestation/attest.py` | Fix task 002 incomplete |
| G3 | May 27 bundles have task_count | run_code | All 5 May 27 bundle JSONs have non-null `task_count` in `predicate.metadata` | Backfill task 003 incomplete |
| G4 | attest.py dry-run passes | run_code | `python lib/attestation/attest.py --dry-run` exits 0 with valid bundle | Test task 004 failed |
| G5 | Workspace committed | run_code | `git -C workspace status --short` has no untracked/modified files in lib/ | Commit task 005 incomplete |
