# Claude Vision Curation

## Status
NEW

## Location
`D:\my_ai_projects\ai-icon-pack-factory\src\curate.py`

## What It Does
Pipes generated PNG candidates through Claude's vision API to score each one on three axes. Outputs a ranked JSON file. The top N (default 50 total across all concepts) are selected for processing. A human can inspect the ranked list and override selections before the pipeline continues — but this step is not required.

## Scoring Criteria
Each icon scored 1-10 on:
1. **Legibility at 32px** — does the concept read clearly at small size? (no fine detail that disappears)
2. **Style consistency** — matches the flat/outlined game icon style (not photorealistic, not too detailed)
3. **Distinctiveness** — clearly distinguishable from other icons in the same category

Final score = weighted average (legibility: 40%, consistency: 35%, distinctiveness: 25%)

## Input
```
output/raw/{category}/manifest.json   (concept→file mapping)
output/raw/{category}/*.png
```

## Output
```json
{
  "category": "dungeon-terrain",
  "scored": [
    {
      "file": "stone_floor_3.png",
      "concept": "stone floor",
      "scores": { "legibility": 8, "consistency": 9, "distinctiveness": 7 },
      "final": 8.15,
      "selected": true
    }
  ],
  "selected_count": 50,
  "rejected_count": 263
}
```

## Implementation
- Use Claude API with vision (claude-sonnet-4-6 or claude-opus-4-6)
- Batch images: send 4-8 per API call (multi-image prompt) to reduce API calls
- Prompt template: "You are evaluating game icons. Score each image 1-10 for: legibility at 32px, flat style consistency, distinctiveness. Return JSON only."
- Human override: if `curation_overrides.json` exists in output dir, apply before selecting

## Dependencies
- `anthropic` Python SDK
- `ANTHROPIC_API_KEY` environment variable
- Output from scenario-api step
