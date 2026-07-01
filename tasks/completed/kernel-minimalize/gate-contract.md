# Gate Contract — Kernel Minimalize

| Gate ID | Type | Check | File/Path | Expected |
|---------|------|-------|-----------|----------|
| BUILD-01 | file_exists | Feature freeze policy | docs/kernel-feature-freeze-policy.md | File exists with freeze rules |
| REFACTOR-01 | grep | CLAUDE.md lists only core commands | CLAUDE.md | No execute-pipeline, task-builder, prod-test, audit-workflow in Commands section |
| BUILD-02 | file_exists | Core vs extension doc | docs/kernel-core-vs-extension.md | Classification table exists |
| TEST-01 | grep | Core commands still listed | CLAUDE.md | session-start, anchor, learn, complete, fix, domain-setup present |
