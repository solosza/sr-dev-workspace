# /build-command

Scaffold or rebuild a complete 6-layer command structure from a design doc or existing skill.

## Usage

```
/build-command [source]
```

| Argument | Purpose | Example |
|----------|---------|---------|
| `source` | Design doc index, skill directory, or command file | `.claude/docs/design/validate-tc/index.md` |

## Input Modes

| Input | Mode | What Happens |
|-------|------|-------------|
| Design doc path | **New build** | Validate design doc → scaffold full skill package |
| Skill directory | **Rebuild** | Read existing skill → validate against pattern → regenerate gaps |
| Command file | **Rebuild** | Follow Skill Reference → validate → regenerate gaps |
| Command name | **Rebuild** | Resolve to `.claude/skills/[name]/SKILL.md` → validate → regenerate gaps |

**Rebuild mode:** Reads the existing skill package, validates every layer against command-skill-pattern, reports gaps, and regenerates missing/malformed files. Existing files that pass validation are preserved. Files that fail are regenerated from the design doc (if one exists) or flagged for `/design` first.

## What It Does

Reads a design document OR an existing skill package and produces/validates the complete 6-layer structure — SKILL.md, workflow, gate contract, step files, reference index, contract JSONs, and command entry point. In new-build mode, all generation is mechanical translation from the design doc. In rebuild mode, validates what exists and fills gaps.

## Instructions

1. Read and follow: `.claude/skills/build-command/SKILL.md`
2. Execute steps 1-8 sequentially, reading each step file before executing

## Examples

```
# New build from design doc
/build-command .claude/docs/design/validate-tc/index.md

# Rebuild existing skill
/build-command .claude/skills/gap-check/
/build-command .claude/commands/kernel/gap.md
/build-command gap-check
```

## Design Reference

> `.claude/docs/design/build-command/index.md`

## Skill Reference

> `.claude/skills/build-command/`
