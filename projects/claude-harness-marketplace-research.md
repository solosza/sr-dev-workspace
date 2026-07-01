# Claude Code Harness Marketplace Research

## Research Date
2026-06-14

## Executive Summary

**Finding:** Multiple existing marketplaces already support Claude Code harnesses. Building a custom marketplace is NOT recommended. Instead, leverage existing platforms where distribution is already mature.

**Recommendation:** LIST on existing platforms rather than build custom marketplace. The ecosystem is fragmented but established.

---

## Existing Platforms & Marketplace Options

### 1. **Official/Anthropic-Supported**

| Platform | URL | Claude Support | Harness Support | Monetization | Status |
|----------|-----|---|---|---|---|
| Claude Plugins Directory | anthropic | Yes (native) | Yes | Pending | Official, 101 vetted + 68 partner plugins |
| Claude Desktop Connectors | platform.claude.com | Yes (native) | Yes | Pending | Official MCP registry |

**Key:** These are first-class distribution channels with native Claude Code integration. No custom harness format needed — they use standard plugins/skills/MCP servers.

### 2. **Community-Maintained (High Traffic)**

| Platform | URL | Claude Support | Format | Community | Discovery |
|----------|-----|---|---|---|---|
| claudemarketplaces.com | claudemarketplaces.com | Yes | Plugins/Skills/MCP | Large | Daily updates from GitHub |
| aitmpl.com | aitmpl.com | Yes (primary) | Agent Harness + Skills | Moderate | 1000+ pre-built components |
| agentskills.io | agentskills.io | Yes (primary) | Skills (open standard) | Growing | Netresearch curated catalog |

**Key:** These three are THE primary community discovery channels for Claude Code harnesses. They aggregate from GitHub and provide searchable directories.

### 3. **Multi-Agent Platforms (Broader Than Claude)**

| Platform | URL | Claude Support | Format | Reach | Monetization |
|----------|-----|---|---|---|---|
| Poe | poe.com | Yes | Bots/Agents | Large | Pays creators (per-message) |
| GPT Store | openai | Partial | GPTs | Large | Pending monetization |
| Hugging Face Spaces | huggingface.co | Yes | Deployable agents | Very large | Open source model |

**Key:** These platforms reach beyond Claude users but Claude Code harnesses must be adapted to their format.

### 4. **Enterprise/Developer-Focused**

| Platform | URL | Claude Support | Use Case | Distribution |
|----------|-----|---|---|---|
| AWS Marketplace | aws.amazon.com | Yes (via integrations) | Enterprise agents | Broad cloud distribution |
| Salesforce AppExchange | salesforce | Partial | CRM agents | Enterprise salesforce users |
| GitHub Marketplace | github.com | Yes | Tools/Actions | Developer community |

**Key:** Limited relevance for pure harnesses; better for enterprise integrations.

---

## Technical Harness Formats in Distribution

### What Gets Distributed

1. **Plugins** (Claude Code native)
   - Bundle: Skills + Hooks + MCP configs
   - Format: JSON manifest + source code
   - Platforms: Anthropic official, claudemarketplaces.com

2. **Skills** (Open standard via agentskills.io)
   - Format: Portable across 30+ agents
   - Platform: agentskills.io (Netresearch)
   - Includes: AGENTS.md, procedures, resources

3. **Agent Harnesses** (Full stack)
   - Format: YAML/JSON config + enforcement hooks
   - Platforms: aitmpl.com, GitHub repos
   - Includes: Hooks, state management, lifecycle

4. **MCP Servers**
   - Format: Standard model context protocol
   - Platforms: Claude Desktop, Anthropic registry, community

---

## Competitive Landscape (Q2 2026)

### Eight Marketplaces That Matter

1. **Anthropic's Official Plugin Directory** — native distribution, highest trust
2. **claudemarketplaces.com** — largest community index
3. **aitmpl.com** — agent harness optimization focus
4. **agentskills.io** — open standards advocacy
5. **Poe** — monetization available, broad reach
6. **GPT Store** — OpenAI ecosystem (less relevant for Claude)
7. **Hugging Face Spaces** — open source models + agents
8. **GitHub Marketplace** — for tool integrations

**Key Insight:** Successful teams in 2026 publish once and distribute to 4-6 platforms with format-specific tuning (Skill + Plugin + MCP + Hugging Face Space).

---

## Gaps Analysis

