# Write Final Report

## Type
BUILD

## Description
Compile all research into a single final report.

## Requirements
1. Create `projects/ai-clone-opportunity/final-report.md`
2. Structure:
   - **Executive Summary** — thesis, methodology, #1 pick in 3 sentences
   - **Methodology** — how candidates were identified and scored
   - **Candidate Matrix** — embed or link to the scored matrix
   - **Top 3 Analysis** — summarize each deep dive
   - **Recommendation** — #1 pick with rationale
   - **MVP Plan Summary** — key points from the detailed MVP plan
   - **Next Steps** — concrete actions (create BUILD backlog, use website cloner on target, etc.)
   - **References** — link to candidate-matrix.md, top-3-deep-dives.md, mvp-plan.md
3. This is the executive-readable output — someone should be able to read just this file and understand the full recommendation

## Acceptance Criteria
- [ ] `test -f projects/ai-clone-opportunity/final-report.md`
- [ ] Report references all scored candidates
- [ ] #1 pick has tech stack, timeline, and revenue path
- [ ] Next steps section includes actionable items
