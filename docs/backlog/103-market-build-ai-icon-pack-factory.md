# Build AI Icon Pack Factory

## Status
Open

## Priority
High — fully autonomous end-to-end: category list in, published itch.io product out. Zero manual steps except a quick visual scan of the Claude-curated candidates. Builds directly on the gap confirmed in backlog 102.

## Summary
An AI-powered pipeline that takes a category list (e.g., "Dungeon Terrain", "Status Conditions") and produces a published itch.io icon pack with no human steps except an optional final visual review. The pipeline generates 300-500 candidates via Scenario.gg API, uses Claude vision to score and select the best 50, removes backgrounds, normalizes palette, assembles a spritesheet, writes all packaging collateral, and publishes via Playwright MCP. The D&D game engine at `dnd-game-engine-test` serves as built-in QA — icons are loaded into the grid and screenshotted to verify 32px rendering before publication.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[103-market-build-ai-icon-pack-factory/scenario-api]] | Scenario.gg API integration — generate 300-500 candidates per category |
| [[103-market-build-ai-icon-pack-factory/claude-vision-curation]] | Claude vision scoring — legibility, style consistency, distinctiveness at 32px |
| [[103-market-build-ai-icon-pack-factory/image-processing]] | rembg background removal + ImageMagick palette normalization |
| [[103-market-build-ai-icon-pack-factory/spritesheet-assembly]] | Pillow/TexturePacker spritesheet + individual PNG export |
| [[103-market-build-ai-icon-pack-factory/packaging]] | README, license, preview image, metadata generation |
| [[103-market-build-ai-icon-pack-factory/itchio-publisher]] | Playwright MCP automation for itch.io upload + listing |
| [[103-market-build-ai-icon-pack-factory/dnd-engine-qa]] | D&D engine grid rendering QA — screenshot verification at 32px |

## Architecture

```
Input: category_list.json (e.g., ["dungeon-terrain", "status-conditions"])
         ↓
[1] Scenario.gg API → 300-500 candidate PNGs per category
         ↓
[2] Claude vision → score each candidate (legibility, consistency, distinctiveness)
         → select top 50, flag rejects
         ↓ (optional human review of ranked list)
[3] rembg → transparent background
[4] ImageMagick → palette lock, edge cleanup, grid alignment
         ↓
[5] Pillow/TexturePacker → individual PNGs + spritesheet + metadata JSON
         ↓
[6] Claude → write README, license, itch.io description, tags
         ↓
[7] D&D engine QA → load icons into grid, Playwright screenshot, assert 32px render
         ↓
[8] Playwright MCP → itch.io upload form, set price/tags, publish
         ↓
Output: Published itch.io page + attested bundle
```

## Requirements
- Scenario.gg API key required (or Stability AI as fallback)
- rembg, ImageMagick, Pillow must be installed in pipeline env
- Playwright MCP must be configured (already available in workspace)
- D&D game engine at `dnd-game-engine-test` must have an icon-loading test mode
- Output: published itch.io page, spritesheet PNG, individual PNGs, metadata JSON
- Curation step: Claude vision scores candidates; human can override before processing continues but is not required

## References
- D&D game engine: `D:\my_ai_projects\project_test_repos\dnd-game-engine-test`
- Research report: `projects/custom-game-emoji-research/research-report.md`
- Gap analysis: `projects/custom-game-emoji-research/02-gap-analysis.md`
- Scenario.gg API docs: https://docs.scenario.gg
- Backlog 102: `docs/backlog/done/102-market-research-custom-game-emoji-market.md`

## Task Builder Input
- **Deliverable:** Runnable icon pack factory — `python factory.py --category dungeon-terrain` produces a published itch.io pack end-to-end
- **Location:** `new-repo:D:\my_ai_projects\ai-icon-pack-factory`
- **Scope:** BUILD
- **Constraints:** Requires Scenario.gg API key (free tier available); itch.io account required for publishing step; D&D engine must exist at dnd-game-engine-test path
