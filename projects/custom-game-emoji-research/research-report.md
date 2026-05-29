# Custom Game Emoji Market — Final Research Report

**Date:** 2026-05-29
**Pipeline:** 102 — Custom Game Emoji Market Research

---

## 1. Executive Summary

- **A clear gap exists** in the game icon market: no unified, emoji-style icon set serves grid-based tactical/dungeon gameplay. Existing icon packs cover weapons/armor/items extensively but leave terrain, status conditions, game mechanics, environmental hazards, and dungeon features almost entirely unserved.
- **The D&D grid engine use case proves the gap is real** — our own engine resorts to reusing generic Unicode (same emoji for goblin and orc, same emoji for water and difficult terrain) because purpose-built icons don't exist.
- **Production is feasible and cheap** — AI-assisted pipeline (Midjourney/Stable Diffusion + Aseprite polish) can produce a 100-icon pack in 3-5 days for $70-120 in tool costs.
- **Revenue is modest but stackable** — Year 1 estimate of $500-5,000 for a single pack, scaling with catalog depth and channel expansion.
- **Recommendation: BUILD** — the opportunity is real, the production cost is low, and the D&D engine provides a built-in first customer and proof-of-concept.

---

## 2. Market Overview

The game icon/emoji market is large but fragmented. Seven major sources were surveyed (01-existing-icon-sets.md):

| Source | Icons Available | License | Price |
|--------|----------------|---------|-------|
| game-icons.net | 4,180+ | CC-BY 3.0 | Free |
| OpenGameArt.org | ~870 | CC0/CC-BY/GPL | Free |
| itch.io | 1,500+ across 20+ packs | Varies | $0-6/pack |
| GameDev Market | ~500+ | Commercial | $3-20/pack |
| Unity Asset Store | 10,000+ | Unity EULA | $10-59/pack |
| Kenney.nl | ~300 dungeon-related | CC0 | Free |
| Humble Bundle | Varies | Per-bundle | $1-25 |

**The oversupplied categories** are weapons, armor, potions, and loot items — these are available from multiple free and paid sources in every art style.

**The undersupplied categories** are terrain types, status conditions, game mechanics, environmental hazards, grid/hex tokens, dungeon features, and emoji-sized purpose-built sets. No single product serves these categories with a unified style at the 32-64px scale grid engines require.

---

## 3. The Opportunity

The gap analysis (02-gap-analysis.md) identified **145-208 missing icons across 7 categories** that no existing product covers:

| Category | Missing Icons | Why It's Missing |
|----------|--------------|------------------|
| Dungeon Terrain | 18-25 | Existing packs offer tile sets (full sprites), not symbolic grid tokens |
| Monsters & Creatures | 40-60 | D&D has 400+ creature types; Unicode provides ~10 usable monster emoji |
| Status Conditions | 25-35 | D&D 5e has 15 conditions + buffs/debuffs; no purpose-built emoji exist |
| Spell Effects & AoE | 15-20 | AoE shapes on a tactical grid are a product category that doesn't exist |
| Game Mechanics & UI | 20-30 | Initiative, action economy, cover — game-state indicators have no icon source |
| Dungeon Features | 15-20 | Interactive objects (chests, levers, altars) only exist as full sprites |
| Environmental Hazards | 12-18 | Trap types, hazard zones — no source distinguishes them visually |

**The D&D grid engine proves this gap concretely.** The engine at `dnd-game-engine-test` uses emoji as visual tokens on a tactical grid (5ft squares). Its current mappings show the problem:
- Same emoji (👹) reused for both goblin AND orc — no visual distinction
- 💧 represents both water and difficult terrain — two different game concepts
- 🗂️ (file folder) used for dungeon furniture — because nothing better exists
- No symbols defined for cover, elevation, spell effects, conditions, or line-of-sight blockers

This is not a theoretical gap — it's a functional limitation in a working game engine that purpose-built icons would directly solve.

---

## 4. Business Model Options

Three options were evaluated (03-sales-channels-pricing.md, 05-discord-emoji-angle.md):

### Option A: Game Developer Asset Packs (itch.io/Gumroad)

