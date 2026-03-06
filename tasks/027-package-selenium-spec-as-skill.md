# Package Selenium Spec as Marketplace Skill

## Context
Convert the selenium-spec from repo format to skill-installable format. This is the first QA spec SKU. The goal: a user installs this skill, runs domain-setup, and has a governed Selenium/Python QA workspace.

## Dependencies
- **024** — kernel spec complete (the kernel spec must exist so users can install kernel first, then this)

## Phase Gate
- [ ] Kernel spec repo complete and pushed at `isagawa-co/kernel-spec`

## Requirements

### Read the existing selenium-spec
Read ALL files in: `D:\my_ai_projects\project_test_repos\specs\selenium-spec\`
- `.claude/skills/` — all skill files
- `.claude/commands/` — all commands
- `.claude/lessons/` — all lessons
- Any reference code, framework files, etc.

### Assess skill-readiness
Document what needs to change for marketplace distribution:
- Are all files self-contained? (no references to external repos or absolute paths)
- Are commands using Kernel Loop Integration?
- Do skill files have YAML frontmatter?
- Are lessons seeded with domain knowledge?
- Is there a README that explains install + usage?

### Apply changes
Fix any issues found in the assessment. Ensure:
- All absolute paths replaced with relative paths
- No references to sr_dev_test, cognitive-agent, or other internal repos
- Commands reference the skill folder correctly
- README includes install flow: install kernel → install this spec → domain-setup → restart

### Commit and push
- Work in the existing repo: `D:\my_ai_projects\project_test_repos\specs\selenium-spec`
- Commit message: `feat: package selenium spec for marketplace distribution`
- Push to `isagawa-co/selenium-spec`

## Output
- Updated selenium-spec repo ready for marketplace distribution

## Validation
- [ ] All skill files have YAML frontmatter
- [ ] All commands have Kernel Loop Integration
- [ ] No absolute paths or internal repo references
- [ ] README exists with install flow
- [ ] Committed and pushed

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
