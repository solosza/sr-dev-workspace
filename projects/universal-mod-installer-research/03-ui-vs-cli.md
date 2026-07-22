# UI vs CLI — Interface Analysis

## Target Audience Analysis

### FM Community
- **Technical level:** Low to medium. Many users follow step-by-step YouTube guides for manual mod installation
- **Platform:** Windows dominant (95%+). Some Mac users
- **Comfort with CLI:** Very low. FM players are mainstream gamers, not developers
- **Current workflow:** Download zip → Extract → Copy to folder → Reload in-game. Entirely GUI-based
- **Pain point:** Not the complexity of the tool, but knowing WHAT to install and WHERE files go

### Skyrim/Bethesda Community
- **Technical level:** Medium to high. Comfortable with MO2, Vortex, xEdit, LOOT
- **Platform:** Windows dominant
- **Comfort with CLI:** Low to medium. Some use command-line tools but prefer GUIs
- **Current workflow:** Vortex or MO2 — fully GUI-based mod management
- **Pain point:** They already have excellent tools. Hard to compete on UX

### General Modding Community (Stardew, Cities Skylines, Unity games)
- **Technical level:** Varies widely
- **Platform:** Cross-platform matters more
- **Comfort with CLI:** Low for casual, medium for active modders
- **Current workflow:** Game-specific tools (SMAPI, r2modman, Steam Workshop)

### Key Insight
Gamers are not developers. Every successful mod manager is GUI-first. The CLI is a barrier to adoption for the primary target audience.

## Interface Options Evaluated

### Option 1: CLI Only (Claude Code Terminal)

**What it is:** User runs Claude Code, types natural language commands like `/mod-install fm24 --all`

| Factor | Assessment |
|--------|------------|
| Development effort | **Lowest** — skill/command definition + Playwright automation |
| User experience | **Poor for gamers** — requires Claude Code installed, terminal comfort |
| Maintenance burden | **Lowest** — no UI to maintain |
| Distribution | npm install / Claude Code marketplace |
| Audience reach | **Very narrow** — only Claude Code users who also mod games |

**Pros:**
- Already built (FM24 POC works today)
- Natural language interface is powerful for those who use it
- No frontend development needed

**Cons:**
- Gamers won't install a developer terminal tool to install mods
- $20/month Claude Pro subscription just to install mods is not competitive
- Audience is developers who also game — very small intersection

### Option 2: Web UI (Dashboard)

**What it is:** Web application showing installed mods, game detection, one-click install buttons

| Factor | Assessment |
|--------|------------|
| Development effort | **High** — full-stack web app (React + API + file system bridge) |
| User experience | **Good** — familiar web interface, visual mod browsing |
| Maintenance burden | **High** — frontend + backend + API changes |
| Distribution | Web app URL or local server |
| Audience reach | **Medium** — accessible but requires local server for file ops |

**Pros:**
- Familiar interface for gamers
- Visual mod browsing and status
- Could show mod previews, descriptions, compatibility

**Cons:**
- File system access requires local server (Electron-like complexity)
- Full-stack development for what should be a simple tool
- Competing with Vortex/MO2 on their home turf (GUI)

### Option 3: Desktop App (Electron/Tauri)

**What it is:** Native-feeling desktop application like Vortex or MO2

| Factor | Assessment |
|--------|------------|
| Development effort | **Very high** — Electron/Tauri app + full mod management UI |
| User experience | **Best** — native feel, drag-and-drop, system integration |
| Maintenance burden | **Very high** — platform-specific builds, updates, installer |
| Distribution | exe/msi installer, auto-updater |
| Audience reach | **Highest** — familiar format for gamers |

**Pros:**
- Matches what gamers expect (Vortex, MO2 are desktop apps)
- Full file system access without server
- Could distribute as standalone tool

**Cons:**
- Massive development effort — essentially building a new Vortex
- Competing with established tools that have years of polish
- Requires maintaining installers, auto-updates, platform-specific code
- Way beyond research scope — this is a product decision

### Option 4: Hybrid — CLI Backend + Simple Status Page (RECOMMENDED)

**What it is:** Claude Code skill as the engine, with an optional localhost web page showing installation status and mod inventory

| Factor | Assessment |
|--------|------------|
| Development effort | **Low-medium** — CLI skill + simple HTML status page |
| User experience | **Adequate** — natural language commands + visual feedback |
| Maintenance burden | **Low** — minimal UI, CLI does the work |
| Distribution | Claude Code skill (npm/marketplace) |
| Audience reach | **Narrow but targeted** — Claude Code users who game |

**Pros:**
- CLI does the heavy lifting (already proven)
- Status page provides visual confirmation without full app development
- Can generate an HTML report after installation: "Here's what was installed, where, and how to verify"
- Incrementally improvable — start CLI-only, add status page later

**Cons:**
- Still requires Claude Code — limits audience to developers/enthusiasts
- Status page is a nice-to-have, not a game-changer

## How Existing Mod Managers Handle UI

| Tool | UI Framework | Why |
|------|-------------|-----|
| Vortex | Electron (web tech) | Cross-platform, extensible, familiar for web devs |
| MO2 | Qt/C++ | Native performance, complex UI (virtual filesystem browser) |
| r2modman | Electron | Lightweight, rapid development, web tech |
| Wabbajack | WPF/.NET | Windows-only, native Windows look |
| CurseForge | Overwolf + standalone | Platform integration + standalone option |

**Pattern:** Every successful mod manager is a GUI desktop app. Most use Electron for cross-platform ease. None are CLI-only.

## Recommendation

**Build as a CLI skill (Option 1) with optional HTML report generation (from Option 4).**

### Rationale
1. **The audience is Claude Code users**, not general gamers. Building a GUI competes with established tools on their turf
2. **The unique value is intelligence**, not interface — natural language mod discovery, cross-site navigation, game-specific guidance. These work in CLI
3. **Development effort alignment** — the skill approach fits the kernel architecture, requires minimal new code, and is incrementally improvable
4. **Portfolio showcase** — a compelling demo doesn't need a polished GUI. A terminal recording of "install the best FM24 mods" that works is more impressive to the target audience (AI/dev community) than a mediocre Electron app
5. **HTML report** — after installation, generate a simple report showing what was installed, where, and verification status. This provides visual feedback without building a full UI

### Effort Estimate
- **CLI skill (Phase 1):** 1 backlog — game config schema, skill definition, Playwright automation wrapper
- **HTML report (Phase 2):** 1 additional backlog — template + generation after install
- **Desktop app (if ever):** 5-10 backlogs — not recommended unless market demand is proven

### If the Goal Changes to "Product for Gamers"
If the goal shifts from "portfolio showcase" to "product for gamers," the answer changes to **Electron app** (like Vortex/r2modman). But that's a much larger commitment and competes with established tools. Not recommended at this stage.
