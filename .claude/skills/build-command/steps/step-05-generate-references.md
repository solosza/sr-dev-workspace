# Step 5: Generate References

## Purpose

Create the Layer 4 reference index that links back to design doc references. No content duplication — the INDEX.md is a routing table.

## Input

- Design doc's Design Documents table (lists all reference payloads)
- Template: > `.claude/docs/design/build-command/references/layer-templates-supporting.md#References INDEX.md`

## Output

- `.claude/skills/[name]/references/INDEX.md`
- Stub files only if new canonical examples are needed (not in design doc)

## Acceptance Criteria

- [ ] INDEX.md has `## Design Doc References` with wikilinks to all design doc reference files
- [ ] INDEX.md has `## By Step` section organized by step number
- [ ] INDEX.md has `## By Artifact Type` section
- [ ] No design doc content duplicated — INDEX.md only links
- [ ] Under 200 lines

## References

- > `.claude/docs/design/build-command/references/layer-templates-supporting.md`

## Procedure

1. Read the design doc's Design Documents table
2. Create INDEX.md with wikilinks pointing to design doc references (absolute paths)
3. Organize by step and by artifact type
4. Do NOT copy design doc reference content into skill references

## Verification

- Every wikilink in INDEX.md resolves to an existing file
- No content duplication (INDEX.md should be short — only links)

## Failure Recovery

If design doc has no Design Documents table, create minimal INDEX.md pointing to the design doc index only.
