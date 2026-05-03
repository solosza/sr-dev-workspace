# Game Dev Site Integration — Research Report

## Executive Summary

**Recommendation: Portfolio showcase page now. A separate product site is premature unless the game engine has a unique angle (AI-driven gameplay, governance-backed game development) and a playable demo.**

The game engine space in 2026 is dominated by established players (Unity, Unreal, Godot) and web-focused engines (Phaser, PlayCanvas). Competing directly is unrealistic. The game engine and game-dev spec are best positioned as portfolio proof-of-work demonstrating AI-agent-built software, not as a standalone game engine product.

---

## 1. Competitor Landscape

### Game Engine Sites — Market Map

| Engine | Type | Site Style | Key Pattern |
|--------|------|------------|-------------|
| **Godot** | Open-source, 2D/3D | Static Jekyll site, open-source | Download + showcase + docs |
| **Phaser** | Open-source, 2D HTML5 | Product site with examples | Playable demos embedded in site |
| **PlayCanvas** | Web-first, 3D | Product site with editor | Live editor/playground in browser |
| **Unity** | Commercial, full-featured | Enterprise product site | Download + learn + asset store |
| **Unreal** | Commercial, AAA | Enterprise product site | Showcase + download + marketplace |
| **itch.io** | Indie game platform | Creator marketplace | User-generated game pages |

### What Game Engine Sites Have in Common

1. **Playable demos or showcase games** — visitors can see/play something immediately
2. **"Get started" flow** — download, install, first project tutorial
3. **Community showcase** — games built with the engine
4. **Documentation hub** — central docs site with tutorials
5. **Open-source badge** — for indie engines, this is a key differentiator

### Key Insight

Game engine sites live or die by their **showcase** — "look what people built with this." Without shipped games or impressive demos, the site has nothing to show. Screenshots of code don't sell game engines.

---

## 2. Game Dev Project Assessment

### Current State

| Dimension | Status | Notes |
|-----------|--------|-------|
| **Repos** | 2 repos (game-dev, game-engine-master) | Split architecture |
| **Maturity** | Prototype/spec stage | Has specs and architecture, needs production games |
| **Unique Features** | AI coaching, personality packs, simulation engine | Interesting differentiators |
| **Playable Demos** | Unknown | Critical — need at least one |
| **Users** | Creator only | No external adoption |
| **Documentation** | Specs exist | Needs user-facing docs |

### Differentiator Analysis

The game-dev project's potential differentiators:

| Feature | Unique? | Competitor Comparison |
|---------|---------|----------------------|
| AI coaching | Yes (if implemented) | No game engine has built-in AI coaching |
| Personality packs | Yes | Novel concept for NPC behavior |
| Simulation engine | Partially | PlayCanvas and Phaser have physics, but not AI simulation |
| Agent-built | Yes | The engine itself was built by the Isagawa kernel loop |
| Governance-backed | Yes | No game engine has attestation or governance |

The strongest differentiator is the meta-story: **"An AI agent built this game engine."** The game engine is proof that the loop can produce complex software autonomously.

---

## 3. Option Analysis

### Option A: Portfolio Showcase Page

**How it works:** Add a case study page to isagawa.co for the game engine — architecture, screenshots, tech highlights, the "built by AI" narrative.

**Pros:**
- Fast to build
- Honest positioning — proof-of-work, not product promise
- The "AI-built game engine" narrative is compelling for the portfolio audience
- No need for playable demos (screenshots + architecture diagrams work for case studies)

**Cons:**
- Doesn't drive game developer adoption
- Limited reach

**Best for:** Current stage. Immediately actionable.

### Option B: Separate Product Site

**How it works:** Build a standalone site (gamedev.isagawa.co or similar) with engine showcase, docs, demos.

**Pros:**
- Professional product positioning
- Can include playable WebGL demos
- SEO potential for "AI game engine" keywords

**Cons:**
- Premature — no shipped games, no users
- Needs playable demos (high effort to produce)
- Competing against Godot (60K+ GitHub stars) is unrealistic
- Maintenance burden

**Best for:** Only after shipping at least 2-3 playable demos and gaining external contributors.

### Option C: itch.io Game Page

**How it works:** Ship a playable game built with the engine on itch.io. Link from portfolio.

**Pros:**
- Existing platform with discovery
- Immediate feedback from players
- Proves the engine works in production
- Low effort (no custom site needed)

**Cons:**
- Showcases the game, not the engine
- itch.io audience is gamers, not developers

**Best for:** Validation — does the engine produce playable, fun games?

---

## 4. Design Reference Sites

### For Portfolio Showcase Page

| Reference | Why |
|-----------|-----|
| Godot showcase (godotengine.org/showcase) | Shows games built with the engine |
| Phaser examples page (phaser.io/examples) | Embedded playable demos |
| isagawa.co existing sections | Maintain visual consistency |

### For Future Product Site (if/when)

| Reference | Why | Key Pattern |
|-----------|-----|-------------|
| godotengine.org | Open-source engine landing page | Download + showcase + community |
| phaser.io | Web-first game engine | Embedded playable examples |
| playcanvas.com | 3D web engine | Live editor in browser |
| itch.io creator pages | Indie game showcase | Game cards with screenshots + play button |

---

## 5. Open Questions Resolved

| Question | Answer |
|----------|--------|
| Integrate into portfolio or separate site? | **Portfolio showcase now** |
| Include playable demos? | **Not required for portfolio page** — screenshots + architecture diagrams |
| Naming/domain strategy? | **isagawa.co/projects/game-engine** — portfolio path |
| Enough maturity for own site? | **No** — needs shipped games and playable demos first |

---

## 6. Recommended Next Steps

1. **Build a portfolio showcase page** on isagawa.co — focus on the "AI-built game engine" narrative
2. **Ship one playable demo** on itch.io — validates the engine works, provides screenshots for showcase
3. **Write user-facing documentation** — even for the portfolio page, architecture docs add credibility
4. **Lean into the meta-narrative** — "This game engine was built autonomously by an AI agent using the Isagawa kernel" is the compelling story, not "here's another game engine"
5. **Only build a separate site** when there are playable games to showcase and developer interest
