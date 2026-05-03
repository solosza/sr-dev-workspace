# SSH Compliance Foundation — Task Index

**Backlog:** docs/backlog/076-domain-build-ssh-compliance-foundation.md
**Target:** D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test
**Scope:** BUILD

## Tasks

| # | Type | Task | Depends On |
|---|------|------|------------|
| 001 | BUILD | [[001-build-write-compliance-validator]] | — |
| 002 | BUILD | [[002-build-edit-service-validator]] | — |
| 003 | BUILD | [[003-build-edit-host-configs]] | — |
| 004 | BUILD | [[004-build-edit-batch-executor]] | 001 |
| 005 | BUILD | [[005-build-write-test-fixture]] | — |
| 006 | BUILD | [[006-build-write-compliance-tests]] | 001, 002, 003, 004, 005 |
| 007 | TEST | [[007-test-l1-structural-verification]] | 001, 002, 003, 004, 005, 006 |
| 008 | TEST | [[008-test-l2-import-verification]] | 007 |
| 009 | TEST | [[009-test-l3-live-ssh-compliance]] | 008 |

## Phases

**Phase 1: Build (001-006)** — Write base class, edit existing files, write tests
**Phase 2: Test (007-009)** — L1/L2/L3 verification
