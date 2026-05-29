# itch.io Publisher

## Status
NEW

## Location
`D:\my_ai_projects\ai-icon-pack-factory\src\publish.py`

## What It Does
Automates the itch.io upload and listing creation via Playwright MCP. Reads the packaged metadata and ZIP, navigates to itch.io dashboard, creates a new project, fills all fields, uploads the ZIP and preview image, sets price and tags, and publishes.

## Input
```
output/package/{category}/
  metadata.json          (title, description, price, tags, license)
  preview.png            (600x450 cover image)
  {category}-icons.zip   (distributable)
```

## itch.io Flow

### Step 1: Login
- Navigate to `https://itch.io/login`
- Fill credentials from env vars: `ITCHIO_USERNAME`, `ITCHIO_PASSWORD`
- Handle 2FA if present (pause and prompt user if TOTP required — only manual step)

### Step 2: Create New Project
- Navigate to `https://itch.io/game/new`
- Fill: Title, Kind (= "Other"), Classification (= "game_mod")

### Step 3: Fill Listing
- Description: paste from `metadata.json.description`
- Tags: add each tag from `metadata.json.tags`
- Cover image: upload `preview.png`

### Step 4: Upload File
- Click "Upload files"
- Upload `{category}-icons.zip`
- Set display name to "Icon Pack ZIP"

### Step 5: Pricing
- Set to paid: `metadata.json.price_usd`
- Enable "Also allow free downloads" = false (paid only)

### Step 6: Publish
- Set visibility to "Public"
- Click "Save & view page"
- Capture published URL from redirect

## Output
```json
{
  "published": true,
  "url": "https://isagawa.itch.io/{category}-icon-pack",
  "timestamp": "2026-05-29T...",
  "category": "dungeon-terrain"
}
```
Written to: `output/package/{category}/publish-result.json`

## Implementation Notes
- Use Playwright MCP browser tools (`mcp__playwright__*`)
- After each major step: take screenshot to log/screenshots/ for audit trail
- If any step fails: write error to publish-result.json with `"published": false` and stop
- Do NOT retry publish steps automatically — publishing is not idempotent (could create duplicates)
- Selector strategy: prefer `aria-label` and `name` attributes over CSS class selectors (itch.io updates classes frequently)

## Environment Variables
- `ITCHIO_USERNAME` — itch.io account username
- `ITCHIO_PASSWORD` — itch.io account password
- `ITCHIO_2FA_SECRET` — TOTP secret (optional; if absent, pipeline pauses for manual 2FA)

## Dependencies
- Playwright MCP (already configured in workspace)
- Output from packaging step
- `ITCHIO_USERNAME`, `ITCHIO_PASSWORD` environment variables
