# Image Processing

## Status
NEW

## Location
`D:\my_ai_projects\ai-icon-pack-factory\src\process.py`

## What It Does
Takes the selected PNG candidates from the curation step and prepares them for distribution: removes backgrounds with rembg, normalizes the palette to a consistent set of colors, cleans up edges, and aligns each icon to the 32x32 grid.

## Input
```
output/raw/{category}/*.png         (selected candidates only — from curation ranked JSON)
output/raw/{category}/curation.json (selected: true entries)
```

## Output
```
output/processed/{category}/{concept}_{n}.png   (transparent background, normalized palette, 32x32)
```

## Steps

### 1. Background Removal (rembg)
- Run `rembg remove` on each input PNG
- Output: RGBA PNG with transparent background
- Model: default u2net (or u2netp for speed)

### 2. Palette Normalization (ImageMagick)
- Lock to a game-friendly palette (32 colors max)
- Command: `magick {input} -quantize transparent -colors 32 -remap {palette_file} {output}`
- Palette file: `config/palette.png` — ship a default 32-color game palette; user can override

### 3. Edge Cleanup (ImageMagick)
- Remove fringe pixels from background removal artifacts
- Command: `magick {input} -alpha on -fuzz 5% -trim +repage {output}`

### 4. Grid Alignment (ImageMagick)
- Resize and center on exact 32x32 canvas
- Command: `magick {input} -resize 28x28 -gravity center -extent 32x32 -background none {output}`
- 28x28 content area leaves 2px padding on each side

## Implementation
- Process in sequence per selected icon (not batched — rembg loads model once, reuses)
- Log failures to `output/processed/{category}/errors.log`
- Skip on error, continue to next (don't abort pipeline)

## Dependencies
- `rembg` Python library (pip install rembg)
- ImageMagick (system install — `magick` on PATH)
- `REMBG_MODEL` env var (optional, default: u2net)
- Output from curation step (`curation.json` with `selected: true` entries)

## Config
`config/processing.json`:
```json
{
  "canvas_size": 32,
  "content_size": 28,
  "max_palette_colors": 32,
  "fuzz_pct": 5,
  "palette_file": "config/palette.png"
}
```
