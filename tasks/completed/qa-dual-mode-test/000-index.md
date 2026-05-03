# QA Dual-Mode Test — Task Index

## Goal
Prove the same test suite runs from either location (within the framework or from a dev project) by setting QA_FRAMEWORK_PATH env var.

## Testbed
Clone sr-dev-workspace to `C:/Users/solos/my_ai_projects/qa-dual-mode-testbed/`. Framework lives at `py-selenium-framework-mcp/`.

## Tasks

### Phase 1: Setup

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-setup-clone-testbed]] | BUILD | none | pending |
| 002 | [[002-setup-install-fw-deps]] | BUILD | 001 | pending |

### Phase 2: Build Config Override

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 003 | [[003-build-read-conftest]] | RESEARCH | 001 | pending |
| 004 | [[004-build-modify-conftest]] | BUILD | 003 | pending |

### Phase 3: Test Mode A (baseline — no env var)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 005 | [[005-test-mode-a-copy-tests]] | BUILD | 002, 004 | pending |
| 006 | [[006-test-mode-a-run-pytest]] | TEST | 005 | pending |
| 007 | [[007-test-mode-a-read-results]] | RESEARCH | 006 | pending |

### Phase 4: Test Mode B (env var override)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 008 | [[008-test-mode-b-create-env]] | BUILD | 004 | pending |
| 009 | [[009-test-mode-b-run-pytest]] | TEST | 005, 008 | pending |
| 010 | [[010-test-mode-b-read-results]] | RESEARCH | 009 | pending |

### Phase 5: Compare + Document

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 011 | [[011-compare-results]] | TEST | 007, 010 | pending |
| 012 | [[012-write-report]] | BUILD | 011 | pending |

### Production Test

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 013 | [[013-prod-test-dual-mode-e2e]] | TEST | 006, 009 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- Modified conftest.py with QA_FRAMEWORK_PATH env var support
- Test report at `docs/research/qa-dual-mode-test-report.md`
