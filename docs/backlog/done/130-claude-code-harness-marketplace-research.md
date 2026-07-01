# Claude Code Harness Marketplace Research & Distribution Strategy

## Status
Complete — Research conducted 2026-06-14

## Priority
High — Informs product strategy for harness distribution and marketplace positioning

## Summary
Comprehensive research on existing Claude Code harness marketplaces, distribution platforms, and competitive landscape. Determines whether to build a custom harness marketplace or leverage existing platforms. **Key finding: LIST on existing platforms, DO NOT build custom marketplace.**

## Deliverables

1. **Marketplace Inventory** — Identified 8 major platforms supporting Claude Code harness distribution
   - Official channels (Anthropic Plugin Directory, Claude Desktop MCP registry)
   - Community-maintained (claudemarketplaces.com, aitmpl.com, agentskills.io)
   - Multi-agent platforms (Poe, GPT Store, Hugging Face Spaces)
   - Enterprise channels (AWS, Salesforce, GitHub)

2. **Platform Analysis** — For each platform:
   - Native Claude Code support (yes/no)
   - Harness format support (Plugin/Skill/MCP/Agent Harness)
   - Traffic/reach (100K+ potential users across platforms)
   - Monetization models (Poe pays creators; others pending)
   - Submission requirements (free or paid)

3. **Competitive Landscape** — Eight marketplaces currently matter in Q2 2026
   - Fragmented ecosystem (no single dominant harness marketplace)
   - Successful teams distribute to 4-6 platforms with format-specific tuning
   - Open standard (agentskills.io) enables portable distributions

4. **Gaps Analysis** — What's missing from current ecosystem
   - Specialized harness marketplace (does NOT exist)
   - Harness composability registry (does NOT exist)
   - Performance/benchmark marketplace (does NOT exist)
   - Vertical-specific harness catalogs (does NOT exist)
   - Clear harness monetization (only Poe has it)

5. **Build vs. List Decision Framework** — Detailed analysis
   - **LIST on existing platforms** — RECOMMENDED for creators/independent teams
     - Cost: 1-2 weeks per harness to package for 4-6 platforms
     - Benefit: Access to 100K+ users, zero infrastructure cost
   - **BUILD custom marketplace** — NOT recommended unless:
     - Have 50+ proprietary harnesses
     - Vertical specialization (healthcare/finance)
     - Revenue model in place
     - 6+ engineers available for 6-12 months

6. **Strategic Recommendations** — Three paths forward
   - **Independent harness creators:** List on claudemarketplaces.com + aitmpl.com + agentskills.io + Poe
   - **Platform companies:** Build only if have 50+ harnesses and vertical specialization
   - **Content-first approach:** Become curator on existing platform (minimal cost, maximum reach)

## Research Findings

### Existing Platforms (Verified)
- **claudemarketplaces.com** — Largest community index, daily GitHub updates, 1000+ listings
- **aitmpl.com** — Agent harness optimization system, 1000+ pre-built components
- **agentskills.io** — Open standard for portable skills across 30+ agents
- **Poe** — Only platform paying creators today (per-message pricing)
- **Anthropic Plugin Directory** — 101 official + 68 partner plugins
- **GPT Store** — OpenAI ecosystem, monetization pending
- **Hugging Face Spaces** — Very large reach, open source model
- **AWS/Salesforce/GitHub** — Enterprise-focused, limited harness relevance

### Format Portability
- Harnesses can be packaged as: Plugin (native to Claude Code) + Skill (agentskills.io standard) + MCP Server (Claude Desktop) + HF Space (open source)
- One harness = multiple distribution formats with platform-specific tuning

### Key Gap Opportunities
- No specialized harness marketplace exists (opportunity exists but 6-12 months + $200K-500K cost)
- Performance benchmarking for harnesses not available
- Vertical-specific catalogs (healthcare harnesses) would add value but require curator model, not custom platform

## Sources

1. [GitHub - netresearch/claude-code-marketplace](https://github.com/netresearch/claude-code-marketplace)
2. [claudemarketplaces.com](https://claudemarketplaces.com/)
3. [aitmpl.com](https://www.aitmpl.com/)
4. [agentskills.io](https://agentskills.io/)
5. [Anthropic Claude API Docs](https://platform.claude.com/docs/en/managed-agents/overview)
6. [Top AI Agent Marketplaces - Fastio](https://fast.io/resources/top-ai-agent-marketplaces/)
7. [Claude Skills & MCP Servers 2026 Guide](https://codersera.com/blog/claude-skills-mcp-servers-practitioner-guide-2026/)
8. [Build vs Buy for Agent Harnesses](https://dev.to/arezvov/build-vs-buy-for-agent-harnesses-the-real-question-123e)

## Output Artifacts
- Full research report: `projects/claude-harness-marketplace-research.md`
- Key findings: Eight platforms identified, four distribution formats documented, build vs. list decision matrix created

## Next Steps

1. **If distributing a harness:** Package as Plugin + Skill, submit to claudemarketplaces.com, aitmpl.com, and agentskills.io (2-3 weeks effort)
2. **If building a product:** Use existing platforms, don't build custom marketplace unless have vertical specialization
3. **If pursuing vertical specialization:** Become curator on claudemarketplaces.com rather than building custom marketplace (curator approach costs 1/10th and reaches existing audience)
4. **If monetization critical:** List on Poe (only platform with creator payments today); others (Anthropic, Hugging Face) monetization pending
