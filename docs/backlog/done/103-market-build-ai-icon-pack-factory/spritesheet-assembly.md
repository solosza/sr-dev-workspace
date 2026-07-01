# Spritesheet Assembly

## Status
NEW

## Location
`D:\my_ai_projects\ai-icon-pack-factory\src\assemble.py`

## What It Does
Takes all processed 32x32 PNGs and assembles them into a spritesheet plus individual PNG exports. Outputs the spritesheet PNG, a JSON metadata file mapping icon names to spritesheet coordinates, and the individual PNGs in a flat folder ready for distribution.

## Input
```
output/processed/{category}/*.png   (32x32 transparent PNGs)
```

## Output
```
output/final/{category}/
  spritesheet.png            (all icons in a grid)
  spritesheet.json           (name → {x, y, w, h} coordinate map)
  icons/                     (individual PNGs, flat)
    stone_floor.png
    water_tile.png
    ...
```

## Spritesheet Layout
- Grid: auto-calculate columns to keep aspect ratio near square
  - Formula: `cols = ceil(sqrt(count))`, `rows = ceil(count / cols)`
- Cell size: 32x32 (matches icon size exactly — no padding in spritesheet)
- Background: transparent
- File format: PNG-32 (RGBA)

## Metadata Format
```json
{
  "category": "dungeon-terrain",
  "cell_size": 32,
  "cols": 8,
  "rows": 7,
  "icons": {
    "stone_floor": { "x": 0, "y": 0, "w": 32, "h": 32, "index": 0 },
    "water_tile":  { "x": 32, "y": 0, "w": 32, "h": 32, "index": 1 }
  }
}
```

## Implementation
- Use Pillow (`PIL.Image`) for all image operations — no external tools needed
- Assembly loop:
  1. Load all processed PNGs, sort by concept name (alphabetical)
  2. Create blank RGBA canvas: `cols * 32` × `rows * 32`
  3. Paste each icon at its grid position
  4. Save spritesheet.png
  5. Write spritesheet.json
  6. Copy individual PNGs to `icons/` (rename to concept name, no `_{n}` suffix)

## Individual PNG Naming
- Rename from `stone_floor_3.png` → `stone_floor.png` (drop the candidate index)
- Concept name: slugify (lowercase, spaces to underscores, no special chars)

## Dependencies
- `Pillow` Python library (pip install Pillow)
- Output from image-processing step (`output/processed/{category}/`)
- No API keys required
