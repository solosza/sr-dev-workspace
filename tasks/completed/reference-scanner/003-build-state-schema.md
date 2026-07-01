# Build State Schema

## Type
BUILD

## Phase Gate
Task 001 must be complete.

## Deliverable
`.claude/skills/reference-scanner/state-schema.md`

## Instructions
1. Read the state-schema design doc: `docs/backlog/153-kernel-build-reference-scanner/state-schema.md`
2. Create `.claude/skills/reference-scanner/state-schema.md` documenting:
   - The `references` state object schema (index_path, scan_timestamp, payload_catalog, by_step)
   - Where state lives: inside each command's existing state file
   - Caching rules: skip re-scan if `references` populated and index file not modified since `scan_timestamp`
   - Invalidation: user says "reconfigure" at Step 0, or index file mtime > scan_timestamp
   - How steps use it: read `by_step["all"]` + `by_step[step_number]` at step start
3. Include the JSON schema example from the design doc

## Verification
- File exists at `.claude/skills/reference-scanner/state-schema.md`
- Contains JSON schema for references state object
