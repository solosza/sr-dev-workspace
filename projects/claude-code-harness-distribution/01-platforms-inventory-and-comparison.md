# Platforms Inventory and Comparison

**Backlog:** 131 — Claude Code Harness Distribution Strategy
**Task:** 002
**Date:** 2026-06-15
**Status:** Complete

---

## Executive Summary

The Claude Code harness distribution landscape comprises 9 identified platforms spanning official Anthropic channels, community-driven marketplaces, and GitHub-based discovery mechanisms. This report inventories each platform, compares their characteristics, and identifies the optimal multi-platform submission strategy for distributing the Isagawa Kernel as a Claude Code harness.

The key finding: **Agent Skills (SKILL.md) is the emerging universal standard**, supported by 30+ AI coding agents as of early 2026. Early adoption of this format provides maximum portability across tools (Claude Code, Cursor, Copilot, Codex CLI, Gemini CLI, Cline, Windsurf, OpenCode) while minimizing maintenance burden through a single-source distribution approach.

No single platform dominates discovery. Successful distribution requires listing on 3-5 platforms simultaneously, with format-specific tuning for each channel's curation model and audience expectations.

---

## Platform Inventory — 9-Platform Comparison Matrix

| # | Platform | URL | Claude Code Native | Format(s) | Estimated Reach | Curation Model | Listing Cost | Monetization | Review Timeline |
|---|----------|-----|--------------------|-----------|-----------------|----------------|-------------|--------------|-----------------|
| 1 | Claude Code Plugins Official | claudepluginhub.com | Yes | Plugin | 100K+ users | Anthropic-curated | Free | None (pending) | 2-4 weeks |
| 2 | Claude Marketplace | claude.com/platform/marketplace | Yes | Plugin, App | 50K+ enterprise | Anthropic (selective) | Free | Zero revenue cut | By application |
| 3 | Agent Skills Hub (skills.sh) | inference.sh/blog/skills | Yes | SKILL.md | 30+ agents | Community + Anthropic | Free | Not yet defined | Immediate |
| 4 | agentskills.io | agentskills.io | Yes | SKILL.md | Multi-harness | Community | Free | Not yet defined | Immediate (auto-index) |
| 5 | claudemarketplaces.com | claudemarketplaces.com | Yes | Plugin, Skill | 100K+ community | Community voting + editor | Free | None | 1-2 days (automated) |
| 6 | claudeskills.info | claudeskills.info | Yes | Skill | 50K+ community | Community | Free | None | Daily updates |
| 7 | GitHub (Direct) | github.com | Yes (manual) | SKILL.md, Code | Unlimited (organic) | Self-managed | Free | Self-determined | Immediate |
| 8 | netresearch Marketplace | github.com/netresearch/claude-code-marketplace | Yes | Agent Skills | Multi-agent | Curated | Free | None | Community review |
| 9 | wshobson/agents | github.com/wshobson/agents | Yes | Multi-format | Multi-harness | Community | Free | None | Community review |

### Matrix Key Observations

1. **All 9 platforms are free to list** — no financial barrier to multi-platform distribution
2. **Monetization is absent or pending** across all platforms — revenue generation is not yet a factor in platform selection
3. **Review timelines vary from immediate to 4 weeks** — official channels are slower, community channels are near-instant
4. **SKILL.md format is supported by 7 of 9 platforms** — the clear convergence point for format standardization
5. **Reach estimates are additive** — listing on all platforms provides cumulative exposure, not overlapping audiences

---

## Official Channels (Anthropic-Controlled)

### Claude Code Plugins Official

The primary discovery channel for Claude Code users. Built directly into the Claude Code `/plugin` command's "Discover" tab, this channel provides the highest organic discoverability for any Claude Code extension.

**Strengths:**
- Highest discoverability — users encounter plugins during normal Claude Code workflow
- Anthropic brand endorsement — listed plugins carry implicit trust signal
- 100K+ active Claude Code user base as potential audience
- Direct integration with Claude Code's plugin installation flow

