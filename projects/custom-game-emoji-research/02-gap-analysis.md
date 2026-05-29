# Gap Analysis — What's Missing for D&D-Style Grid Engines

**Research Date:** 2026-05-29
**Pipeline:** 102 — Custom Game Emoji Market Research
**Reference:** Task 003 — Gap analysis for grid-based dungeon/tactical games

---

## D&D Grid Engine — Current State

The D&D game engine at `D:\my_ai_projects\project_test_repos\dnd-game-engine-test` uses emoji as visual tokens on a tactical grid (5ft squares). Its current emoji mappings reveal the problem directly:

### What the Engine Currently Uses

| Category | Emoji Used | Problems |
|----------|-----------|----------|
| **Characters** | 🐢 🐴 ⚒️ ☠️ 🧙 ✝️ | Race/class approximations — turtle for tortle, horse for centaur. No purpose-built class icons. |
| **Monsters** | 👹 👺 💀 🧟 👻 🐉 🐻 🐍 | Same emoji (👹) reused for goblin AND orc. Bugbear uses bear. Drow uses snake. No visual distinction. |
| **NPCs** | 👑 🤝 🧟 ⛏️ | Generic symbols — crown for quest-giver, handshake for ally. No NPC archetype icons. |
| **Environment** | 🧱 🚪 🔲 ⚠️ ⚰️ 💧 🔦 📿 | Pillar and obstacle both use 🔲. Door open and closed both use 🚪. No state distinction. |
| **Terrain** | 💧 (water AND difficult terrain) | Single emoji covers two different game concepts. |

### What the Engine Template Defines But Can't Represent

The tactical grid template (`tactical-grid-template.json`) defines these symbol categories but falls back to generic Unicode because purpose-built emoji don't exist:

- `⚡` for "Elemental Hazard" — lightning bolt doesn't communicate fire/ice/acid/necrotic
- `🗂️` for "Furniture/Barrels" — a file folder icon for dungeon furniture
- No symbols defined for: cover, elevation, spell effects, conditions, line-of-sight blockers

---

## Gap Table

| Category | Gap Description | Why Existing Sources Don't Cover It | Est. Missing Icons |
|----------|----------------|-------------------------------------|-------------------|
| **1. Dungeon Terrain** | No symbolic emoji for: corridor tiles, room walls (corner/T-junction/cross), lava, ice, pit, pressure plate, secret door, portcullis, drawbridge, rubble, collapsed passage | game-icons.net has silhouettes (not emoji-sized); itch.io has tile sets (full sprites, not symbolic tokens); no source offers 32-64px symbolic terrain icons designed for grid overlay | 18-25 |
| **2. Monsters & Creatures** | D&D has 400+ creature types; Unicode provides ~10 usable monster emoji. Missing: goblin vs. hobgoblin vs. bugbear distinction, mindflayer, beholder, owlbear, gelatinous cube, mimic, lich, vampire, werewolf variants, elementals (fire/water/earth/air), aberrations, constructs, fiends (devil vs. demon) | game-icons.net has creature silhouettes but at wrong scale/style; itch.io token packs are character portraits (top-down or bust), not symbolic emoji; no pack provides emoji-style creature icons where each creature type is visually distinct at 32-64px | 40-60 |
| **3. Status Conditions** | D&D 5e has 15 conditions (blinded, charmed, deafened, frightened, grappled, incapacitated, invisible, paralyzed, petrified, poisoned, prone, restrained, stunned, unconscious, exhaustion 1-6). None have purpose-built emoji. Additional: concentration, raging, blessed, cursed, hasted, enlarged, polymorphed | game-icons.net has some status icons but as B&W silhouettes, not colored emoji. No source provides a unified condition icon set designed for grid combat overlays where multiple conditions stack visually on one tile | 25-35 |
| **4. Spell Effects & AoE** | Spell area shapes: cone (15/30/60ft), sphere (5/10/20ft radius), line (30/60/100ft), cube, cylinder. Spell types: fireball, lightning bolt, wall of fire, fog cloud, darkness, silence, spirit guardians, bless radius. No emoji for any AoE indicator or spell-effect zone | No existing source addresses this — it's a grid-engine-specific need. AoE shapes on a tactical grid require transparent overlay-style icons that indicate affected squares. This is a product category that doesn't exist yet | 15-20 |
| **5. Game Mechanics & UI** | Initiative tracker markers (current turn, readied action, delayed), action economy tokens (action, bonus action, reaction — used/available), movement indicators (dash, disengage, dodge), cover indicators (half/three-quarter/full), advantage/disadvantage markers, death save trackers | These are game-system UI elements, not traditional "art assets." game-icons.net covers RPG items/creatures but not game-state indicators. No source targets the tactical combat UI layer | 20-30 |
| **6. Dungeon Features** | Interactive dungeon objects: chest (open/closed/trapped/locked), lever (up/down), altar, fountain, forge, jail cell, throne, bookshelf, barrel, crate, table, bed, campfire, ladder, trapdoor, bridge, well | itch.io has sprite-based furniture packs but they're designed for tile-based rendering (full sprites), not symbolic emoji for grid overlay. The engine currently uses 🗂️ (file folder) for furniture because nothing better exists | 15-20 |
| **7. Environmental Hazards** | Trap types: pit trap, spike trap, poison dart, rolling boulder, flame jet, magical glyph, alarm ward. Hazards: cave-in zone, unstable floor, poisonous gas, magical darkness, anti-magic zone, wild magic zone | game-icons.net has a generic trap icon; no source distinguishes trap types visually. Environmental hazards as overlay markers (transparent, stackable on terrain) don't exist as a product category | 12-18 |

