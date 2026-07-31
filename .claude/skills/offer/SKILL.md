---
name: offer
description: Post-GO loop. Design the offer + pricing that captures the most value, honestly. Kill-by-default if no price clears margin. Lean output, every run saved.
---

# Offer / Pricing Loop

**Purpose:** For a committed business, answer *"how do I package and price this to capture the most value — honestly?"*
**Runs after** `/deep-dive` says go; **feeds** `/gtm` (the offer is what GTM sells).
**Philosophy:** value-based, honest (no overclaiming), kill-by-default on margin. The user decides; the loop designs.

## Cross-cutting rules
- **LEAN OUTPUT.** Quickest view to the pertinent info — never a long doc. See [[loop-output-lean]].
- **Standalone & modular.** Runs alone on any business input, OR as a sub-step called by another loop. If an input an upstream loop would normally supply is missing, gather it (research) or ask — never require the upstream loop to have run first. Returns its verdict/output cleanly so a caller can consume it.
- **Never acts.** Designs the offer; the human commits + sets real prices live.
- **Honest framing.** The words must match reality (e.g. "screened" not "vetted" unless actually validated) — overclaiming burns trust.
- **Kill-by-default** if no viable price clears margin.
- **Prior-art first** (read the ledger) + **every run saved, compact** (see Persist).

## Steps

| # | Step | Do |
|---|------|-----|
| 0 | Prior-art | Read `state/ledger.jsonl`; surface an equivalent past offer run; let the human choose. |
| 1 | Value metric | What you charge FOR (per seat, per result, per month, per lead). Pick the one that scales with the value the buyer gets. |
| 2 | Packaging | Tiers / bundles / free-vs-paid ladder. What's in each, what's the wedge into the next. |
| 3 | Price points | Benchmark rivals (cite) + willingness-to-pay for the ICP; set concrete numbers. |
| 4 | Model | One-time vs recurring vs hybrid; name why (recurring compounds; one-time is a treadmill). |
| 5 | Risk-reversal | Trial / money-back / guarantee — the friction-remover, sized so it doesn't get abused. |
| 6 | Test | The single cheapest offer/price test (a price A/B, a pre-sale, a fake-door) + threshold. |

## Research
Use `WebSearch`/`WebFetch` for Step 3 (competitor pricing, category benchmarks). Cite. Thin data -> flag, don't invent a number.

## HITL (the one stop)
After Step 6, present the recommended offer + price + the test. User: `commit <offer>` / `park` / `kill` (no price clears margin).

## Output (lean)
1. **The offer in one line** (what, to whom, for how much).
2. **Packaging** — a small tier table (tier · what's in it · price).
3. **The model + why** (1 line).
4. **The cheapest test** to prove people pay (number + deadline).
5. **One line:** commit / park / kill.

Tables over prose. No essay.

## Persist (compact, mandatory)
- **Report** -> `projects/assay/offer/runs/<YYYY-MM-DD>-<slug>.md` (re-runs suffix `-2`; never overwrite).
- **Ledger** -> `.claude/skills/offer/state/ledger.jsonl` — one JSON line (business, value_metric, packaging, prices, model, risk_reversal, test, report path).
- **Index** -> `projects/assay/offer/runs/INDEX.md` — one row.
- **Venture record** -> `projects/assay/ventures/<slug>.md` — append this run to its Journey + update Stage/Verdict/Next-action; refresh `projects/assay/ventures/INDEX.md`.
UTF-8, no BOM. All land before presenting.

## Chain
`/deep-dive` (go) -> **`/offer` (package + price)** -> `/gtm` (get customers).
