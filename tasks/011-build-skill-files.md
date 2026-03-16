# Build Skill Files

## Context
The skill definition that teaches the kernel agent how to operate the lease option wholesaling pipeline. Follows the same pattern as docker-spec's image-testing-guidance skill. All output goes into the creative-finance-spec repo.

## Dependencies
- **007** — seller pipeline (steps 1-3 reference seller flow)
- **008** — buyer pipeline (steps 4-5 reference buyer flow)
- **009** — matching engine (step 4 references matching)
- **010** — client config (workflow references config loading)

## Requirements

Read these files before building:
- `creative-finance-spec/pipeline/seller/` — all 4 files
- `creative-finance-spec/pipeline/buyer/` — all 6 files
- `creative-finance-spec/pipeline/matching/` — all 4 files
- `creative-finance-spec/pipeline/config/schema.md`

Build into: `D:\my_ai_projects\project_test_repos\specs\creative-finance-spec\.claude\skills\lease-option-pipeline\`

### SKILL.md
- Identity: "Lease Option Pipeline — Speed-to-Lead Domain Spec"
- Philosophy: "Speed kills — first credible response wins. Qualify before you communicate. Match precisely, not broadly."
- 5-step overview table pointing to step files
- File index: all files in the skill directory with purpose
- Critical rules:
  - NEVER send email without qualification passing first
  - NEVER auto-send without investor config allowing it
  - ALWAYS personalize — generic templates are a protocol violation
  - ALWAYS update deal/buyer status after every interaction

### workflow.md
- Data flow diagram: lead intake → qualification → outreach → matching → disposition → handoff
- State transitions for deals: new → qualified → locked → matched → assigned → closed
- State transitions for buyers: new → active → matched → interested → scheduled → closed
- Session management: one session-id per lead, persists across interactions
- Config loading: read client config at session start, apply thresholds and HITL preferences

### gate-contract.md
- HITL gates (what requires human approval):
  - First-touch email to seller (configurable: draft vs auto-send based on config)
  - Disposition email to buyers (configurable: draft vs auto-send based on config)
  - Deal-locked status change (always manual — investor confirms contract is signed)
  - Investor handoff (system prepares briefing, investor takes over)
- Autonomous actions (what the system does without asking):
  - Qualification scoring
  - Buyer matching and ranking
  - Follow-up sequence execution (after first touch is approved)
  - Education sequence execution (after buyer shows interest)
  - Calendar event creation
  - Nurture emails to warm list

### steps/step-01.md — Lead Intake
- Receive webhook payload or manual input
- Parse and validate against seller lead schema
- Check for duplicate (search by email/phone/address)
- Create session with session-id
- Log: "New lead received: [name] — [property address]"
- Next: proceed to step 02

### steps/step-02.md — Qualification & Scoring
- Load client config (thresholds)
- Run qualification logic from `pipeline/seller/qualification.md`
- If disqualified: log reason, notify investor (optional), STOP
- If qualified: run scoring from `pipeline/seller/scoring.md`
- Log: "Lead qualified: [score] — [tier]"
- Next: proceed to step 03

### steps/step-03.md — Seller Outreach
- Load communication patterns from `pipeline/seller/first_touch.md`
- Generate personalized first-touch email using lead data + score + voice guidelines
- Check HITL config: draft or auto-send?
- If draft: create Gmail draft, notify investor
- If auto-send: send via Gmail, log
- Initiate follow-up sequence from `pipeline/seller/follow_up.md`
- Monitor for "deal locked" trigger
- Next: when deal locked → proceed to step 04

### steps/step-04.md — Matching & Disposition
- Trigger: deal status → "locked"
- Run matching engine from `pipeline/matching/engine.md`
- Rank buyers from `pipeline/matching/ranking.md`
- Execute batch outreach from `pipeline/matching/outreach_rules.md`
- Check HITL config for disposition emails
- Log: "Deal matched: [N] buyers contacted"
- Next: proceed to step 05

### steps/step-05.md — Follow-up & Handoff
- Handle buyer responses from `pipeline/matching/response_handling.md`
- Interested buyers: route to education sequence or schedule call
- Run education sequence from `pipeline/buyer/education_sequence.md`
- Schedule calls from `pipeline/buyer/scheduling.md`
- Prepare investor handoff briefing: buyer profile + deal details + match score + communication history
- Non-matching buyers: route to nurture from `pipeline/buyer/nurture.md`
- Log: "Handoff ready: [buyer name] — [deal address]"

### checkpoints/pre-send.md
- Before any email send: verify recipient exists, email not bounced previously, content personalized (not template), HITL config respected

### checkpoints/on-failure.md
- Email send fails: log error, retry once, if still fails notify investor
- Matching returns 0 results: notify investor, suggest expanding buyer list or search area
- gws CLI error: log full error, check OAuth status, notify investor

### checkpoints/propose-fix.md
- When a failure is fixable: propose the fix to investor, wait for approval, then execute
- Never auto-fix something that changes deal status or sends communication

## Output
- `creative-finance-spec/.claude/skills/lease-option-pipeline/SKILL.md`
- `creative-finance-spec/.claude/skills/lease-option-pipeline/workflow.md`
- `creative-finance-spec/.claude/skills/lease-option-pipeline/gate-contract.md`
- `creative-finance-spec/.claude/skills/lease-option-pipeline/steps/step-01.md`
- `creative-finance-spec/.claude/skills/lease-option-pipeline/steps/step-02.md`
- `creative-finance-spec/.claude/skills/lease-option-pipeline/steps/step-03.md`
- `creative-finance-spec/.claude/skills/lease-option-pipeline/steps/step-04.md`
- `creative-finance-spec/.claude/skills/lease-option-pipeline/steps/step-05.md`
- `creative-finance-spec/.claude/skills/lease-option-pipeline/checkpoints/pre-send.md`
- `creative-finance-spec/.claude/skills/lease-option-pipeline/checkpoints/on-failure.md`
- `creative-finance-spec/.claude/skills/lease-option-pipeline/checkpoints/propose-fix.md`

## Validation (check ALL before completing)
- [ ] All 11 files exist at their output paths (Glob to confirm)
- [ ] SKILL.md file index lists all 11 files with correct relative paths
- [ ] SKILL.md critical rules include the 4 rules from requirements
- [ ] workflow.md has state transition definitions for deals and buyers
- [ ] gate-contract.md clearly separates HITL gates from autonomous actions
- [ ] Each step file has: input, process, output, logging, and "Next" pointer
- [ ] Step files reference the correct pipeline spec files by path
- [ ] Checkpoint files cover: pre-send validation, failure handling, fix proposal
- [ ] No step allows email send without qualification check passing first

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
