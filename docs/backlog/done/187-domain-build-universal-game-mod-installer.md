# Universal Game Mod Installer Harness

## Status
Open

## Priority
Medium — high market appeal as a Claude Code showcase, proof of concept already validated with FM24

## Summary
Research the feasibility and landscape of a universal game mod installer powered by Claude Code + Playwright MCP. Investigate existing mod managers (Vortex, MO2, Thunderstore, r2modman), assess whether a Claude Code harness adds value over existing tools, determine if a UI is needed or if CLI is sufficient, and evaluate which games/mod ecosystems are best suited. The FM24 manual setup session is the proof of concept — this research determines whether automating that workflow as a universal harness is worth building.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[187-domain-build-universal-game-mod-installer/game-detection]] | Detect installed games and their mod folder locations |
| [[187-domain-build-universal-game-mod-installer/mod-site-registry]] | Registry of mod sites per game with scraping/navigation patterns |
| [[187-domain-build-universal-game-mod-installer/download-engine]] | Download, extract, and place files in correct folders |
| [[187-domain-build-universal-game-mod-installer/conflict-resolution]] | Handle mod conflicts, load order, and compatibility |
| [[187-domain-build-universal-game-mod-installer/verification]] | Verify installation and report results |

## Architecture

```
User: /mod-install fm24 --all
  ↓
Game Detection → find install path + mod folders
  ↓
Mod Site Registry → lookup best mod sites for game
  ↓
Playwright MCP → navigate sites, find downloads, authenticate
  ↓
Download Engine → download, extract, place in correct folders
  ↓
Conflict Resolution → check for overwrites, load order
  ↓
Verification → confirm files exist, report summary
```

## Requirements
- Detect game installations (Steam, Epic, GOG, standalone)
- Support at minimum: FM24, Skyrim, Cities Skylines, Stardew Valley
- Navigate community mod sites via Playwright MCP (sortitoutsi, Nexus Mods, Steam Workshop, CurseForge)
- Handle authentication where required (sortitoutsi login proven in FM24 POC)
- Download and extract archives (zip, rar, 7z) to correct mod folders
- Handle mod conflicts and load order where applicable
- Verify installation and produce summary report
- Extensible — adding a new game should be config-driven, not code changes

## References
- FM24 manual setup session (2026-07-06) — proof of concept
- sortitoutsi.net — FM24 mod site (login + download proven via Playwright)
- Nexus Mods — largest general mod repository
- Steam Workshop — integrated mod distribution
- Harness design pattern: `docs/harness-design-pattern/`

## Task Builder Input
- **Deliverable:** Research report with feasibility assessment, competitive landscape, architecture recommendation, and go/no-go decision
- **Location:** `subproject:universal-mod-installer-research`
- **Scope:** RESEARCH
- **Constraints:** Must evaluate existing mod managers honestly. Must answer: does Claude Code add value here or is this a solved problem? Should include UI vs CLI analysis, game ecosystem prioritization, and monetization potential.
