# Phase 4: Refactor game-dev to Use Shared Lib

**Status:** Depends on Phase 1 + Phase 2 completion

**Deliverable:** game-dev hook refactored to thin orchestrator using shared validators + L1/L2/L3 validation

---

## Workspace Details

- **Path:** `D:\my_ai_projects\project_test_repos\game-dev`
- **Domain:** `game-dev`
- **Current hooks:** To be discovered in Phase 1.2 (discovery task)

---

## Discovery Phase (1.2)

Same discovery steps as Phase 3:
1. List `.claude/` structure
2. Identify existing hook files
3. Document current validators
4. Determine domain name and any domain-specific rules

---

## Refactoring (Standard Pattern)

Follow identical pattern as Phase 2 and Phase 3:

1. Backup current hooks
2. Create thin orchestrator importing shared validators
3. Remove local validators directory
4. Test L1/L2/L3
5. Verify Claude Code integration

**Same orchestrator template as Phase 3, updating domain to `game-dev`**

---

## Key Difference: Parallel Execution

Unlike Phase 2 (sequential to Phase 1), Phase 3 and Phase 4 can run **in parallel** because:
- They both depend on Phase 1 (shared lib) being complete
- They don't depend on each other
- Each modifies an isolated workspace

Task-builder should execute Phase 3 and Phase 4 tasks concurrently.

---

## Tasks for Phase 4

| Task | Sequence |
|------|----------|
| 1 | Discover: List `.claude/` structure in game-dev |
| 2 | Discover: Identify current hook files |
| 3 | Discover: Document current validators in use |
| 4 | Backup: Copy current hook file(s) |
| 5 | Create: Thin orchestrator (game-dev-gate-enforcer.py) |
| 6 | Remove: Local validators/ directory |
| 7 | Update: sys.path to point to isagawa-kernel/lib/validators |
| 8 | Test L1: Hook imports without errors |
| 9 | Test L2: Verify all validators work |
| 10 | Test L3: Feed known violations, verify blocking |
| 11 | Verify: Claude Code hook integration works |

---

## Acceptance Criteria

- [ ] Current hooks backed up
- [ ] New thin orchestrator created and valid
- [ ] Hook imports shared validators without errors (L1)
- [ ] All validators work correctly (L2)
- [ ] L3: Test suite with known violations all blocked
- [ ] Behavior preserves original validation rules
- [ ] sys.path resolves correctly to isagawa-kernel

---

## Notes

- Can execute **in parallel with Phase 3** (both depend on Phase 1 only)
- Self-contained workspace: no cross-dependencies

