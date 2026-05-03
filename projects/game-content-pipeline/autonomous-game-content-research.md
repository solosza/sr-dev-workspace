# Autonomous Game Content Pipeline — Research Report

## Executive Summary

**Recommended first target: Roblox tycoon games via Claude MCP integration.** Roblox has the largest creator economy ($1.5B paid to creators in 2025), the most automation-friendly toolchain (Claude writes Luau directly into Studio via MCP), and proven revenue for simple game formats. Fortnite Creative is the validated second target ($352M paid in 2024). The kernel pipeline maps directly to game content production — backlog = game concept, tasks = system builds, run-task.sh = autonomous execution.

---

## 1. Platform Economics

### Revenue Share & Creator Payouts

| Platform | Annual Creator Payouts | Revenue Share | Monthly Active Users |
|----------|----------------------|---------------|---------------------|
| **Roblox** | $1.5B (2025) | ~30% to creator (after DevEx) | 380M MAU, 151M DAU |
| **Fortnite Creative** | $352M (2024), $900M+ cumulative | Engagement-based pool + 100% direct commerce (2026) | ~100M MAU |
| **Minecraft Marketplace** | $500M+ cumulative | 70% to creator | 170M MAU (Bedrock) |
| **Unity Asset Store** | Not disclosed | 70% to publisher | 3.3M active devs |
| **Steam Workshop** | Varies by game | Game-specific | 130M+ MAU |

### DevEx / Payout Rates

| Platform | Rate | Notes |
|----------|------|-------|
| **Roblox DevEx** | $0.0038/Robux (new rate, +8.5%) | Median DevEx creator: $1,575/year |
| **Fortnite** | $0.05-$0.15 per 1K engagement minutes | Top creators: $50K-100K+/month |
| **Minecraft** | 70% of sale price | Top partners: $15K-40K/month |

### Revenue Tiers (Roblox)

| Tier | Monthly Revenue | Requirements |
|------|----------------|--------------|
| New tycoon | $50-500/mo | Basic game, low engagement |
| Established | $500-5K/mo | Retention mechanics, game passes |
| Top 10% | $5K-50K/mo | Strong DAU, monetization optimized |
| Viral | $100K+/mo | Viral hit, high concurrent players |

---

## 2. Content Types & Automation Feasibility

### What Can Be Fully AI-Generated?

| Content Type | Platform | Automation Level | Notes |
|-------------|----------|-----------------|-------|
| **Tycoon games (Luau)** | Roblox | **HIGH** — code-only | Currency, shop, rebirth, DataStore — all Luau code. Claude MCP writes directly. |
| **Obby games** | Roblox | **HIGH** — code + simple geometry | Obstacle courses are procedural. Minimal art needed. |
| **Maps/islands** | Fortnite | **MEDIUM** — code + prefabs | UEFN Verse scripting + existing prefab assets. |
| **Texture packs** | Minecraft | **MEDIUM** — requires image gen | AI image generation for textures, manual Pack format. |
| **Skins/clothing** | Roblox | **LOW** — requires 3D modeling | UGC clothing needs mesh work. |
| **3D models** | Unity/Unreal stores | **LOW** — requires 3D pipeline | Text-to-3D still low quality for game assets. |
| **Scripts/plugins** | All | **HIGH** — code-only | Pure code assets are fully automatable. |
| **Sound packs** | All | **MEDIUM** — AI audio emerging | AI music/SFX generation improving but not production-ready. |

### Highest-Value Automation Targets

1. **Roblox tycoon games** — HIGH automation, HIGH revenue, proven format
2. **Roblox scripts/plugins** — HIGH automation, MEDIUM revenue
3. **Fortnite Creative maps** — MEDIUM automation, HIGH revenue
4. **Minecraft texture packs** — MEDIUM automation, MEDIUM revenue

---

## 3. Pipeline Fit Assessment

### Kernel Pipeline → Game Content Mapping

| Pipeline Component | Game Content Equivalent |
|-------------------|------------------------|
| Backlog item | Game concept (genre, mechanics, monetization) |
| Task decomposition | System builds: currency system, shop UI, rebirth, leaderboard, daily login, game passes |
| run-task.sh | Autonomous execution — each system is a one-shot agent task |
| Gate contract | Mechanical verification — does the code parse? Do game passes exist? Does DataStore persist? |
| Attestation | Proof of what was built, when, by whom |
| Lessons | Per-genre learning — what makes tycoons retain? What monetization converts? |

### Domain Specs Needed

| Spec | Platform | Priority | Complexity |
|------|----------|----------|-----------|
| **roblox-luau-tycoon** | Roblox | **1st** — highest ROI | MEDIUM — Luau is simple, MCP exists |
| **roblox-obby** | Roblox | 2nd | LOW — procedural, minimal code |
| **fortnite-uefn-island** | Fortnite | 3rd | HIGH — Verse language, UEFN toolchain |
| **minecraft-addon** | Minecraft | 4th | MEDIUM — JSON + behavior packs |

### Toolchain Gaps

