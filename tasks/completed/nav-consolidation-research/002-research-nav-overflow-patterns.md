# Research: Nav Overflow/Consolidation Patterns

**Type:** RESEARCH
**Phase:** 1
**Depends on:** 001

## Goal

Research the leading patterns for collapsing a large nav into a smaller footprint on portfolio/product sites. The current isagawa.co home nav has 8+ items and will keep growing as more pipelines ship products.

## Research Questions

1. What are the established patterns for handling nav overflow? (ellipsis menu, "More ↓" dropdown, tab-overflow scroll, grouped sections, mega menu)
2. Which patterns are most common on minimal/monochrome engineering portfolio sites vs SaaS product sites?
3. What is the standard split between "always visible" primary items and "collapsed" secondary items?
4. Does a "Products" or "Work" grouped dropdown preserve the hub-spoke architecture (factory home → product pages) better than a flat overflow?
5. What are the CSS/JS implementation patterns for a pure vanilla dropdown (no framework)?
6. Any known UX research on nav item count limits before cognitive overload?

## Search Queries to Run

1. "navigation overflow menu best practices portfolio site 2024"
2. "too many nav items dropdown consolidation UX patterns"
3. "monochrome minimal portfolio navigation design patterns"
4. "vanilla css javascript dropdown nav overflow pattern"
5. "hub spoke website navigation architecture product portfolio"

## Output

Write findings to `projects/nav-consolidation-research/01-overflow-patterns.md`

Include:
- List of identified patterns with pros/cons
- Recommended pattern for isagawa.co specifically (considering monochrome aesthetic, vanilla JS constraint, hub-spoke architecture)
- Note on primary vs secondary nav split (which items always visible, which collapse)

## Acceptance Criteria
- [ ] `projects/nav-consolidation-research/01-overflow-patterns.md` exists
- [ ] File contains at least 3 identified patterns with tradeoffs
- [ ] File includes a recommendation section
