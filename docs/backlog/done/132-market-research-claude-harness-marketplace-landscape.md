# Market Research — Claude Code Harness Marketplace Landscape

## Status
Open

## Priority
High — Determines distribution strategy for Isagawa Kernel and future harness monetization

## Summary

Research existing marketplaces and distribution platforms for Claude Code harnesses, automation templates, and agent skills. Determine competitive landscape, identify gaps, and recommend optimal distribution strategy: build custom harness marketplace vs. list on existing platforms (Anthropic, GitHub, HuggingFace, etc.).

This informs:
- Go-to-market strategy for Isagawa Kernel
- Potential revenue model (licensing, subscriptions, marketplace fees)
- Platform selection for distributing methodology-driven harnesses vs. individual components

## Design Documents

| Document | Purpose |
|----------|---------|
| [[132-market-research-claude-harness-marketplace-landscape/existing-platforms]] | Catalog of marketplaces and distribution channels with platform features and limitations |
| [[132-market-research-claude-harness-marketplace-landscape/competitive-analysis]] | Analysis of existing harness projects, positioning, and market share |
| [[132-market-research-claude-harness-marketplace-landscape/gaps-and-opportunities]] | Identified market gaps and business opportunities |
| [[132-market-research-claude-harness-marketplace-landscape/distribution-strategy]] | Recommendation: build vs. list strategy with rationale |

## Requirements

- Document all major Claude Code harness/automation marketplaces and their characteristics
- Analyze competitive landscape: existing harness projects, their positioning, audience
- Identify unmet market needs: what gaps exist in current offerings?
- Compare business models: transaction fees, subscriptions, open-source with support, etc.
- Determine optimal distribution: Anthropic Marketplace, GitHub Marketplace, custom marketplace, multi-channel
- Assess technical feasibility: can Isagawa Kernel integrate with multiple platforms?
- Evaluate revenue potential: subscription, licensing, marketplace fees, consulting
- Provide clear recommendation with pros/cons of each approach

## References

**Platforms discovered:**
- [Anthropic Claude Code Marketplace](https://github.com/anthropics/claude-plugins-official) — Official, curated plugin directory
- [aitmpl.com](https://www.aitmpl.com/) — 1000+ Claude templates, agents, commands, MCP integrations
- [claudemarketplaces.com](https://claudemarketplaces.com/) — Community-curated Claude Code plugins
- [HuggingFace Skills Marketplace](https://huggingface.co/docs/hub/agents-skills) — Agent skills for Claude, Codex, Gemini
- [agentskills.io](https://agentskills.io/) — Open standard for portable agent skills
- [LobeHub Agent Skills Marketplace](https://lobehub.com/skills) — Cross-platform agent skills
- [GitHub Marketplace](https://github.com/marketplace) — GitHub Apps including agent harnesses
- [netresearch/claude-code-marketplace](https://github.com/netresearch/claude-code-marketplace) — Curated agent skills (agentskills.io standard)

**Notable harness projects:**
- [wshobson/agents](https://github.com/wshobson/agents) — Multi-harness marketplace (Claude + Cursor + Copilot + Codex + Gemini)
- [Chachamaru127/claude-code-harness](https://github.com/Chachamaru127/claude-code-harness) — Development harness
- [affaan-m/ECC](https://github.com/affaan-m/ecc) — Agent harness performance optimization
- [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) — Comprehensive toolkit (135 agents, 35 skills, 42 commands)
- [ecc.tools](https://ecc.tools/) — ECC Tools as GitHub App

## Task Builder Input

- **Deliverable:** Comprehensive market analysis report with platform inventory, competitive positioning, and business model recommendation
- **Location:** `subproject:claude-harness-marketplace-research`
- **Scope:** RESEARCH
- **Constraints:**
  - No direct access to Morphex platform (search returned no results)
  - Recommendation must address multi-platform distribution (not just Anthropic)
  - Consider Isagawa Kernel's methodology-first positioning vs. component-level marketplaces
  - Research should inform go-to-market strategy for kernel and future commercial harness products
