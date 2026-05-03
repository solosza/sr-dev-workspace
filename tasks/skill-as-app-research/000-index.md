# Skill-as-App Architecture Research — Task Index

## Goal
Research whether apps should be built traditionally (code that runs independently) or as skills that orchestrate agents. Analyze two test subjects: website-cloner (skill-based) and fraud detector (traditional app). Produce a decision framework and generation skills design sketch.

## Source
Backlog 043: `docs/backlog/043-kernel-research-skill-as-app-architecture.md`

## Tasks

### Phase 1: Analyze Test Subjects
| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-research-analyze-website-cloner]] | RESEARCH | none | pending |
| 002 | [[002-research-analyze-fraud-detector]] | RESEARCH | none | pending |
| 003 | [[003-research-analyze-portfolio-site]] | RESEARCH | none | pending |

### Phase 2: Synthesize Findings
| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 004 | [[004-build-create-project-dir]] | BUILD | none | pending |
| 005 | [[005-build-write-decision-framework]] | BUILD | 001, 002, 003 | pending |
| 006 | [[006-build-write-generation-skills-design]] | BUILD | 001, 003 | pending |
| 007 | [[007-build-write-research-report]] | BUILD | 005, 006 | pending |

### Phase 3: Verify
| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 008 | [[008-test-verify-deliverables]] | TEST | 007 | pending |

## Gate Contract
-> [[gate-contract.md]]

## Deliverables
- Research document at `projects/kernel-architecture/skill-as-app-research.md`
- Decision framework for skill-vs-traditional
- Generation skills design sketch
