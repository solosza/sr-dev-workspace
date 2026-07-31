# Step 1: Opportunity

## Purpose

From one idea, produce a ranked set of capturable revenue wedges. Diverge wide across the abstraction rungs, then converge hard through an adversarial, kill-by-default gate battery.

## Input

- The raw `<idea>` argument (mine or pulled from the internet)
- Canonical reference: `.claude/docs/design/assay/references/io-contracts.md` (Idea, Wedge)
- `.claude/docs/design/assay/references/lenses.md` (the 6 divergence lenses)
- `.claude/docs/design/assay/references/gates.md` (the adversarial gate battery)
- Contract: `contracts/step-01-contract.json`
- Run ledger: `state/ledger.jsonl` (for the prior-art check — may not exist on first run)

## Output

- `Wedge[]` — the **FULL candidate set**, every idea generated. Survivors carry `status:"survived"` (ranked); killed carry `status:"killed"` + a plain-language `kill_reason`. Nothing generated is discarded — the killed ideas are preserved for the report/ledger (content fodder). Downstream steps process only survivors; an empty *survivor* set is VALID and means "no opening found" (explicit, not an error).

## Acceptance Criteria

- [ ] Idea normalized to `{ value, who_pays, mechanism }`
- [ ] Prior-art check run against the ledger (match on meaning, not wording); any material match surfaced to the human with options a/b/c BEFORE divergence — inform, never silent-block or silent-skip
- [ ] Legitimacy checked: real business vs funnel; who actually earns (doer vs seller-of-the-how-to)
- [ ] Abstraction ladder climbed; each rung kept as a candidate root
- [ ] All 7 lenses applied to each rung BEFORE any gating (diverge/converge kept separate)
- [ ] MANDATORY quotas met: >=1 transpose wedge (changes artifact/mechanism domain) AND >=1 payer-swap wedge (changes who_pays) — or an explicit `quota_miss` logged with the reason. A run where every survivor shares the input's artifact AND payer is flagged as a divergence-failure (low confidence)
- [ ] Every candidate run through the full gate battery kill-by-default (incl. TAM/demand-density and reachability); uncertain gates killed or flagged for escalation, never silent-passed
- [ ] Each survivor names its opening (the un-easy part the crowd skips)
- [ ] Output shape matches io-contracts; survivors ranked by gate_scores

## References

- [[../references/INDEX]] -> design doc `references/io-contracts.md`, `references/lenses.md`, `references/gates.md`

## Procedure

1. **Normalize:** strip the idea to `{ value, who_pays, mechanism }`.
2. **Prior-art check (have we assayed this before?):** read the run ledger `state/ledger.jsonl` (skip if it does not exist yet — first run). Compare THIS idea's normalized `{ value, who_pays, mechanism }` against every prior run's normalized idea — **match on meaning, not raw wording** (an LLM judgment: "same value + same buyer + same mechanism" = a match, even if worded differently). If a material match is found: **STOP and surface it to the human** before doing any divergence work —
   > "You assayed an equivalent idea on `<date>` — verdict was `<prior top wedge / decision>`. Options: (a) show me the prior result, (b) re-run fresh anyway, (c) re-run but focus on what's changed."
   Inform, do NOT block: a re-run is often correct (the market moved, or the engine itself improved). Proceed only per the human's choice; if (c), note what is different (new gates, new info) so Decide can highlight the delta. Log the match decision. If no match, continue silently.
3. **Legitimacy:** real business vs funnel; identify who actually earns (the doer vs the seller-of-the-how-to).
3. **Abstract up:** literal -> pattern -> underlying capability/market; keep each rung as a candidate root.
4. **DIVERGE:** apply the 7 lenses (adjacent, transpose, recombine, invert/picks-and-shovels, constraint-break, zoom, payer-swap) to each rung -> candidate wedges. Generous, no killing yet. **Enforce the quotas:** you MUST produce at least one transpose wedge (strip the artifact, keep the mechanism — a different domain) and at least one payer-swap wedge (a different buyer). If genuinely none is viable, log `quota_miss` with the reason instead of skipping silently.
5. **GATE:** run every candidate through the adversarial battery (legal/reg, unit economics, saturation, timing/why-now, moat, speed+cost-to-first-dollar, recurring-vs-one-shot, TAM/demand-density, reachability, guru-source/doer-vs-seller), kill-by-default. Reachability especially: can you actually *reach* this buyer through a channel you can run? Guru-source: do the idea's promoters make money selling the blueprint rather than running the business? **NOTE: fit-to-me is NOT in the kill battery** — compute it and DISPLAY it as a tag (high/cond/low), but never kill or down-rank on it. A great idea survives at fit:low (the operator can build/partner/learn). Kill on absolute merit, not on whether it's "yours."
6. **Find the opening:** for survivors, name the un-easy part the crowd skips (distribution / integration / service / compliance).
7. **Rank on absolute merit + preserve:** rank survivors by opportunity strength (pain + why-now + defensibility + size) via gate scores — **NOT by fit-to-me**. Attach fit as a displayed tag only. Emit the FULL `Wedge[]` (survivors ranked + every killed candidate with `status:"killed"` and a one-line `kill_reason`), each with `lens_origin` + `abstraction_rung` recorded. Never drop a generated idea.
8. **Bias-check (unbiased guard):** if the ranked survivors all cluster around the operator's existing assets/domain, raise a **bias-failure flag** ("everything funneled back to what I already do - under-explored") and go back to DIVERGE, forcing genuinely distant ideas (`/lateral`, transpose, arbitrage into unfamiliar domains). The engine must be willing to rank #1 a great business with fit:low.

## Verification

- Output validates against `contracts/step-01-contract.json` (shape + empty-ok + kill-by-default rules)
- Every survivor carries a per-gate score and a named opening

## Failure Recovery

- If diverge was cut short by early gating, restart the lens pass before any kill.
- If a gate can neither confidently kill nor keep, flag the wedge for ambiguity escalation at Step 4 — do not silent-pass.
- If nothing survives, emit an explicit empty `Wedge[]` (this is a valid, useful "fast kill").
