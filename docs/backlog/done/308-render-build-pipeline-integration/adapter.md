# Component: Output-to-Leaderboard Adapter

## Status
NEW

## Location
`.claude/skills/render/adapters/loop_to_leaderboard.py` (new) + a short spec `.claude/skills/render/adapters/INDEX.md`

## What it does
Converts a venture loop's decide/output structure into the leaderboard template's `items.json`, so no human hand-translation is needed. This is the glue that was done by hand this session.

## Input
A loop result object (assay/competition/deep-dive/etc.). Common shape from assay decide: a list of wedges, each with a name, a description, a recommendation, a fit level, and a rank/merit signal. The adapter reads whatever the loop emits and normalizes it.

## Output
`items.json` matching `templates/leaderboard/generate.py` data model exactly:
```
{ title, lead, recLegend, legend:{label,tags}, items:[{id, rank, name, desc, rec:{label,tone}, tag:{label,tone}}] }
```

## Rules baked in (not left to the caller)
- **Plain vocabulary**: translate every internal term to plain English (not "wedge/fit/GO-IF/assay"). Idea names too.
- **NO em dashes** anywhere in the produced strings.
- **Rank on merit**, not on fit. Order = opportunity strength.
- **Recommendation** per item: Build (tone c), Test first (tone b), Don't build (tone e).
- **Fit-to-you = a displayed tag only** (New for you / Partly yours / Your strength → tones a/b/c). Never affects order.
- `id` = stable slug from the item name (the annotate target).

## Dependencies
- Reads the loop output; writes items.json consumed by the render-step ([[render-step]]).

## Tests (L1/L2/L3)
- L1: adapter module + INDEX exist.
- L2: given a sample assay decide output, it emits schema-valid items.json (validate keys/tones).
- L3: run generate.py on the emitted items.json and confirm a page.html renders with the right rows, recs, and tags; assert zero em dashes and no jargon terms from a ban-list in the output strings.
