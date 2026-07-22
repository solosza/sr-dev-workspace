# SSH Platform 5-Layer Refactor — Task Index

**Backlog:** [[192-qa-refactor-ssh-platform-5-layer-compliance]]
**Target:** `D:\my_ai_projects\project_test_repos\platform-ssh\framework\_reference\`
**Contract:** `.claude/docs/design/check-5-layer/references/5-layer-contract.md`
**Scope:** REFACTOR

## Phase 1: Foundation (Layer 1 + Utilities)

| # | Task | Type |
|---|------|------|
| 001 | [[001-build-write-autologger]] | BUILD |
| 002 | [[002-build-write-init-files]] | BUILD |
| 003 | [[003-build-rewrite-ssh-interface]] | BUILD |

## Phase 2: Refactor Existing Validators (Layer 2)

| # | Task | Type |
|---|------|------|
| 004 | [[004-build-delete-compliance-validator-abc]] | BUILD |
| 005 | [[005-build-rewrite-stig-validator]] | BUILD |
| 006 | [[006-build-rewrite-config-validator]] | BUILD |
| 007 | [[007-build-rewrite-kernel-validator]] | BUILD |
| 008 | [[008-build-rewrite-package-validator]] | BUILD |
| 009 | [[009-build-rewrite-service-validator]] | BUILD |

## Phase Boundary: Verify Phases 1-2

| # | Task | Type |
|---|------|------|
| 010 | [[010-test-verify-phase-1-2-imports]] | TEST |

## Phase 3: New Compliance Validators (Layer 2)

| # | Task | Type |
|---|------|------|
| 011 | [[011-build-write-cis-validator]] | BUILD |
| 012 | [[012-build-write-fips-validator]] | BUILD |
| 013 | [[013-build-write-nist-validator]] | BUILD |
| 014 | [[014-build-write-pci-dss-validator]] | BUILD |
| 015 | [[015-build-write-hipaa-validator]] | BUILD |
| 016 | [[016-build-write-soc2-validator]] | BUILD |
| 017 | [[017-build-write-iso27001-validator]] | BUILD |

## Phase 4: Task + Role (Layers 3-4)

| # | Task | Type |
|---|------|------|
| 018 | [[018-build-rewrite-task-layer]] | BUILD |
| 019 | [[019-build-rewrite-role-layer]] | BUILD |

## Phase 5: Tests (Layer 5)

| # | Task | Type |
|---|------|------|
| 020 | [[020-build-rewrite-conftest]] | BUILD |
| 021 | [[021-build-rewrite-test-stig]] | BUILD |
| 022 | [[022-build-rewrite-test-batch]] | BUILD |

## Verification

| # | Task | Type |
|---|------|------|
| 023 | [[023-test-import-validation]] | TEST |
| 024 | [[024-test-full-suite]] | TEST |
