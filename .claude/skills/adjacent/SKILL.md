---
name: adjacent
description: Expansion angle-loop. Adjacent VENTURES in the same space (new businesses to own), fed back to /assay. Think bigger, generative. Lean output, saved.
---

# Adjacent Angle-Loop

**Purpose:** For an idea, answer *"what OTHER businesses live next to this one that I could also own?"* — maps adjacent territory, feeds the best back to `/assay`. Part of the `/expand` family.
**Philosophy:** generative — dream the whole territory, not one business; the adversarial loops (assay+) vet each candidate.

## Cross-cutting rules
- **THINK BIGGER.** Not one business — the SPACE. Same customer / same capability / same data / same channel = adjacent ventures you could also own. Map the empire's territory.
- **LEAN OUTPUT** ([[loop-output-lean]]). **Standalone & modular.** **Generative, not kill-by-default.** **Every run saved.**
- **Capture new angles.** Spot a monetization/expansion path with NO existing angle-loop? Append it to `projects/assay/loop-candidates.jsonl` — `/sharpen` promotes recurring ones into new loops.

## Steps
| # | Step | Do |
|---|------|-----|
| 1 | The shared assets | What this venture owns that ports: customer relationship, capability, data, channel, brand. |
| 2 | Adjacent ventures | New businesses reachable off each shared asset (same customer needs X; same capability does Y). |
| 3 | Rank | By reuse of the shared asset x size x speed. |
| 4 | Hand off | The top 1-3 -> run each through `/assay` as its own venture. |

## Output (lean)
1. **The shared assets** (what ports).
2. **Adjacent ventures** — a short ranked list (venture · which asset it reuses).
3. **Top 1-3 to assay.** One line: send which to `/assay`?

## Persist (compact)
- **Report** -> `projects/assay/adjacent/runs/<YYYY-MM-DD>-<slug>.md`.
- **Ledger** -> `.claude/skills/adjacent/state/ledger.jsonl` (idea, shared_assets, adjacent[], top[], report path).

## Chain
`/expand` -> **`/adjacent`** -> feeds `/assay` (each candidate becomes its own venture run).
