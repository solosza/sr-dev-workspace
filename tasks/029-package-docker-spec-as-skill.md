# Package Docker Spec as Marketplace Skill

## Context
Convert the docker-spec from repo format to skill-installable format. Same process as tasks 027-028 (selenium/playwright specs). Follow the exact same steps.

## Dependencies
- **027** — selenium spec packaged (use as reference for consistency)

## Phase Gate
- [ ] Selenium spec packaged and pushed (task 027 complete)

## Requirements

### Read the existing docker-spec
Read ALL files in: `D:\my_ai_projects\project_test_repos\specs\docker-spec\`

### Apply the same changes as 027
- Replace absolute paths with relative
- Remove internal repo references
- Ensure YAML frontmatter on all skill files
- Ensure Kernel Loop Integration on all commands
- Add/update README with install flow

### Commit and push
- Work in: `D:\my_ai_projects\project_test_repos\specs\docker-spec`
- Commit message: `feat: package docker spec for marketplace distribution`
- Push to `isagawa-co/docker-spec`

## Output
- Updated docker-spec repo ready for marketplace distribution

## Validation
- [ ] Same checks as 027 (YAML frontmatter, Kernel Loop Integration, no absolute paths, README, pushed)

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
