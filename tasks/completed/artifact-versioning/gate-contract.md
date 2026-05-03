# Gate Contract — Artifact Versioning Research

## Gates

| ID | Check | Method | Path/Command |
|----|-------|--------|--------------|
| RESEARCH-01 | Artifact inventory covers commands, skills, hooks, protocols, domain specs, infrastructure | grep | `grep -c "commands\|skills\|hooks\|protocols\|domain specs\|infrastructure" projects/kernel-architecture/artifact-versioning-report.md` >= 6 |
| RESEARCH-02 | At least 3 versioning schemes evaluated | grep | `grep -c "^###" projects/kernel-architecture/artifact-versioning-report.md` >= 3 |
| RESEARCH-03 | Drift detection mechanism described | grep | `grep -q "drift" projects/kernel-architecture/artifact-versioning-report.md` |
| RESEARCH-04 | Sync workflow integration described | grep | `grep -q "domain-setup\|anchor\|sync" projects/kernel-architecture/artifact-versioning-report.md` |
| RESEARCH-05 | Domain vs kernel versioning addressed | grep | `grep -q "domain.*artifact\|kernel.*artifact" projects/kernel-architecture/artifact-versioning-report.md` |
| RESEARCH-06 | Migration path with numbered steps | grep | `grep -q "Step [0-9]" projects/kernel-architecture/artifact-versioning-report.md` |
| BUILD-07 | Versioning report exists | file_exists | `projects/kernel-architecture/artifact-versioning-report.md` |
| BUILD-08 | Manifest schema exists | file_exists | `projects/kernel-architecture/kernel-manifest-schema.json` |
| TEST-09 | Both deliverable files exist | run_code | `test -f projects/kernel-architecture/artifact-versioning-report.md && test -f projects/kernel-architecture/kernel-manifest-schema.json` |
| TEST-10 | All 6 research questions answered in report | run_code | `python -c "c=open('projects/kernel-architecture/artifact-versioning-report.md').read(); assert all(q in c for q in ['What needs versioning','versioning scheme','drift','sync','domain-specific','migration'])"` |
