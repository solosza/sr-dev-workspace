# Research Search Terms and Discoverability

## Context
Understand what people actually search for when looking for this category of tooling. This informs whether "loops" or "agent systems" would improve discoverability.

## Type
RESEARCH

## Execution
inline

## Dependencies
- None

## Requirements
- Research common search queries for agent governance, loop-based agent frameworks, agent orchestration tools
- Check GitHub topic tags: what tags do similar repos use?
- Look at job postings (reference backlog 029, 036) for language employers use around loops and agent systems
- Identify gap: are people searching for terms Isagawa doesn't rank for?
- Assess whether "spec-driven loop engineering" is searchable or too niche
- Output: search terms analysis with discoverability recommendations

## Acceptance Criteria
- [ ] File exists: `projects/isagawa-site-pivot-research/search-terms.md`
- [ ] Common search queries listed with estimated relevance
- [ ] GitHub topic tag analysis included
- [ ] Job posting language cross-referenced
- [ ] Discoverability gap identified (if any)

## Gates Satisfied
- RESEARCH-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
