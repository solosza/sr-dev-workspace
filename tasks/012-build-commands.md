# Build Commands

## Context
Pipeline workflow commands adapted for lease option wholesaling. These are what the agent invokes to operate the pipeline. All output goes into the creative-finance-spec repo.

## Dependencies
- **011** — skill files must exist (commands reference skill steps)

## Requirements

Read these files before building:
- `creative-finance-spec/.claude/skills/lease-option-pipeline/SKILL.md`
- `creative-finance-spec/.claude/skills/lease-option-pipeline/workflow.md`

Build into: `D:\my_ai_projects\project_test_repos\specs\creative-finance-spec\.claude\commands\`

### pipeline-workflow.md
Main 5-step workflow command. Invokes the full pipeline for a single seller lead:
1. Receive lead data (from argument or prompt)
2. Run step-01 (intake)
3. Run step-02 (qualification)
4. Run step-03 (outreach)
5. Report status and wait for deal-locked trigger
References: skill steps 01-03

### pipeline-workflow-dev.md
Dev mode variant — same as above but:
- All emails go as draft (never auto-send regardless of config)
- Verbose logging of every decision
- Dry-run option: qualify and score but don't create any emails

### process-lead.md
Process a single seller lead end-to-end. Input: lead data as JSON or natural language.
- Parse input into seller lead schema
- Run full pipeline-workflow
- Report: qualified (yes/no), score, email sent/drafted, next steps

### match-deal.md
Run matching engine for a locked deal. Input: deal identifier or deal data.
- Load deal from state or parse from input
- Run step-04 (matching + disposition)
- Run step-05 (follow-up setup)
- Report: N buyers matched, N emails sent/drafted, next steps

### on-failure.md
HITL failure triage. When something fails:
- Show what failed, why, and what data was involved
- Propose fix options
- Wait for investor decision
- Execute approved fix

### run-pipeline.md
Batch process — run all pending leads through the pipeline:
- Scan for unprocessed leads (status: new)
- Process each sequentially via pipeline-workflow
- Report summary: N processed, N qualified, N disqualified, N emails sent/drafted

## Output
- `creative-finance-spec/.claude/commands/pipeline-workflow.md`
- `creative-finance-spec/.claude/commands/pipeline-workflow-dev.md`
- `creative-finance-spec/.claude/commands/process-lead.md`
- `creative-finance-spec/.claude/commands/match-deal.md`
- `creative-finance-spec/.claude/commands/on-failure.md`
- `creative-finance-spec/.claude/commands/run-pipeline.md`

## Validation (check ALL before completing)
- [ ] All 6 files exist at their output paths
- [ ] pipeline-workflow.md references skill steps 01-03 by path
- [ ] pipeline-workflow-dev.md adds draft-only and verbose flags
- [ ] process-lead.md defines input format (JSON or natural language)
- [ ] match-deal.md references skill steps 04-05 by path
- [ ] on-failure.md defines the triage flow (show → propose → wait → execute)
- [ ] run-pipeline.md defines batch logic with summary report
- [ ] Each command has clear Instructions section with numbered steps

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
