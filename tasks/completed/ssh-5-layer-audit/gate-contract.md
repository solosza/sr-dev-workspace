# Gate Contract — SSH 5-Layer Compliance Audit

## Gates

| Gate | Task | Check | Method |
|------|------|-------|--------|
| BUILD-01 | 001 | File map exists | `file_exists: tasks/ssh-5-layer-audit/ssh-platform-file-map.md` |
| BUILD-02 | 002 | Reference checklist exists | `file_exists: tasks/ssh-5-layer-audit/5-layer-reference-checklist.md` |
| BUILD-03 | 003 | L1 violations report exists | `file_exists: tasks/ssh-5-layer-audit/l1-violations.md` |
| BUILD-04 | 004 | L2 violations report exists | `file_exists: tasks/ssh-5-layer-audit/l2-violations.md` |
| BUILD-05 | 005 | L3 violations report exists | `file_exists: tasks/ssh-5-layer-audit/l3-violations.md` |
| BUILD-06 | 006 | L4 violations report exists | `file_exists: tasks/ssh-5-layer-audit/l4-violations.md` |
| BUILD-07 | 007 | L5 violations report exists | `file_exists: tasks/ssh-5-layer-audit/l5-violations.md` |
| BUILD-08 | 008 | Import direction violations exists | `file_exists: tasks/ssh-5-layer-audit/import-direction-violations.md` |
| BUILD-09 | 009 | Compliance report exists | `file_exists: projects/ssh-5-layer-audit/compliance-report.md` |