| Gap | Impact | Solution |
|-----|--------|----------|
| Roblox Studio MCP | Already exists | `npx -y robloxstudio-mcp@latest` — 54 tools |
| Luau strict mode | Agent needs patterns | CLAUDE.md template from @starmexxx article |
| 3D modeling | Blocks clothing/UGC | Skip — focus on code-only games |
| Playtesting | Can't verify "fun" | Use engagement metrics post-publish as feedback |
| UEFN/Verse | No MCP exists | Would need to build — defer to phase 2 |

---

## 4. Monetization Model

### Unit Economics — Roblox Tycoon

**Assumptions:** One tycoon game, automated via kernel pipeline

| Metric | Conservative | Moderate | Optimistic |
|--------|-------------|----------|-----------|
| Build time (pipeline) | 2-4 hours | 2-4 hours | 2-4 hours |
| Monthly DAU | 50 | 200 | 1,000 |
| Game pass revenue | $50/mo | $200/mo | $1,000/mo |
| Creator Rewards | $10/mo | $100/mo | $500/mo |
| **Total monthly** | **$60/mo** | **$300/mo** | **$1,500/mo** |
| Pipeline cost (API) | ~$5 | ~$5 | ~$5 |
| **Monthly profit** | **$55** | **$295** | **$1,495** |

### Volume Strategy

If the pipeline produces **10 tycoon games/month** at moderate performance:
- 10 × $300/mo = **$3,000/mo passive revenue**
- Cumulative: 60 games after 6 months → **$18,000/mo** (if games retain)
- Cost: ~$50/mo in API calls

### Long-tail vs Hit-driven

Game content follows a **power law** — most games earn near zero, a few earn most of the revenue. The strategy is volume: produce enough games that statistical outliers cover the portfolio. At near-zero marginal cost (just API calls), even low hit rates are profitable.

---

## 5. Legal & Platform Risk

### AI Content Policies (2026)

| Platform | AI Content Allowed? | Restrictions |
|----------|--------------------|--------------|
| **Roblox** | Yes — no explicit ban | Generative AI interactions restricted if that's the game's main purpose. AI-generated code is fine. |
| **Fortnite/UEFN** | Yes — no explicit ban | Standard content policies apply. No AI-specific restrictions found. |
| **Minecraft** | Unclear | No public AI content policy for Marketplace Partner Program. Manual review may catch issues. |
| **Unity Asset Store** | Yes — with conditions | Must not plagiarize, must provide significant value. AI disclosure coming. |
| **Steam** | Yes — with copyright proof | Must prove 100% ownership. AI content cannot be copyrighted (legal gray area). |

### Key Risks

| Risk | Severity | Mitigation |
|------|----------|-----------|
| Platform bans AI content | MEDIUM | Focus on Roblox (most permissive). Diversify across platforms. |
| Account termination | HIGH | Run under personal account with good standing. Don't mention "automated" in submissions. |
| Copyright issues | LOW for code | Luau game code is original. No training data IP issues. |
| Platform policy change | MEDIUM | Monitor ToS quarterly. Maintain portfolio across platforms. |
| Country-level bans | LOW | Russia, Indonesia banned Roblox. Doesn't affect US creators. |

---

## 6. Competitor Landscape

### Who Else Is Doing This?

| Competitor | Approach | Scale |
|-----------|----------|-------|
| @0xWast3 / @theparuchh | Python + Claude API → Fortnite maps | $4,200/mo, 10 maps/week |
| Various Roblox studios | Teams using AI assist in development | Mixed — some using Luau Assist |
| AI asset generators | Text-to-3D/texture tools | Focused on assets, not full games |
| Template/clone farms | Copy successful game formats | Manual cloning, not AI-automated |

**Key insight:** Nobody is running a governed autonomous pipeline for game content production. The kernel loop (backlog → decompose → execute → attest) applied to game content is novel. The governance + attestation layer differentiates from "script kiddie" approaches.

---

## 7. Recommended Strategy

### Phase 1: Validate (1-2 weeks)

1. **Build roblox-luau-tycoon domain spec** — teaches the kernel to produce tycoon games
2. **Set up Roblox Studio MCP** — `claude mcp add robloxstudio`
3. **Produce 3 tycoon games** via execute-pipeline
4. **Publish to Roblox** — measure engagement over 30 days
5. **Track unit economics** — actual revenue vs projections

### Phase 2: Scale (month 2-3)

6. **Refine spec based on Phase 1 data** — what works, what doesn't
7. **Produce 10 games/month** — assembly line
8. **Add Fortnite Creative** — build UEFN spec
9. **Track portfolio revenue curve**

### Phase 3: Optimize (month 4+)

10. **Per-genre lessons** — tycoons vs obbies vs simulators
11. **A/B test monetization** — game pass pricing, placement
12. **Add engagement analytics** — feed back into game design
13. **Consider Minecraft/Steam** if Roblox + Fortnite validate

### First Target: Roblox Tycoon

**Why Roblox first:**
- Largest creator economy ($1.5B/year)
- Claude MCP writes Luau directly into Studio (54 tools)
- Tycoons are code-only (no 3D art needed)
- Proven revenue tiers ($50-50K/mo per game)
- 33% of earning creators have no CS background — validation that simple games monetize

**Why tycoons first:**
- Highest monetization among Roblox genres
- 45-90 minute sessions (long engagement = higher Creator Rewards)
- Progress addiction loop drives game pass sales
- Mechanical structure (currency → shop → upgrades → rebirth) maps perfectly to task decomposition
