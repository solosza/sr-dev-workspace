# Design Kernel Spec Schema

## Context
Design the kernel spec — a domain spec that, when consumed by domain-setup, builds the Isagawa Kernel into any workspace. This is the bootstrap spec.

**Critical rule:** domain-setup is the constant primitive. It always exists. The kernel spec is just the first domain spec it consumes. domain-setup is NOT built by the kernel spec.

## Dependencies
- **017** — kernel audit (know what files the kernel spec must produce)
- **018** — template comparison (know which spec template to use as base)

## Phase Gate
- [ ] `research/017-kernel-audit.md` exists with Category 1 files identified
- [ ] `research/018-spec-template-comparison.md` exists with template recommendation

## Requirements

### Define what the kernel spec produces
Using the 017 audit, list every file domain-setup must create when reading the kernel spec:
- `CLAUDE.md` — kernel rules, loop, commands reference
- Kernel commands (session-start, anchor, learn, complete, fix, reset, autonomous-cycle)
- Hook files (universal gate enforcer, action counter)
- `settings.local.json` hook registration
- State file templates
- Skills: kernel-domain-setup (the setup skill itself gets installed), autonomous-cycling

### Define the workflow steps
What are the "steps" for building a kernel? Example:
- Step 1: Workspace validation (clean workspace? existing kernel?)
- Step 2: Build CLAUDE.md from reference
- Step 3: Build kernel commands
- Step 4: Build hooks + gate enforcer
- Step 5: Build skills (domain-setup, autonomous-cycling)
- Step 6: Register hooks in settings.local.json
- Step 7: Initialize state files
- Step 8: Verify + restart

### Define the file structure
Design the full directory tree for the kernel-spec repo.

### Write the design document
Write to: `D:\my_ai_projects\project_test_repos\sr_dev_test\research\019-kernel-spec-design.md`

Include:
- What the kernel spec produces (every file)
- Workflow steps
- Bootstrap sequence (domain-setup → kernel spec → restart → domain spec → restart → governed)
- File structure for the kernel-spec repo
- Reference code strategy (how does the spec ship template files?)
- Open questions

## Output
- `sr_dev_test/research/019-kernel-spec-design.md`

## Validation
- [ ] Design document exists with all sections
- [ ] Every Category 1 file from 017 audit is accounted for
- [ ] Workflow steps defined with clear inputs/outputs per step
- [ ] Bootstrap sequence documented
- [ ] File structure defined

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
