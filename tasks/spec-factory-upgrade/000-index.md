# Spec Factory Upgrade + SSH Platform — Task Index

## Goal
Sync kernel changes to spec factory, rebuild step-11 with tiered indexing + run-task.sh, then run factory for SSH/CIQ domain.

## Tasks

### Phase 1: Kernel Sync — Hooks (4 tasks)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-sync-copy-hook-auto-approve]] | BUILD | none | pending |
| 002 | [[002-sync-copy-hook-actions-log]] | BUILD | none | pending |
| 003 | [[003-sync-copy-hook-gate-enforcer]] | BUILD | none | pending |
| 004 | [[004-sync-copy-hook-test-failure]] | BUILD | none | pending |

### Phase 1: Kernel Sync — Commands (11 tasks)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 005 | [[005-sync-copy-cmd-anchor]] | BUILD | none | pending |
| 006 | [[006-sync-copy-cmd-complete]] | BUILD | none | pending |
| 007 | [[007-sync-copy-cmd-session-start]] | BUILD | none | pending |
| 008 | [[008-sync-copy-cmd-domain-setup]] | BUILD | none | pending |
| 009 | [[009-sync-copy-cmd-fix]] | BUILD | none | pending |
| 010 | [[010-sync-copy-cmd-learn]] | BUILD | none | pending |
| 011 | [[011-sync-copy-cmd-reset]] | BUILD | none | pending |
| 012 | [[012-sync-copy-cmd-task-builder]] | BUILD | none | pending |
| 013 | [[013-sync-copy-cmd-audit-workflow]] | BUILD | none | pending |
| 014 | [[014-sync-copy-cmd-backlog]] | BUILD | none | pending |
| 015 | [[015-sync-copy-cmd-autonomous-cycle]] | BUILD | none | pending |

### Phase 1: Kernel Sync — Skills (4 tasks)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 016 | [[016-sync-copy-skill-task-builder]] | BUILD | none | pending |
| 017 | [[017-sync-copy-skill-audit-workflow]] | BUILD | none | pending |
| 018 | [[018-sync-copy-skill-autonomous-cycling]] | BUILD | none | pending |
| 019 | [[019-sync-copy-skill-domain-setup]] | BUILD | none | pending |

### Phase 1: Kernel Sync — Scripts + Config (4 tasks)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 020 | [[020-sync-copy-run-task]] | BUILD | none | pending |
| 021 | [[021-sync-copy-run-task-batch]] | BUILD | none | pending |
| 022 | [[022-sync-update-settings]] | BUILD | 001-004 | pending |
| 023 | [[023-sync-update-claude-md]] | BUILD | 005-019 | pending |

### Phase 2: Step-11 Rebuild (12 tasks)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 024 | [[024-s11-create-validation-dir]] | BUILD | none | pending |
| 025 | [[025-s11-write-setup-workspace]] | BUILD | 024 | pending |
| 026 | [[026-s11-write-run-domain-setup]] | BUILD | 024 | pending |
| 027 | [[027-s11-write-install-dependencies]] | BUILD | 024 | pending |
| 028 | [[028-s11-write-generate-gate-tasks]] | BUILD | 024 | pending |
| 029 | [[029-s11-write-run-gate-cycling]] | BUILD | 024 | pending |
| 030 | [[030-s11-write-verify-gates]] | BUILD | 024 | pending |
| 031 | [[031-s11-write-mock-data-comparison]] | BUILD | 024 | pending |
| 032 | [[032-s11-write-coverage-report]] | BUILD | 024 | pending |
| 033 | [[033-s11-write-validation-report-schema]] | BUILD | 024 | pending |
| 034 | [[034-s11-write-retry-cleanup]] | BUILD | 024 | pending |
| 035 | [[035-s11-rewrite-step11-index]] | BUILD | 025-034 | pending |

