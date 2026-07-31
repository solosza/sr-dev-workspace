---
name: pain
description: Idea-hunter (source family). From a seed space, mine real pain (complaints, workarounds, bad solutions) into business ideas. Feeds /assay. Lean output, saved.
---

# Pain Hunter

**Purpose:** From a seed space, answer *"what are people already suffering / paying badly to solve?"* — real pain = real demand. Part of the `/source` family.
**Input:** a seed theme/space. **Output:** ranked pain-driven idea candidates → `/assay`.

## Cross-cutting rules
- **LEAN OUTPUT** ([[loop-output-lean]]). **Standalone & modular.** **Every scan saved.**
- **Dedup** against the assay ledger (match on meaning).
- **Capture new angles.** Spot an idea-source method with no hunter? Append to `projects/assay/loop-candidates.jsonl`.

## Steps
| # | Step | Do |
|---|------|-----|
| 1 | Mine pain | Web-research the seed for complaints, "I'd pay for X", workarounds, 1-star reviews of incumbents, recurring forum gripes (Reddit, reviews, communities). Cite. |
| 2 | Rank pain | Strongest signals: frequent + urgent + already-being-paid-for-badly. |
| 3 | Idea per pain | The business that solves the top pains; normalize (value · who-pays · mechanism). |
| 4 | Dedup + rank | Drop already-assayed; rank by pain intensity × willingness-to-pay evidence. |

## Output (lean)
1. **Top idea candidates** — table (idea · the pain · the evidence).
2. **Dropped as already-explored** (one line).
3. One line: send which to `/assay`?

## Persist (compact)
- **Report** -> `projects/assay/source/runs/<YYYY-MM-DD>-pain-<seed>.md`.
- **Ledger** -> `.claude/skills/pain/state/ledger.jsonl` (seed, pains, ideas[], report path).

## Chain
`/source` -> **`/pain`** -> ideas -> `/assay`.
