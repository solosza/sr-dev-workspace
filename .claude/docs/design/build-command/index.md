---
name: build-command
type: design-document
version: 1.0
date_created: 2026-06-20
status: draft
purpose: Command that scaffolds any new command's 6-layer structure from a design doc
---

# /build-command — Design Index

<!-- INDEX file — points to payloads. Do not duplicate payload content here. -->
<!-- 200-line threshold: split when exceeded. -->

## Position in System

```
intent → /kernel/backlog → /kernel/task-builder → /kernel/execute-pipeline
                                                        ↓
                                                  /build-command ← you are here
                                                        ↓
                                                  new command ready
                                                  (standalone or inner loop)
```

`/build-command` is itself a command built on the command-skill-pattern. It reads a design doc and produces a complete 6-layer command structure. It is the loop that builds other loops.

## Skill Identity

You are a command scaffolder. You read a design doc that describes a command's identity, steps, references, and contracts, and you produce the complete skill package — every file in the right place, following the canonical command-skill-pattern exactly.

## Philosophy

1. **Design doc is the spec** — the design doc contains everything needed to build. If information is missing, flag it — don't guess.
2. **Mechanical, not creative** — scaffolding is translation from design to file structure. The creative work happened during design. This command just materializes it.
3. **Standalone first** — every command built by this tool must work as a standalone outer loop before being integrated as an inner loop.
4. **One source of truth** — the design doc is the authority. The generated files are derived artifacts. If they conflict, the design doc wins.
5. **Validate before done** — every generated file is checked against the command-skill-pattern template. Missing sections or wrong structure = build failure.

## Vocabulary

| Term | Meaning |
|------|---------|
| **design doc** | The input — a tiered-index design document describing a command (identity, steps, contracts, references) |
| **skill package** | The output — the complete `.claude/skills/[name]/` directory tree |
| **command entry point** | The `.claude/commands/kernel/[name].md` file users invoke |
| **command name** | Derived from design doc folder name (e.g., `validate-tc` from `.claude/docs/design/validate-tc/index.md`) |
| **layer** | One of the 6 levels in command-skill-pattern (command, skill, steps, references, contracts, hooks) |
| **completeness checklist** | The 7 required + 5 optional sections from command-skill-pattern that a design doc must contain |
| **scaffolding** | Translating design doc sections into files — not inventing content |
| **rebuild** | Re-running `/build-command` on a design doc that already has a skill package. Overwrites all generated files. |

## Input

```
/build-command [design-doc-path]
```

Single argument: path to the design doc index (e.g., `.claude/docs/design/validate-tc/index.md`).

**Command name extraction:** The command name is the design doc's parent folder name. For `.claude/docs/design/validate-tc/index.md`, the command name is `validate-tc`. This drives all generated paths (`skills/validate-tc/`, `commands/kernel/validate-tc.md`).

## Output

Complete 6-layer command structure:

```
.claude/
├── commands/kernel/
│   └── [name].md                          ← Layer 1: command entry point
├── skills/[name]/
│   ├── SKILL.md                           ← Layer 2: orchestrator
│   ├── workflow.md                        ← Layer 2: phase definitions
│   ├── gate-contract.md                   ← Layer 2: phase gates
│   ├── steps/
│   │   ├── step-01-[name].md              ← Layer 3: per-step procedures
│   │   └── step-NN-[name].md
│   ├── references/
│   │   ├── INDEX.md                       ← Layer 4: reference index
│   │   └── step-NN/                       ← Layer 4: per-step references
│   │       └── [reference-files].md
│   └── contracts/
│       └── step-NN-contract.json          ← Layer 5: validation rules
└── hooks/
    └── [name]-*.py                        ← Layer 6: hard gates (if needed)
```

## Design Documents

| Document | Purpose |
|----------|---------|
| [[build-command/references/workflow]] | Steps 1-8: validate input, generate each layer, verify output |
| [[build-command/references/cross-cutting-rules]] | No-code rule, name extraction, rebuild, failure recovery, 200-line threshold, HITL modes |
| [[build-command/references/input-contract]] | What the design doc must contain (completeness checklist as formal input spec) |
| [[build-command/references/layer-templates]] | Templates for core layers (SKILL.md, step files, command entry point) |
| [[build-command/references/layer-templates-supporting]] | Templates for supporting layers (references INDEX, contracts, workflow, gates, hooks) |

