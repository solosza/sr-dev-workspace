# Fraud Detector Patterns — Task Index

## Goal
Add 12 new real-world fraud detection patterns to the fraud detection app's pattern library, sourced from public investigations, congressional testimony, and journalism.

## Source
> [[docs/backlog/039-domain-upgrade-fraud-detector-pattern-library.md]]

## Target Repo
`D:\my_ai_projects\fraud-detection-app`

## Tasks

### Phase 1: Pattern Definitions (001-004)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-add-ngo-grant-patterns]] | BUILD | none | pending |
| 002 | [[002-build-add-healthcare-fraud-patterns]] | BUILD | none | pending |
| 003 | [[003-build-add-government-finance-patterns]] | BUILD | none | pending |
| 004 | [[004-build-add-political-corruption-patterns]] | BUILD | none | pending |

### Phase 2: Pattern Check Logic (005-008)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 005 | [[005-build-write-ngo-checks]] | BUILD | 001 | pending |
| 006 | [[006-build-write-healthcare-checks]] | BUILD | 002 | pending |
| 007 | [[007-build-write-government-checks]] | BUILD | 003 | pending |
| 008 | [[008-build-write-political-checks]] | BUILD | 004 | pending |

### Phase 3: Test Fixtures (009-012)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 009 | [[009-build-write-ngo-fixtures]] | BUILD | 005 | pending |
| 010 | [[010-build-write-healthcare-fixtures]] | BUILD | 006 | pending |
| 011 | [[011-build-write-government-fixtures]] | BUILD | 007 | pending |
| 012 | [[012-build-write-political-fixtures]] | BUILD | 008 | pending |

### Phase 4: Verification (013-015)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 013 | [[013-test-l1-verify-pattern-files]] | TEST | 001-012 | pending |
| 014 | [[014-test-l2-import-and-parse]] | TEST | 001-012 | pending |
| 015 | [[015-test-l3-run-fixtures-against-patterns]] | TEST | 009-012 | pending |

## Gate Contract
> [[gate-contract.md]]
