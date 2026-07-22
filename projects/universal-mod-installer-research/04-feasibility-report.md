# Universal Game Mod Installer — Feasibility Report

## Decision: CONDITIONAL GO

Build as a **Claude Code skill** (not a harness, not a standalone app), starting with FM24. The unique value is real but narrow — this is a portfolio showcase with potential to grow, not a product play.

## Decision Matrix

| Question | Answer | Evidence |
|----------|--------|----------|
| Is the problem solved by existing tools? | **Partially.** Solved for Nexus/Thunderstore/CurseForge ecosystems. Unsolved for FM24, sports games, niche titles | 01-existing-mod-managers.md — 7 tools analyzed, none cover FM24 |
| Does Claude Code add unique value? | **Yes, for underserved games.** Natural language discovery, cross-site navigation, adaptive browser automation | 02-claude-code-value-add.md — 5 unique advantages identified |
| Is the target audience reachable? | **Small but real.** Claude Code users who also mod games. Portfolio audience (AI/dev community) is larger | 03-ui-vs-cli.md — gamers won't install a dev tool for mods |
| Is it worth the development effort? | **Yes, as a skill.** 1-2 backlogs. No as a harness (3-5 backlogs) or desktop app (5-10 backlogs) | Effort scales with architecture choice |
| What's the monetization path? | **Portfolio/showcase primary.** Direct monetization unlikely. Nexus Premium ($9/mo) shows mod convenience has value, but addressable market is small | 02-claude-code-value-add.md — market analysis |

## Recommendation: Build as Kernel Skill

### Architecture
```
/mod-install [game] [--mods list | --all | --category category]
  ↓
Game Config (JSON) → detect install path, mod folder structure
  ↓
Mod Registry (JSON) → sites, categories, recommended mods per game
  ↓
Playwright MCP → navigate sites, authenticate, download
  ↓
File Operations → extract, place, verify
  ↓
HTML Report → what was installed, where, verification status
```

### Why Skill, Not Harness
- No development lifecycle to govern — it's a runtime utility
- No need for hooks, protocol enforcement, or quality gates
- Fits naturally as a kernel command alongside existing skills
- Can reference game configs without needing domain-setup

### Interface
- **CLI-first** via Claude Code terminal (natural language commands)
- **HTML report** generated after installation (visual confirmation)
- No GUI, no desktop app, no web dashboard

## Game Priority

| Priority | Game | Rationale |
|----------|------|-----------|
| 1 | **FM24** | POC already proven. No existing mod manager. Underserved community. Clear mod categories (faces, logos, skins, kits, databases) |
| 2 | **Skyrim SE** | Largest modding community. Tests cross-site (Nexus + SKSE + ENB sites). High portfolio visibility |
| 3 | **Stardew Valley** | SMAPI ecosystem. Simpler mod structure. Cross-platform (tests Mac/Linux) |
| 4 | **Cities Skylines** | Steam Workshop + external mods. Tests Workshop integration |

### Why FM24 First
- **Proven:** The 2026-07-06 session successfully installed 6+ mods via Playwright
- **Uncontested:** No other tool does this — zero competition
- **Clear structure:** Mod categories map directly to folder paths (faces → `graphics/faces/`, skins → `skins/`)
- **Real user:** The developer is the user — immediate dogfooding

## Phase 1 Scope (Minimum Viable)

### Deliverables
1. **Game config schema** — JSON format for game detection, mod folder mapping, mod site registry
2. **FM24 game config** — first implementation of the schema
3. **Skill definition** — `/mod-install` command with natural language parsing
4. **Playwright automation** — site navigation, auth, download, extract, place
5. **Verification** — confirm files exist in correct locations
6. **HTML report template** — post-install summary

### What's NOT in Phase 1
- Multi-game support (FM24 only)
- Conflict resolution (FM24 mods don't conflict at file level)
- Load order management (not applicable to FM24)
- Mod updates/versioning (install-only, no tracking)
- Desktop app or web UI

### Effort Estimate
- **1 BUILD backlog** for the skill + FM24 config + Playwright automation
- **1 optional backlog** for HTML report generation
- Tasks: ~8-12 (config schema, FM24 config, skill definition, site configs for sortitoutsi/df11, download engine, extract engine, placement engine, verification, report)

## FM24 POC — What Worked, What Didn't

### Worked
- Playwright navigated sortitoutsi.net successfully — login, navigation, download initiation
- `browser_run_code` with `waitForEvent('download')` + `saveAs()` pattern reliably captured downloads
- Archive extraction (unzip) and file placement worked correctly
- AI understood mod categories and folder structure without hardcoded rules
- Cross-site navigation (sortitoutsi + df11faces.com) in one session

### Didn't Work / Needs Improvement
- **Rate limiting:** sortitoutsi free tier limits to one download at a time — slowed installation significantly
- **Large files:** Multi-GB downloads (DF11 Megapack) are slow via browser-based download
- **No state persistence:** No memory of what's already installed — risk of re-downloading
- **Manual category knowledge:** AI knew where files go, but this should be codified in game config, not reliant on LLM knowledge
- **No verification step:** Files were placed but no automated check that they work in-game

## Risks

| Risk | Mitigation |
|------|------------|
| Mod site layout changes break automation | AI-powered navigation adapts to layout changes (key advantage over scraping) |
| Anti-bot detection on mod sites | Use realistic browser profiles, respect rate limits, authenticate properly |
| Large file downloads unreliable via Playwright | Fall back to direct HTTP download when URL is known (bypass browser for file transfer) |
| Scope creep into full mod manager | Strict Phase 1 scope: FM24 only, install only, no tracking |
| Claude API costs for simple file operations | Most operations are Playwright + bash — LLM usage is for decision-making only |

## Alternatives If NO-GO

If this project is shelved, the following alternatives capture partial value:
1. **FM24-specific install script** — shell script that automates the download/extract/place workflow for known mods. No AI, no Playwright, just `curl` + `unzip`. Loses the intelligence layer
2. **Contribute to Vortex** — add FM24 game extension to Vortex. Gains ecosystem reach but requires learning Vortex extension API and getting accepted upstream
3. **Document the manual process** — write a comprehensive guide for FM24 mod installation. Low effort, some community value, no showcase potential
4. **Keep as ad-hoc skill** — the FM24 POC already works as an informal skill. Don't formalize it, just use it when needed

## Conclusion

The universal mod installer has genuine value for underserved game communities, primarily as a Claude Code showcase and secondarily as a utility. The FM24 proof of concept validates the core capability. Building it as a kernel skill (not a harness or standalone app) keeps effort proportional to value. Phase 1 is one backlog targeting FM24 only, with expansion to other games driven by demand.

**Next step:** If approved, create BUILD backlog for Phase 1 skill implementation.
