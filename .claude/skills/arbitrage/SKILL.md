---
name: arbitrage
description: Idea-hunter (source family). From a seed space, find proven-elsewhere models missing here (transplant). Feeds /assay. Lean output, saved.
---

# Arbitrage Hunter

**Purpose:** From a seed space, answer *"what works in another market/geo/vertical that's missing here?"* — proven-elsewhere = lower risk. Part of the `/source` family.
**Input:** a seed theme/space. **Output:** ranked transplant idea candidates → `/assay`.

## Cross-cutting rules
- **LEAN OUTPUT** ([[loop-output-lean]]). **Standalone & modular.** **Every scan saved.**
- **Dedup** against the assay ledger (match on meaning).
- **Capture new angles.** Spot an idea-source method with no hunter? Append to `projects/assay/loop-candidates.jsonl`.

## Steps
| # | Step | Do |
|---|------|-----|
| 1 | Find the proof | Web-research models/tools/offers thriving in another geography, vertical, or era relevant to the seed. Cite. |
| 2 | Spot the gap | Where is it absent or weak *here*, and why (timing, awareness, no local operator)? |
| 3 | Transplant idea | The "bring X to Y" business; normalize (value · who-pays · mechanism). |
| 4 | Dedup + rank | Drop already-assayed; rank by proof strength × transplant feasibility. |

## Output (lean)
1. **Top transplant ideas** — table (idea · proven where · the local gap).
2. **Dropped as already-explored** (one line).
3. One line: send which to `/assay`?

## Persist (compact)
- **Report** -> `projects/assay/source/runs/<YYYY-MM-DD>-arbitrage-<seed>.md`.
- **Ledger** -> `.claude/skills/arbitrage/state/ledger.jsonl` (seed, proofs, ideas[], report path).

## Chain
`/source` -> **`/arbitrage`** -> ideas -> `/assay`.
