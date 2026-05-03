# Add Hydration Wait Strategy

## Context
Some sites use deferred-hydration React/Next.js components that render placeholder content initially. The real typography values only appear after hydration completes. This task adds a fallback strategy that waits for hydration before re-extracting.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- Add a new section "Fallback Strategy 1: Hydration Wait" to `.claude/skills/website-cloner/references/extraction.md`
- Place it after the Sanity Check section
- Include a `browser_evaluate` JavaScript snippet that:
  - Waits for a configurable delay (default 5000ms)
  - Optionally uses `MutationObserver` to detect DOM changes and wait until mutations settle
  - Returns `{ waited: true, mutations_detected: N, settled: true/false }`
- Add guidance: after waiting, re-run the Step 4c section extraction and re-check with the sanity check
- Note: this is a best-effort strategy — some sites may never hydrate fully without user interaction

## Acceptance Criteria
- [ ] `.claude/skills/website-cloner/references/extraction.md` contains section header "Hydration Wait"
- [ ] Section includes a `browser_evaluate` JavaScript block with delay + MutationObserver
- [ ] Section includes guidance to re-extract after wait

## Gates Satisfied
- BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
