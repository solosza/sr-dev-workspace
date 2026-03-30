# Rewrite step-11.md as Thin Index

## Context
Rewrite step-11.md to be a thin index (<60 lines) pointing to all 10 sub-references via wikilinks.

## Type
BUILD

## Dependencies
- 025-034 (all 10 sub-reference files exist)

## Phase Gate
- [ ] All 10 sub-reference files exist in validation/

## Requirements
- Rewrite `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/spec-factory/steps/step-11.md`
- Under 60 lines, YAML frontmatter, sub-step table with wikilinks, references run-task.sh
- No inline implementation detail

## Acceptance Criteria
- [ ] step-11.md under 60 lines (verify: wc -l)

## Gates Satisfied
S11-12, S11-13

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
