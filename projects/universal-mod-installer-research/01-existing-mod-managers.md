# Existing Mod Managers — Landscape Analysis

## Feature Comparison Table

| Tool | Games Supported | Install Method | Conflict Resolution | Load Order | UI/CLI | Free | Community Size |
|------|----------------|----------------|---------------------|------------|--------|------|----------------|
| **Vortex** (Nexus Mods) | 500+ | Auto-detect (Steam, GOG, Epic, Xbox), one-click from Nexus | Visual conflict trees, LOOT-powered sorting | Automated via LOOT | GUI (Electron) | Free (GPL-3.0) | Largest — Nexus Mods ecosystem |
| **Mod Organizer 2** | ~20+ (Bethesda focus) | Manual + Nexus integration | Virtual filesystem (USVFS) — non-destructive | Manual drag-and-drop + LOOT | GUI (Qt) | Free (open source) | Large — Bethesda modding community |
| **r2modman** | 100+ Unity games | One-click from Thunderstore | BepInEx plugin ordering | Profile-based | GUI (Electron) | Free (open source) | Growing — Thunderstore ecosystem |
| **Steam Workshop** | Developer-dependent | Subscribe button | None — last-write-wins | Subscription order (no manual control) | Web + in-client | Free (platform) | Massive — Steam platform |
| **SMAPI** | Stardew Valley only | Manual install + mod folder | Error interception + auto-recovery | Alphabetical + dependency-aware | CLI + console window | Free (open source) | Medium — Stardew community |
| **Wabbajack** | Bethesda games primarily | Curated modlist auto-installer | Pre-resolved by list curator | Pre-configured | GUI | Free (open source) | Medium — curated list community |
| **CurseForge** | Minecraft, WoW, Sims 4, Palworld, others | One-click + modpack install | Loader-aware (Forge/Fabric/NeoForge/Quilt) | Modpack-managed | GUI (standalone + Overwolf) | Free | Large — Minecraft/WoW community |

## Gap Analysis — What Existing Tools Miss

### 1. Cross-Game Universal Management
- **Vortex** comes closest with 500+ games, but is tightly coupled to the Nexus Mods ecosystem
- **No tool** manages mods across different mod ecosystems (Nexus + Thunderstore + CurseForge + game-specific sites) in a single interface
- Each tool is locked to its distribution platform — you need Vortex for Nexus, r2modman for Thunderstore, CurseForge app for CurseForge

### 2. AI-Assisted Mod Discovery and Recommendation
- **Zero tools** offer AI-powered mod recommendations based on playstyle, existing mod list, or compatibility analysis
- Mod discovery is entirely manual — browse, read descriptions, check compatibility yourself
- No tool answers "what mods should I install for [game goal]?" — this is a human research task today

### 3. Automated Downloading from Multiple Sites
- Every mod manager downloads exclusively from its own ecosystem
- Vortex only downloads from Nexus Mods, r2modman only from Thunderstore, CurseForge only from CurseForge
- **No tool** navigates to arbitrary mod sites (e.g., sortitoutsi.net for FM24), handles site-specific authentication, and downloads files
- This is the exact capability Playwright MCP provides that no existing tool has

### 4. Game-Specific Setup Guidance
- Existing tools install files but don't explain what to install or why
- Wabbajack solves this for Bethesda games via curated lists, but the curation is human labor
- No tool provides contextual guidance: "For FM24, you need a facepack, a skin, a logo pack, and a database update — here's what's recommended and why"

### 5. Non-Standard Mod Ecosystems
- Games without Nexus Mods presence (like FM24) have no mod manager at all
- FM24 mods live on sortitoutsi.net, fmscout.com, and individual forums — none of these integrate with any mod manager
- Sports games, racing sims, and niche titles are completely unserved

## FM24 Modding Ecosystem — Why It's Underserved

### Current State
FM24 modding has **zero dedicated mod manager support**. The entire installation process is:
1. Manually navigate to sortitoutsi.net, fmscout.com, or community forums
2. Create accounts and log in (sortitoutsi requires login for downloads)
3. Download zip/rar archives one at a time (free users: one download at a time, rate-limited)
4. Extract archives with WinRAR or 7-Zip
5. Manually copy extracted folders to the correct location under `Documents/Sports Interactive/Football Manager 2024/`
6. Know which subfolder each mod type goes in: `graphics/faces/`, `graphics/logos/`, `skins/`, `editor data/`, etc.
7. Reload skin in-game preferences, untick caching, verify installation

### Why No Tool Exists
- FM24 is not on Nexus Mods (no Vortex support)
- FM24 is not on Thunderstore (no r2modman support)
- Steam Workshop has limited FM24 support (mostly tactics, not graphics)
- The mod sites (sortitoutsi) have no API — downloading requires browser navigation with authentication
- The modding community is large but fragmented across multiple sites with different download mechanisms

### Opportunity
- **DF11 Megapack** alone has 229,000+ faces — this is a massive download + extract + place operation
- A typical FM24 mod setup requires 6-10 different mods from multiple sites, each with different extraction and placement rules
- The FM24 proof of concept (2026-07-06) demonstrated that Playwright MCP can navigate sortitoutsi, authenticate, download, and install mods — this is the exact workflow no existing tool automates

## Key Takeaways

1. **Solved problem (partially):** For Bethesda games and Nexus-ecosystem titles, Vortex + MO2 are excellent. The mod manager space is mature for these games.

2. **Unsolved problem:** For games outside the Nexus/Thunderstore/CurseForge ecosystems (FM24, racing sims, sports games, niche titles), there is **no mod management at all**.

3. **Unique capability gap:** No existing tool can navigate arbitrary websites, handle site-specific authentication, and download files. This is exactly what Playwright MCP enables.

4. **AI gap:** No existing tool provides intelligent mod recommendations, setup guidance, or understands what mods are appropriate for a given game/goal combination.
