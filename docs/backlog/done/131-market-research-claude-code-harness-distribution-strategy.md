# Claude Code Harness Distribution Strategy — Marketplace Landscape & Recommendation

## Status
Open

## Priority
High — Informs Isagawa Kernel product strategy and distribution roadmap

## Summary
Comprehensive market research on Claude Code harness distribution platforms, marketplace gaps, and competitive positioning. Evaluated 6+ existing distribution channels and analyzed build vs. list trade-offs. **Primary recommendation: Adopt Agent Skills spec + list on community marketplaces (Phase 1), defer custom marketplace until market signals >100 installs/month (Phase 2).**

## Design Documents

| Document | Purpose |
|----------|---------|
| [[131-market-research-claude-code-harness-distribution-strategy/existing-platforms]] | Inventory of 6+ distribution platforms with feature comparison |
| [[131-market-research-claude-code-harness-distribution-strategy/marketplace-gaps]] | Identified gaps in current ecosystem |
| [[131-market-research-claude-code-harness-distribution-strategy/competitive-landscape]] | Harness performance gap analysis vs Cursor/Copilot, market timing |
| [[131-market-research-claude-code-harness-distribution-strategy/distribution-options]] | 4 distribution strategies with effort/benefit analysis |
| [[131-market-research-claude-code-harness-distribution-strategy/recommendation]] | Phased strategy: Agent Skills spec + community lists (Phase 1) → custom marketplace (Phase 2) |

## Key Findings (Executive Summary)

### Existing Distribution Platforms
- **Official:** Claude Marketplace (Anthropic, enterprise focus), Claude Code Plugins Official (automatic in /plugin command)
- **Community:** claudemarketplaces.com, claudeskills.info, agentskills.io
- **GitHub-based:** netresearch/claude-code-marketplace, wshobson/agents (multi-harness)

### Critical Insight: The Harness Matters More Than the Model
- Claude Opus 4.7 in Cursor outperforms same model in Claude Code by ~4% on benchmarks
- Root cause: Claude Code's context compaction triggers at 80-90%, Cursor's architectural choices differ
- Implication: Distribution strategy must account for harness-specific optimization

### Agent Skills Specification (Newly Adopted Dec 2025)
- Open standard released by Anthropic Dec 2025
- Supported by: Claude Code, Codex CLI, Gemini CLI, GitHub Copilot, Cursor (with placement), and community tools
- Distribution hub: skills.sh + agentskills.io
- **Opportunity:** Early adopters get first-mover advantage in multi-harness portability

### Market Gaps
1. No specialized Claude Code harness marketplace (exists for general agents, not harnesses)
2. No harness composability registry
3. No cross-harness performance benchmarking
4. No vertical-specific harness catalogs (e.g., healthcare-optimized harnesses)
5. Limited monetization (Poe has creator payments; Anthropic/HF pending)

### Competitive Landscape
- Market is **fragmented:** no single dominant platform
- Successful teams distribute to **4-6 platforms** with format-specific tuning
- Cursor marketplace + Claude Code ecosystem still diverging (different context strategies)
- Anthropic positioning Claude Marketplace for **enterprise B2B** play

## Recommendation: Phased Hybrid Strategy

### Phase 1 (Immediate: 2-3 weeks)
**Dual-Track Launch via Agent Skills**

1. **Refactor Isagawa Kernel to Agent Skills SKILL.md spec**
   - Read [Agent Skills specification](https://github.com/agentskills/agentskills)
   - Convert kernel to SKILL.md frontmatter + instructions
   - Verify compatibility across 30+ supported agents

2. **List on Primary Distribution Channels**
   - Claude Code Plugins Official (Anthropic marketplace)
   - [skills.sh](https://inference.sh/blog/skills/agent-skills-overview) (primary discovery hub)
   - GitHub + agentskills.io registration (automatic indexing)
   - claudemarketplaces.com (community manual submission)

3. **Result:** Available to Claude Code, Codex CLI, Gemini CLI, GitHub Copilot, Cursor, and 25+ community tools

4. **Effort:** 2-3 days engineering + documentation

### Phase 2 (Conditional: 3-6 months if traction >100 installs/month)
**Build Harness-Optimized Marketplace (Only If Market Signals Demand)**

1. Collect usage data from Phase 1 (which harnesses matter? which platforms driving adoption?)
2. Build custom discovery UI + harness variants
3. Model on wshobson/agents (multi-harness framework)
4. Maintain backward compatibility with Agent Skills spec (critical for long-term flexibility)

### Why This Approach
- **Agent Skills spec is the new standard** (Anthropic endorsed, Dec 2025) → first-mover advantage now
- **Single source (SKILL.md) → multiple harnesses** reduces maintenance burden
- **Community marketplaces + official Claude listing = organic discovery** without custom platform cost
- **GitHub as home base** keeps control + flexibility for future pivots
- **Defers custom marketplace until proven market demand** (reduces sunk cost, respects market signals)

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| Anthropic changes harness/API | Version SKILL.md, maintain GitHub mirror, stay loosely coupled |
| Agent Skills adoption slows | Maintain Plugin format as fallback, monitor adoption metrics |
| Competitors build custom marketplace first | Early Agent Skills adoption + community curation (curator model) as alternative |
| Community marketplaces become gatekeepers | Publish directly to GitHub, agentskills.io auto-indexes, stay portable |

## References

**Official Resources:**
- [Claude Marketplace](https://claude.com/platform/marketplace)
- [Claude Code Plugins Official Directory](https://www.claudepluginhub.com/marketplaces/anthropics-claude-plugins-official)
- [Agent Skills Specification](https://github.com/agentskills/agentskills)
- [Agent Skills Hub (skills.sh)](https://inference.sh/blog/skills/agent-skills-overview)

**Community Platforms:**
- [claudemarketplaces.com](https://claudemarketplaces.com/)
- [claudeskills.info](https://claudeskills.info/)
- [agentskills.io](https://agentskills.io)
- [GitHub - netresearch/claude-code-marketplace](https://github.com/netresearch/claude-code-marketplace)
- [GitHub - wshobson/agents](https://github.com/wshobson/agents)

**Market Analysis & Comparisons:**
- [Claude Code vs Cursor vs GitHub Copilot: 2026 Comparison](https://www.sitepoint.com/claude-code-vs-cursor-vs-copilot-the-2026-developer-comparison/)
- [Cursor SDK vs Claude Code Harness](https://www.mindstudio.ai/blog/cursor-sdk-vs-claude-code-harness-comparison)
- [What Is an Agent Harness? Architecture Behind Claude Code, Codex, Cursor](https://www.mindstudio.ai/blog/what-is-agent-harness-architecture-explained)

## Task Builder Input

- **Deliverable:**
  1. Comprehensive markdown research report with platform comparison matrix
  2. Distribution roadmap document (Phase 1 checklist, Phase 2 decision criteria)
  3. Agent Skills refactor specification for Isagawa Kernel
  4. Submission templates for each platform (claude-plugins-official, skills.sh, claudemarketplaces.com)

- **Location:** `subproject:claude-code-harness-distribution` → `projects/claude-code-harness-distribution/`

- **Scope:** RESEARCH + PLANNING (deliverables are documentation + templates, not code changes)

- **Constraints:**
  - Agent Skills spec must be compliant (external dependency: https://github.com/agentskills/agentskills)
  - Must research actual submission requirements for each platform (forms, fees, review times)
  - Recommendation should include cost/benefit for each Phase
  - Decision framework for Phase 2 trigger (install metrics, market feedback channels)