**Weaknesses:**
- 2-4 week review cycle creates lag between submission and listing
- Anthropic curation standards may require specific formatting or compliance
- No monetization path currently available
- Plugin format is Claude Code-specific (not portable to other agents)

**Submission Requirements:**
- Plugin manifest file conforming to Claude Code plugin specification
- Documentation meeting Anthropic's quality standards
- Functional testing across supported platforms

**Strategic Value:** Must-have. First-priority submission target due to highest organic reach within the Claude Code ecosystem.

### Claude Marketplace

An enterprise-focused marketplace operated by Anthropic with a notable zero-revenue-cut model. Currently in selective launch phase with prominent launch partners (Replit, Harvey, Lovable).

**Strengths:**
- Enterprise procurement audience — higher-value potential users
- Zero revenue cut model — unique among AI marketplaces
- Anthropic backing provides credibility for enterprise sales
- 50K+ enterprise customer base

**Weaknesses:**
- Currently selective (launch partners only at start)
- Enterprise-focused curation may exclude developer tools or open-source harnesses
- Application-based acceptance — no guaranteed listing
- Separate from the Claude Code plugin ecosystem

**Strategic Value:** Wait-list for Phase 2. The enterprise focus and selective admission make this a poor fit for initial distribution. Revisit after demonstrating traction on other platforms (>100 installs/month).

---

## Community Channels (GitHub-Based Discovery)

### Agent Skills Hub (skills.sh + agentskills.io)

The primary hub for the Agent Skills (SKILL.md) open standard, maintained by the community with Anthropic participation. This is the canonical discovery mechanism for portable agent skills that work across 30+ AI coding agents.

**Strengths:**
- Multi-harness portability — single SKILL.md works across Claude Code, Cursor, Copilot, Codex CLI, Gemini CLI, Cline, Windsurf, OpenCode, and 20+ more
- Anthropic maintains the specification — standard has institutional backing
- Auto-indexing from GitHub — publish to GitHub and skills.sh discovers it automatically
- Future-proof — as new agents adopt the spec, existing skills gain compatibility for free

**Weaknesses:**
- Relatively new standard (December 2025) — ecosystem still maturing
- Discovery primarily within developer communities already aware of Agent Skills
- No monetization framework yet
- Smaller individual reach per platform compared to Claude Code Plugins Official

**Submission Requirements:**
- SKILL.md file conforming to Agent Skills specification (YAML frontmatter + markdown instructions)
- Published to public GitHub repository
- Tagged with appropriate agent compatibility metadata

**Strategic Value:** Must-have. The Agent Skills standard is the emerging universal format. Early adoption provides first-mover advantage and maximum portability.

### agentskills.io

The specification authority for the Agent Skills standard. Functions as a GitHub-based registry that automatically indexes SKILL.md files from public repositories.

**Strengths:**
- Automatic discovery — GitHub publication triggers indexing
- Multi-harness compatibility documentation
- Specification authority — defines what SKILL.md should contain
- Zero-effort listing (if already on GitHub with SKILL.md)

**Weaknesses:**
- Primarily serves as a specification site, not a discovery marketplace
- Traffic is developer-focused and spec-curious, not end-user browsing
- No curation or quality signals beyond presence in the registry

**Strategic Value:** Automatic benefit from GitHub + SKILL.md publication. No additional effort required beyond having a compliant SKILL.md in the repo.

### claudemarketplaces.com

The largest community-driven index of Claude Code extensions, updated daily via GitHub crawler. Features community voting and editor curation for quality signals.

**Strengths:**
- Largest community reach (100K+ community members)
- Daily automated updates from GitHub — minimal maintenance burden
- Community voting provides social proof and quality signals
- 1000+ listings — active, growing ecosystem
- Supports both Plugin and Skill formats

**Weaknesses:**
- Community-curated — less authoritative than Anthropic channels
- No monetization framework
- Quality varies — listings range from production-ready to experimental
- Automated crawling may index incomplete or draft submissions

