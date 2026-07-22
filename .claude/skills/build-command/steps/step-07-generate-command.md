# Step 7: Generate Command Entry Point

## Purpose

Create the Layer 1 user-facing command file that routes to the skill.

## Input

- Design doc Input/Output spec and usage examples
- Template: > `.claude/docs/design/build-command/references/layer-templates.md#Command Entry Point`

## Output

- `.claude/commands/kernel/[name].md`

## Acceptance Criteria

- [ ] Command file has `## Usage` with signature and arguments table
- [ ] Has `## What It Does` (2-3 sentences from design doc summary)
- [ ] Has `## Examples` (from design doc or generated from input spec)
- [ ] Has `## Design Reference` pointing to design doc index
- [ ] Has `## Skill Reference` pointing to skill directory
- [ ] Under 200 lines

## References

- > `.claude/docs/design/build-command/references/layer-templates.md`

## Procedure

1. Read design doc Input section > write Usage + Arguments table
2. Read design doc summary > write What It Does
3. Generate examples from input spec
4. Add Design Reference wikilink to design doc index
5. Add Skill Reference wikilink to skill directory

## Verification

- File exists at `.claude/commands/kernel/[name].md`
- Has all required sections
- Under 200 lines

## Failure Recovery

If design doc lacks usage examples, generate from the input spec (path argument + expected output).
