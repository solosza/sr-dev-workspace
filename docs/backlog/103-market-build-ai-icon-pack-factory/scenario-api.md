# Scenario.gg API Integration

## Status
NEW

## Location
`D:\my_ai_projects\ai-icon-pack-factory\src\generate.py`

## What It Does
Calls the Scenario.gg API to generate a batch of icon candidates for a given category. Takes a prompt template, a style model (trained or base), and a count, and returns PNG file paths.

## Input
```json
{
  "category": "dungeon-terrain",
  "prompt_template": "top-down view of {concept}, flat icon style, black outline, transparent background, 32x32 pixel grid, game asset",
  "concepts": ["stone floor", "water tile", "lava", "pit trap", "door", "chest"],
  "count_per_concept": 8,
  "model_id": "scenario-gg-model-id-or-base"
}
```

## Output
```
output/raw/{category}/{concept}_{n}.png   (300-500 files total)
output/raw/{category}/manifest.json       (concept→file mapping)
```

## API Notes
- Scenario.gg REST API: POST /v1/models/{modelId}/inferences
- Auth: Bearer token from env var `SCENARIO_API_KEY`
- Free tier: 100 generations/month; paid: unlimited
- Fallback: Stability AI API (same interface shape, swap base URL + key)
- Response includes image URLs; download and save locally
- Retry on 429 (rate limit) with exponential backoff

## Dependencies
- `requests` or `httpx` for API calls
- `SCENARIO_API_KEY` environment variable
- `category_config.json` — maps category names to concept lists and prompt templates
