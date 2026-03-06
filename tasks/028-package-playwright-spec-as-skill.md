# Package Playwright Spec as Marketplace Skill

## Context
Convert the playwright-spec from repo format to skill-installable format. Same process as task 027 (selenium-spec). Follow the exact same steps.

## Dependencies
- **027** — selenium spec packaged (use it as the reference for consistency)

## Phase Gate
- [ ] Selenium spec packaged and pushed (task 027 complete)

## Requirements

### Read the existing playwright-spec
Read ALL files in: `D:\my_ai_projects\project_test_repos\specs\playwright-spec\`

### Apply the same changes as 027
- Replace absolute paths with relative
- Remove internal repo references
- Ensure YAML frontmatter on all skill files
- Ensure Kernel Loop Integration on all commands
- Add/update README with install flow

### Commit and push
- Work in: `D:\my_ai_projects\project_test_repos\specs\playwright-spec`
- Commit message: `feat: package playwright spec for marketplace distribution`
- Push to `isagawa-co/playwright-spec`

## Output
- Updated playwright-spec repo ready for marketplace distribution

## Validation
- [ ] Same checks as 027 (YAML frontmatter, Kernel Loop Integration, no absolute paths, README, pushed)

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
