# D&D Engine QA

## Status
NEW

## Location
`D:\my_ai_projects\ai-icon-pack-factory\src\qa.py`

## What It Does
Loads the assembled icons into the D&D game engine grid and takes a Playwright screenshot to verify they render correctly at 32px. Asserts that icons are visible (non-empty pixels) and not broken (no all-white or all-transparent tiles). Acts as the final QA gate before the publishing step.

## D&D Engine Reference
- Repo: `D:\my_ai_projects\project_test_repos\dnd-game-engine-test`
- The engine must have a test mode that accepts a spritesheet and renders it in the grid
- Test mode URL: `file:///...dnd-game-engine-test/index.html?test=icons&sheet={path}`
- If test mode does not exist, this step writes a minimal test harness HTML alongside the repo

## Test Harness (if engine test mode missing)
```html
<!-- qa-render.html (written to dnd-game-engine-test/) -->
<!-- Loads spritesheet, renders all icons in a grid, exposes window.QA_READY -->
```
Written by `qa.py` if `dnd-game-engine-test/qa-render.html` does not exist.

## QA Steps

### 1. Start local server
```bash
python -m http.server 8765 --directory "D:\my_ai_projects\project_test_repos\dnd-game-engine-test"
```

### 2. Navigate to test page
- URL: `http://localhost:8765/qa-render.html?sheet=../../ai-icon-pack-factory/output/final/{category}/spritesheet.png&meta=spritesheet.json`

### 3. Wait for render
- Wait for `window.QA_READY === true` (injected by test harness when all icons load)
- Timeout: 10 seconds

### 4. Take screenshot
- Full page screenshot → `output/qa/{category}/render.png`

### 5. Assert icon visibility
- For each icon in `spritesheet.json`: sample center pixel of its tile
- Assert: not (r=0, g=0, b=0, a=0) — not fully transparent
- Assert: not (r=255, g=255, b=255, a=255) — not fully white (broken)
- Pass threshold: 90% of icons must pass both assertions

### 6. Stop server

## Output
```json
{
  "category": "dungeon-terrain",
  "passed": true,
  "total_icons": 50,
  "visible": 49,
  "broken": 1,
  "pass_rate": 0.98,
  "screenshot": "output/qa/dungeon-terrain/render.png",
  "failures": ["pit_trap"]
}
```
Written to: `output/qa/{category}/qa-result.json`

## Pass/Fail Behavior
- If `passed: true`: pipeline continues to publish step
- If `passed: false` (pass_rate < 0.90): pipeline stops, writes qa-result.json, reports failure to console
- Broken icons are logged but do not block if pass_rate >= 0.90 (tolerance for edge cases)

## Dependencies
- Playwright MCP for screenshot and pixel sampling
- `mcp__playwright__browser_navigate`, `mcp__playwright__browser_take_screenshot`, `mcp__playwright__browser_evaluate`
- Python `http.server` for local file serving
- D&D engine at `D:\my_ai_projects\project_test_repos\dnd-game-engine-test`
- Output from spritesheet-assembly step (`spritesheet.png`, `spritesheet.json`)
