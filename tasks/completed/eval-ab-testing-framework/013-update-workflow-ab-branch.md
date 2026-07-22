# Task 013: Update workflow.md — AB State Machine Branch

## Action
Edit `.claude/skills/eval/workflow.md` to add the A/B mode state machine.

## Changes
Add a new section "## A/B Mode State Machine" after the existing state machine:

| State | Entry Condition | Exit Condition |
|-------|-----------------|----------------|
| `ab_generating_variants` | Source resolved, mode=ab | Flat + tiered variants created |
| `ab_building_prompt` | Variants exist | Task prompt ready |
| `ab_running` | Prompt ready | N iterations complete |
| `ab_scoring` | All outputs captured | All runs scored |
| `ab_reporting` | Scores computed | Report generated, verdict determined |

Add A/B loop behavior table referencing steps step-ab-1 through step-ab-5.

## Acceptance Criteria
- workflow.md has A/B state machine section
- States map to step-ab-* files
- Error handling references included
