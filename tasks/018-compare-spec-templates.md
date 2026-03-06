# Compare Spec Templates — Choose Base

## Context
The kernel spec needs a template base. Compare the docker-spec and playwright-spec to determine which is the better starting point. The chosen template will be adapted for the kernel spec and all future specs.

## Dependencies
- **017** — kernel audit must be complete so we know what the kernel spec needs to produce

## Phase Gate
- [ ] `research/017-kernel-audit.md` exists and has content

## Requirements

### Read both spec templates fully
**Docker spec:** `D:\my_ai_projects\project_test_repos\specs\docker-spec\.claude\skills\image-testing-guidance\`
- SKILL.md, workflow.md, gate-contract.md
- steps/step-01.md through step-05.md
- checkpoints/ (all files)

**Playwright spec:** `D:\my_ai_projects\project_test_repos\specs\playwright-spec\.claude\skills\`
- Find the skill folder, read SKILL.md, workflow.md, gate-contract.md
- All step files
- All checkpoint files

### Also read the commands from both
- Docker spec commands: `D:\my_ai_projects\project_test_repos\specs\docker-spec\.claude\commands\`
- Playwright spec commands: `D:\my_ai_projects\project_test_repos\specs\playwright-spec\.claude\commands\`

### Compare and document
Write to: `D:\my_ai_projects\project_test_repos\sr_dev_test\research\018-spec-template-comparison.md`

Structure:
```markdown
# Spec Template Comparison

## Docker Spec
- File count:
- Step count:
- Gate contract pattern:
- Strengths:
- Weaknesses:

## Playwright Spec
- File count:
- Step count:
- Gate contract pattern:
- Strengths:
- Weaknesses:

## Comparison Matrix
| Aspect | Docker Spec | Playwright Spec |

## Recommendation
Which template and why. How to adapt it for the kernel spec.
```

## Output
- `sr_dev_test/research/018-spec-template-comparison.md`

## Validation
- [ ] Both specs fully read (all skill files, commands, checkpoints)
- [ ] Comparison document exists with all sections
- [ ] Clear recommendation with rationale

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