---

## Total Estimated Missing Icons

| Category | Low Estimate | High Estimate |
|----------|-------------|---------------|
| Dungeon Terrain | 18 | 25 |
| Monsters & Creatures | 40 | 60 |
| Status Conditions | 25 | 35 |
| Spell Effects & AoE | 15 | 20 |
| Game Mechanics & UI | 20 | 30 |
| Dungeon Features | 15 | 20 |
| Environmental Hazards | 12 | 18 |
| **Total** | **145** | **208** |

A comprehensive "D&D Grid Emoji" pack would need **145-208 purpose-built icons** across 7 categories.

---

## Why This Gap Exists

1. **Wrong format:** Existing icon packs are designed for game engine UIs (inventory screens, skill trees, item tooltips) — not for grid-based tactical maps where icons represent positions on a board
2. **Wrong scale:** Most packs offer 128-512px icons optimized for menus. Grid emoji need to be readable at 32-64px and work side-by-side in a dense grid
3. **Wrong abstraction level:** Tile sets are too detailed (full environment sprites). Unicode emoji are too generic (one ogre emoji for all large humanoids). The gap is *symbolic icons* — simple, distinct, recognizable at small sizes
4. **No game-state icons:** The entire concept of "game state as visual icon" (conditions, AoE shapes, action economy, cover) has no product category. These are inventions needed by grid-based digital tabletop engines
5. **Duplicate collision:** The D&D engine reuses 👹 for both goblins and orcs, 💧 for both water and difficult terrain, 🔲 for both pillars and obstacles — because Unicode simply doesn't have enough distinct symbols for these concepts

---

## Competitive Gap Summary (from Task 002)

Based on the existing icon set research (01-existing-icon-sets.md), the Category Coverage Analysis showed:

| Market Status | Categories |
|--------------|------------|
| **Well-covered** | Weapons, armor, potions, items/loot |
| **Moderate** | Spells/skills, monsters (as portraits), pixel art packs |
| **Weak/Absent** | Terrain types, status conditions, game mechanics, environmental hazards, grid/hex tokens, dungeon features, emoji-sized purpose-built sets |

The **primary opportunity space** is a unified, emoji-style icon set specifically designed for grid-based tactical/dungeon gameplay — filling the weak/absent categories above with 145-208 purpose-built icons at 32-64px.
