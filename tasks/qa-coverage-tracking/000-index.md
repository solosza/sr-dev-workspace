# QA Coverage Tracking + Auto-Extension — Task Index

## Goal
Build coverage tracking and automatic suite extension into the QA framework (py-selenium-framework-mcp).

## Tasks

### Phase 1: Coverage Scanner

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-scanner]] | BUILD | none | pending |
| 002 | [[002-build-report]] | BUILD | 001 | pending |
| 003 | [[003-build-init]] | BUILD | 001 | pending |

### Phase 2: Auto-Extension Generator

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 004 | [[004-build-generator]] | BUILD | 001 | pending |
| 005 | [[005-build-template]] | BUILD | 004 | pending |

### Phase 3: CLI + Integration

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 006 | [[006-build-cli]] | BUILD | 002, 004 | pending |
| 007 | [[007-build-conftest-hook]] | BUILD | 006 | pending |

### Phase 4: MCP Server

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 008 | [[008-build-mcp-coverage]] | BUILD | 001 | pending |

### Phase 5: Tests

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 009 | [[009-test-scanner]] | TEST | 001 | pending |
| 010 | [[010-test-generator]] | TEST | 004 | pending |
| 011 | [[011-test-scan-real]] | TEST | 009 | pending |
| 012 | [[012-test-generate-real]] | TEST | 010 | pending |
| 013 | [[013-test-prod-e2e]] | TEST | 006, 011, 012 | pending |

### Phase 6: Documentation

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 014 | [[014-write-docs]] | BUILD | 013 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- `framework/coverage/` module (scanner, report, generator, cli)
- MCP server get_test_coverage() implemented
- pytest integration hook
- Coverage report showing 7/12 fully mapped, 5 gaps
- Skeleton test generation for uncovered workflows
- Documentation
