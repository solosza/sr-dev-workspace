# /source

Give it a seed; it provides business ideas. The idea-provision pipeline — the dispatcher over 6 idea-hunters that feeds `/assay`.

## Usage

```
/source [seed theme or space]
```

| Argument | Purpose | Example |
|----------|---------|---------|
| `[seed]` | A theme/space to hunt from. Omit for the ambient weekly drop. | `/source AI for local services` |

## What It Does

You give a seed and the loop takes it from there: runs 6 hunters — `/trends` (why-now), `/pain` (real demand), `/arbitrage` (proven-elsewhere), `/assets` (your moat), `/gaps` (underserved), `/bookmarks` (your saves) — then **cross-references** for ideas that hit multiple signals (pain × why-now × fit), dedups against the assay ledger, ranks, and **auto-runs the top 1-3 through `/assay`**. Output = a lean ranked idea-drop + verdicts. Runs on demand or on a weekly schedule.

## Skill Reference

-> `.claude/skills/source/`
