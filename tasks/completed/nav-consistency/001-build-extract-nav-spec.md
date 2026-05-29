# Build: Extract Nav Spec from Research Report

**Type:** BUILD
**Phase:** 1

## Goal

Read the pipeline 106 research report and extract the concrete nav specification that will be applied to all 7 pages.

## Prerequisite

`projects/nav-consolidation-research/research-report.md` must exist (produced by pipeline 106).

## What to Extract

From the `## Recommendation` section of the research report, identify:
1. Which items are **always visible** (primary nav)
2. Which items go **under a dropdown** (secondary/collapsed) and what the dropdown label is
3. Whether the attested counter (`N ✓`) stays in nav or moves
4. Any CSS class names the report specifies for the dropdown

Write the extracted spec to `projects/nav-consolidation-research/nav-spec.md` in this format:

```markdown
# Nav Spec (from Pipeline 106)

## Primary items (always visible)
- Logo: ISAGAWA → index.html
- [item]: [href]
- ...

## Dropdown label
[label text, e.g. "Products ▾" or "Work ▾"]

## Dropdown items
- [item]: [href]
- ...

## Counter
[keep in nav | move to footer | remove]

## CSS pattern
[brief description of dropdown mechanism]
```

## Acceptance Criteria
- [ ] `projects/nav-consolidation-research/nav-spec.md` exists
- [ ] File contains `## Primary items` section
- [ ] File contains `## Dropdown label` section
- [ ] File contains `## Dropdown items` section
