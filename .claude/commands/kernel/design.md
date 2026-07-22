# /design

Produce or update a design doc — from user intent, an existing command, or an existing skill.

## Usage

```
/design [command-name] [description]
/design [existing-source]
```

| Argument | Purpose | Example |
|----------|---------|---------|
| `command-name` | Kebab-case name for the command | `audit-workflow` |
| `description` | What the command should do (natural language) | `"Walk through a completed pipeline run and verify all artifacts exist"` |
| `existing-source` | Path to existing command, skill, or design doc to update | `.claude/skills/gap-check/` |

## Input Modes

| Input | Mode | What Happens |
|-------|------|-------------|
| Name + description | **New** | Interview → draft → validate → write design doc |
| Description only | **New** | Agent proposes name, then same as above |
| Skill directory | **Extract** | Read existing skill → reverse-engineer design doc from it |
| Command file | **Extract** | Follow Skill Reference → read skill → reverse-engineer design doc |
| Existing design doc | **Update** | Read existing design doc → validate → interview for gaps → update |

**Extract mode:** Reads an existing skill package (SKILL.md, steps, workflow, contracts) and produces the design doc that *should* exist for it. Fills the gap for commands that were built manually without going through `/design` first. The extracted design doc is then valid input for `/build-command` rebuild.

**Update mode:** Reads an existing design doc, validates completeness, identifies gaps, interviews the user to fill them, and writes the updated version.

## What It Does

Takes user intent OR an existing command/skill and produces a structured design doc that satisfies all 7 required sections from build-command's input contract AND follows tiered-index architecture (all 3 layers).

**Tiered-index enforcement:** Every design doc produced by this command must pass build-command Step 1 validation:
- **Layer 1:** index.md is pure index, all payloads in references/, every file under 200 lines
- **Layer 2:** Workflow steps have pre-generation checkpoints with specific file paths
- **Layer 3:** Contract definitions with soft_validation_rules and mechanical_validations arrays

## Examples

```
# New design from intent
/design validate-tc "Validate test case data against truth tables and SQL dumps"
/design "Walk through a completed pipeline run and verify all artifacts exist"

# Extract design doc from existing skill
/design .claude/skills/gap-check/
/design .claude/commands/kernel/anchor.md

# Update existing design doc
/design .claude/docs/design/build-command/index.md
```

## Design Reference

> `.claude/docs/design/design-command/index.md`

## Skill Reference

> `.claude/skills/design-command/`
