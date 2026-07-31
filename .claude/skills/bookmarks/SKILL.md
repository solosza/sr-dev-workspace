---
name: bookmarks
description: Idea-hunter (source family). Mine the operator's own saved reels/links/notes for business ideas. Feeds /assay. Lean output, saved.
---

# Bookmarks Hunter

**Purpose:** Answer *"what business ideas are hiding in what I've already saved?"* — your saves are a curated interest/pain signal you already trust. Part of the `/source` family.
**Input:** optional seed to filter. **Output:** ranked personal-signal idea candidates → `/assay`.

## Cross-cutting rules
- **LEAN OUTPUT** ([[loop-output-lean]]). **Standalone & modular.** **Every scan saved.**
- **Dedup** against the assay ledger (match on meaning).
- **Capture new angles.** Spot an idea-source method with no hunter? Append to `projects/assay/loop-candidates.jsonl`.

## Steps
| # | Step | Do |
|---|------|-----|
| 1 | Gather saves | Read the operator's saved signal — bookmarked links/reels/notes; use the X bookmark scanner (`kernel:scan-bookmarks`) if available. Filter to the seed if one is given. |
| 2 | Extract ideas | What recurring interest / pain / opportunity do the saves point at? Turn clusters into candidate ideas. |
| 3 | Normalize | Each idea one line (value · who-pays · mechanism). |
| 4 | Dedup + rank | Drop already-assayed; rank by how often the theme recurs in the saves (recurrence = real interest). |

## Output (lean)
1. **Top ideas from your saves** — table (idea · what saves point at it).
2. **Dropped as already-explored** (one line).
3. One line: send which to `/assay`?

## Persist (compact)
- **Report** -> `projects/assay/source/runs/<YYYY-MM-DD>-bookmarks.md`.
- **Ledger** -> `.claude/skills/bookmarks/state/ledger.jsonl` (seed, clusters, ideas[], report path).

## Chain
`/source` -> **`/bookmarks`** -> ideas -> `/assay`.
