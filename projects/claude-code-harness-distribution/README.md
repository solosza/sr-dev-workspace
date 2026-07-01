# Claude Code Harness Distribution Strategy — Market Research

This folder contains comprehensive market research, analysis, and implementation planning for distributing the Isagawa Kernel as a Claude Code harness across multiple distribution platforms.

## Project Overview

**Backlog:** 131 (Market Research: Claude Code Harness Distribution Strategy & Marketplace Landscape)
**Scope:** RESEARCH + PLANNING (documentation, templates, roadmap)
**Duration:** 7 tasks, ~28 atomic subtasks

## Deliverables

1. **01-platforms-inventory-and-comparison.md** — Inventory and comparison of 9+ distribution platforms (official, community, GitHub-based)

2. **02-marketplace-gaps-and-opportunities.md** — Analysis of 6 marketplace gaps, opportunity ranking, and curator strategy recommendation

3. **03-distribution-roadmap.md** — Phased implementation plan: Phase 1 (4 weeks, $6-12K) for Agent Skills refactor + multi-platform listing; Phase 2 conditional expansion (3 options: variants, custom marketplace, or curation)

4. **04-agent-skills-refactor-spec.md** — Technical specification for refactoring Isagawa Kernel to Agent Skills SKILL.md format with harness compatibility matrix

5. **05-submission-templates.md** — Ready-to-use submission templates for each platform (Claude Code Plugins Official, skills.sh, claudemarketplaces.com, GitHub)

6. **RESEARCH-REPORT.md** — Master synthesis report with all findings, recommendations, timeline, and budget

7. **INTEGRATION-DESIGN.md** — Phase 1→2 progression logic and decision framework

## Key Findings (Executive Summary)

### Recommendation: Phased Hybrid Strategy

**Phase 1 (Immediate, 4 weeks):** Dual-track launch via Agent Skills standard
- Track A: Refactor Kernel to SKILL.md, submit to 4 primary platforms (Claude Code Plugins Official, skills.sh, claudemarketplaces.com, GitHub)
- Track B: Establish curator collection on claudemarketplaces.com, write integration guides, engage community

**Phase 2 (Conditional, if >100 installs/month):** Choose one of 3 options
- Option A: Build harness variants (Claude Code-optimized, Cursor-optimized, Copilot-optimized)
- Option B: Build custom harness marketplace ($200-500K, 6-12 months)
- Option C: Double down on curation + consulting model ($10-25K/month ongoing)

### Why This Approach

- Agent Skills spec is the new standard (Anthropic-endorsed, Dec 2025) → first-mover advantage
- Existing platforms already reach 100K+ developers → no need to build custom platform
- Early adoption via SKILL.md standard = multi-harness portability across 30+ tools
- Defers expensive custom marketplace until market validates demand
- Single source (SKILL.md) reduces maintenance burden

## Platform Landscape

**Official Channels:**
- Claude Code Plugins Official (100K+ reach, Anthropic-curated)
- Claude Marketplace (50K+ enterprise reach, zero revenue cut)

**Community Channels:**
- Agent Skills Hub / skills.sh (30+ agents, primary discovery)
- claudemarketplaces.com (100K+ community, daily updates)
- GitHub direct (unlimited reach, version control native)

**Key Insight:** No single dominant platform. Successful distribution = multi-platform listing with format-specific tuning.

## Budget & Timeline

| Phase | Duration | Internal Cost | External | Effort |
|-------|----------|---------------|----------|--------|
| **Phase 1** | 4 weeks | $5-10K | Free | 1 FTE |
| **Phase 2A** (variants) | 3-4 months | $30-50K/variant | Free | 2-3 engineers |
| **Phase 2B** (custom marketplace) | 6-12 months | $200-500K | Infrastructure | 3-5 engineers |
| **Phase 2C** (curation) | Ongoing | $2-5K/month | Tools | Community mgmt |

## Success Metrics

**Phase 1 Success (EON 4 weeks):**
- ✓ Kernel listed on 4 platforms
- ✓ 50+ views in first 2 weeks
- ✓ 10+ downloads/installs
- ✓ 0 platform rejections

**Phase 2 Trigger (if all met):**
- ✓ >100 installs/month
- ✓ >30% repeat users
- ✓ User feedback: "More harness variants" mentioned 3+ times
- ✓ 200+ community followers
- ✓ Monetization available on ≥1 platform

## File Structure

```
projects/claude-code-harness-distribution/
├── README.md (this file)
├── 01-platforms-inventory-and-comparison.md
├── 02-marketplace-gaps-and-opportunities.md
├── 03-distribution-roadmap.md
├── 04-agent-skills-refactor-spec.md
├── 05-submission-templates.md
├── RESEARCH-REPORT.md (master synthesis)
├── INTEGRATION-DESIGN.md (Phase 1→2)
└── _test/
    ├── fixtures/ (test input data)
    └── expected/ (test expected outputs)
```

## References

**Backlog & Design Docs:**
- Backlog: `docs/backlog/131-market-research-claude-code-harness-distribution-strategy.md`
- Design: `docs/backlog/131-*/` folder with 5 reference documents

**External References:**
- [Claude Marketplace](https://claude.com/platform/marketplace)
- [Agent Skills Specification](https://github.com/agentskills/agentskills)
- [skills.sh Hub](https://inference.sh/blog/skills/agent-skills-overview)
- [claudemarketplaces.com](https://claudemarketplaces.com)
- [GitHub Agents Community](https://github.com/netresearch/claude-code-marketplace)

## Task Status

| Task | Status | Deliverable |
|------|--------|-------------|
| 001 | ✓ COMPLETE | Project directory + README |
| 002 | ⧰ READY | 01-platforms-inventory-and-comparison.md |
| 003 | ⧰ READY | 02-marketplace-gaps-and-opportunities.md |
| 004 | ⧰ READY | 03-distribution-roadmap.md |
| 005 | ⧰ READY | 04-agent-skills-refactor-spec.md |
| 006 | ⧰ READY | 05-submission-templates.md |
| 007 | ⧰ READY | RESEARCH-REPORT.md + INTEGRATION-DESIGN.md |

---

*Generated by task-builder for Backlog 131*  
*Kernel domain: sr_dev*  
*Date: 2026-06-14*
