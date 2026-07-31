---
name: trends
description: Idea-hunter (source family). From a seed space, find why-now catalysts and the business ideas they newly enable. Feeds /assay. Lean output, saved.
---

# Trends Hunter

**Purpose:** From a seed space, answer *"what just became possible, and what business does that enable?"* Part of the `/source` family.
**Input:** a seed theme/space. **Output:** ranked trend-driven idea candidates → `/assay`.

## Cross-cutting rules
- **LEAN OUTPUT** ([[loop-output-lean]]). **Standalone & modular** (alone or called by `/source`). **Every scan saved.**
- **Dedup** against `.claude/skills/assay/state/ledger.jsonl` (match on meaning) — don't re-surface explored ideas.
- **Capture new angles.** Spot an idea-source method with no hunter? Append to `projects/assay/loop-candidates.jsonl`.

## Steps
| # | Step | Do |
|---|------|-----|
| 1 | Catalysts | Web-research the seed for why-now shifts: new tools/models, platform changes, regulation, cost curves, cultural shifts. Cite + date. |
| 2 | Enablement | For each catalyst: what business is newly possible *because* of it (that wasn't 2 years ago)? |
| 3 | Normalize | Each idea as one line: value · who-pays · mechanism. |
| 4 | Dedup + rank | Drop already-assayed; rank by catalyst strength × freshness. |

## Output (lean)
1. **Top idea candidates** — short table (idea · the catalyst · why-now).
2. **Dropped as already-explored** (one line).
3. One line: send which to `/assay`?

## Persist (compact)
- **Report** -> `projects/assay/source/runs/<YYYY-MM-DD>-trends-<seed>.md`.
- **Ledger** -> `.claude/skills/trends/state/ledger.jsonl` (seed, catalysts, ideas[], report path).

## Chain
`/source` -> **`/trends`** -> ideas -> `/assay`.