### What Exists
- ✅ Mature plugin/skill distribution infrastructure
- ✅ Open standard (agentskills.io) for format portability
- ✅ Multiple discovery platforms (3+ high-traffic directories)
- ✅ Creator monetization (Poe pays; others pending)
- ✅ Enterprise distribution (AWS, Salesforce)

### What's Missing
- ❌ Specialized harness marketplace (focused, curated harness selection)
- ❌ Harness-to-harness composability registry
- ❌ Performance/benchmark marketplace (which harnesses are fastest?)
- ❌ Vertical-specific harness catalogs (e.g., "Healthcare Harnesses", "Finance Harnesses")
- ❌ Harness monetization clarity (Poe has it, others don't)

---

## Build vs. List Decision Framework

### List on Existing Platforms ✅ RECOMMENDED
**When:** If goal is maximum distribution with minimal effort

**Pros:**
- Zero marketplace infrastructure cost
- Instant access to 100K+ potential users
- Built-in discoverability (search, categories, reviews)
- Creator monetization already available (Poe) or pending (Anthropic)
- Format-agnostic: can list same harness as Plugin + Skill + MCP

**Cons:**
- Limited control over discovery/branding
- Competition from thousands of other harnesses
- Fragmented audience across 3+ platforms
- No vertical specialization

**Cost:** Time to package harness for 4-6 platforms (1-2 weeks per harness)

### Build Custom Marketplace ❌ NOT RECOMMENDED
**When:** If you have 50+ proprietary harnesses and need vertical control

**Pros:**
- Full control over discovery/curation
- Can specialize (healthcare harnesses only, etc.)
- Brand differentiation
- Can enforce quality/security standards

**Cons:**
- 6-12 months to build + iterate
- $200K-500K in development/infrastructure
- Must bootstrap user base (no existing traffic)
- Creator incentives must be invented (payout structure, rev-share, etc.)
- Maintenance burden (keep harnesses updated, security reviews)

**Cost:** 6-12 months + $200K-500K + ongoing maintenance

---

## Recommendation Summary

### For Independent Harness Creators
1. List on **claudemarketplaces.com** (free, passive submission)
2. List on **aitmpl.com** (agent harness focused)
3. List on **agentskills.io** (if follows open standard)
4. List on **Poe** (only monetization option today)
5. Consider **GPT Store** for reach (but test format compatibility)

**Action:** Package harness as Plugin + Skill, submit to 3-4 platforms. Done in 2-3 weeks.

### For Harness Platform/Tooling Companies
1. **DO build** if you have:
   - 50+ proprietary harnesses to distribute
   - Vertical specialization (healthcare/finance/legal)
   - Revenue model (enterprise licensing, paid harnesses)
   - Team capacity (6+ engineers, 6-12 months)

2. **DO NOT build** if:
   - Goal is general-purpose harness discovery
   - Limited vertical differentiation
   - Trying to compete with Anthropic/Poe

### Alternative: Specialize Within Existing Platforms
Instead of building, create authority within existing platforms:
- Become curator on claudemarketplaces.com (e.g., "Healthcare Harnesses" collection)
- Build educational content + vetted harness bundles
- Establish marketplace reputation as trusted source
- Minimal cost, maximum reach

---

## Sources Reviewed

1. [GitHub - netresearch/claude-code-marketplace](https://github.com/netresearch/claude-code-marketplace) — Agentskills.io reference implementation
2. [claudemarketplaces.com](https://claudemarketplaces.com/) — Community directory
3. [aitmpl.com](https://www.aitmpl.com/) — Agent harness optimization system
4. [Anthropic Claude API Docs - Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview)
5. [Top AI Agent Marketplaces - Fastio](https://fast.io/resources/top-ai-agent-marketplaces/) — Competitive analysis
6. [Claude Skills and MCP Servers in 2026: A Practitioner's Guide](https://codersera.com/blog/claude-skills-mcp-servers-practitioner-guide-2026/)
7. [Claude Code Plugin Marketplace Guide (2026)](https://www.agensi.io/learn/claude-code-plugin-marketplace-guide)
8. [Build vs Buy for Agent Harnesses](https://dev.to/arezvov/build-vs-buy-for-agent-harnesses-the-real-question-123e)

---

## Next Actions

1. If building harness: List on existing platforms first (validate demand)
2. If specializing: Apply to become curator on claudemarketplaces.com or aitmpl.com
3. If enterprise: Evaluate Salesforce/AWS marketplaces for vertical integration
