# Identify Gaps and Opportunities

## Context

Identify unmet market needs, gaps in existing offerings, and strategic opportunities for Isagawa Kernel and the harness marketplace space. This task synthesizes findings from competitive analysis and platforms research. Reference the design document at `docs/backlog/132-market-research-claude-harness-marketplace-landscape/gaps-and-opportunities.md` which has been pre-researched.

## Type

RESEARCH

## Execution

inline

## Dependencies

- 001-market-create-project-dir
- 002-market-document-platform-inventory
- 003-market-analyze-competitive-landscape

## Phase Gate

- [ ] Directory exists: `projects/claude-harness-marketplace-research/`
- [ ] Platforms document exists: `projects/claude-harness-marketplace-research/platforms.md`
- [ ] Competitive analysis exists: `projects/claude-harness-marketplace-research/competitive-analysis.md`

## Requirements

- Identify 6+ major market gaps (no specialized marketplace, poor discoverability, no evaluation framework, complex onboarding, limited monetization, no compatibility standard)
- For each gap: Evidence, Opportunity, Target User, Potential Features, Market Size
- Document 4+ strategic opportunities for Isagawa Kernel (Anthropic Marketplace, GitHub App, Custom Marketplace, Enterprise Support)
- Include market size and growth estimates
- Reference existing research from `docs/backlog/132-market-research-claude-harness-marketplace-landscape/gaps-and-opportunities.md`

## Acceptance Criteria

- [ ] File `projects/claude-harness-marketplace-research/gaps-and-opportunities.md` created
- [ ] Contains 6+ Market Gaps sections (each with Evidence, Opportunity, Target User, Potential Features)
- [ ] Contains 4+ Strategic Opportunities sections for Isagawa Kernel (each with Path, Effort, Timeline, Pros, Cons, Outcomes)
- [ ] Market Size & Growth section included with projections
- [ ] Recommendations section included
- [ ] Verified via: `test -f projects/claude-harness-marketplace-research/gaps-and-opportunities.md && grep -c "^###" projects/claude-harness-marketplace-research/gaps-and-opportunities.md | awk '{if ($1 >= 10) exit 0; else exit 1}'`

## Gates Satisfied

- DOC-06, DOC-07

## Completion Signal

When ALL acceptance criteria are met, invoke `/kernel/complete`.
