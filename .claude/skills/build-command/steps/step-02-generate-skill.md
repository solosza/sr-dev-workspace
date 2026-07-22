# Step 2: Generate SKILL.md

## Purpose

Create the Layer 2 skill orchestrator from the design doc's identity, philosophy, vocabulary, and critical rules sections. This is the foundation file — all downstream generation inherits from it.

## Input

- Design doc sections: Identity, Philosophy, Vocabulary, Critical Rules, Workflow Summary
- Template: > `.claude/docs/design/build-command/references/layer-templates.md#SKILL.md`

## Output

- `.claude/skills/[name]/SKILL.md`

## Acceptance Criteria

- [ ] SKILL.md has frontmatter with: name, version, status, type, design_doc, design_doc_hash
- [ ] Has `## Identity` (one sentence from design doc)
- [ ] Has `## Philosophy` (numbered list from design doc)
- [ ] Has `## Vocabulary` (table from design doc)
- [ ] Has `## Workflow` (overview + step table, points to workflow.md)
- [ ] Has `## Critical Rules` (numbered list from design doc)
- [ ] Has `## File Index` (table listing all skill files)
- [ ] Under 200 lines

## References

- > `.claude/docs/design/build-command/references/layer-templates.md`
- > `.claude/docs/design/build-command/references/cross-cutting-rules.md`

## Procedure

1. Read design doc Identity section > write `## Identity`
2. Read Philosophy > write `## Philosophy`
3. Read Vocabulary > write `## Vocabulary`
4. Read Critical Rules > write `## Critical Rules`
5. Read Workflow Summary > write `## Workflow` (overview only)
6. Generate `## File Index` listing all files to be created
7. Compute design doc hash > add to frontmatter

## Verification

Present SKILL.md preview to user. User must `approve` before proceeding.

## Failure Recovery

| Response | Action |
|----------|--------|
| approve | Write SKILL.md, proceed to Step 3 |
| modify | User provides corrections, agent updates, re-presents |
| stop | Abort build |
