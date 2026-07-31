---
name: launch
description: Post-GO loop. Ship the smallest sellable asset that delivers the promise. Reuse-first. Kill-by-default if core value can't be delivered. Lean output, every run saved.
---

# Build / Launch Loop

**Purpose:** For a committed business + offer, answer *"what's the smallest thing I can ship that delivers the promise, and how?"*
**Runs after** `/gtm` (or alongside); **feeds** `/operate`.
**Philosophy:** smallest sellable unit, reuse-first, deliver the core value or don't ship. The user decides; the loop plans + (on approval) builds.

## Cross-cutting rules
- **LEAN OUTPUT.** Quickest view — never a long doc. See [[loop-output-lean]].
- **Standalone & modular.** Runs alone on any business input, OR as a sub-step called by another loop. If an input an upstream loop would normally supply is missing, gather it (research) or ask — never require the upstream loop to have run first. Returns its verdict/output cleanly so a caller can consume it.
- **Reuse-first.** Before building anything, check what existing assets/tools already cover it (the website-cloner, the kernel, prior work). Build only the gap.
- **HITL line explicit.** Name what a human approves vs what's automated — carried into `/operate`.
- **Kill-by-default** if the MVP can't actually deliver the core value.
- **Prior-art first** + **every run saved** (see Persist). Any actual building is HITL-gated and on a branch, never silent.

## Steps

| # | Step | Do |
|---|------|-----|
| 0 | Prior-art | Read `state/ledger.jsonl`; surface an equivalent past launch; let the human choose. |
| 1 | MVP | The smallest unit that delivers the offer's core promise. Cut everything else. |
| 2 | Reuse scan | What existing assets/tools cover part of it? Build only the remainder. |
| 3 | Build-vs-buy | For each piece: build, buy, or reuse. Cheapest path to shippable. |
| 4 | HITL/automation line | What the human approves each cycle vs what runs automatically (feeds `/operate`). |
| 5 | Launch checklist | The concrete steps to go live (assets, accounts, wiring). |
| 6 | Go-live test | Prove the thing delivers the promised value ONCE, end-to-end, for real. |

## HITL (the one stop)
After Step 3, present the MVP scope + build-vs-buy + effort. User: `approve <scope>` / `trim` / `kill`. Building proceeds only on approval, on a branch.

## Output (lean)
1. **The MVP in one line** (smallest sellable thing).
2. **Reuse vs build** — a short table (piece · reuse/build/buy).
3. **The HITL/automation line** (what a human approves).
4. **Go-live test** — the one end-to-end value proof.
5. **One line:** approve / trim / kill.

Tables over prose. No essay.

## Persist (compact, mandatory)
- **Report** -> `projects/assay/launch/runs/<YYYY-MM-DD>-<slug>.md` (re-runs suffix `-2`).
- **Ledger** -> `.claude/skills/launch/state/ledger.jsonl` — one JSON line (business, mvp, reuse_vs_build, hitl_line, checklist, go_live_test, report path).
- **Index** -> `projects/assay/launch/runs/INDEX.md` — one row.
- **Venture record** -> `projects/assay/ventures/<slug>.md` — append run to Journey + update header; refresh ventures INDEX.
UTF-8, no BOM. All land before presenting.

## Chain
`/gtm` (customers) -> **`/launch` (ship the MVP)** -> `/operate` (run it).
