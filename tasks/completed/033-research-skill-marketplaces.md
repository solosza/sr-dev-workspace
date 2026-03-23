# Research Skill Marketplaces

## Context
Research distribution channels for domain specs as installable skills. No payment platforms (Gumroad, etc.) — distribution is through skill marketplaces only.

## Dependencies
- None (can run in parallel with other autonomous tasks)

## Requirements

### Research Claude Code skill marketplace
- Web search for Claude Code skill marketplace, Anthropic skill marketplace, Claude Code extensions
- Is there an official marketplace? Beta? Planned?
- What's the submission process?
- What format do skills need to be in?
- Revenue sharing model?

### Research other AI tool marketplaces
- Cursor extensions/marketplace
- Windsurf skill marketplace
- GitHub Marketplace (Actions, Apps — could specs be distributed as Actions?)
- VS Code marketplace (could a VS Code extension wrap the spec install?)

### Research skill format requirements
- What file structure do different marketplaces expect?
- How do our specs map to each marketplace's skill format?
- Any packaging changes needed beyond what tasks 027-029 already do?
- Discovery and search — how do users find skills?

### Document findings
Create `research/033-skill-marketplace-research.md` with:
1. **Marketplace comparison table** — name, status, format, revenue share, submission process
2. **Recommended primary channel** — based on format fit and audience reach
3. **Format mapping** — how our spec structure maps to each marketplace's requirements
4. **Timeline** — what's available now vs coming soon

## Output
- `research/033-skill-marketplace-research.md`

## Validation
- [ ] At least 3 marketplaces researched
- [ ] Comparison table with actionable recommendations
- [ ] Format mapping documented
- [ ] Primary distribution channel recommended

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
