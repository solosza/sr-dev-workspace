# Build: Write Research Report + Recommendation

**Type:** BUILD
**Phase:** 1
**Depends on:** 002, 003

## Goal

Synthesize findings from tasks 002 and 003 into a final research report with a concrete implementation recommendation for isagawa.co's nav consolidation.

## Output File

`projects/nav-consolidation-research/research-report.md`

## Required Sections

### 1. Problem Statement
- Current nav item count on each page
- Why it's a problem (cognitive overload, signals "growing without design intent")

### 2. Patterns Evaluated
- Summary table: pattern name | pros | cons | fit for isagawa.co
- At least: overflow/ellipsis dropdown, grouped label dropdown ("Products"), tab-scroll, hamburger-only

### 3. Reference Site Summary
- What leading sites do (condensed from 02-reference-sites.md)
- Common pattern that emerges

### 4. Recommendation
- **Chosen pattern** (be specific — e.g., "Products dropdown with 5 items, always-visible: Home + Feed + Attestation")
- **Primary items** (always visible, 3-4 max)
- **Collapsed items** (under dropdown, labeled "Products" or "Work")
- **Implementation sketch** — what HTML/CSS/JS changes are needed (so backlog 107 can execute directly from this)
- **Mobile behavior** — how it interacts with existing hamburger menu

### 5. Validation Verdict
One paragraph: does research confirm the "consolidate products under a dropdown" direction? Or did research surface a better approach?

## Acceptance Criteria
- [ ] `projects/nav-consolidation-research/research-report.md` exists
- [ ] Contains `## Recommendation` section
- [ ] Recommendation specifies which items are always visible vs collapsed
- [ ] Contains `## Implementation Sketch` with specific HTML/CSS notes
- [ ] Contains `## Validation Verdict`
