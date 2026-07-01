# Integration Design — Phase 1 to Phase 2 Progression

**Backlog:** 131 — Claude Code Harness Distribution Strategy
**Date:** 2026-06-15
**Status:** Complete

---

## Purpose

This document defines the progression logic from Phase 1 (dual-track launch) to Phase 2 (conditional expansion). It specifies the success metrics that trigger Phase 2, the decision tree for selecting among three Phase 2 options, and the cross-references to all supporting documents in the research corpus.

---

## Phase 1 to Phase 2 Progression Logic

### Phase 1 Completion Criteria

Phase 1 is complete when all Track A and Track B success criteria are met OR when the 4-week timeline expires (whichever comes first). At Phase 1 completion, the team evaluates Phase 2 triggers.

**Track A (Distribution) must achieve:**
- Kernel listed on 4+ platforms (Claude Code Plugins Official, skills.sh, claudemarketplaces.com, GitHub)
- 50+ views/impressions in first 2 weeks
- 10+ downloads/installs
- Zero platform rejections
- Zero critical bugs from community feedback

**Track B (Community) must achieve:**
- "Enterprise Harnesses" curator collection with 10+ vetted harnesses
- 2-3 integration guides published on dev.to and GitHub
- Active community presence (comments, discussions)
- 100+ followers/watchers across platforms

### Transition Gate

The Phase 1 to Phase 2 transition is not automatic. It requires explicit evaluation of five trigger criteria during Week 4 of Phase 1, with monthly re-evaluation thereafter.

**Transition states:**

```
Phase 1 In Progress
  → Phase 1 Complete (criteria met or timeline expired)
    → Evaluate Phase 2 Triggers
      → All 5 triggers met: Select Phase 2 option (A, B, or C)
      → 3-4 triggers met: Continue Phase 1 optimization (2 more weeks)
      → 0-2 triggers met: Stay in Phase 1 indefinitely, optimize messaging
```

No investment in Phase 2 infrastructure, engineering, or planning occurs until all five triggers are confirmed. Premature Phase 2 commitment is the primary risk this gate prevents.

---

## Phase 2 Trigger Metrics

### The Five Triggers

Each trigger represents a distinct market signal. All five must be present simultaneously to justify Phase 2 investment. Individual triggers being met does not constitute Phase 2 readiness — the combination proves market maturity.

| # | Metric | Threshold | Measurement Source | Signal Meaning |
|---|--------|-----------|-------------------|----------------|
| T1 | Total installs | >100/month | Platform analytics (aggregated across all platforms) | Organic demand exists beyond initial launch excitement |
| T2 | Repeat users | >30% return rate | Platform analytics, GitHub clone frequency | Value retention — users return because the kernel solves real problems |
| T3 | User feedback | "More harness variants" mentioned 3+ times | GitHub issues, Reddit, support tickets, platform comments | Market explicitly requests platform-specific optimization |
| T4 | Community growth | 200+ followers/engagement | claudemarketplaces.com followers, GitHub stars, dev.to subscribers | Brand awareness sufficient to support expansion investment |
| T5 | Revenue model clarity | Monetization available on at least 1 platform | Poe creator payments, Anthropic marketplace announcement | Economic sustainability path exists for the investment |

### Measurement Cadence

- **Weekly:** T1 (installs), T4 (followers) — tracked in install spreadsheet
- **Biweekly:** T2 (repeat users), T3 (feedback themes) — aggregated from all sources
- **Monthly:** T5 (revenue model) — checked against platform announcements and industry news
- **Monthly trigger review:** First Friday of each month, all 5 criteria evaluated against thresholds. Decision documented in `projects/claude-code-harness-distribution/trigger-reviews/YYYY-MM.md`.

### Monitoring Setup (Created During Phase 1 Week 4)

1. **Install tracking spreadsheet** — One row per platform per week. Columns: platform, views, installs, uninstalls, net installs, cumulative.
2. **Feedback aggregation** — GitHub Issues label: `user-feedback`. Reddit/HN bookmark folder. Weekly review of all feedback mentioning "variants," "optimization," or "platform-specific."
3. **Community metrics** — GitHub stars, followers, forks. claudemarketplaces.com follower count. dev.to article views and reactions.
4. **Revenue model watch** — Google Alert for "Anthropic marketplace monetization," "Claude Code plugins revenue," "agent skills monetization." Weekly check of Anthropic blog and changelog.

---

## Phase 2 Decision Tree

### Option Selection Logic

When all five triggers are met, the decision tree maps the relative strength of each trigger to the appropriate Phase 2 option:

```
ALL 5 TRIGGERS MET
│
├─ T3 strongest (variant feedback is dominant theme)?
│  └─ YES → Phase 2A: Build Harness Variants
│     Rationale: Users are explicitly requesting platform-specific
│     optimization. Technical demand is validated.
│     Investment: $90-150K, 4-6 months
│
├─ T1 strongest (installs >500/month) AND T5 confirmed (revenue model)?
│  └─ YES → Phase 2B: Build Custom Marketplace
│     Rationale: Scale justifies infrastructure investment AND
│     revenue model makes it self-sustaining.
│     Investment: $200-500K, 6-12 months
│
├─ T4 strongest (community authority is the differentiator)?
│  └─ YES → Phase 2C: Double Down on Curation + Consulting
│     Rationale: Trust and authority are the competitive moat,
│     not technology. Revenue via services.
│     Investment: $25-60K/year, ongoing
│
└─ No clear signal dominance
   └─ Default to Phase 2C (lowest risk, lowest cost)
      Re-evaluate in 30 days with updated trigger data
```

### Option Comparison

