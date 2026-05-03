# SP Sanitizer Pipeline — Task Index

## Goal
Build a private Python package (solosza/sp-sanitizer) that sanitizes SQL Server stored procedures for safe sharing with AI agents. Aggressive replace + heuristic leak detection architecture.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-create-repo]] | BUILD | none | pending |
| 002 | [[002-build-project-structure]] | BUILD | 001 | pending |
| 003 | [[003-build-pyproject-toml]] | BUILD | 002 | pending |
| 004 | [[004-build-tsql-keywords]] | BUILD | 002 | pending |
| 005 | [[005-build-data-contracts]] | BUILD | 002 | pending |
| 006 | [[006-build-test-fixtures]] | BUILD | 002 | pending |
| 007 | [[007-build-extract]] | BUILD | 004, 005 | pending |
| 008 | [[008-build-catalog-replace]] | BUILD | 005, 007 | pending |
| 009 | [[009-build-leak-detector]] | BUILD | 004, 005 | pending |
| 010 | [[010-build-refine]] | BUILD | 005 | pending |
| 011 | [[011-build-reverse]] | BUILD | 005 | pending |
| 012 | [[012-build-runner]] | BUILD | 007, 008, 009, 010, 011 | pending |
| 013 | [[013-build-gitignore]] | BUILD | 002 | pending |
| 014 | [[014-build-test-extract]] | BUILD | 006, 007 | pending |
| 015 | [[015-build-test-catalog-replace]] | BUILD | 006, 008 | pending |
| 016 | [[016-build-test-leak-detector]] | BUILD | 006, 009 | pending |
| 017 | [[017-build-test-refine]] | BUILD | 006, 010 | pending |
| 018 | [[018-build-test-reverse]] | BUILD | 006, 011 | pending |
| 019 | [[019-build-test-integration]] | BUILD | 012 | pending |
| 020 | [[020-test-production-l3]] | TEST | 019 | pending |

## Gate Contract
-> [[gate-contract.md]]

## Deliverables
- Private GitHub repo `solosza/sp-sanitizer` with working Python package
- 5 core modules: extract, catalog_replace, leak_detector, refine, reverse
- Orchestrator (runner.py) with CLI entry point
- Pydantic data contracts between all modules
- T-SQL keyword whitelist (200+ keywords)
- Full test suite (unit + integration + L3 production)
- Leak detector as quality gate (zero-leak or fail)
