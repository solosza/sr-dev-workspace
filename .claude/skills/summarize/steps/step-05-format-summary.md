# Step 5: Format Summary

## Purpose

Assemble the dynamic summary report from all collected data.

## Procedure

1. **Header:**
   ```
   SUMMARY: [backlog title or project name]
   Backlog: [NNN] | Scope: [scope]
   Status: [complete/partial/failed]
   ```

2. **Requirement Diff** (backlog mode only):
   - Full diff table from Step 3
   - Summary line: "Requirements: N/M met, K partial, J not addressed"

3. **Decisions Needed** (only if decisions exist):
   - Each decision as a bullet with title, description, options

4. **Deliverable Inventory** (always):
   - Full file table from Step 2
   - Summary line: "Files: N created, M modified"

5. **Problems** (only if problems exist):
   - Each problem as a bullet with description, impact, fix

6. **Informational** (only if informational items exist):
   - Each item as a bullet

## Dynamic Sizing

- Show ALL items in each section. No truncation, no "and N more."
- Omit empty sections entirely (don't show "Decisions Needed: none").
- Requirement diff is always present in backlog mode.

## Acceptance Criteria

- [ ] Summary follows template format
- [ ] All applicable sections present
- [ ] No artificial compression
- [ ] Empty sections omitted
