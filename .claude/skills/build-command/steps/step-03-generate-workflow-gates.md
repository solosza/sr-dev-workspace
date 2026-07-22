# Step 3: Generate Workflow + Gates

## Purpose

Create the workflow definition and phase gate contract files (Layer 2). Generated workflow MUST include Layer 2 pre-generation checkpoints in every step that produces output.

## Input

- Design doc workflow/step summary
- Design doc step payloads (for checkpoint reading lists)
- State persistence schema from design doc
- Phase gates from design doc
- Templates: -> `.claude/docs/design/build-command/references/layer-templates-supporting.md`
- Tiered-index Layer 2: -> `.claude/docs/design/tiered-index-architecture/references/layer-2-checkpoints.md`

## Output

- `.claude/skills/[name]/workflow.md`
- `.claude/skills/[name]/gate-contract.md`

## Acceptance Criteria

- [ ] workflow.md has `## Phases` with phase definitions
- [ ] workflow.md has `## State Persistence` with state schema
- [ ] workflow.md has `## HITL Stops` if design doc specifies them
- [ ] **Every step that generates output has a "Pre-generation checkpoint" block** (Layer 2 enforcement)
- [ ] **Checkpoints list specific file paths** (not generic "read references")
- [ ] **Checkpoints include: canonical reference, contract, input from prior step**
- [ ] gate-contract.md has `## Phase Gates` table
- [ ] gate-contract.md has `## Step Gates` table
- [ ] Both files under 200 lines

## Layer 2 Checkpoint Enforcement

When generating workflow.md, each step section MUST include:

```markdown
### Step N: [Step Name]

**Pre-generation checkpoint:**
- Read canonical reference: `[specific file path]`
- Read contract: `contracts/step-NN-contract.json` (if contract exists for this step)
- Read [specific input from prior step]
- Read [any domain-specific reference needed]

**How agent uses the reference:**
1. Agent reads reference -- sees the exact format
2. Agent reads input -- knows what content to generate
3. Agent generates artifact matching reference format with input content
```

Steps that only read data (no output artifact) may omit the checkpoint but MUST still list their reading dependencies.

## References

- -> `.claude/docs/design/build-command/references/layer-templates-supporting.md`
- -> `.claude/docs/design/build-command/references/workflow.md`
- -> `.claude/docs/design/tiered-index-architecture/references/layer-2-checkpoints.md`

## Procedure

1. Read design doc workflow/step summary -> write phase definitions
2. Read state persistence schema -> write state section
3. Read phase gates -> write gate-contract.md
4. Document HITL stops if specified
5. **For each step:** read the step's design doc payload, extract its reading list, write a pre-generation checkpoint block
6. **Verify:** every output-producing step has a checkpoint with specific file paths

## Verification

- workflow.md has required sections
- gate-contract.md has required tables
- Both under 200 lines
- **Every output-producing step has a checkpoint block with specific paths**

## Failure Recovery

If design doc lacks phase definitions, use step boundaries as implicit phases.
If design doc step payloads lack checkpoints, generate them from the step's References section.
