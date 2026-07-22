# Build Sequence — Loop-by-Loop Execution Plan

## Principle: Build Standalone First, Integrate Second

Per loop-architecture design: build each inner loop as standalone (own SKILL.md, contracts, tests), then integrate into the outer loop's routing.

## Phase 1: Generalized Loop Template (workspace)

Build the reusable loop template in the sr_dev_workspace so any repo can use it:

1. **Loop template** — Skeleton SKILL.md with DDD structure + contract stubs
2. **Contract templates** — Input, output, rules, integration JSON schemas
3. **Gate contract template** — Standard enforcement pattern
4. **Test fixture template** — Standard _test/ structure

Deliverable: `.claude/skills/loop-template/` or `framework/loop-template/` in workspace

## Phase 2: Fix Existing Game Loops (dnd-game-engine-test)

For each of the 9 sub-loops, in dependency order:

### Tier 1 — Leaf loops (no downstream invocations)
These are invoked by other loops but don't invoke any loops themselves:
1. **ability-saves** — Already well-structured (190 lines, contracts, gate, tests). Verify and fill gaps.
2. **item-use** — Minimal (55 lines). Needs contracts, gate, tests.

### Tier 2 — Mid-level loops (invoke Tier 1 downstream)
3. **combat** — Invokes ability-saves, env-hazards. Needs contracts, gate, tests.
4. **social** — Standalone. Has _test/. Needs gate contract.
5. **challenge** — Invokes ability-saves, env-hazards. Remove Python code. Needs contracts, gate, tests.
6. **environmental-hazards** — Already well-structured. Verify and fill gaps.
7. **downtime-activities** — Already well-structured. Verify and fill gaps.

### Tier 3 — Complex loops (invoke multiple Tier 2 downstream)
8. **travel** — Invokes combat, social, env-hazards. Most complex integration.
9. **rest** — Invokes downtime, env-hazards. Move contract to proper location. Remove Python code.

### Tier 4 — Outer loops (orchestrate everything)
10. **orchestration-loop** — Already has DDD + 3 contracts. Add per-loop integration validation.
11. **campaign** — Align to DDD pattern. Verify contract completeness.

## Phase 3: Integration Testing

After all loops are individually complete:
1. Walk through a full game turn (campaign → orchestration → sub-loop → return → describe → next turn)
2. Verify contract chain: each loop's output satisfies the caller's expected input
3. Verify downstream invocations fire when conditions are met
4. Verify state-check validates after every sub-loop return

## Per-Loop Task Decomposition (8 tasks each)

For each loop that needs fixing:

| Task | Action | Depends On |
|------|--------|-----------|
| 1 | Audit SKILL.md for DDD compliance | — |
| 2 | Build/fix input contract | Task 1 |
| 3 | Build/fix output contract | Task 1 |
| 4 | Build/fix rules contract | Task 1 |
| 5 | Build integration contract | Tasks 2-3 |
| 6 | Build gate contract | Tasks 2-4 |
| 7 | Build test fixtures | Tasks 2-4 |
| 8 | Wire into orchestration-loop routing | Tasks 1-5 |

**Estimated scope:** ~80-100 tasks total (9 loops x 8 tasks + template + integration testing)

## Code Removal

These loops have legacy Python that must be removed (game is agent-orchestrated, no code):
- `challenge/` — `__init__.py`, `challenge_resolution.py`, `tests/`
- `rest/` — `__init__.py`, `condition_removal.py`, `interruption.py`, `rest_operations.py`, `tests/`
- `atomic-ops/` — All Python files (keep contracts only)
