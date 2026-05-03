# Sync All Domain Specs to Master Kernel

**Source:** docs/backlog/057-kernel-refactor-sync-all-domain-specs.md
**Location:** workspace (orchestration here, targets across repos)
**Total tasks:** 21 (18 BUILD + 3 TEST)

## Source

`D:\my_ai_projects\isagawa-kernel` (master kernel, synced from sr_dev_workspace in pipeline 061)

## Targets (17 repos)

### project_test_repos/
1. cognitive-agent
2. domain-spec-factory
3. game-dev
4. game-engine-master
5. healthcare-qa-spec-master
6. hmsa-healthcare-qa
7. isagawa-qa-zentyant
8. platform-deepeval
9. platform-playwright
10. platform-selenium
11. test-content-production
12. test-kernel-bootstrap
13. test-platform-deepeval

### Top-level (D:\my_ai_projects\)
14. isagawa-kernel-a
15. isagawa-kernel-b
16. py_sel_framework_mcp
17. qa_kernel_test

## Tasks

### Phase 1: Setup
| # | Task | Type |
|---|------|------|
| 001 | Write sync script | BUILD |

### Phase 2: Sync Repos (one per repo)
| # | Task | Type |
|---|------|------|
| 002 | Sync cognitive-agent | BUILD |
| 003 | Sync domain-spec-factory | BUILD |
| 004 | Sync game-dev | BUILD |
| 005 | Sync game-engine-master | BUILD |
| 006 | Sync healthcare-qa-spec-master | BUILD |
| 007 | Sync hmsa-healthcare-qa | BUILD |
| 008 | Sync isagawa-qa-zentyant | BUILD |
| 009 | Sync platform-deepeval | BUILD |
| 010 | Sync platform-playwright | BUILD |
| 011 | Sync platform-selenium | BUILD |
| 012 | Sync test-content-production | BUILD |
| 013 | Sync test-kernel-bootstrap | BUILD |
| 014 | Sync test-platform-deepeval | BUILD |
| 015 | Sync isagawa-kernel-a | BUILD |
| 016 | Sync isagawa-kernel-b | BUILD |
| 017 | Sync py_sel_framework_mcp | BUILD |
| 018 | Sync qa_kernel_test | BUILD |

### Phase 3: Verification
| # | Task | Type |
|---|------|------|
| 019 | L1 — verify file counts | TEST |
| 020 | L2 — verify content match | TEST |
| 021 | L3 — verify domain preservation | TEST |
