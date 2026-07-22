# Build Generalized Loop Integration for D&D Game Engine

## Status
Open

## Priority
High — Game is unplayable without properly integrated loops. All gameplay runs through agent-orchestrated loops with no code. Currently loops exist but have inconsistent structure, missing contracts, and broken outer/inner composition.

## Summary

Build a generalized loop pattern (reusable across repos) and apply it to the dnd-game-engine-test repo. Every game loop (outer or inner) needs: SKILL.md with DDD structure, contracts as part of the loop (input/output/rules/integration), gate contracts for enforcement, and test fixtures. The composition pattern (outer loop invokes inner loop via integration contract) must be formalized so loops can be built standalone and plugged in.

The game is 100% agent-orchestrated — no Python code. The agent reads prescriptive skills (markdown) and applies contracts (JSON) to run D&D 5e sessions. This pattern is not game-specific: any repo with loops uses the same template.

Design references:
- `hmsa-healthcare-qa/.claude/docs/design/loop-architecture/` — Loop theory and composition
- `hmsa-healthcare-qa/.claude/docs/design/tiered-index-architecture/` — File organization pattern
- `hmsa-healthcare-qa/.claude/docs/design/command-skill-pattern/` — 6-layer command/skill/contract structure

## Design Documents

| Document | Purpose |
|----------|---------|
| [[180-domain-build-dnd-game-loop-integration/generalized-loop-pattern]] | Reusable loop template: SKILL.md + contracts + gate + tests. Repo-agnostic. |
| [[180-domain-build-dnd-game-loop-integration/loop-inventory]] | Current state audit of all 11 game loops — what exists, what's missing |
| [[180-domain-build-dnd-game-loop-integration/integration-contracts]] | Bidirectional integration contracts for outer/inner loop composition |
| [[180-domain-build-dnd-game-loop-integration/build-sequence]] | Phased execution plan: template → fix loops → integration testing |

## Requirements

- **Generalized loop template** — Reusable skeleton (SKILL.md + contract stubs + gate + test structure) that any repo can instantiate
- **Contracts as part of the loop** — Every loop gets input, output, rules, and integration contracts embedded in its own `contracts/` directory
- **DDD compliance** — All loops follow Declare-Determine-Describe pattern
- **Integration contracts** — Each inner loop declares what it receives and returns; outer loop validates against it
- **Gate contracts** — Enforcement for every loop (not just 3 of 11)
- **Remove legacy Python** — challenge, rest, atomic-ops have code files. Game is agent-only, no code.
- **Test fixtures** — Every loop gets `_test/fixtures/` with scenarios
- **Build standalone, integrate second** — Each loop is independently complete before wiring into orchestration

## References

- Game repo: `D:/my_ai_projects/project_test_repos/dnd-game-engine-test/`
- Loop architecture design: `D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/docs/design/loop-architecture/design.md`
- Command-skill pattern: `D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/docs/design/command-skill-pattern/index.md`
- Tiered index: `D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/docs/design/tiered-index-architecture/index.md`
- Existing game backlogs: `docs/backlog/done/033-*`, `docs/backlog/done/034-*`, `docs/backlog/done/037-*`, `docs/backlog/035-*`

## Task Builder Input
- **Deliverable:** Generalized loop template (reusable) + all 11 game loops with complete contracts, DDD structure, gates, and integration
- **Location:** `new-repo:D:/my_ai_projects/project_test_repos/dnd-game-engine-test`
- **Scope:** BUILD
- **Constraints:** No Python code — agent-orchestrated only. Contracts are part of the loop, not separate. Must follow hmsa design patterns. Build standalone loops first, then integrate. ~80-100 tasks estimated across 3 phases.