**Submission Requirements:**
- GitHub repository with Claude Code extension
- Optional manual submission for faster listing
- Community engagement improves visibility (voting, comments)

**Strategic Value:** Nice-to-have with high value. The automated crawling means near-zero effort for listing, while the community reach provides significant exposure. Recommended as a Phase 1 target.

### claudeskills.info

A skills-focused discovery platform for Claude Code, updated daily. Narrower focus than claudemarketplaces.com — exclusively targets skills rather than broader plugins or apps.

**Strengths:**
- Skills-specific audience — visitors are specifically seeking skills/harnesses
- Daily updates keep listings current
- 50K+ community reach
- Focused discovery reduces noise from unrelated listings

**Weaknesses:**
- Narrower audience than broader marketplaces
- Less community interaction (voting, reviews) than claudemarketplaces.com
- No monetization

**Strategic Value:** Nice-to-have. Useful for skills-focused discovery but lower priority than the primary platforms.

### GitHub Direct

The permanent home for any open-source harness. Provides maximum control over presentation, versioning, and documentation. Functions as the canonical source that all other platforms reference or auto-index.

**Strengths:**
- Maximum control — complete ownership of listing presentation, README, releases
- Version control native — harness updates flow through normal git workflow
- Auto-indexed by agentskills.io and community crawlers
- Unlimited organic reach via GitHub search, trending, and social sharing
- Self-determined monetization (sponsorships, dual licensing, etc.)

**Weaknesses:**
- No built-in discovery mechanism beyond GitHub search and trending
- Requires active community building and marketing to drive traffic
- Self-managed curation means no quality signals from platform operators

**Strategic Value:** Must-have. The canonical source repository. All other platform listings should reference the GitHub repo as the authoritative source.

### netresearch Marketplace

A curated GitHub-based marketplace focused on portability across 30+ AI coding agents. Emphasizes the Agent Skills open standard.

**Strengths:**
- Portability focus aligns with SKILL.md strategy
- Multi-agent compatibility testing and documentation
- Open standard advocacy — promotes best practices
- Community curation with quality standards

**Weaknesses:**
- Smaller audience than mainstream platforms
- GitHub-based (not a standalone discovery site)
- Limited traffic compared to claudemarketplaces.com or skills.sh

**Strategic Value:** Phase 2 evaluation. Worth monitoring for community growth and cross-pollination with other Agent Skills platforms.

### wshobson/agents

A multi-harness agentic plugin marketplace on GitHub, supporting harness-specific variants (Claude Code-optimized, Cursor-optimized, etc.).

**Strengths:**
- Multi-format support — can list harness variants for different tools
- Multi-harness perspective — useful for understanding variant demand
- Community-driven with active contributors

**Weaknesses:**
- Smaller audience and contributor base
- GitHub-based (limited discoverability outside GitHub)
- Less established than other community platforms

**Strategic Value:** Phase 2 evaluation. Useful reference for understanding multi-harness variant demand but lower priority for initial distribution.

---

## Format Compatibility

### Plugin Format (Claude Code Native)

The original extension format for Claude Code, defined by Anthropic's plugin specification.

| Attribute | Detail |
|-----------|--------|
| **Format** | .plugin file or manifest JSON |
| **Supported By** | Claude Code, GitHub Copilot (partial) |
| **Discovery** | Official Claude Code Plugins directory |
| **Maturity** | Mature (2025+) |
| **Portability** | Low — Claude Code-specific |

Best suited for: Claude Code Plugins Official submission where maximum native integration is required.

### SKILL.md Format (Agent Skills Standard)

The emerging universal standard for portable agent knowledge, introduced December 2025.

| Attribute | Detail |
|-----------|--------|
| **Format** | Markdown file with YAML frontmatter + instructions |
| **Supported By** | Claude Code, Cursor, Copilot, Codex CLI, Gemini CLI, Cline, Windsurf, OpenCode (9+ tools) |
| **Discovery** | skills.sh, agentskills.io, GitHub, community marketplaces |
| **Maturity** | New standard (Dec 2025); early adoption phase |
| **Portability** | High — single source, multi-agent compatibility |

