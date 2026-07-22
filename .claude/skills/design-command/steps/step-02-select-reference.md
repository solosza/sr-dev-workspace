# Step 2: Select Reference Design

## Purpose

Pick the best existing design doc to use as structural template for the new command.

## Input

- Confirmed command name + description from Step 1
- All existing design doc indexes (discovered via glob)

## Output

- Reference design path
- Rationale for selection

## Acceptance Criteria

- [ ] All existing design docs discovered via glob
- [ ] Best match selected based on workflow similarity
- [ ] Selected reference design fully read (index + all payloads)

## References

- Design doc: `.claude/docs/design/design-command/references/workflow.md` (Step 2)

## Procedure

1. Read all existing design doc indexes:
   - `.claude/docs/design/build-command/index.md`
   - `.claude/docs/design/gap-check/index.md`
   - (and any others found via glob at `.claude/docs/design/*/index.md`)
2. Compare description to each reference design:
   - Data processing / validation → gap-check (corpus detection, per-item loops)
   - Code generation / scaffolding → build-command (input validation, file generation)
   - Pipeline / orchestration → execute-pipeline or spawn-agent-swarm patterns
3. Select best match based on workflow similarity
4. Read the selected reference design fully (index + all payloads)

## Verification

- Reference design path is a valid existing file
- Rationale explains why this reference was chosen

## Failure Recovery

| Situation | Action |
|-----------|--------|
| No existing design docs found | Use build-command's input-contract as minimal template |
| Multiple equally good matches | Pick the one with more steps (richer template) |
