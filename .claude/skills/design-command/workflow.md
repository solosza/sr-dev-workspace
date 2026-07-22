# Workflow

## Phases

### Phase 1: Setup (Steps 1-2)
- Steps: Parse Intent, Select Reference Design
- Gate: Command name confirmed + reference design selected

### Phase 2: Requirements (Step 3)
- Steps: Interview
- Gate: Structured requirements covering all 7 required sections

### Phase 3: Generation (Steps 4-6)
- Steps: Draft Design Doc, Validate Completeness, Write Files
- Gate: Design doc passes completeness check (7/7 required sections) + files written to disk

### Phase 4: Closeout (Step 7)
- Steps: Report
- Gate: Summary delivered + state cleaned up

## State Persistence

**Location:** `.claude/state/design-command-state.json`

```json
{
  "command_name": "[name]",
  "description": "[original intent]",
  "reference_design": "[path to reference design doc]",
  "current_step": 0,
  "steps_complete": [],
  "requirements": {},
  "last_updated": null
}
```

**Resume:** Re-run `/design [same-name]`. Agent reads state, skips completed steps.

## HITL Stops

| After Step | Why | User Options |
|-----------|-----|-------------|
| 1. Parse Intent | Confirm command name | approve / rename / stop |
| 3. Interview | Full interactive session | User provides requirements |

## Step Dependency Map

```
Step 1 (Parse Intent)
  ↓
Step 2 (Select Reference)
  ↓
Step 3 (Interview) ← HITL: interactive
  ↓
Step 4 (Draft Design Doc)
  ↓
Step 5 (Validate Completeness) → fail? → loop to Step 3
  ↓
Step 6 (Write Files)
  ↓
Step 7 (Report)
```
