# Write SKILL.md

## Type
BUILD

## Description
Write the SKILL.md for the website-cloner skill, following kernel skill structure.

## Requirements
Create `.claude/skills/website-cloner/SKILL.md` with:
- Skill identity: "Website Cloner — Clone any website via Playwright MCP"
- Usage: `/clone https://example.com` or `/clone https://example.com output-dir/`
- Step table: navigate → extract → generate → output
- Key principles: clean semantic HTML, actual fonts, responsive breakpoints, self-contained output
- File index pointing to reference files
- Implementation approach determined by decision.md (task 005)

## Acceptance Criteria
- [ ] `test -f .claude/skills/website-cloner/SKILL.md`
- [ ] `grep -q "Website Cloner" .claude/skills/website-cloner/SKILL.md`
