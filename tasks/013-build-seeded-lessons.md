# Build Seeded Lessons

## Context
Pre-seed the lessons index with domain-specific knowledge categories. Cheat-sheet format — actionable directives, not descriptions. Same format as docker-spec lessons. All output goes into the creative-finance-spec repo.

## Dependencies
- **001-004** — research (distilled into actionable rules)
- **007-009** — pipeline specs (distilled into flow rules)

## Requirements

Read these files before building:
- `creative-finance-spec/research/001-lease-option-structure.md`
- `creative-finance-spec/research/002-buyer-types-matching.md`
- `creative-finance-spec/research/003-communication-patterns.md`
- `creative-finance-spec/research/004-integration-surface.md`
- `creative-finance-spec/pipeline/seller/qualification.md`
- `creative-finance-spec/pipeline/matching/engine.md`

Build into: `D:\my_ai_projects\project_test_repos\specs\creative-finance-spec\.claude\lessons\`

### lessons.md (index)
Cheat-sheet index with category table and payload links. Format:
```
| Topic | File | Key Rules |
|-------|------|-----------|
| Lease Options | `lease-options/deal-structure.md` | Qualification gates, scoring, disqualifiers |
| Communication | `communication/voice.md` | Tone rules, never-say list, personalization |
| Integration | `integration/gmail-patterns.md` | gws CLI, session management, error handling |
| Pipeline | `pipeline/flow-rules.md` | Execution order, gates, handoff points |
```

### lease-options/deal-structure.md
Distill from 001 research into actionable directives:
- "If equity < X%, REJECT — not a lease option candidate"
- "If seller needs cash in < 30 days, REJECT — lease options need time"
- "Score = (equity_weight × equity_score) + (motivation_weight × motivation_score) + ..."
- "Strong ≥ 80, Moderate 50-79, Weak 30-49, Reject < 30"
- Key disqualifiers as a quick-reference list

### communication/voice.md
Distill from 003 research into actionable directives:
- "NEVER use 'we buy houses' language — positions you as investor, not solution provider"
- "ALWAYS reference the specific property address in first touch"
- "Seller tone: empathetic → educational → action. NOT: salesy → urgent → pressure"
- "Buyer tone: encouraging → informative → next-step. NOT: condescending → pushy"
- Never-say list for each side

### integration/gmail-patterns.md
Distill from 004 research into actionable directives:
- "ALWAYS search Gmail for prior contact before first touch"
- "Session-id format: `{lead_type}-{name_slug}-{property_slug}` — e.g., `seller-john-smith-123-main-st`"
- "NEVER send more than 10 emails per day per deal (spam trigger)"
- "If gws CLI returns auth error: check OAuth token expiry, re-auth, retry once"
- Error handling patterns as quick-reference

### pipeline/flow-rules.md
Distill from pipeline specs into actionable directives:
- "Execution order: intake → qualify → score → outreach → [wait for lock] → match → disposition → handoff"
- "GATE: No outreach without qualification. No disposition without matching. No handoff without interest confirmation."
- "Deal status progression: new → qualified → locked → matched → assigned → closed. NEVER skip a status."
- "Buyer status progression: new → active → matched → interested → scheduled → closed."
- Handoff rules as quick-reference

## Output
- `creative-finance-spec/.claude/lessons/lessons.md`
- `creative-finance-spec/.claude/lessons/lease-options/deal-structure.md`
- `creative-finance-spec/.claude/lessons/communication/voice.md`
- `creative-finance-spec/.claude/lessons/integration/gmail-patterns.md`
- `creative-finance-spec/.claude/lessons/pipeline/flow-rules.md`

## Validation (check ALL before completing)
- [ ] All 5 files exist at their output paths
- [ ] lessons.md index has table with all 4 categories and correct file paths
- [ ] Each topic file is under 200 lines
- [ ] Each topic file uses cheat-sheet format (actionable directives, not descriptions)
- [ ] deal-structure.md has specific numeric thresholds (not vague)
- [ ] voice.md has never-say lists for both seller and buyer sides
- [ ] gmail-patterns.md has session-id format definition
- [ ] flow-rules.md has status progressions for both deals and buyers
- [ ] No file duplicates content from another file (index points, details in topic files)

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
