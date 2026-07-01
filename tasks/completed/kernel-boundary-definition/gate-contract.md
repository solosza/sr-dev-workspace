# Gate Contract — Kernel Boundary Definition

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| RESEARCH-01 | Three-way diff report exists | file_exists | `projects/kernel-boundary/three-way-diff.md` exists | Create report |
| BUILD-01 | kernel-manifest.json exists | file_exists | File at isagawa-kernel root | Create manifest |
| BUILD-02 | kernel-sync.sh exists | file_exists | Script at isagawa-kernel root | Create script |
| BUILD-03 | Extensions identified and documented | file_exists | `projects/kernel-boundary/extension-list.md` exists | Document extensions |
| BUILD-04 | domain-setup reads manifest | grep | `kernel-manifest` appears in domain-setup command | Update domain-setup |
| TEST-01 | Manifest lists only governance files | run_code | All entries are loop commands, hooks, or scripts | Fix manifest |