**The primary channel.** itch.io offers the best combination of low fees (creator-set, default 10%), largest indie game dev audience, and strong discoverability for game assets. Gumroad serves as a secondary channel for email-list-driven sales.

- **Pricing sweet spot:** $5-15 for 100-500 icon packs; $15-25 for 500+ mega packs
- **Revenue share:** itch.io nets the creator ~81% ($4.05 on a $5 sale); Gumroad nets ~71%
- **Target buyer:** Indie game developers building grid-based/tactical RPGs (estimated 2,000-10,000 active devs)
- **No direct competitor** exists in the grid-tactical emoji category — first-mover advantage

### Option B: Discord/Community Emoji Packs

**A viable secondary channel** sharing production assets with Option A. The same D&D icons reformatted as Discord emoji (112x112, 56x56, 28x28px) can sell on Etsy/Gumroad with minimal additional work.

- **Market evidence:** 5,000+ Discord emote listings on Etsy, 1,000+ tagged D&D/TTRPG
- **Pricing:** $3-40 per pack (small packs $3-8, large packs $15-40)
- **Addressable market:** 2,000-10,000 D&D Discord servers, $20K-300K total addressable revenue
- **Weakness:** Highly fragmented market, free alternatives (emoji.gg), no Discord-native marketplace
- **Verdict:** MODERATE — treat as incremental revenue from existing assets, not standalone business

### Option C: Direct Licensing to Game Studios

**Bonus revenue, not primary.** High margins (no platform fees) but requires outbound sales effort. Common models: per-project license ($50-500), per-studio license ($200-2,000).

- Best pursued after establishing a portfolio and reputation via Options A and B
- Requires an ArtStation/portfolio presence and active outreach

**Recommended approach:** Option A as primary, Option B as low-effort derivative, Option C as opportunistic.

---

## 5. Production Feasibility

The production pipeline research (04-production-pipeline.md) confirms that a solo creator can produce a professional 100-icon pack in **3-5 working days** at minimal cost:

**Time estimate for a 100-icon pack:**

| Phase | Hours |
|-------|-------|
| Art direction & prompt engineering | 4-6h |
| AI generation (batch, 300-500 candidates) | 2-4h |
| Curation & selection | 2-3h |
| Manual polish (background removal, alignment, palette) | 8-15h |
| Sprite sheet assembly + multi-resolution export | 2-4h |
| Quality check + packaging | 3-5h |
| **Total** | **21-37 hours** |

**Cost for first pack (DIY):** $70-120 (Midjourney/Scenario.gg subscription + Aseprite + TexturePacker). Subsequent packs cost only the AI subscription ($10-60/month).

**The consistency challenge** — maintaining visual coherence across 100+ AI-generated icons — is solvable through custom LoRA training (Stable Diffusion) or Scenario.gg custom models, combined with prompt templates and post-processing palette locks. Creators report 90%+ consistency with these techniques.

**Recommended tool stack:** Midjourney or Scenario.gg for generation, Aseprite ($20) for pixel editing and palette normalization, TexturePacker ($40) for spritesheet export, ImageMagick (free) for batch resizing.

---

## 6. Revenue Potential

**Year 1 projections for a single 150-200 icon pack at $9.99 on itch.io:**

| Scenario | Year 1 Revenue (Net) |
|----------|---------------------|
| Conservative (organic only) | $450-1,200 |
| Optimistic (active marketing, niche dominance) | $1,500-5,000 |
| Lifetime (with updates) | $3,000-15,000 |

**Revenue multipliers that scale beyond a single pack:**

- **Multiple themed packs** (conditions, terrain, AoE, monsters): 4-6x single pack revenue
- **Cross-platform listing** (itch.io + Gumroad + Etsy for Discord emoji): 1.3-1.5x
- **Bundle participation** on itch.io: volume exposure boost
- **VTT integration partnerships** (Roll20, Foundry VTT): access to large captive audiences
- **Discord emoji derivative packs**: incremental revenue from reformatted assets

**Realistic Year 1 across all channels:** $2,000-10,000 with 3-4 themed packs and active marketing. This is supplemental income, not a primary business — but the production cost is so low ($70-120 per pack) that ROI is achieved within 10-25 sales.

