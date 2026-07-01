# Existing Platforms — Feature Comparison & Distribution Channels

## Status
Research Complete

## Platform Inventory

| Platform | URL | Native Claude Code Support | Format(s) | Reach | Curation | Notes |
|----------|-----|:--:|----------|-------|----------|-------|
| **Claude Code Plugins Official** | [claudepluginhub.com](https://www.claudepluginhub.com/marketplaces/anthropics-claude-plugins-official) | ✓ Yes | Plugin | 100K+ | Anthropic-curated | Built into /plugin command; high discovery |
| **Claude Marketplace** | [claude.com/platform/marketplace](https://claude.com/platform/marketplace) | ✓ Yes | Plugin, App | 50K+ (enterprise) | Anthropic | Enterprise-focused; zero revenue cut model; launch partners (Replit, Harvey, Lovable) |
| **Agent Skills Hub** | [skills.sh](https://inference.sh/blog/skills/agent-skills-overview) | ✓ Yes | SKILL.md | 30+ agents | Community + Anthropic | Open standard (Dec 2025); primary discovery hub for portable skills; auto-indexes agentskills.io |
| **agentskills.io** | [agentskills.io](https://agentskills.io) | ✓ Yes | SKILL.md | Multi-harness | Community | Specification authority; GitHub-based registry; 30+ agents supported |
| **claudemarketplaces.com** | [claudemarketplaces.com](https://claudemarketplaces.com/) | ✓ Yes | Plugin, Skill | 100K+ | Community | Largest community index; daily GitHub updates; 1000+ listings |
| **claudeskills.info** | [claudeskills.info](https://claudeskills.info/) | ✓ Yes | Skill | 50K+ | Community | Skills-focused discovery; daily updates |
| **GitHub (Direct)** | [github.com](https://github.com) | ✓ Yes (manual) | SKILL.md, Code | Organic | Self-managed | Highest control; version control native; auto-indexed by agentskills.io |
| **netresearch Marketplace** | [github.com/netresearch/claude-code-marketplace](https://github.com/netresearch/claude-code-marketplace) | ✓ Yes | Agent Skills | Multi-agent | Curated | Focused on portability across 30+ agents; open standard |
| **wshobson/agents** | [github.com/wshobson/agents](https://github.com/wshobson/agents) | ✓ Yes | Multi-format | Multi-harness | Community | Multi-harness agentic plugin marketplace; harness-specific variants |

## Platform Characteristics

### Official Channels (Anthropic-Controlled)

#### Claude Code Plugins Official
- **Discovery:** Automatic /plugin command → "Discover" tab
- **Reach:** 100K+ Claude Code users
- **Curation:** Anthropic team reviews submissions
- **Timeline:** 2-4 weeks review
- **Cost:** Free
- **Monetization:** None (pending)

#### Claude Marketplace
- **Discovery:** Visited by enterprise procurement teams
- **Reach:** 50K+ enterprise customers
- **Curation:** High bar (launch partners only at start)
- **Timeline:** By application (selective)
- **Cost:** Free to list
- **Monetization:** Zero revenue cut (unique model); pending for developers

### Community Channels (GitHub-Based Discovery)

#### Agent Skills Hub (skills.sh + agentskills.io)
- **Discovery:** Primary hub for SKILL.md standard
- **Reach:** 30+ agents (Claude Code, Cursor, Copilot, Codex CLI, Gemini CLI, etc.)
- **Curation:** Community submissions; Anthropic maintains spec
- **Timeline:** Immediate (auto-index on GitHub publish)
- **Cost:** Free
- **Monetization:** Not yet defined

#### claudemarketplaces.com
- **Discovery:** Community-curated, daily GitHub crawler updates
- **Reach:** 100K+ community
- **Curation:** Community voting + editor curation
- **Timeline:** 1-2 days (automated)
- **Cost:** Free
- **Monetization:** None

#### GitHub Direct
- **Discovery:** Organic search, word-of-mouth
- **Reach:** Unlimited (internet-wide)
- **Curation:** None (self-managed)
- **Timeline:** Immediate
- **Cost:** Free
- **Monetization:** Self-determined

## Recommended Submission Strategy (Phase 1)

### Must-Haves
1. **Claude Code Plugins Official** → Highest discoverability, Anthropic endorsement
2. **Agent Skills Hub (skills.sh)** → Multi-harness portability (30+ agents), future-proof
3. **GitHub** → Version control, permanent home, auto-indexed

### Nice-to-Have
4. **claudemarketplaces.com** → High community reach, minimal effort (automated)
5. **claudeskills.info** → Skills-specific discovery

### Wait-List (Phase 2 Decision)
- **Claude Marketplace** → Enterprise-only; revisit after Phase 1 traction
- **netresearch/wshobson** → Custom lists; evaluate after understanding user base

## Format Compatibility

### Plugin Format (Claude Code Native)
- What: .plugin file or manifest JSON
- Supported by: Claude Code, GitHub Copilot (partial)
- Discovery: Official Claude Code Plugins directory
- Status: Mature (2025+)

### SKILL.md Format (Agent Skills Standard)
- What: Markdown file with YAML frontmatter + instructions
- Supported by: Claude Code, Cursor, Copilot, Codex CLI, Gemini CLI, Cline, Windsurf, OpenCode (9+ tools as of 2026)
- Discovery: skills.sh, agentskills.io, GitHub, community marketplaces
- Status: **NEW standard (Dec 2025); early adoption phase**

### MCP Server Format
- What: Model Context Protocol servers
- Supported by: Claude Desktop, some Claude Code integrations
- Discovery: Claude Desktop marketplace (separate ecosystem)
- Status: Emerging

## Key Insight: Agent Skills Spec is the Future

As of December 2025, Agent Skills (SKILL.md) is the emerging standard for portable agent knowledge across 30+ tools. **Early adoption now = higher compatibility window + first-mover advantage.**

All major platforms (Anthropic, Google, OpenAI community, GitHub) support it. GitHub-based discovery means automatic indexing across all platforms. **This is the recommended distribution vehicle for Phase 1.**
