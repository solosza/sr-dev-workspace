# Task Index: Universal Hook Validator System (Backlog 089)

**Backlog:** 089-domain-build-universal-hook-validator-system

**Dates:** Phases 0-7 (git setup → shared lib → 4 refactors → integration → merge)

**Deliverable:** Shared lib/validators/ in isagawa-kernel + refactored hooks in 4 workspaces

**Status:** ⏳ All tasks PENDING

---

## Task Summary Table

| Task # | Type | Phase | Title | Dependencies | Status |
|--------|------|-------|-------|--------------|--------|
| **001** | GIT | 0 | Create feature branch in isagawa-kernel | — | ⏳ |
| **002** | BUILD | 1a | Create lib/validators directory structure | 001 | ⏳ |
| **003** | BUILD | 1b | Create code_quality.py validator | 002 | ⏳ |
| **004** | BUILD | 1c | Create state_validation.py validator | 002 | ⏳ |
| **005** | BUILD | 1d | Create bash_validation.py validator | 002 | ⏳ |
| **006** | BUILD | 1e | Create common.py utilities | 002 | ⏳ |
| **007** | BUILD | 1f | Create EXTENSIBILITY.md guide | 002 | ⏳ |
| **008** | TEST | 1g | Test validators L1 (imports) | 003-007 | ⏳ |
| **009** | BUILD | 2a | Refactor sr_dev hook to thin orchestrator | 008 | ⏳ |
| **010** | BUILD | 2b | Remove sr_dev local validators directory | 009 | ⏳ |
| **011** | TEST | 2c | Test sr_dev hook L1 (imports) | 009 | ⏳ |
| **012** | TEST | 2d | Test sr_dev hook L2 (functional) | 009 | ⏳ |
| **013** | TEST | 2e | Test sr_dev hook L3 (behavioral) | 009 | ⏳ |
| **014** | BUILD | 3a | Discover hmsa-healthcare-qa hooks | — | ⏳ |
| **015** | BUILD | 3b | Refactor hmsa hook to thin orchestrator | 008, 014 | ⏳ |
| **016** | BUILD | 3c | Remove hmsa local validators directory | 015 | ⏳ |
| **017** | TEST | 3d | Test hmsa hook L1/L2/L3 | 015 | ⏳ |
| **018** | BUILD | 4a | Discover game-dev hooks | — | ⏳ |
| **019** | BUILD | 4b | Refactor game-dev hook to thin orchestrator | 008, 018 | ⏳ |
| **020** | BUILD | 4c | Remove game-dev local validators directory | 019 | ⏳ |
| **021** | TEST | 4d | Test game-dev hook L1/L2/L3 | 019 | ⏳ |
| **022** | BUILD | 5a | Analyze platform-ssh hook | — | ⏳ |
| **023** | BUILD | 5b | Refactor platform-ssh hook to thin orchestrator | 008, 022 | ⏳ |
| **024** | BUILD | 5c | Remove platform-ssh local validators directory | 023 | ⏳ |
| **025** | TEST | 5d | Test platform-ssh hook L1/L2/L3 | 023 | ⏳ |
| **026** | TEST | 6a | Integration L1: All 4 hooks load together | 013, 017, 021, 025 | ⏳ |
| **027** | TEST | 6b | Integration L2: Debug violation in all 4 | 013, 017, 021, 025 | ⏳ |
| **028** | TEST | 6c | Integration L2: Secret violation in all 4 | 013, 017, 021, 025 | ⏳ |
| **029** | TEST | 6d | Integration L2: Wildcard violation in all 4 | 013, 017, 021, 025 | ⏳ |
| **030** | TEST | 6e | Integration L2: Bash cd violation in all 4 | 013, 017, 021, 025 | ⏳ |
| **031** | TEST | 6f | Integration L2: Valid code passes all 4 | 013, 017, 021, 025 | ⏳ |
| **032** | TEST | 6g | Integration L3: Workspace isolation | 013, 017, 021, 025 | ⏳ |
| **033** | TEST | 6h | Integration L4: Performance testing | 013, 017, 021, 025 | ⏳ |
| **034** | TEST | 6i | Integration L4: PoC new workspace adoption | 013, 017, 021, 025 | ⏳ |
| **035** | GIT | 7 | Merge feature branch to origin/main | 034 | ⏳ |

**Total: 35 atomic tasks**

- **BUILD tasks:** 19
- **TEST tasks:** 15
- **GIT tasks:** 1

---

## Phases (Dependency Groups)

### Phase 0: Git Setup
- **001** — Create feature branch

### Phase 1: Create Shared Library
- **002-007** — Create lib/validators directory + 4 validators + documentation
- **008** — Test L1 (all modules import)

### Phase 2-5: Refactor Workspaces (Parallel After Phase 1)
Each workspace has same pattern:
- **x-a** — Refactor hook (or discover if needed)
- **x-b** — Remove local validators directory
- **x-c** — Test L1/L2/L3

**Phase 2 (sr_dev):** Tasks 009-013
**Phase 3 (hmsa-healthcare-qa):** Tasks 014-017
**Phase 4 (game-dev):** Tasks 018-021
**Phase 5 (platform-ssh):** Tasks 022-025

### Phase 6: Integration Testing
- **026-034** — Cross-workspace L1/L2/L3/L4 testing

### Phase 7: Git Merge
- **035** — Merge feature branch back to main

---

## Execution Order

```
001 (git setup)
  ↓
002-008 (Phase 1: shared lib)
  ↓
  ├─→ 009-013 (Phase 2: sr_dev) ─┐
  │                               ├─→ 026-034 (Phase 6: integration) → 035 (Phase 7: merge)
  ├─→ 014-017 (Phase 3: hmsa) ───┤
  │                               ├─→ (parallel after Phase 1)
  ├─→ 018-021 (Phase 4: game-dev) ┤
  │                               │
  └─→ 022-025 (Phase 5: ssh) ─────┘

Phases 2-5 run in PARALLEL (no inter-dependencies).
Phase 6 waits for ALL of 2-5 to complete.
Phase 7 waits for Phase 6 to complete.
```

---

## Gate Contract Reference

See: `gate-contract.md` — 43 deliverables with L1/L2/L3/L4 gates

---

## Key Files

| File | Purpose |
|------|---------|
| **000-index.md** | This file — task overview + execution order |
| **gate-contract.md** | Mechanical verification gates for all deliverables |
| **001-..** | Phase 0 git setup |
| **002-007** | Phase 1 shared lib creation |
| **008** | Phase 1 L1 testing |
| **009-013** | Phase 2 sr_dev refactoring |
| **014-017** | Phase 3 hmsa refactoring |
| **018-021** | Phase 4 game-dev refactoring |
| **022-025** | Phase 5 platform-ssh refactoring |
| **026-034** | Phase 6 integration testing |
| **035** | Phase 7 git merge |

---

## Notes

- All tasks are atomic (one action per task)
- L1/L2/L3 tests required for each deliverable
- Use `gate-contract.md` to verify each deliverable before proceeding
- Phases 2-5 can execute in parallel (independent workspaces)
- Phase 6 depends on ALL of phases 2-5 completing
- Phase 7 depends on phase 6 completing
- Pipeline mode: `no_execute: true` (skip execution, return task count/folder)

