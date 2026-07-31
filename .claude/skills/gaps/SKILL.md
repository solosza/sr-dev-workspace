---
name: gaps
description: Idea-hunter (source family). From a seed space, find underserved segments + "everyone dies on X = X is the opportunity". Feeds /assay. Lean output, saved.
---

# Gaps Hunter

**Purpose:** From a seed space, answer *"who's underserved, and what failure point IS the opening?"* Part of the `/source` family.
**Input:** a seed theme/space. **Output:** ranked gap idea candidates → `/assay`.

## Cross-cutting rules
- **LEAN OUTPUT** ([[loop-output-lean]]). **Standalone & modular.** **Every scan saved.**
- **Dedup** against the assay ledger (match on meaning).
- **Capture new angles.** Spot an idea-source method with no hunter? Append to `projects/assay/loop-candidates.jsonl`.

## Steps
| # | Step | Do |
|---|------|-----|
| 1 | Underserved | Web-research + the assay ledger for segments/jobs nobody serves well in the seed space. |
| 2 | The failure point | What keeps killing ventures here (from the kill-patterns / anti-library)? "Everyone dies on X" → X is often the real opportunity (the un-easy part the crowd skips). |
| 3 | Idea per gap | The business that serves the underserved / owns the failure point; normalize. |
| 4 | Dedup + rank | Drop already-assayed; rank by gap size × how skippable the crowd finds it. |

## Output (lean)
1. **Top gap ideas** — table (idea · the gap / failure-point · why it's open).
2. **Dropped as already-explored** (one line).
3. One line: send which to `/assay`?

## Persist (compact)
- **Report** -> `projects/assay/source/runs/<YYYY-MM-DD>-gaps-<seed>.md`.
- **Ledger** -> `.claude/skills/gaps/state/ledger.jsonl` (seed, gaps, ideas[], report path).

## Chain
`/source` -> **`/gaps`** -> ideas -> `/assay`.
