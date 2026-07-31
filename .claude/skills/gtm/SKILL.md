---
name: gtm
description: Post-GO loop, highest-leverage. Find the channel + funnel that actually gets customers. Kill-by-default on reachability. Heavier HITL (spend). Lean output, every run saved.
---

# Go-to-Market Loop

**Purpose:** For a committed business + offer, answer *"how do I actually get customers — which channel, what funnel?"*
**Runs after** `/offer`; **feeds** `/launch` + `/operate`.
**Philosophy:** distribution decides; pick few channels and win them; reachability is the gate. The user decides; the loop plans.

## Cross-cutting rules
- **LEAN OUTPUT.** Quickest view — never a long doc. See [[loop-output-lean]].
- **Standalone & modular.** Runs alone on any business input, OR as a sub-step called by another loop. If an input an upstream loop would normally supply is missing, gather it (research) or ask — never require the upstream loop to have run first. Returns its verdict/output cleanly so a caller can consume it.
- **Heavier HITL (post-GO).** Every spend / outreach / campaign step PROPOSES; a human APPROVES before money or messages go out. Never auto-send.
- **Kill-by-default** if no channel you can actually run reaches the buyer (the reachability killer — watch the self-selection trap: a target defined by low digital engagement is hard to reach digitally).
- **Never acts** (drafts the plan + assets; the human sends). **Prior-art first** + **every run saved** (see Persist).

## Steps

| # | Step | Do |
|---|------|-----|
| 0 | Prior-art | Read `state/ledger.jsonl`; surface an equivalent past GTM run; let the human choose. |
| 1 | Channel | Where the ICP ACTUALLY is — pick 1-2 (not all). Cite why (audience, intent, cost). |
| 2 | Hook | The one-line message that stops the ICP. Tie to their pain, not your features. |
| 3 | Funnel | Awareness -> interest -> action, mapped to the channel. The minimum steps. |
| 4 | Mechanic | The repeatable motion (content cadence / outreach sequence / paid loop) + the assets it needs. |
| 5 | Reachability check | Can you actually reach + convert this buyer through this channel? If no -> kill or switch channel. |
| 6 | First-customer test | The smallest campaign to get the first customers + a response/CAC threshold + budget cap. |
| 7 | Scale | One line: what you'd pour into once the test works. |

## Research
Use `WebSearch`/`WebFetch` for Steps 1-2 (where the ICP gathers, channel benchmarks/CAC, what hooks work). Cite.

## HITL (the one stop)
After Step 6, present the channel + hook + funnel + the first test (with budget cap). User: `commit <channel>` / `park` / `kill` (unreachable).

## Output (lean)
1. **The channel + why** (1 line).
2. **The hook** (the actual line).
3. **The funnel** — 3-5 steps.
4. **First-customer test** — the campaign + threshold + budget cap.
5. **One line:** commit / park / kill.

Tables/bullets over prose. No essay.

## Persist (compact, mandatory)
- **Report** -> `projects/assay/gtm/runs/<YYYY-MM-DD>-<slug>.md` (re-runs suffix `-2`).
- **Ledger** -> `.claude/skills/gtm/state/ledger.jsonl` — one JSON line (business, channels, hook, funnel, mechanic, reachability, test, report path).
- **Index** -> `projects/assay/gtm/runs/INDEX.md` — one row.
- **Venture record** -> `projects/assay/ventures/<slug>.md` — append run to Journey + update header; refresh ventures INDEX.
UTF-8, no BOM. All land before presenting.

## Chain
`/offer` (package + price) -> **`/gtm` (get customers)** -> `/launch` (ship) + `/operate` (run).
