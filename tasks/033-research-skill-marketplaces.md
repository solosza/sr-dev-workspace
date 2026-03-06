# Research Skill Marketplaces

## Context
Research distribution channels for domain specs. The spec-led growth strategy identifies Gumroad as Tier 1 distribution, but Claude Code skill marketplace and other AI tool marketplaces may offer native distribution. This research informs marketplace publishing tasks later.

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

### Research Gumroad distribution
- How to auto-provision GitHub repo access after Gumroad purchase
- Gumroad API capabilities for access provisioning
- Payment → private repo invite automation
- Alternatives: Lemon Squeezy, Paddle, Stripe + custom provisioning

### Document findings
Create `research/033-skill-marketplace-research.md` with:
1. **Marketplace comparison table** — name, status, format, revenue share, submission process
2. **Recommended primary channel** — based on format fit and audience reach
3. **Gumroad automation plan** — payment → access flow
4. **Timeline** — what's available now vs coming soon

## Output
- `research/033-skill-marketplace-research.md`

## Validation
- [ ] At least 3 marketplaces researched
- [ ] Gumroad automation plan documented
- [ ] Comparison table with actionable recommendations
- [ ] Primary distribution channel recommended

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
