# Layer Templates — Supporting Layers

**Purpose:** Templates for supporting generated files (references INDEX, contracts, workflow, gate contract, hooks). The agent reads these templates and fills in values from the design doc.

**Core layer templates:** See [[build-command/references/layer-templates]]

---

## References INDEX.md

```markdown
# References Index

## Design Doc References

→ `.claude/docs/design/[command-name]/references/workflow.md` — step procedures
→ `.claude/docs/design/[command-name]/references/[file].md` — [purpose]

## By Step

### Step 1: [Name]
- → design doc: [[references/[file]]] — what it is

### Step 2: [Name]
- → design doc: [[references/[file]]] — what it is

## By Artifact Type

### [Type 1]
- → design doc: [[references/[file]]] — context
```

**Note:** The skill's INDEX.md links to design doc references — it does not duplicate content.

---

## Contract JSON

```json
{
  "contract_metadata": {
    "contract_id": "[command-name]:step-N:output",
    "version": "1.0",
    "artifact_type": "[markdown|sql|json|xlsx]",
    "artifact_filename": "[expected output filename]",
    "canonical_reference": {
      "path": "docs/design/[command-name]/references/[file].md",
      "hash": null
    },
    "dependencies": [],
    "validation_metadata": {
      "validation_count": 0,
      "last_validated_at": null,
      "staleness_threshold_hours": 24
    }
  },
  "validations": [],
  "mechanical_validations": [],
  "overrides": []
}
```

**Notes:**
- `validations` = soft gate rules (agent checks during execution)
- `mechanical_validations` = hard gate rules (hook checks on write)
- `dependencies` = upstream contracts this step requires (dbt pattern — downstream declares)
- `canonical_reference.path` points to design doc references, not skill references
- `canonical_reference.hash` = populated after first build, updated when reference changes

---

## Workflow.md

```markdown
# Workflow

## Phases

### Phase 1: [Name]
- Steps: 1, 2, ...
- Gate: [what must be true before proceeding]

### Phase 2: [Name]
- Steps: ..., ...
- Gate: [what must be true]

## State Persistence

**Location:** [path from design doc]

{
  "command_name": "[command-name]",
  "current_step": 0,
  "steps_complete": [],
  "last_updated": null
}

## HITL Stops

| After Step | Why | User Options |
|-----------|-----|-------------|
[From design doc's workflow summary — HITL column]
```

---

## Gate Contract

```markdown
# Gate Contract

## Phase Gates

| Gate | Trigger | Check | On Fail |
|------|---------|-------|---------|
[From design doc — what must be true between phases]

## Step Gates

| Step | Output | Validation |
|------|--------|-----------|
[One row per step — what the step must produce and how to verify]
```

---

## Hook Files (Layer 6 — Optional)

Only generated if the design doc specifies mechanical validations that need enforcement at write time.

```python
# .claude/hooks/[command-name]-[hook-purpose].py
# Generated from contract mechanical_validations
# Reads: .claude/skills/[command-name]/contracts/step-NN-contract.json
# Blocks: writes to [artifact pattern] that fail validation
```

If no mechanical validations are specified in the design doc, Layer 6 is skipped entirely.
