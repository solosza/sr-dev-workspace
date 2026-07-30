# Step 2: Buildability

## Purpose

Decide, per surviving wedge, whether the operator can build + automate + govern it with an edge — reusing the existing stack (ALA data/scrapers, kernel, agents, check-5-layer-style gates) before proposing new build.

## Input

- Step 1's `Wedge[]`
- Canonical reference: `.claude/docs/design/assay/references/io-contracts.md` (Wedge in, BuildVerdict out)
- Contract: `contracts/step-02-contract.json`

## Output

- `BuildVerdict[]` — one per input `Wedge`, each with `decision` in {build, pass}, and an optional `picks_and_shovels_variant` flagged for 1-hop re-entry into Step 1.

## Acceptance Criteria

- [ ] One `BuildVerdict` per input `Wedge`
- [ ] buildable scored reuse-first (existing stack before new build)
- [ ] automatable_pct + the HITL line stated per verdict
- [ ] moat_applies honest — false when governance/audit adds no real defensibility
- [ ] compounds, build_cost, strategic_dividend scored
- [ ] any picks-and-shovels variant flagged for exactly 1-hop re-entry into Step 1
- [ ] output shape matches io-contracts

## References

- [[../references/INDEX]] -> design doc `references/io-contracts.md`

## Procedure

1. For each `Wedge`, score: **buildable** (reuse stack vs new), **automatable_pct** + the **HITL line** (90%-manual = not our leverage), **moat_applies** (does governance/audit make our version defensible, or add nothing), **compounds** (stacks on existing builds), **build_cost** (speed to a shippable MVP from existing parts), **strategic_dividend** (does building it strengthen Isagawa — new reusable capability / dogfood).
2. If "can't build the literal wedge, but could build the layer/tool for it" -> emit a **picks-and-shovels variant** that RE-ENTERS Step 1's diverge, bounded to **1 hop** (no infinite loops).
3. Decide **build** / **pass** per wedge.

## Verification

- Output validates against `contracts/step-02-contract.json` (shape + reuse-first + hitl-line + moat-honesty + pns-reentry rules)
- Verdict count equals input wedge count

## Failure Recovery

- If a wedge's buildability is genuinely unknown, mark `decision: pass` with the reason logged rather than guessing `build`.
- If a picks-and-shovels variant would trigger a second re-entry, stop at the 1-hop bound and record it as a wedge for the next run instead.
