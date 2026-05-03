# SSH STIG Validator — Task Index

**Backlog:** docs/backlog/077-domain-build-ssh-stig-validator.md
**Target:** D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test
**Scope:** BUILD

## Tasks

| # | Type | Task | Depends On |
|---|------|------|------------|
| 001 | BUILD | [[001-build-write-stig-fixture]] | — |
| 002 | BUILD | [[002-build-write-stig-validator]] | 001 |
| 003 | BUILD | [[003-build-write-stig-tests]] | 001, 002 |
| 004 | TEST | [[004-test-l1-l2-verification]] | 001, 002, 003 |
| 005 | TEST | [[005-test-l3-live-stig]] | 004 |
