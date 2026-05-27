# Verify GitHub Repo is Live

## Context
After pushing, verify the public GitHub repo at https://github.com/isagawa-qa/platform-ssh shows the updated README with badges, contact, and LICENSE.

## Type
TEST

## Execution
agent

## Dependencies
005

## Phase Gate
- [ ] Platform-SSH repo has been pushed to origin

## Requirements
- Use web fetch or GitHub CLI to verify the public repo
- Check LICENSE file is visible
- Check README renders with badges and contact section

## Acceptance Criteria
- [ ] `gh api repos/isagawa-qa/platform-ssh/contents/LICENSE` returns 200
- [ ] `gh api repos/isagawa-qa/platform-ssh/contents/README.md` shows updated content

## Gates Satisfied
TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