| Dimension | Phase 2A (Variants) | Phase 2B (Marketplace) | Phase 2C (Curation) |
|-----------|:---:|:---:|:---:|
| **Cost** | $90-150K | $200-500K | $25-60K/year |
| **Timeline** | 4-6 months | 6-12 months | Ongoing |
| **Risk** | Medium | High | Low |
| **Revenue potential** | Indirect (adoption) | High (platform fees) | Medium (consulting) |
| **Team size** | 1-2 engineers | 3-5 engineers | 1 person |
| **Reversibility** | Medium | Low | High |
| **Competitive moat** | Technical | Infrastructure | Trust/Authority |

### Pivot Rules

Phase 2 option selection is not permanent. Pivot rules define when to switch:

- **2A → 2C:** If variant adoption <2x after 3 months, stop variant investment and pivot to curation
- **2B → 2C:** If marketplace visits <1,000/month after 6 months, freeze marketplace development and pivot to curation
- **2C → 2A:** If consulting clients repeatedly request platform-specific variants, upgrade to Phase 2A
- **Any → Continue Phase 1:** If trigger metrics regress below thresholds for 2 consecutive months, scale back to Phase 1

---

## Cross-References

### Research Corpus

| Document | Key Content | Location |
|----------|-------------|----------|
| Platforms Inventory | 9-platform comparison matrix, format compatibility, submission strategy | `01-platforms-inventory-and-comparison.md` |
| Marketplace Gaps | 6 gaps identified, opportunity ranking, curation vs build analysis | `02-marketplace-gaps-and-opportunities.md` |
| Distribution Roadmap | Phase 1 dual-track plan, Phase 2 options with budgets, risk mitigation | `03-distribution-roadmap.md` |
| Agent Skills Refactor Spec | SKILL.md format, 7-step refactor plan, 8-harness compatibility matrix | `04-agent-skills-refactor-spec.md` |
| Submission Templates | 5 platform templates with keywords, categories, instructions | `05-submission-templates.md` |
| Master Research Report | Full synthesis of all findings, executive summary, strategic recommendation | `RESEARCH-REPORT.md` |

### Design Documents (Backlog 131)

| Document | Key Content | Location |
|----------|-------------|----------|
| Existing Platforms | Platform inventory with URLs, reach estimates, curation models | `docs/backlog/131-*/existing-platforms.md` |
| Marketplace Gaps | Raw gap analysis, demand signals, cost estimates | `docs/backlog/131-*/marketplace-gaps.md` |
| Competitive Landscape | Harness benchmark data, market timing, differentiation strategy | `docs/backlog/131-*/competitive-landscape.md` |
| Distribution Options | Phase 1/2 option analysis, effort estimates | `docs/backlog/131-*/distribution-options.md` |
| Recommendation | Final strategic recommendation, budget summary | `docs/backlog/131-*/recommendation.md` |

### Key Data Points for Phase 2 Decisions

| Data Point | Source Document | Relevance |
|-----------|-----------------|-----------|
| Cursor vs Claude Code performance gap (4.2 points) | Competitive Landscape | Validates variant demand (Phase 2A) |
| Custom marketplace cost ($200-500K) | Marketplace Gaps | Budget gate for Phase 2B |
| Curation cost ($5-10K/year) | Marketplace Gaps | Low-cost alternative (Phase 2C) |
| 30+ agents support SKILL.md | Platforms Inventory | Validates multi-platform strategy |
| All 9 platforms are free | Platforms Inventory | No financial barrier to Phase 1 |
| Vertical catalogs = highest ROI gap | Marketplace Gaps | Informs Phase 2C curation focus |

---

## Glossary

| Term | Definition |
|------|-----------|
| **Agent Skills** | Open standard (SKILL.md) for portable agent knowledge across 30+ AI coding agents. Introduced December 2025. |
| **Harness** | An integrated agent system combining kernel, protocol, hooks, skills, and domain packs into a deployable agent configuration. Distinguished from individual skills or plugins by architectural complexity and self-management capabilities. |
| **Kernel** | The core engine of a harness. Manages protocol enforcement, lesson learning, anchor ceremonies, autonomous cycling, and self-improvement loops. The Isagawa Kernel is the specific implementation being distributed. |
| **SKILL.md** | The file format defined by the Agent Skills specification. Contains YAML frontmatter (metadata) and markdown body (instructions). Single-source distribution format for multi-agent compatibility. |
| **Curator** | A trusted expert who evaluates, categorizes, and recommends harnesses on existing platforms. Differentiated from platform operators by depth of architectural expertise. |
| **Phase 1** | 4-week dual-track launch: Track A (platform distribution) + Track B (community authority). Budget: $6-12K. |
| **Phase 2** | Conditional expansion triggered by 5 market metrics. Three options: Variants (2A), Marketplace (2B), Curation (2C). |
| **Trigger** | A specific, measurable market signal (install count, repeat usage, feedback theme, community size, revenue model) that must exceed its threshold before Phase 2 investment is authorized. |
| **Vertical** | An industry-specific segment (healthcare, finance, legal, DevOps) with distinct compliance, workflow, and integration requirements for harness adoption. |
| **Hook Enforcement** | Claude Code's PreToolUse/PostToolUse mechanism for mechanically enforcing protocol rules. Not available on other agents — a key portability limitation. |
| **Honor System Mode** | How the Isagawa Kernel operates on non-Claude-Code agents: the agent follows protocol instructions because they're in the SKILL.md, but there's no mechanical enforcement preventing violations. |
| **Context Management** | The harness-level strategy for managing the agent's context window — what to retain, when to compact, how to prioritize code vs conversation vs tool definitions. Root cause of the Cursor vs Claude Code performance gap. |

---

*Generated for Backlog 131 — Claude Code Harness Distribution Strategy*
*Kernel domain: sr_dev*
*Date: 2026-06-15*
