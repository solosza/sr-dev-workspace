---
name: deep-dive
description: Loop B of the venture loops. Pressure-test a chosen business into a go/no-go + first-90-days plan, on evidence. Calls /competition for the rival read. Kill-by-default, lean output, every run saved.
---

# Deep-Dive Loop (B)

**Purpose:** For one chosen business, answer *"is this real, and what's the plan?"* — validate on evidence, then a go/no-go + a concrete first-90-days plan (or a clean kill).
**Runs after** `/competition`; **calls** `/competition` for the rival read (don't repeat it).
**Philosophy:** evidence over opinion, cheapest-test-first, kill-by-default. The user decides; the loop researches + presents.

## Cross-cutting rules
- **LEAN OUTPUT (directive).** Quickest view to the most pertinent info — never a long multi-section doc. Reads in under two minutes. See [[loop-output-lean]].
- **Standalone & modular.** Runs alone on any business, OR as a sub-step called by another loop. It already calls `/competition` as a sub-step (the modular pattern). If an input an upstream loop would normally supply is missing, gather it or ask. Returns its go/no-go cleanly so a caller can consume it.
- **Never acts.** Produces a go/no-go + a plan the human commits to; runs no real-world experiment itself.
- **Kill-by-default.** A failed must-be-true or no demand signal → a clean "no-go" with reasons is a valid, useful output.
- **Prior-art first.** Read the ledger before diving; surface an equivalent past run (show / re-run / delta).
- **Every run saved, compact** (see Persist).

## Steps

| # | Step | Do |
|---|------|-----|
| 0 | Prior-art | Read `state/ledger.jsonl`; surface an equivalent past dive; let the human choose. |
| 1 | Assumptions | Write the 3-5 riskiest "must-be-true"s. These are what the dive tests. |
| 2 | Market size | TAM/SAM/SOM — is there room? Rough numbers, cited. (Ties to assay's TAM gate.) |
| 3 | Customer | Sharp ICP: psychographics + jobs-to-be-done + where they are — not just demographics. |
| 4 | Demand evidence | The decisive step: the single cheapest real-world signal test (interviews / survey / landing-page / pre-orders / waitlist) + a pre-set threshold. Web-research comparable signals to sanity-check. |
| 5 | Competition | CALL `/competition <business>` — reuse its verdict + angle; do not re-map rivals here. |
| 6 | Economics | Pricing, unit economics, CAC/LTV, path to profit. Kill if no margin path. |
| 7 | Build & ops | What it takes to deliver: reuse assay's buildability + the human-in-the-loop line (what's automated vs. approved). |
| 8 | Risks & stress test | Legal/reg, reachability, worst-case, and the explicit kill-conditions. |
| 8b | Fit-to-you (conscious, LATE) | NOW — and only now — weigh fit: given the idea is real, is it the right one for YOU given finite time + assets, or would you build/partner/acquire the capability? This is the ONE place fit is allowed to influence the call (deliberately, by the human), never upstream. A high-merit / low-fit idea is a real option — pursue, partner, or pass with eyes open. |
| 9 | Go/No-Go + plan | Decide on the evidence (+ the conscious fit call); if go, a concrete first-90-days plan (milestones + the first experiment). If no-go, the reasons. |

## Research
Use `WebSearch`/`WebFetch` for Steps 2, 4, 6 (market size, comparable demand signals, pricing benchmarks). Cite. Thin evidence → flag + lean toward kill, never invent a signal.

## HITL (the one stop)
After Step 9, present the go/no-go + plan (or kill reasons). User: `commit` (+ which experiment first) / `park` / `kill`.

## Output (what you SHOW — lean)
1. **Verdict in one line:** GO / NO-GO / GO-IF (+ the one condition).
2. **Why** — the 2-3 findings that drove it (market, demand signal, economics).
3. **The riskiest assumption + the cheapest test to de-risk it** (number + deadline).
4. **If GO:** the first-90-days plan as 3-5 bullets. **If NO-GO:** the reason in one line.
5. **One line:** commit / park / kill.

Tables/bullets over prose. No essay. If it's getting long, cut.

## Persist (compact, mandatory — no run lost)
Before presenting, save all three:
- **Report** -> `projects/assay/deep-dive/runs/<YYYY-MM-DD>-<slug>.md` — the lean view above. Re-runs suffix `-2`; never overwrite.
- **Ledger** -> `.claude/skills/deep-dive/state/ledger.jsonl` — one appended JSON line (business, assumptions[], market_size, icp, demand_test, economics, risks[], decision, plan, report path).
- **Index** -> `projects/assay/deep-dive/runs/INDEX.md` — one row (date · business · verdict · link).
- **Venture record** -> `projects/assay/ventures/<slug>.md` — match this business to its venture (create if none); append this run to its Journey table + update Stage/Verdict/Next-action; refresh `projects/assay/ventures/INDEX.md`. The cross-loop journey.
UTF-8, no BOM. All land before presenting.

## Chain
`/assay` (which idea) -> `/competition` (can I win) -> **`/deep-dive` (is it real + plan)**. Natural next after a GO: the Go-to-Market + Offer/Pricing loops (roadmap gaps).
