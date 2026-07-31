---
name: source
description: Front-of-pipeline loop. Surface fresh ideas worth assaying, deduped against past runs, ranked by signal. Feeds /assay. Lean output, every scan saved.
---

# Source / Scan Loop

**Purpose:** Answer *"what ideas are even worth putting through the pipeline right now?"* — the front of the funnel that feeds `/assay`.
**Feeds** `/assay`.
**Philosophy:** wide, signal-ranked, dedup-aware. Generous on generation (killing happens in assay), strict on not re-surfacing what's already been explored.

## Cross-cutting rules
- **LEAN OUTPUT.** A short ranked queue, never a long doc. See [[loop-output-lean]].
- **Standalone & modular.** Runs alone (a broad or themed scan), OR as a sub-step called by another loop that needs fresh candidates. Returns its ranked idea queue cleanly so a caller (e.g. `/assay`) can consume it.
- **Dedup against history.** Drop ideas already in the assay ledger (match on meaning) — don't re-surface explored ground.
- **Never acts.** Produces an idea queue; the human (or `/assay`) picks what to run.
- **Every scan saved** (see Persist).

## Steps

| # | Step | Do |
|---|------|-----|
| 1 | Scan | Pull candidate ideas from sources: trends, web search, communities (Reddit/X/forums), recurring pain-points, the user's bookmarks/notes. Optional theme narrows it. |
| 2 | Extract | Normalize each to a one-line idea (value · who-pays · mechanism). |
| 3 | Dedup | Drop any that match an existing assay-ledger idea by MEANING (already explored). Note dupes dropped. |
| 4 | Rank | Score the fresh ones by signal (demand evidence, momentum, fit-to-operator, why-now). |
| 5 | Hand off | Present the top few + offer to run the top pick through `/assay`. |

## Research
Use `WebSearch`/`WebFetch` for Step 1 (trends, pain-points, what's rising). Cite sources. Also read `.claude/skills/assay/state/ledger.jsonl` for the dedup.

## Output (lean)
1. **Top ideas** — a short ranked table (idea one-line · signal · why-now).
2. **Dropped as already-explored** — one line (count + which).
3. **One line:** which to send to `/assay`?

Table over prose. No essay.

## Persist (compact, mandatory)
- **Report** -> `projects/assay/source/runs/<YYYY-MM-DD>-<theme-or-scan>.md` — the ranked queue.
- **Ledger** -> `.claude/skills/source/state/ledger.jsonl` — one JSON line (ts, theme, candidates, dropped_dupes, top[], report path).
UTF-8, no BOM.

## Chain
**`/source` (find ideas)** -> `/assay` (which is worth it) -> competition -> deep-dive -> ...
