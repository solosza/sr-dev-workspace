---
name: expand
description: The generative loop. Take an idea and think BIGGER — dispatch it through the expansion angle-loops (data/distribution/platform/productize/license/stack/adjacent) to find how big it can get. Not kill-by-default. Lean output, saved.
---

# Expand Loop (generative)

**Purpose:** For an idea, answer *"how big can this get?"* — the ambitious counterweight to the adversarial pipeline. Dispatches through the expansion angle-loops and synthesizes the biggest coherent version.
**Runs** on a GO idea (to find its ceiling before committing), or standalone to stretch anything.
**Philosophy:** dream the ceiling; the adversarial loops (assay→…→operate) test what survives. Diverge-big here, converge there.

## Cross-cutting rules
- **THINK BIGGER (the DNA).** Push to the ambitious, empire-scale version — every way to monetize the *space*, not just the one product; the adjacent territory to own. Generative and bold, never incremental. Don't self-censor for feasibility — that's the adversarial loops' job.
- **LEAN OUTPUT.** Quickest view — never a long doc. See [[loop-output-lean]].
- **Standalone & modular.** Runs alone on any idea, OR calls the angle-loops as sub-steps. Returns the expanded vision cleanly.
- **Generative, NOT kill-by-default.** Angle-loops propose upside; they don't gate. (The adversarial loops gate later.)
- **Capture new angles (self-extending).** Spot an expansion/monetization path with NO existing angle-loop? Append it to `projects/assay/loop-candidates.jsonl` (don't drop it) — `/sharpen` promotes recurring candidates into new loops. This is how the family grows itself.
- **Prior-art first** + **every run saved** (see Persist).

## The angle-loops (the menu)
| Angle | Command | Asks |
|-------|---------|------|
| Data | `/data` | monetize the data this generates (sell / product / moat / benchmark) |
| Distribution | `/distribution` | the social/content/channel lanes that make it BIG |
| Platform | `/platform` | become the rails others build on |
| Productize | `/productize` | service → product/SaaS (escape hours-for-dollars) |
| License | `/license` | franchise / white-label / license the method |
| Stack | `/stack` | adjacent revenue on the SAME customer |
| Adjacent | `/adjacent` | adjacent VENTURES in the space → feed `/assay` |

## Steps
| # | Step | Do |
|---|------|-----|
| 0 | Prior-art | Read `state/ledger.jsonl`; surface a prior expand of this idea. |
| 1 | Read | The idea + its venture record (if any). What space is this really in? |
| 2 | Pick angles | Which of the 7 angle-loops fit this idea? (Not all will.) |
| 3 | Run / queue | Run the fitting angle-loops (or hand the user the list to run). Each returns its play. |
| 4 | Synthesize | The biggest COHERENT vision (the empire version — how the angles combine) + the single highest-leverage next expansion. |

## HITL
After Step 4, present the big vision + the angles' plays + the one highest-leverage move. User: `pursue <angle/vision>` / `park` / `just the core` (stay small).

## Output (lean)
1. **The empire version** in 2-3 lines (how big this could be).
2. **The angles that hit** — a short table (angle · the play · the upside).
3. **Highest-leverage next expansion** (1 line).
4. **One line:** pursue what?

Tables over prose. No essay.

## Persist (compact)
- **Report** -> `projects/assay/expand/runs/<YYYY-MM-DD>-<slug>.md`.
- **Ledger** -> `.claude/skills/expand/state/ledger.jsonl` — one line (idea, angles_run, empire_vision, top_move, report path).
- **Venture record** -> `projects/assay/ventures/<slug>.md` — add an "Expansion" note (the ceiling + the top move); refresh ventures INDEX.
UTF-8, no BOM.

## Render the result (final step, optional)
After presenting, render the angles + top move as a live, question-able board via [[../render/steps/step-serve-and-watch]]: pass this loop's output through the adapter [[../render/adapters/INDEX]] (`to_items`), then serve-and-watch. Standalone and modular — the loop still runs headless without it. Plain vocabulary, no em dashes, fit as a tag only are baked into the adapter.

## Chain
`/deep-dive` (GO) -> **`/expand` (how big?)** -> pick expansions -> the adversarial loops test them. Or standalone anytime.