Best suited for: All community channels and future-proofing. Recommended primary format for Isagawa Kernel distribution.

### MCP Server Format

Model Context Protocol servers, primarily for Claude Desktop integrations.

| Attribute | Detail |
|-----------|--------|
| **Format** | MCP server implementation |
| **Supported By** | Claude Desktop, some Claude Code integrations |
| **Discovery** | Claude Desktop marketplace (separate ecosystem) |
| **Maturity** | Emerging |
| **Portability** | Medium — growing adoption but separate from Agent Skills |

Best suited for: Claude Desktop-specific distribution. Not recommended for primary harness distribution — different ecosystem from Claude Code.

---

## Key Insight: Agent Skills as the Emerging Standard

As of December 2025, the Agent Skills specification (SKILL.md) represents the convergence point for portable agent knowledge across the AI coding tools ecosystem. The specification is:

1. **Backed by Anthropic** — the specification maintainer has institutional support
2. **Adopted by 30+ agents** — broadest cross-tool compatibility of any format
3. **Auto-indexed** — GitHub publication triggers automatic discovery across multiple platforms
4. **Single-source** — one SKILL.md file works everywhere, reducing maintenance to a single artifact
5. **Early adoption phase** — first-mover advantage is available now, before the ecosystem matures

**Recommendation:** Adopt SKILL.md as the primary distribution format for the Isagawa Kernel. Maintain a Plugin format submission for Claude Code Plugins Official to maximize native integration, but invest primarily in the SKILL.md ecosystem for long-term portability and reach.

---

## Recommended Submission Strategy

### Phase 1 — Must-Haves (Week 1-4)

| Priority | Platform | Format | Expected Timeline | Effort |
|----------|----------|--------|--------------------|--------|
| 1 | Claude Code Plugins Official | Plugin | 2-4 weeks review | Medium (format conversion) |
| 2 | Agent Skills Hub (skills.sh) | SKILL.md | Immediate | Low (write SKILL.md) |
| 3 | GitHub Direct | SKILL.md + Code | Immediate | Already done (repo exists) |

### Phase 1 — Nice-to-Haves (Week 2-4)

| Priority | Platform | Format | Expected Timeline | Effort |
|----------|----------|--------|--------------------|--------|
| 4 | claudemarketplaces.com | Auto-indexed | 1-2 days (automated) | Zero (auto-crawl) |
| 5 | claudeskills.info | Auto-indexed | Daily updates | Zero (auto-crawl) |

### Phase 2 — Conditional (After 100+ installs/month)

| Priority | Platform | Format | Trigger |
|----------|----------|--------|---------|
| 6 | Claude Marketplace | Plugin/App | Enterprise demand validated |
| 7 | netresearch Marketplace | Agent Skills | Community growth validated |
| 8 | wshobson/agents | Multi-format | Multi-harness variant demand validated |

---

## References

### Platform URLs

- Claude Code Plugins Official: https://www.claudepluginhub.com/marketplaces/anthropics-claude-plugins-official
- Claude Marketplace: https://claude.com/platform/marketplace
- Agent Skills Hub: https://inference.sh/blog/skills/agent-skills-overview
- agentskills.io: https://agentskills.io
- claudemarketplaces.com: https://claudemarketplaces.com/
- claudeskills.info: https://claudeskills.info/
- GitHub: https://github.com
- netresearch Marketplace: https://github.com/netresearch/claude-code-marketplace
- wshobson/agents: https://github.com/wshobson/agents

### Source Documents

- Design doc: `docs/backlog/131-market-research-claude-code-harness-distribution-strategy/existing-platforms.md`
- Backlog: `docs/backlog/131-market-research-claude-code-harness-distribution-strategy.md`

---

*Generated for Backlog 131 — Task 002*
*Kernel domain: sr_dev*
*Date: 2026-06-15*
