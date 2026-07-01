# Build Recommendation Report — Pivot, Stay, or Hybrid

## Context
Synthesize all research into a clear recommendation with specific copy suggestions for each approach.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-market-research-current-messaging-audit
- 002-market-research-competitor-framing
- 003-market-research-search-terms-discoverability

## Phase Gate
- [ ] `projects/isagawa-site-pivot-research/current-messaging-audit.md` exists
- [ ] `projects/isagawa-site-pivot-research/competitor-framing.md` exists
- [ ] `projects/isagawa-site-pivot-research/search-terms.md` exists

## Requirements
- Synthesize findings from all three research tasks
- Present three options: PIVOT (full rebrand to loops/agent systems), STAY (keep current messaging), HYBRID (evolve current with loops language)
- For each option: specific copy suggestions for tagline, value prop, key sections
- Include pros/cons for each option
- Make a clear recommendation with rationale
- Account for alignment with LinkedIn profile, GitHub presence, and resume (backlog 149)
- Output: recommendation report

## Acceptance Criteria
- [ ] File exists: `projects/isagawa-site-pivot-research/recommendation.md`
- [ ] Three options presented with specific copy
- [ ] Clear recommendation with rationale
- [ ] Cross-channel alignment (site, LinkedIn, resume) addressed

## Gates Satisfied
- BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
