---
name: competition
description: Loop A of the venture loops. Take a chosen business, map the rival field, find the actionable gaps + your defensible angle to win. Kill-by-default, lean output, every run saved.
---

# Competition Loop (A)

**Purpose:** For one chosen business, answer *"can I win this arena, and how?"* — map rivals, structure the arena, surface the gaps where you win.
**Runs after** `/assay` picks an idea; **feeds** `/deep-dive` (B calls A instead of repeating it).
**Philosophy:** adversarial, gap-focused (not feature lists), kill-by-default. The user decides; the loop researches + presents.

## Cross-cutting rules
- **LEAN OUTPUT (directive).** Quickest view to the most pertinent info — never a long multi-section doc. Reads in under two minutes. See [[loop-output-lean]].
- **Standalone & modular.** Runs alone on any business, OR as a sub-step called by another loop (e.g. `/deep-dive` calls this). If an input an upstream loop would normally supply is missing, gather it or ask. Returns its verdict/angle cleanly so a caller can consume it.
- **Never acts.** Produces a verdict + positioning options only; the commit is the human's.
- **Kill-by-default.** Entrenched, funded incumbents + no seam left → "don't enter here" is a valid, useful output.
- **Prior-art first.** Before researching, read the ledger; if this arena was mapped before, surface it (show / re-run / re-run-on-delta) — don't silently re-spend.
- **Every run saved, compact** (see Persist).

## Steps

| # | Step | Do |
|---|------|-----|
| 0 | Prior-art | Read `state/ledger.jsonl`; if an equivalent arena was mapped, surface it and let the human choose (show / fresh / delta). |
| 1 | Frame | State the strategic question + scope: which segment, geo, and what "winning" means here. |
| 2 | Identify | Find 5-10 real rivals (direct, indirect, substitute). Use web search + reviews + listings — cite what you find. |
| 3 | Profile | Compact matrix per rival: offer · price · positioning · channel · strength · weakness · proof (reviews/traffic). |
| 4 | Structure | Porter's Five Forces (rivalry, new entrants, substitutes, buyer power, supplier power) → how hard is the arena? + a 4-box SWOT for you vs the field. |
| 5 | Gaps | THE money step: underserved segments, pricing holes, service weaknesses, positioning white space. Actionable gaps, not feature lists. |
| 6 | Angle | Your defensible way-to-win + the moat + where you deliberately DON'T compete. Kill here if no gap + entrenched field. |
| 7 | Watch | One-line ongoing intel cadence: what to monitor, how often. |

## Research
Use `WebSearch`/`WebFetch` for Steps 2-4 (find + profile rivals, market structure). Prefer real, cited signals (reviews, pricing pages, traffic) over guesses. Kill-by-default when evidence is thin — flag, don't invent.

## HITL (the one stop)
After Step 6, present the ranked positioning angle(s) + the arena verdict. User: `commit <angle>` / `park` / `kill` (arena not winnable).

## Output (what you SHOW — lean)
1. **Verdict in one line** (e.g. "Winnable via X — the field ignores Y.").
2. **The gap(s) you'd attack** — 1-3 bullets.
3. **Your angle to win + the moat** — 1-2 lines.
4. **The rivals** — a compact table (name · their edge · their hole), not write-ups.
5. **One line:** commit the angle / park / kill.

Tables over prose. No essay. If it's getting long, cut.

## Persist (compact, mandatory — no run lost)
Before presenting, save all three:
- **Report** -> `projects/assay/competition/runs/<YYYY-MM-DD>-<slug>.md` — the lean view above (verdict + gaps + angle + rival table). Re-runs suffix `-2`, `-3`; never overwrite.
- **Ledger** -> `.claude/skills/competition/state/ledger.jsonl` — one appended JSON line (business, scope, rivals[], five_forces, gaps[], angle, verdict, report path). Machine index + prior-art memory.
- **Index** -> `projects/assay/competition/runs/INDEX.md` — one row (date · business · verdict · angle · link).
- **Venture record** -> `projects/assay/ventures/<slug>.md` — match this business to its venture (create if none); append this run to its Journey table + update Stage/Verdict/Next-action; refresh `projects/assay/ventures/INDEX.md`. The cross-loop journey.
UTF-8, no BOM. All land before presenting.

## Render the result (final step, optional)
After presenting, render the arena verdict + positioning angles as a live, question-able board via [[../render/steps/step-serve-and-watch]]: pass this loop's output through the adapter [[../render/adapters/INDEX]] (`to_items`), then serve-and-watch. Standalone and modular — the loop still runs headless without it. Plain vocabulary, no em dashes, fit as a tag only are baked into the adapter.

## Chain
`/assay` (which idea) -> **`/competition` (can I win the field)** -> `/deep-dive` (is it real + plan; calls this loop).
