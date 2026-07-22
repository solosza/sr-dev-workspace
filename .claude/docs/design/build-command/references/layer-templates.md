# Layer Templates — Core Layers

**Purpose:** Templates for the primary generated files (SKILL.md, step files, command entry point). The agent reads these templates and fills in values from the design doc.

**Supporting layer templates:** See [[build-command/references/layer-templates-supporting]]

---

## SKILL.md

```markdown
---
name: [command-name]
version: 1.0
status: draft
type: skill
design_doc: .claude/docs/design/[command-name]/index.md
design_doc_hash: [sha256]
---

# [Command Name] — Skill

## Identity

[One sentence from design doc's Skill Identity section]

## Philosophy

[Numbered list from design doc's Philosophy section]

## Vocabulary

| Term | Meaning |
|------|---------|
[From design doc's Vocabulary table]

## Workflow

[Brief overview — point to workflow.md for details]

| Step | What It Does |
|------|-------------|
[One row per step from design doc's Workflow Summary]

## Critical Rules

[Numbered list from design doc's Critical Rules section]

## File Index

| File | Purpose |
|------|---------|
| `SKILL.md` | This file — orchestrator |
| `workflow.md` | Phase definitions, state schema |
| `gate-contract.md` | Phase gates, verification |
| `steps/step-01-[name].md` | [purpose] |
| ... | ... |
| `references/INDEX.md` | Reference index |
| `contracts/step-NN-contract.json` | [purpose] |
```

---

## Step Files

```markdown
# Step N: [Step Name]

## Purpose

[From design doc's step spec]

## Input

[What feeds into this step — files, data, prior step output]

## Output

[What this step produces — files, data, state changes]

## Acceptance Criteria

[How to verify step success — checkable conditions]

## References

[Wikilinks to relevant reference files]

## Procedure

[Step-by-step what to do — from design doc's step spec]

## Verification

[How to confirm step is complete — concrete checks]

## Failure Recovery

[What to do if step fails — from design doc or reasonable default]
```

---

## Command Entry Point

```markdown
# /[command-name]

[One-line description from design doc]

## Usage

/[command-name] [arguments]

| Argument | Purpose | Example |
|----------|---------|---------|
[From design doc's Input section]

## What It Does

[2-3 sentences from design doc summary]

## Examples

[From design doc or generated from input spec]

## Design Reference

→ `.claude/docs/design/[command-name]/index.md`

## Skill Reference

→ `.claude/skills/[command-name]/`
```
