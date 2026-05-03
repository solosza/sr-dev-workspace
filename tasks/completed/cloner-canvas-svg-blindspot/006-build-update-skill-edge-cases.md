# Update SKILL.md Edge Cases Table

## Context
The SKILL.md has an Edge Cases table in extraction.md. The new non-DOM rendering strategies need corresponding entries in the SKILL.md edge cases guidance so agents know when to apply them.

## Type
BUILD

## Execution
inline

## Dependencies
- 001, 002, 003, 004, 005

## Phase Gate
- [ ] `.claude/skills/website-cloner/references/extraction.md` contains "Sanity Check" section
- [ ] `.claude/skills/website-cloner/references/extraction.md` contains "Hydration Wait" section
- [ ] `.claude/skills/website-cloner/references/extraction.md` contains "SVG Text" section
- [ ] `.claude/skills/website-cloner/references/extraction.md` contains "Canvas Detection" section
- [ ] `.claude/skills/website-cloner/references/extraction.md` contains "Custom Property" section

## Requirements
- Edit `.claude/skills/website-cloner/SKILL.md`
- Add these rows to the Edge Cases table in `references/extraction.md`:
  - Canvas-rendered content → Run canvas detection, mark as unextractable
  - SVG text rendering → Run SVG text extraction fallback
  - Deferred hydration (React/Next.js) → Run hydration wait, then re-extract
  - All typography values identical → Sanity check flagged, use fallback strategies
  - CSS custom property divergence → Compare getPropertyValue vs getComputedStyle, prefer computed
- Also mention canvas and SVG in the SKILL.md principles or edge cases area

## Acceptance Criteria
- [ ] `.claude/skills/website-cloner/SKILL.md` contains "canvas" (case-insensitive)
- [ ] `.claude/skills/website-cloner/references/extraction.md` Edge Cases table has entries for canvas, SVG text, hydration, and divergence

## Gates Satisfied
- BUILD-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
