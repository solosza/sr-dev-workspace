# Existing Platforms & Marketplaces

## Anthropic Claude Code Marketplace (Official)

**Status:** Production / Official

**URL:** [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | View in Claude Code via `/plugin` → Discover

**Features:**
- Official, Anthropic-curated directory
- Two tiers: `claude-plugins-official` (Anthropic-maintained) + `claude-community` (community submissions with review)
- Includes `/plugins` (official) and `/external_plugins` (partners/community)
- Automatically available in Claude Code
- Plugin discovery via `/plugin` command and web at claude.com/plugins

**Positioning:** High-trust, curated by Anthropic

**Limitations:** Curated review process means slower onboarding

---

## aitmpl.com

**Status:** Production

**URL:** [www.aitmpl.com](https://www.aitmpl.com/)

**Offerings:**
- 1000+ Claude Code templates
- Agents, commands, skills, MCP integrations, hooks, settings
- Multi-language support (135+ agents, 35+ curated skills, 42+ commands, 176+ plugins, 20 hooks, 15 rules, 7 templates, 14 MCP configs, 26 companion apps)

**Positioning:** Comprehensive component marketplace

**Limitations:** Focused on individual components (skills, commands) not holistic harnesses

---

## claudemarketplaces.com

**Status:** Production

**URL:** [claudemarketplaces.com](https://claudemarketplaces.com/)

**Features:**
- Community-curated directory of Claude Code plugins, skills, MCP servers
- Updated daily from GitHub
- Plugin browsing and discovery

**Positioning:** Real-time, community-driven index

**Limitations:** Discovery mechanism not detailed

---

## HuggingFace Skills Marketplace

**Status:** Production

**URL:** [huggingface.co/docs/hub/agents-skills](https://huggingface.co/docs/hub/agents-skills)

**Features:**
- Agent skills for AI/ML tasks (dataset creation, model training, evaluation)
- Cross-platform: Claude Code, Codex, Gemini CLI, Cursor
- Skills accessible via agent prompts
- Source catalog with marketplace.json pointing to individual skill repos

**Positioning:** ML/AI-focused agent skills

**Limitations:** Domain-specific (not general-purpose harnesses), primarily ML/data science tasks

---

## agentskills.io

**Status:** Production / Open Standard

**URL:** [agentskills.io](https://agentskills.io/)

**Features:**
- Open standard for agent skills
- Portable across 30+ agent tools (Claude Code, Cursor, Copilot, Codex, Gemini CLI, etc.)
- Emphasizes standardization and cross-platform compatibility

**Positioning:** Open standard, enabling portable skills across tools

**Limitations:** Standard definition only; no centralized marketplace

---

## netresearch/claude-code-marketplace

**Status:** Production

**URL:** [github.com/netresearch/claude-code-marketplace](https://github.com/netresearch/claude-code-marketplace)

**Features:**
- Curated Agent Skills collection
- Implements agentskills.io open standard
- Portable across Claude Code, Cursor, Copilot, Codex, Gemini CLI, and 30+ agents

**Positioning:** Production-ready curated skills using open standard

**Limitations:** GitHub-based distribution (not web UI); skills-only (not full harnesses)

---

## LobeHub Agent Skills Marketplace

**Status:** Production

**URL:** [lobehub.com/skills](https://lobehub.com/skills)

**Features:**
- Agent skills for Claude, Codex, ChatGPT
- Web UI with browsing and discovery
- Integration with LobeHub platform

**Positioning:** Web-first, user-friendly skills marketplace

**Limitations:** LobeHub-specific; not standalone

---

## GitHub Marketplace (Apps & Actions)

**Status:** Production

**URL:** [github.com/marketplace](https://github.com/marketplace)

**Features:**
- Distribute GitHub Apps, Actions, and integrations
- [ECC Tools](https://ecc.tools/) distributed as GitHub App
- Version control, reviews, issue tracking built-in

**Positioning:** Developer-native, tied to GitHub workflow

**Limitations:** Requires GitHub integration; not Claude-specific

---

## GitHub as Source-of-Truth

**Status:** De facto standard

**Pattern:** Multiple platforms (awesome-claude-code-toolkit, wshobson/agents, etc.) use GitHub repos as primary distribution

**Features:**
- Direct source code access
- Community contributions via PRs
- Version control built-in
- Discoverability via GitHub search

**Positioning:** Most harness projects ship from GitHub

**Limitations:** Requires users to manually find and configure; no built-in marketplace UI

---

## Summary Table

| Platform | Type | Primary Audience | Component Focus | Harness Support | Web UI | Curation |
|----------|------|------------------|-----------------|-----------------|--------|----------|
| Anthropic Official | Curated | All | Plugins/Skills | Limited | /plugin cmd | Anthropic |
| aitmpl.com | Directory | Developers | Components | No | Yes | Community |
| claudemarketplaces.com | Directory | Developers | Components | No | Yes | Community |
| HuggingFace | Marketplace | ML/AI | Skills | No | Yes | Community |
| agentskills.io | Standard | All | Skills | No | No (standard) | Open |
| LobeHub | Marketplace | Users | Skills | No | Yes | Community |
| GitHub Marketplace | Platform | Developers | Apps | Yes | Yes | GitHub |
| GitHub (direct) | Distribution | Developers | Any | Yes | No | None |

---

## Key Insights

1. **No specialized harness marketplace exists** — Most platforms focus on individual components (skills, commands, plugins)
2. **GitHub dominates harness distribution** — Projects ship from GitHub repos as source-of-truth
3. **Open standards emerging** — agentskills.io enables portability across tools
4. **Multi-platform support** — Successful harnesses target Claude Code + Cursor + Copilot + Codex + Gemini
5. **Official curated list** — Anthropic's marketplace is high-trust but curated (slower onboarding)