---

## 7. Risks and Challenges

### Risk 1: Market Saturation in Adjacent Categories

Weapons, armor, and item icons are thoroughly saturated. The opportunity exists specifically in the **underserved categories** (terrain, conditions, mechanics). If the packs drift toward covered categories, they'll compete against free CC0 alternatives (game-icons.net, Kenney.nl) with no differentiation. **Mitigation:** Stay laser-focused on the 7 gap categories identified in the gap analysis. Do not produce "another fantasy weapon pack."

### Risk 2: AI Art Legality and Marketplace Policies

AI-generated art faces evolving legal scrutiny around copyright eligibility and marketplace acceptance. Some platforms may restrict or label AI-generated content. The US Copyright Office has indicated that purely AI-generated images without human creative control may not be copyrightable. **Mitigation:** The production pipeline includes significant human creative input (art direction, curation, manual polish, palette normalization) which strengthens copyright claims. Disclose AI-assisted production transparently. Monitor marketplace policy changes.

### Risk 3: Production Consistency at Scale

Maintaining visual coherence across 500+ icons (the full gap of 145-208 icons across multiple themed packs) is the hardest technical challenge. AI tools introduce subtle variations in line weight, color palette, and perspective between generation sessions. **Mitigation:** Invest upfront in LoRA training or Scenario.gg custom model with 20-30 reference icons. Use strict prompt templates, batch palette normalization, and grid overlay QA. Budget 30% of production time for consistency passes.

---

## 8. Recommendation

**BUILD.**

The evidence supports proceeding:

1. **The gap is real and verified** — 145-208 icons across 7 categories that no existing product serves, confirmed by both market survey and the D&D grid engine's functional limitations.
2. **Production cost is trivially low** — $70-120 for a first pack, 3-5 days of work. The downside risk is a weekend of effort.
3. **First-mover advantage** — no competitor offers a unified grid-tactical emoji set. Being first in a niche category on itch.io drives organic discovery.
4. **Built-in proof-of-concept** — the D&D grid engine at `dnd-game-engine-test` is a ready-made showcase. Icons can be tested in a working game before release, and the engine itself becomes marketing collateral ("these icons were built for a real D&D engine").
5. **Stackable revenue** — each additional themed pack multiplies revenue with decreasing marginal production cost (tool stack is purchased, style pipeline is established, LoRA is trained).
6. **Low commitment** — this is not a startup. It's a digital product with near-zero marginal cost, sold on existing marketplaces with no infrastructure to build.

The D&D engine use case is central to the recommendation: it provides both the market validation (the gap exists because we hit it) and the go-to-market advantage (a working game engine using our icons is the best possible product demo).

---

## 9. Recommended Next Step

**Create a 50-icon "Dungeon Terrain & Conditions" starter pack and list on itch.io at $4.99.**

Why this specific pack:
- **Terrain + Conditions** are the two most acutely missing categories (the D&D engine literally cannot distinguish water from difficult terrain, or goblin from orc)
- **50 icons** is large enough to be useful, small enough to produce in 2-3 days
- **$4.99** is in the high-conversion zone for itch.io indie asset packs
- The pack validates the production pipeline, pricing, and market demand before committing to the full 145-208 icon set

**Concrete actions:**
1. Define art direction: flat/minimal style (fastest production, good AI quality) at 32x32 primary with 16/64/128 variants
2. Generate with Midjourney or Scenario.gg using prompt templates; train LoRA if using Stable Diffusion
3. Polish in Aseprite (palette lock, grid alignment, edge cleanup)
4. Export via TexturePacker (individual PNGs + spritesheet + metadata)
5. Test icons in the D&D grid engine — verify they render correctly on the tactical grid
6. Package with preview image, README, and license
7. List on itch.io with tags: dungeon, tactical, RPG, grid, emoji, icons, D&D, tabletop
8. Cross-list as Discord emoji pack on Etsy ($6.99, reformatted to 112x112/56x56/28x28)
9. Post to r/gamedev, r/tabletopgamedesign, r/dndnext with the D&D engine demo