### Phase 3: Test Kernel Sync (8 tasks)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 036 | [[036-test-sync-hook-gate-enforcer]] | TEST | 003, 022 | pending |
| 037 | [[037-test-sync-hook-actions-log]] | TEST | 002, 022 | pending |
| 038 | [[038-test-sync-hook-auto-approve]] | TEST | 001, 022 | pending |
| 039 | [[039-test-sync-hook-test-failure]] | TEST | 004, 022 | pending |
| 040 | [[040-test-sync-cmd-count]] | TEST | 005-015, 023 | pending |
| 041 | [[041-test-sync-skill-count]] | TEST | 016-019, 023 | pending |
| 042 | [[042-test-sync-run-task-exec]] | TEST | 020 | pending |
| 043 | [[043-test-sync-run-task-batch-exec]] | TEST | 021 | pending |

### Phase 4a: Factory — Research (4 tasks)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 044 | [[044-factory-decompose-ssh]] | RESEARCH | 036-043 | pending |
| 045 | [[045-factory-audit-ssh]] | RESEARCH | 044 | pending |
| 046 | [[046-factory-score-ssh]] | BUILD | 045 | pending |
| 047 | [[047-factory-design-ssh]] | BUILD | 046 | pending |

### Phase 4b: Factory — Build Spec Skill (7 tasks)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 048 | [[048-factory-build-skill-md]] | BUILD | 047 | pending |
| 049 | [[049-factory-build-workflow-md]] | BUILD | 047 | pending |
| 050 | [[050-factory-build-step-01]] | BUILD | 048, 049 | pending |
| 051 | [[051-factory-build-step-02]] | BUILD | 048, 049 | pending |
| 052 | [[052-factory-build-step-03]] | BUILD | 048, 049 | pending |
| 053 | [[053-factory-build-step-04]] | BUILD | 048, 049 | pending |
| 054 | [[054-factory-build-step-05]] | BUILD | 048, 049 | pending |

### Phase 4c: Factory — Build Reference Code (15 tasks)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 055 | [[055-factory-build-ssh-interface]] | BUILD | 047 | pending |
| 056 | [[056-factory-build-validator-package]] | BUILD | 055 | pending |
| 057 | [[057-factory-build-validator-kernel]] | BUILD | 055 | pending |
| 058 | [[058-factory-build-validator-service]] | BUILD | 055 | pending |
| 059 | [[059-factory-build-validator-config]] | BUILD | 055 | pending |
| 060 | [[060-factory-build-task-run-ssh]] | BUILD | 055 | pending |
| 061 | [[061-factory-build-role-batch-executor]] | BUILD | 055-060 | pending |
| 062 | [[062-factory-build-test-ssh-batch]] | BUILD | 055-061 | pending |
| 063 | [[063-factory-build-test-conftest]] | BUILD | 055-061 | pending |
| 064 | [[064-factory-build-fixture-host-configs]] | BUILD | 045, 047 | pending |
| 065 | [[065-factory-build-config-eval]] | BUILD | 047 | pending |
| 066 | [[066-factory-build-doc-architecture]] | BUILD | 047, 055 | pending |
| 067 | [[067-factory-build-doc-validator-catalog]] | BUILD | 056-059 | pending |
| 068 | [[068-factory-build-doc-framework]] | BUILD | 047, 055 | pending |
| 069 | [[069-factory-build-requirements-txt]] | BUILD | 055 | pending |

### Phase 4d: Factory — Gate Contract + Fixtures (4 tasks)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 070 | [[070-factory-build-gate-contract]] | BUILD | 055-069 | pending |
| 071 | [[071-factory-create-test-dirs]] | BUILD | 070 | pending |
| 072 | [[072-factory-write-fixture-inputs]] | BUILD | 071 | pending |
| 073 | [[073-factory-write-fixture-expected]] | BUILD | 071 | pending |

### Phase 4e: Factory — Wrap + Audit (7 tasks)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 074 | [[074-factory-build-cmd-ssh-workflow]] | BUILD | 048, 049 | pending |
| 075 | [[075-factory-build-state-session-template]] | BUILD | 047 | pending |
| 076 | [[076-factory-build-state-workflow-template]] | BUILD | 047 | pending |
| 077 | [[077-factory-build-readme]] | BUILD | 048-069 | pending |
| 078 | [[078-factory-build-contributing]] | BUILD | 047 | pending |
| 079 | [[079-factory-audit-run]] | BUILD | 070-078 | pending |
| 080 | [[080-factory-audit-fix-gaps]] | BUILD | 079 | pending |

