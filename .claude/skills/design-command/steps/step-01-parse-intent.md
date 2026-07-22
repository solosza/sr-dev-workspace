# Step 1: Parse Intent

## Purpose

Detect input mode (new, extract, or update) and resolve the command name.

## Input

- User argument: one of these patterns:
  - `/design [command-name] [description]` — new mode
  - `/design [description]` — new mode (agent proposes name)
  - `/design .claude/skills/[name]/` — extract mode
  - `/design .claude/commands/kernel/[name].md` — extract mode
  - `/design .claude/docs/design/[name]/index.md` — update mode

## Output

- Detected mode: `new`, `extract`, or `update`
- Confirmed command name (kebab-case)
- Source path (for extract/update modes)

## Mode Detection

1. If path contains `skills/` → **extract** mode, name = skill folder name
2. If path contains `commands/` → **extract** mode, read file → find Skill Reference → name = skill folder
3. If path contains `docs/design` → **update** mode, name = design doc folder name
4. Otherwise → **new** mode, parse as name + description

## Acceptance Criteria

- [ ] Mode detected (new, extract, or update)
- [ ] Command name extracted or proposed (kebab-case)
- [ ] For new mode: no conflict with existing design docs (or user confirmed overwrite)
- [ ] For extract mode: source skill exists and is readable
- [ ] For update mode: source design doc exists and is readable
- [ ] User confirmed the name and mode

## References

- Design doc: `.claude/docs/design/design-command/references/workflow.md` (Step 1)

## Procedure

1. Read the argument — detect mode (see Mode Detection above)
2. **New mode:** split into command name (kebab-case) and description. If only description, propose name.
3. **Extract mode:** resolve source to skill directory, read SKILL.md to confirm it exists, extract name.
4. **Update mode:** read design doc index, extract name from folder.
5. Verify name doesn't conflict (new mode) or confirm overwrite (extract/update on existing design doc)
6. Confirm name and mode with user

## Verification

- Command name is kebab-case
- Mode is correctly detected
- Source is readable (extract/update modes)

## Failure Recovery

| Situation | Action |
|-----------|--------|
| Name conflicts with existing design doc | Offer overwrite / rename / stop |
| Source skill doesn't exist (extract) | Report error, suggest correct path |
| Source design doc doesn't exist (update) | Switch to new mode, confirm with user |
| User rejects proposed name | Ask for preferred name |
| No description provided (new mode) | Ask user to describe what the command should do |
