# Packaging

## Status
NEW

## Location
`D:\my_ai_projects\ai-icon-pack-factory\src\package.py`

## What It Does
Generates all human-facing collateral for the itch.io listing: README, LICENSE, itch.io description, preview image, and a metadata JSON. Uses Claude to write the text content. Assembles the final distributable ZIP.

## Input
```
output/final/{category}/
  spritesheet.png
  spritesheet.json
  icons/*.png
category_config.json   (category name, description, concepts list)
```

## Output
```
output/package/{category}/
  README.md
  LICENSE.txt           (CC0 or custom — configurable)
  preview.png           (600x450 itch.io cover image)
  metadata.json         (itch.io listing fields)
  {category}-icons.zip  (distributable: icons/ + spritesheet + README + LICENSE)
```

## Claude-Generated Content

### README.md
Prompt: "Write a README for a game icon pack called '{category_title}'. It contains {count} icons: {concept_list}. Icons are 32x32 PNG with transparent background. Include: what's included, how to use (reference spritesheet.json for coordinates), license, and attribution requirements."

### itch.io Description (stored in metadata.json)
Prompt: "Write an itch.io product description for a game icon pack: '{category_title}', {count} icons, 32x32 PNG, transparent background, flat style, black outline. Concepts: {concept_list}. Make it appealing to indie game developers and tabletop RPG builders. Include bullet points for features."

### Tags (stored in metadata.json)
Prompt: "Generate 10 itch.io tags for this icon pack: {category_title}, {concept_list}. Tags should be short (1-2 words), relevant to game developers searching itch.io. Return JSON array only."

## Preview Image Generation
- Tile the first 16 icons in a 4x4 grid on a dark background (#1a1a2e)
- Scale each icon 3x (32px → 96px) for visibility
- Add category title text (white, 24pt) at bottom
- Output: 600x450 PNG
- Implementation: Pillow only — no external tools

## Metadata Format
```json
{
  "category": "dungeon-terrain",
  "title": "Dungeon Terrain Icon Pack — 50 32px Game Icons",
  "description": "...",
  "price_usd": 4.99,
  "tags": ["game-assets", "icons", "dungeon", "rpg", "tileset", "32px"],
  "kind": "Other",
  "classification": "game_mod",
  "license": "CC0"
}
```

## ZIP Assembly
- Include: `icons/`, `spritesheet.png`, `spritesheet.json`, `README.md`, `LICENSE.txt`
- Exclude: `preview.png`, `metadata.json` (itch.io listing files, not user-facing)
- Naming: `{category}-icons-v1.0.zip`

## Dependencies
- `anthropic` Python SDK
- `Pillow` for preview image
- `ANTHROPIC_API_KEY` environment variable
- Output from spritesheet-assembly step
- `category_config.json` for category metadata
