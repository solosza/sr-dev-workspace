# Audit Domain-Setup for Rerunability

## Context
Domain-setup must be rerunnable: first for the kernel spec (builds the kernel), then again for a domain spec (builds domain governance). Currently domain-setup may not support layered installs — it might overwrite state, clobber existing commands, or conflict on protocol files.

## Dependencies
- **024** — kernel spec complete and pushed (need to know what it produces to check for conflicts)

## Phase Gate
- [ ] Kernel spec repo complete and pushed

## Requirements

### Read domain-setup thoroughly
Read ALL step files in: `D:\my_ai_projects\isagawa-kernel\.claude\skills\kernel-domain-setup\`
- SKILL.md
- All reference files (step-01 through step-10)

### Identify rerunability issues
For each step, answer:
1. Does it check for existing state before writing?
2. Does it merge or overwrite?
3. What happens if kernel commands already exist when a domain spec runs?
4. What happens to `CLAUDE.md` on second run?
5. What happens to hooks on second run?
6. What happens to `settings.local.json` on second run?
7. What happens to the protocol file on second run?
8. What happens to state files on second run?

### Document findings
Write to: `D:\my_ai_projects\project_test_repos\sr_dev_test\research\025-domain-setup-rerunability.md`

Structure:
```markdown
# Domain-Setup Rerunability Audit

## Step-by-Step Analysis
| Step | Action | Existing State Check? | Merge or Overwrite? | Issue? |

## Conflict Points
| File | First Run (kernel spec) | Second Run (domain spec) | Conflict? | Fix |

## Required Changes
1. [change needed]
2. [change needed]

## Proposed Fix Strategy
- Merge vs overwrite per file type
- How to detect "kernel already built, adding domain spec"
```

## Output
- `sr_dev_test/research/025-domain-setup-rerunability.md`

## Validation
- [ ] All domain-setup step files read
- [ ] Every step analyzed for rerunability
- [ ] Conflict points documented
- [ ] Fix strategy proposed

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
