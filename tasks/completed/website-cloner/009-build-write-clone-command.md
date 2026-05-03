# Write Clone Command

## Type
BUILD

## Description
Write the `/clone` command that users invoke to clone a website.

## Requirements
Create `.claude/commands/clone.md` with:
- Usage: `/clone https://example.com` or `/clone https://example.com my-clone/`
- Instructions that reference the SKILL.md: "Read and follow: .claude/skills/website-cloner/SKILL.md"
- Arguments: URL (required), output directory (optional, defaults to `cloned-sites/[domain]/`)
- The command is a thin wrapper — the skill has the actual implementation steps

## Acceptance Criteria
- [ ] `test -f .claude/commands/clone.md`
- [ ] `grep -q "website-cloner/SKILL.md" .claude/commands/clone.md`
