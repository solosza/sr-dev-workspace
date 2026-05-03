# L1 — Verify All New Sections Exist

## Context
Structural verification that all new sections were added to extraction.md and SKILL.md.

## Type
TEST

## Execution
agent

## Dependencies
- 001, 002, 003, 004, 005, 006

## Phase Gate
- [ ] Tasks 001-006 complete

## Requirements
- Run grep checks for all required section headers in extraction.md
- Run grep check for "canvas" in SKILL.md
- Report pass/fail for each

## Acceptance Criteria
- [ ] `grep -q "Sanity Check" .claude/skills/website-cloner/references/extraction.md` exits 0
- [ ] `grep -q "Hydration Wait" .claude/skills/website-cloner/references/extraction.md` exits 0
- [ ] `grep -q "SVG Text" .claude/skills/website-cloner/references/extraction.md` exits 0
- [ ] `grep -q "Canvas Detection" .claude/skills/website-cloner/references/extraction.md` exits 0
- [ ] `grep -q "Custom Property" .claude/skills/website-cloner/references/extraction.md` exits 0
- [ ] `grep -qi "canvas" .claude/skills/website-cloner/SKILL.md` exits 0

## Gates Satisfied
- BUILD-01, BUILD-02, BUILD-03, BUILD-04, BUILD-05, BUILD-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
