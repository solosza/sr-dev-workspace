# Loop Inventory and Gap Analysis

## Current State

The dnd-game-engine-test repo has ~30 skills. The core game loops exist but have inconsistent structure, missing contracts, and broken integration between outer and inner loops.

## Loop Hierarchy (Expected)

```
Campaign Loop (outermost game loop)
  └─ Orchestration Loop (DDD cycle per turn)
       ├─ Combat Loop (inner)
       │    ├─ Ability-Saves Loop (downstream)
       │    └─ Environmental-Hazards Loop (downstream)
       ├─ Social Loop (inner)
       ├─ Challenge Loop (inner)
       │    ├─ Ability-Saves Loop (downstream)
       │    └─ Environmental-Hazards Loop (downstream)
       ├─ Travel Loop (inner)
       │    ├─ Combat Loop (downstream encounter)
       │    ├─ Social Loop (downstream encounter)
       │    └─ Environmental-Hazards Loop (downstream)
       ├─ Rest Loop (inner)
       │    ├─ Downtime-Activities Loop (downstream)
       │    └─ Environmental-Hazards Loop (downstream)
       └─ Item-Use Loop (inner)
```

## Per-Loop Audit

| Loop | SKILL.md | Contracts | DDD Structure | Gate Contract | Test Fixtures | Integration Points |
|------|----------|-----------|---------------|---------------|---------------|-------------------|
| campaign | 81 lines | 6 declared (need verify) | Partial (5-step, not DDD) | No | No | orchestration-loop |
| orchestration-loop | 284 lines | 3 (orch, sub-loop-update, describe-phase) | Yes (DDD) | No | No | All sub-loops |
| combat | 176 lines | 3 | Needs verify | No | No | ability-saves, env-hazards |
| social | 178 lines | 2 | Needs verify | No | Yes (_test/) | — |
| challenge | 168 lines | 2 | Needs verify | No | No | ability-saves, env-hazards |
| travel | 129 lines | 2 | Needs verify | No | No | combat, social, env-hazards |
| rest | 173 lines | 0 (contract at root level) | Needs verify | No | No | downtime, env-hazards |
| item-use | 55 lines | 2 | Needs verify | No | No | — |
| ability-saves | 190 lines | 1 | Yes | Yes | Yes (_test/) | Invoked by combat, challenge |
| environmental-hazards | 481 lines | 1 | Yes | Yes | Yes (_test/) | Invoked by challenge, travel, rest |
| downtime-activities | 355 lines | 1 | Yes | Yes | Yes (_test/) | Invoked by rest |

## Key Gaps

1. **Contracts not embedded in loops** — Some loops declare contracts but they're incomplete or at wrong locations (rest has contract at root). Contracts must be part of the loop per command-skill-pattern Layer 5.
2. **No gate contracts** — Only 3 loops (ability-saves, env-hazards, downtime) have gate-contract.md. The other 8 loops have no enforcement.
3. **No test fixtures** — Only 3 loops have _test/ directories. All loops need test fixtures for DDD validation.
4. **Campaign loop not DDD** — Uses 5-step model instead of DDD (Declare-Determine-Describe). Needs alignment.
5. **Integration contracts missing** — Orchestration loop's sub-loop-update-contract.json defines field ownership, but individual loops don't declare their integration interface (what they receive, what they return).
6. **Legacy code in loops** — challenge, rest, atomic-ops have Python files. Game is agent-orchestrated, no code.
7. **Inconsistent structure** — Some loops follow command-skill-pattern (SKILL.md + contracts/ + references/), others are bare SKILL.md only.

## Helper Skills (Not Loops)

These are invoked by loops but are not loops themselves:
- visual-rendering (invoked by orchestration DECLARE)
- action-prompt (invoked by orchestration DECLARE)
- state-check (invoked by orchestration DESCRIBE)
- atomic-ops (invoked by sub-loops for mechanics)
- character / character-creation-loop
- adventure-creation
- scene
- scaling
- narrative-capture
- entity
- configuration
