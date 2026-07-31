---
name: assets
description: Idea-hunter (source family). From a seed space, reverse from YOUR unique assets to ideas only you can build/own. Feeds /assay. Lean output, saved.
---

# Assets Hunter

**Purpose:** From a seed space, answer *"what could only WE build here, given what we already own?"* — the highest-conviction source (built-in moat). Part of the `/source` family.
**Input:** a seed theme/space. **Output:** ranked fit-to-me idea candidates → `/assay`.

## Cross-cutting rules
- **LEAN OUTPUT** ([[loop-output-lean]]). **Standalone & modular.** **Every scan saved.**
- **Dedup** against the assay ledger (match on meaning).
- **Capture new angles.** Spot an idea-source method with no hunter? Append to `projects/assay/loop-candidates.jsonl`.

## Steps
| # | Step | Do |
|---|------|-----|
| 1 | Inventory assets | The operator's unfair advantages: the kernel/governance, owned data, skills, channels, prior builds, relationships. |
| 2 | Apply to seed | For each asset: what business in the seed space does it uniquely unlock or defend (that a random operator couldn't)? |
| 3 | Normalize | Each idea one line (value · who-pays · mechanism) + which asset is the moat. |
| 4 | Dedup + rank | Drop already-assayed; rank by moat strength × reuse of existing builds. |

## Output (lean)
1. **Top fit-to-me ideas** — table (idea · the asset/moat · why only you).
2. **Dropped as already-explored** (one line).
3. One line: send which to `/assay`?

## Persist (compact)
- **Report** -> `projects/assay/source/runs/<YYYY-MM-DD>-assets-<seed>.md`.
- **Ledger** -> `.claude/skills/assets/state/ledger.jsonl` (seed, assets, ideas[], report path).

## Chain
`/source` -> **`/assets`** -> ideas -> `/assay`.
