# /source

Surface fresh ideas worth assaying — the front of the pipeline (feeds `/assay`).

## Usage

```
/source [theme or niche]
```

| Argument | Purpose | Example |
|----------|---------|---------|
| `[theme]` | Optional focus; omit for a broad scan | `/source AI local-services` |

## What It Does

Scans sources (trends, web, communities, pain-points, your bookmarks), extracts candidate ideas, dedups them against the assay ledger (drops already-explored), ranks by signal, and hands the top few to `/assay`. Output = a short ranked idea queue, never a long doc. Every scan saved (report + ledger).

## Skill Reference

-> `.claude/skills/source/`
