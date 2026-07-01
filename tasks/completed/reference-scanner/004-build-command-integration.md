# Build Command Integration (SKILL.md)

## Type
BUILD

## Phase Gate
Tasks 002 and 003 must be complete.

## Deliverable
`.claude/skills/reference-scanner/SKILL.md`

## Instructions
1. Read the build-command-integration design doc: `docs/backlog/153-kernel-build-reference-scanner/build-command-integration.md`
2. Read the design-decisions doc: `docs/backlog/153-kernel-build-reference-scanner/design-decisions.md`
3. Create `.claude/skills/reference-scanner/SKILL.md` as the skill identity file:
   - Identity: what the scanner is, its purpose
   - File index: point to scanner.py and state-schema.md
   - Usage: how commands invoke the scanner as their Step 0
   - Integration with `/build-command`: how to auto-generate topic declarations in step templates
   - Keyword-to-topic map (from build-command-integration.md)
   - Design decisions summary (from design-decisions.md)
4. Follow tiered-index pattern: SKILL.md is an index, not inline implementation

## Verification
- File exists at `.claude/skills/reference-scanner/SKILL.md`
- References scanner.py and state-schema.md
- Includes keyword-to-topic map
