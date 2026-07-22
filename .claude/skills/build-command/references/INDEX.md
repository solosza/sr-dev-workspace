# References Index

## Design Doc References

> `.claude/docs/design/build-command/index.md` — design doc index (source of truth)
> `.claude/docs/design/build-command/references/workflow.md` — step procedures (1-8)
> `.claude/docs/design/build-command/references/cross-cutting-rules.md` — no-code rule, name extraction, rebuild, 200-line threshold
> `.claude/docs/design/build-command/references/input-contract.md` — completeness checklist (7 required + 5 optional)
> `.claude/docs/design/build-command/references/layer-templates.md` — SKILL.md, step file, command entry point templates
> `.claude/docs/design/build-command/references/layer-templates-supporting.md` — INDEX.md, contract JSON, workflow, gate contract, hook templates

## By Step

### Step 1: Validate Design Doc
- > `.claude/docs/design/build-command/references/input-contract.md` — completeness checklist
- > `.claude/docs/design/build-command/references/cross-cutting-rules.md` — name extraction, rebuild handling

### Step 2: Generate SKILL.md
- > `.claude/docs/design/build-command/references/layer-templates.md` — SKILL.md template

### Step 3: Generate Workflow + Gates
- > `.claude/docs/design/build-command/references/layer-templates-supporting.md` — workflow.md + gate-contract.md templates

### Step 4: Generate Steps
- > `.claude/docs/design/build-command/references/layer-templates.md` — step file template
- > `.claude/docs/design/build-command/references/workflow.md` — step specs

### Step 5: Generate References
- > `.claude/docs/design/build-command/references/layer-templates-supporting.md` — INDEX.md template

### Step 6: Generate Contracts
- > `.claude/docs/design/build-command/references/layer-templates-supporting.md` — contract JSON template

### Step 7: Generate Command Entry Point
- > `.claude/docs/design/build-command/references/layer-templates.md` — command entry point template

### Step 8: Verify Build
- > `.claude/docs/design/build-command/references/cross-cutting-rules.md` — 200-line threshold

## By Artifact Type

### Templates
- > `.claude/docs/design/build-command/references/layer-templates.md` — core layers (SKILL.md, steps, command)
- > `.claude/docs/design/build-command/references/layer-templates-supporting.md` — supporting layers (INDEX, contracts, workflow, gates, hooks)

### Validation
- > `.claude/docs/design/build-command/references/input-contract.md` — design doc completeness checklist

### Rules
- > `.claude/docs/design/build-command/references/cross-cutting-rules.md` — cross-cutting constraints
