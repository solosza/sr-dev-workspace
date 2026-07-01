# Analyze Competitive Landscape

## Context

Analyze the competitive landscape of existing Claude Code harness projects. This task profiles major harness projects across 5 tiers (comprehensive toolkits, methodology-driven, performance optimization, multi-harness ecosystems, and component collections). Reference the design document at `docs/backlog/132-market-research-claude-harness-marketplace-landscape/competitive-analysis.md` which has been pre-researched.

## Type

RESEARCH

## Execution

inline

## Dependencies

- 001-market-create-project-dir

## Phase Gate

- [ ] Directory `projects/claude-harness-marketplace-research/` exists (from task 001)

## Requirements

- Document existing harness projects and their market positioning
- Analyze across 5 tiers: Comprehensive Toolkits, Methodology-Driven, Performance/Optimization, Multi-Harness Ecosystems, Component Collections
- Include projects: awesome-claude-code-toolkit, Claude Code Harness, Isagawa Kernel, ECC, Multi-Harness Marketplace, and others
- For each project: URL, Tagline, Philosophy, Positioning, Distribution, Audience, Strengths, Weaknesses
- Create market positioning summary table
- Identify market gaps
- Reference existing research from `docs/backlog/132-market-research-claude-harness-marketplace-landscape/competitive-analysis.md`

## Acceptance Criteria

- [ ] File `projects/claude-harness-marketplace-research/competitive-analysis.md` created
- [ ] Contains analysis for 5 tiers (Tier 1 through Tier 4+ in structure)
- [ ] Each tier includes at least 1-2 projects with full analysis (URL, Tagline, Philosophy, Positioning, Strengths, Weaknesses)
- [ ] Market Positioning Summary table exists with: Project, Type, Methodology, Multi-Platform, Distribution, GitHub Stars, Marketplace Presence
- [ ] Market gaps section identifies gaps in current offerings
- [ ] Verified via: `test -f projects/claude-harness-marketplace-research/competitive-analysis.md && grep -q "Tier 1" projects/claude-harness-marketplace-research/competitive-analysis.md`

## Gates Satisfied

- DOC-04, DOC-05

## Completion Signal

When ALL acceptance criteria are met, invoke `/kernel/complete`.
