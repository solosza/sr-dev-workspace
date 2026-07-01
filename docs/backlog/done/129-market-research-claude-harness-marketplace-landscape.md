# Claude Harness Marketplace Landscape Research

## Status
Complete

## Priority
High — Informs product strategy for Isagawa Kernel distribution

## Summary
Research existing Claude Code harness marketplaces and agent distribution platforms to determine whether to build a dedicated harness marketplace or distribute via existing platforms. Analyze competitive landscape, identify gaps, and recommend build vs buy strategy.

## Findings

### Existing Claude Harness Distribution Platforms

**Eight major agent marketplaces exist in 2026, each serving distinct audiences:**

1. **[Claude Skills](https://platform.claude.com/docs/en/managed-agents/overview)** (Anthropic official) — Free distribution, editorial review, official extension mechanism for Claude. No monetization model yet.

2. **[Claude Marketplaces (claudemarketplaces.com)](https://claudemarketplaces.com/)** — Largest community-curated directory of Claude Code skills, plugins, MCP servers. Updated daily from GitHub.

3. **[Skills.sh](https://skills.sh)** (Vercel-backed) — npm-style package manager for skills. Launched January 2026. `npx skills add` command interface.

4. **[GPT Store](https://openai.com/gpt-store/)** — OpenAI's marketplace. Revenue-share model. Limited Claude native support.

5. **[MCP Hubs](https://modelcontextprotocol.io/)** — Community-run, no central gatekeeper. Distributed model discovery.

6. **[Hugging Face Spaces](https://huggingface.co/spaces)** — Agent marketplace. General AI audience, not harness-specific.

7. **[LangChain Hub](https://hub.langchain.com/)** — Framework-centric, not harness-specific.

8. **[Replit Agent Market](https://replit.com/)** — Direct-sale model. Runtime-bundled.

**Specific Claude Harness Projects:**

- **[Claude Code Dedicated Development Harness](https://github.com/Chachamaru127/claude-code-harness)** — Open source (1.7K+ stars). Plan→Work→Review cycle. Daily releases.
- **[Everything Claude Code (ECC)](https://medium.com/@tentenco/everything-claude-code-inside-the-82k-star-agent-harness-thats-dividing-the-developer-community-4fe54feccbc1)** — 82K GitHub stars, 10.7K forks. Most-starred Claude configuration repository.
- **[Multi-Harness Agentic Plugin Marketplace](https://github.com/wshobson/agents)** — 84 plugins, 192 agents, 156 skills, 102 commands. Cross-platform consumption (Claude Code, Codex CLI, Cursor, OpenCode, Gemini CLI, GitHub Copilot) from single Markdown source.
- **[Netresearch Claude Code Marketplace](https://github.com/netresearch/claude-code-marketplace)** — Curated skills collection, open standard (agentskills.io). Portable across 30+ agent platforms.

### Platforms User Mentioned

**Morphex** — NOT FOUND in current market (2026). May be user-proposed or niche platform.

**Poe** — [Quora's AI model aggregator platform](https://poe.com/). NOT suitable for harness distribution. Model aggregator, not agent deployment platform. No runtime, integration, or customer-facing deployment capabilities.

**GPT Store** — [OpenAI's marketplace](https://openai.com/gpt-store/). Works with Claude but primarily GPT-focused. Revenue-share model available but limited Claude native harness category.

### Market Gaps

**No dedicated harness-specific marketplace exists with:**
1. **Monetization** — Claude Skills is free. GPT Store/Replit have revenue share but aren't Claude-native.
2. **Harness-as-product** — Existing platforms treat harnesses as "configs" or "skills," not primary distribution units.
3. **Cross-platform harness consumption** — Multi-harness marketplace shows demand but not widely known.
4. **Built-in template + enforcement distribution** — No marketplace bundles protocol + hooks + enforcement as installable unit.
5. **Harness version management** — Auto-update and backward compatibility tracking missing.

### Key Market Insight

**Multi-marketplace strategy is winning approach (2026):** Agencies publish same capability as:
- Skill (Claude Skills, free, lead generation)
- GPT (GPT Store, revenue share)
- MCP Server (MCP Hubs, no gatekeeper)
- Hugging Face Space (Hugging Face Spaces, freemium)
- Direct distribution (GitHub, no intermediary)

Rather than single marketplace bet, successful products land across 4–5 platforms with platform-specific tuning.

### Competitive Advantage Analysis: Build vs Buy

#### Option 1: Build Dedicated Harness Marketplace

**Advantages:**
- Harness-native positioning (not just "skills")
- Built-in monetization model (Claude Skills has none)
- Bundled enforcement distribution (protocol + hooks + commands)
- Standardized harness template (discovery, version management, auto-update)
- Positioned for cross-platform consumption (Claude Code, Cursor, Codex, Gemini CLI, Copilot, etc.)

**Disadvantages:**
- Requires audience cultivation (all other platforms have built-in user bases)
- Fragmented market (8 existing platforms, network effects favor consolidation)
- High barrier to discoverability (new marketplace must compete with established hubs)
- SEO/discovery cost to reach harness builders

#### Option 2: Distribute Across Existing Platforms (Multi-Marketplace)

**Advantages:**
- Instant access to millions of users (leveraging existing platforms)
- Revenue diversification (free + paid models across channels)
- Lower distribution cost (no marketplace maintenance)
- Platform-native integrations already built

**Disadvantages:**
- Less harness-specific positioning (skills/GPTs/spaces are generic)
- No control over discovery/visibility ranking
- Platform dependency (algorithm changes, policy changes affect distribution)
- Harder to establish harness as distinct product category

#### Option 3: Hybrid — List on Existing + Build Community Hub (Recommended)

**Strategy:**
1. **Multi-marketplace distribution** — List Isagawa Kernel on Skills.sh, Claude Marketplaces, MCP Hubs, Hugging Face
2. **GitHub as distribution source** — Maintain canonical repo (isagawa-co/kernel), let platforms index
3. **Community hub** (custom lightweight site) — Curate harness ecosystem, link to all marketplaces, build SEO for "Claude harness"
4. **Harness template + enforcer** — Publish as installable package on all platforms
5. **Revenue model** — Dual track: free distribution (lead gen) + paid consulting/custom harnesses

### Recommendations

1. **Short-term (Months 1–3):** Multi-marketplace distribution
   - Submit Isagawa Kernel to: Skills.sh, Claude Marketplaces, MCP Hubs, Hugging Face Spaces
   - Optimize GitHub visibility (stars, forks, documentation)
   - Build SEO targeting "Claude harness," "agent framework Claude," "Isagawa Kernel"

2. **Medium-term (Months 3–6):** Community positioning
   - Create lightweight harness community hub (curate ecosystem, link to platforms)
   - Position Isagawa Kernel as the "production harness" for Claude Code
   - Case studies from current users (job application automation, RT compliance, etc.)

3. **Long-term (Months 6+):** Marketplace consolidation
   - If demand emerges for harness-only distribution, consider building
   - Monitor market consolidation (Skills.sh vs Claude Marketplaces leadership)
   - Differentiate through enforcement layer + production deployment (unlike generic skill marketplaces)

### Decision

**Recommend: Hybrid approach (Option 3) — Multi-marketplace distribution + community hub**

Rationale:
- Harness marketplace market is immature (8 existing platforms, no clear winner)
- First-mover advantage in distribution > first-mover in building new marketplace
- Existing platforms have immediate reach (millions of users)
- Community hub differentiates without marketplace maintenance costs
- Revenue model benefits from multiple channels
- Can pivot to dedicated marketplace if demand emerges

## Task Builder Input

- **Deliverable:** Backlog entry + distribution strategy recommendation
- **Status:** Complete
- **Next Steps:** Implement multi-marketplace submission process (backlog 130)
- **Sources:** Web research, marketplace platform audits, competitive analysis

## References

- [Claude Code Plugin Marketplaces (Official)](https://code.claude.com/docs/en/plugin-marketplaces)
- [Claude Marketplaces Directory](https://claudemarketplaces.com/)
- [Skills.sh — AI Skill Package Manager](https://skills.sh)
- [Claude Code Harness — GitHub](https://github.com/Chachamaru127/claude-code-harness)
- [Multi-Harness Agentic Marketplace](https://github.com/wshobson/agents)
- [Netresearch Claude Marketplace](https://github.com/netresearch/claude-code-marketplace)
- [Claude Managed Agents — Official Docs](https://platform.claude.com/docs/en/managed-agents/overview)
- [AI Agent Marketplaces 2026: Discovery and Distribution](https://www.digitalapplied.com/blog/ai-agent-marketplaces-2026-discovery-distribution)
- [Agent Harness Architecture Explained](https://www.mindstudio.ai/blog/what-is-agent-harness-architecture-explained)