## Workflow Summary

| Step | Responsibility | Output | HITL |
|------|---------------|--------|------|
| 1. Validate Design Doc | Check completeness checklist | Pass/fail + missing sections list | **FULL STOP** — user reviews completeness |
| 2. Generate SKILL.md | Extract identity, philosophy, vocabulary, rules | Layer 2 orchestrator | **CHECKPOINT** — user approves foundation |
| 3. Generate Workflow + Gates | Extract phases, state schema | Layer 2 workflow + gate-contract | — |
| 4. Generate Steps | Extract per-step specs | Layer 3 step files | — |
| 5. Generate References | Extract/create reference index + files | Layer 4 references | — |
| 6. Generate Contracts | Extract validation rules per step | Layer 5 contract JSONs | — |
| 7. Generate Command Entry Point | Create user-facing command file | Layer 1 command | — |
| 8. Verify Build | Check all files against command-skill-pattern | Pass/fail per layer | Report |

## Critical Rules

1. **Never generate content the design doc doesn't specify.** If the design doc says "3 steps," generate 3 step files — not 4.
2. **Flag missing sections, don't fill them.** If the design doc lacks contract definitions, report "missing: contract definitions" — don't invent contracts.
3. **Follow command-skill-pattern exactly.** File names, folder structure, frontmatter format — all must match the canonical template.
4. **Design doc references inform, skill references link.** The design doc's `references/` folder contains the design knowledge. The skill's `references/` folder links back to the design doc references via wikilinks — no content duplication. The design doc is the source of truth; the skill references point to it.
5. **Hooks are optional.** Not every command needs hard gates. Only generate hooks if the design doc specifies mechanical validations.
6. **Rebuild overwrites.** If the skill package already exists, `/build-command` overwrites all generated files. The design doc is always authoritative. No merge — full regeneration.
7. **200-line threshold.** Every generated file must stay under 200 lines. If a SKILL.md would exceed 200 lines, extract vocabulary or rules into sub-files and link from SKILL.md.
8. **HITL fires in all modes.** HITL checkpoints (Step 1, Step 2) fire whether running as outer loop or inner loop. The design doc is the corpus — the user must confirm it before generation proceeds.

## Outer/Inner Loop Support

```
Outer loop (standalone):
  user → /build-command [design-doc-path]
    → reads design doc
    → scaffolds 6 layers
    → reports results

Inner loop (called by execute-pipeline):
  /kernel/execute-pipeline → task requires building a command
    → calls /build-command [design-doc-path]
    → receives scaffolded command
    → continues pipeline
```

## State Persistence

**Location:** `.claude/state/build-command-state.json`

```json
{
  "command_name": "[name]",
  "design_doc_path": "[path]",
  "current_step": 0,
  "steps_complete": [],
  "files_written": [],
  "last_updated": null
}
```

**Resume:** If interrupted, re-run `/build-command [same-path]`. Agent reads state, skips completed steps, continues from `current_step`. Files already written are overwritten (idempotent).

**Cleanup:** State file is deleted after Step 8 (Verify Build) passes.

## Complete File Structure

**Skill package** (generated output for `/build-command` itself):

```
.claude/commands/kernel/build-command.md          ← Layer 1
.claude/skills/build-command/
├── SKILL.md                                      ← Layer 2
├── workflow.md, gate-contract.md                 ← Layer 2
├── steps/step-{01..08}-*.md                      ← Layer 3 (8 steps)
├── references/INDEX.md                           ← Layer 4 (links to design doc)
└── contracts/step-01-contract.json               ← Layer 5
```

**Design doc** (this document + references):

```
.claude/docs/design/build-command/
├── index.md                                      ← this file
└── references/{workflow,cross-cutting-rules,input-contract,layer-templates,layer-templates-supporting}.md
```

**State:** `.claude/state/build-command-state.json` (deleted after successful build)

## Canonical References

This command reads and follows two canonical design patterns:

- `.claude/docs/design/command-skill-pattern/index.md` — the 6-layer template
- `.claude/docs/design/tiered-index-architecture/index.md` — file organization rules

---

**Version:** 1.0
**Last Updated:** 2026-06-20
**Changelog:**
- **v1.0:** Initial design. 8-step workflow, 6-layer output, design-doc-driven scaffolding.
