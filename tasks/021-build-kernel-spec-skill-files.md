# Build Kernel Spec Skill Files

## Context
Build the core skill files for the kernel spec: SKILL.md, workflow.md, gate-contract.md, and all step files. Use the chosen template from task 018 as the structural base but adapt all content for kernel building (not Docker/browser testing).

## Dependencies
- **019** — kernel spec design (workflow steps defined)
- **020** — kernel spec repo exists

## Phase Gate
- [ ] `research/019-kernel-spec-design.md` exists with workflow steps
- [ ] `D:\my_ai_projects\project_test_repos\specs\kernel-spec` repo exists

## Requirements

### Build into: `D:\my_ai_projects\project_test_repos\specs\kernel-spec\.claude\skills\kernel-build-guidance\`

### Template base
Read the chosen template (from 018 recommendation) and adapt its structure. Read the template's SKILL.md, workflow.md, gate-contract.md, and all step files BEFORE writing any kernel spec files.

### SKILL.md
- Identity: What this spec is (teaches domain-setup to build the kernel)
- Philosophy: "Bootstrap the governance layer. One spec, one command, kernel lives."
- 5-layer overview or step overview (from 019 design)
- File index pointing to all skill files
- Critical rules (what MUST happen, what MUST NOT happen)

### workflow.md
- Step index table with data flow
- State persistence (where state is saved between steps)
- Validation per step
- Protocol execution sequence

### gate-contract.md
- 6 gate responsibilities (Validate, Teach, Learn, Block, Save, Loop) adapted for kernel building
- HITL protocol adapted (kernel building is less risky than production testing — adjust accordingly)

### Step files (step-01 through step-N)
One file per workflow step from 019 design. Each step file must include:
- Identity & Flow table (step N of M, gate responsibilities)
- Skill Instruction block (ACTION / VALIDATE / OUTPUT)
- State Schema JSON (what gets saved after this step)

### Checkpoints
- `checkpoints/on-failure.md` — what to do when a step fails during kernel build
- `checkpoints/pre-build-check.md` — verify workspace is clean before building

## Output
All skill files in `kernel-spec/.claude/skills/kernel-build-guidance/`

## Validation
- [ ] SKILL.md exists with identity, philosophy, file index, critical rules
- [ ] workflow.md exists with step index, data flow, state persistence
- [ ] gate-contract.md exists with 6 responsibilities adapted for kernel building
- [ ] All step files exist (one per workflow step from 019 design)
- [ ] All checkpoint files exist
- [ ] Every file has YAML frontmatter (if template uses it)
- [ ] No Docker/browser/QA content — all adapted for kernel building

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