### Phase 5a: Validation (14 tasks)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 081 | [[081-validate-create-workspace]] | TEST | 080 | pending |
| 082 | [[082-validate-copy-spec-files]] | TEST | 081 | pending |
| 083 | [[083-validate-install-kernel]] | TEST | 081 | pending |
| 084 | [[084-validate-install-deps]] | TEST | 082 | pending |
| 085 | [[085-validate-write-domain-setup-task]] | TEST | 084 | pending |
| 086 | [[086-validate-spawn-domain-setup]] | TEST | 085 | pending |
| 087 | [[087-validate-verify-protocol]] | TEST | 086 | pending |
| 088 | [[088-validate-parse-gate-contract]] | TEST | 087 | pending |
| 089 | [[089-validate-generate-gate-tasks]] | TEST | 088 | pending |
| 090 | [[090-validate-spawn-gate-cycling]] | TEST | 089 | pending |
| 091 | [[091-validate-verify-structural-gates]] | TEST | 090 | pending |
| 092 | [[092-validate-verify-functional-gates]] | TEST | 090 | pending |
| 093 | [[093-validate-calculate-coverage]] | TEST | 091, 092 | pending |
| 094 | [[094-validate-compile-report]] | TEST | 093 | pending |

### Phase 5b: Package (6 tasks)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 095 | [[095-package-add-frontmatter]] | BUILD | 094 | pending |
| 096 | [[096-package-fix-absolute-paths]] | BUILD | 094 | pending |
| 097 | [[097-package-verify-readme]] | TEST | 095, 096 | pending |
| 098 | [[098-package-git-init-commit]] | BUILD | 097 | pending |
| 099 | [[099-package-create-remote]] | BUILD | 098 | pending |
| 100 | [[100-package-git-push]] | BUILD | 099 | pending |

### Phase 5c: E2E Production Test (8 tasks)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 101 | [[101-e2e-create-workspace]] | TEST | 100 | pending |
| 102 | [[102-e2e-install-kernel]] | TEST | 101 | pending |
| 103 | [[103-e2e-copy-spec]] | TEST | 101 | pending |
| 104 | [[104-e2e-run-iteration-1-domain-setup]] | TEST | 102, 103 | pending |
| 105 | [[105-e2e-run-iteration-2-task-complete]] | TEST | 104 | pending |
| 106 | [[106-e2e-run-iteration-3-verify-hooks]] | TEST | 105 | pending |
| 107 | [[107-e2e-verify-results]] | TEST | 106 | pending |
| 108 | [[108-e2e-cleanup-workspace]] | BUILD | 107 | pending |

### Production Tests (7 tasks)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 109 | [[109-test-prod-kernel-session]] | TEST | 022, 023 | pending |
| 110 | [[110-test-prod-run-task-execution]] | TEST | 020, 022 | pending |
| 111 | [[111-test-prod-hooks-live-session]] | TEST | 109, 110 | pending |
| 112 | [[112-test-prod-python-imports]] | TEST | 055-065 | pending |
| 113 | [[113-test-prod-pytest-suite]] | TEST | 062, 063, 069 | pending |
| 114 | [[114-test-prod-gate-contract-parse]] | TEST | 070 | pending |
| 115 | [[115-test-prod-s11-validation-mock]] | TEST | 035 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Reference
→ [[docs/research/ssh-platform-gate-reference.md]] — SSH platform gates (31 gates, verification target)

## Deliverables
- Spec factory with all kernel upgrades (Phase 1)
- Step-11 rebuilt with tiered indexing + run-task.sh (Phase 2)
- platform-ssh spec produced by factory (Phase 4)
- Validation report + production e2e test passing (Phase 5)
- All Level 1/2/3 tests passing (Production Tests)
