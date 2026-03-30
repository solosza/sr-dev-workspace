# SSH Compliance Testing Extension — Task Index

## Goal
Extend isagawa-qa/platform-ssh with compliance testing: validators, fixtures, client configs, corrected directory structure.

## Template
→ [[_context/template-file-map.json]] — platform-ssh file tree
→ [[_context/path-mapping.json]] — new/modified/deleted file mapping
→ [[_context/convention-check.json]] — sibling convention verification
→ [[_context/plan-review.json]] — sub-agent plan audit

## Gate Contract
→ [[gate-contract.md]]

## Tasks

### Phase 1: Structural Corrections
| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-move-interface]] | BUILD | none | pending |
| 002 | [[002-build-create-tests-dir]] | BUILD | none | pending |
| 003 | [[003-build-move-conftest]] | BUILD | 002 | pending |
| 004 | [[004-build-move-host-configs]] | BUILD | 002 | pending |
| 005 | [[005-build-delete-old-interface]] | BUILD | 001 | pending |
| 006 | [[006-build-delete-old-conftest]] | BUILD | 003 | pending |
| 007 | [[007-build-delete-old-fixtures-dir]] | BUILD | 004 | pending |
| 008 | [[008-test-verify-structural-corrections]] | TEST | 001-007 | pending |

### Phase 2: Compliance Fixtures
| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 009 | [[009-research-stig-rocky9]] | RESEARCH | 008 | pending |
| 010 | [[010-build-write-stig-fixture]] | BUILD | 009 | pending |
| 011 | [[011-research-cis-rocky9-l1]] | RESEARCH | 008 | pending |
| 012 | [[012-build-write-cis-fixture]] | BUILD | 011 | pending |
| 013 | [[013-research-nist-800-171]] | RESEARCH | 008 | pending |
| 014 | [[014-build-write-nist-fixture]] | BUILD | 013 | pending |
| 015 | [[015-research-fips-140-3]] | RESEARCH | 008 | pending |
| 016 | [[016-build-write-fips-fixture]] | BUILD | 015 | pending |
| 017 | [[017-build-write-ciq-rlc-pro-config]] | BUILD | 008 | pending |
| 018 | [[018-build-write-ciq-rlc-pro-ai-config]] | BUILD | 008 | pending |
| 019 | [[019-test-verify-fixtures-parse]] | TEST | 010-018 | pending |

### Phase 3: Compliance Code
| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 020 | [[020-build-write-stig-validator]] | BUILD | 019 | pending |
| 021 | [[021-build-write-cis-validator]] | BUILD | 019 | pending |
| 022 | [[022-build-write-nist-validator]] | BUILD | 019 | pending |
| 023 | [[023-build-write-fips-validator]] | BUILD | 019 | pending |
| 024 | [[024-build-write-compliance-tasks]] | BUILD | 020-023 | pending |
| 025 | [[025-build-write-compliance-auditor]] | BUILD | 024 | pending |
| 026 | [[026-build-update-conftest]] | BUILD | 025 | pending |
| 027 | [[027-build-write-compliance-tests]] | BUILD | 026 | pending |
| 028 | [[028-test-verify-existing-tests-pass]] | TEST | 027 | pending |
| 029 | [[029-test-verify-compliance-imports]] | TEST | 027 | pending |

### Phase 4: Documentation
| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 030 | [[030-build-update-validator-catalog]] | BUILD | 029 | pending |
| 031 | [[031-build-update-framework-md]] | BUILD | 029 | pending |
| 032 | [[032-build-update-readme]] | BUILD | 029 | pending |

### Phase 5: Production Testing
| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 033 | [[033-test-l1-verify-all-files-exist]] | TEST | 032 | pending |
| 034 | [[034-test-l2-run-pytest]] | TEST | 033 | pending |
| 035 | [[035-test-l3-production-compliance-audit]] | TEST | 034 | pending |

## Deliverables
- SSH platform with corrected directory structure matching sibling conventions
- 4 compliance validators (STIG, CIS, NIST 800-171, FIPS)
- 6 compliance fixture files (4 frameworks + 2 client configs)
- Updated conftest.py with compliance fixture injection
- Compliance test suite
- Updated docs (validator catalog, FRAMEWORK.md, README.md)
- All committed to isagawa-qa/platform-ssh
