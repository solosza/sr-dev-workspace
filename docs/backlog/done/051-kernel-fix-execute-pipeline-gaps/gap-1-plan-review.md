# Gap 1: Re-enable Plan Review in Autonomous Pipeline

## Status
NEW

## Location
`.claude/skills/execute-pipeline/references/step-03-run-task-builder.md`

## Problem
`step-03-run-task-builder.md` sets `skip_plan_review: true`, meaning the fully autonomous path (the most common one) never validates paths, conventions, gate coverage, or test completeness before writing tasks. Plan review (step 7) catches wrong directory conventions, missing L3 tests, invented paths — exactly the errors that cost the most during execution. Skipping it saves one agent spawn but risks 20+ broken tasks.

## Fix
Remove `skip_plan_review: true` from the pipeline mode flags. The plan review agent spawn is cheap (30-60 seconds). The cost of skipping it is 20+ broken tasks that each take 10 minutes to fail.

Change in `step-03-run-task-builder.md`:
```json
// BEFORE
{
  "pipeline_mode": {
    "skip_plan_review": true,
    "no_execute": true
  }
}

// AFTER
{
  "pipeline_mode": {
    "skip_plan_review": false,
    "no_execute": true
  }
}
```

Also update the process description and comments to reflect that plan review now runs.

## Dependencies
None — standalone change.
