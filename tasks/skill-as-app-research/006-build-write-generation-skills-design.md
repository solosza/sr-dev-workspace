# Write Generation Skills Design Sketch

## Context
The kernel has extraction skills (website-cloner) but no generation skills. Design what a generation skill would look like — structured input → structured output, composable with extraction skills.

## Type
BUILD

## Execution
inline

## Dependencies
- 001, 003, 004

## Phase Gate
- [ ] `projects/kernel-architecture/` exists (task 004)
- [ ] Website cloner analysis complete (task 001) — extraction pattern to mirror
- [ ] Portfolio site analysis complete (task 003) — generation gap identified

## Requirements
- Append `## Generation Skills` section to `projects/kernel-architecture/skill-as-app-research.md`
- Design a generation skill pattern that mirrors the extraction skill pattern:
  - Extraction: URL → navigate → extract → structured data (JSON)
  - Generation: structured data → transform → produce → output files (HTML/CSS/code)
- Sketch a concrete example: "section-generator" skill
  - Input: design tokens (CSS vars) + content spec (section content) + section ID
  - Output: section HTML + section CSS
  - Pipeline: read tokens → read content → generate semantic HTML → generate scoped CSS → append to files
- Address composability: how would extraction → generation chain work?
  - website-cloner extracts → token-merger transforms → section-generator produces
- Address reusability: would this skill work for any static site, or is it portfolio-specific?
- Identify what's needed to build this (new skill folder, reference files, MCP tools if any)

## Acceptance Criteria
- [ ] `## Generation Skills` section exists in research document
- [ ] Concrete "section-generator" skill design with input/output/pipeline
- [ ] Composability model described
- [ ] Reusability assessment included

## Gates Satisfied
BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
