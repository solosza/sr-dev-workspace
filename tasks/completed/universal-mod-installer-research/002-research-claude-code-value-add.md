# Task 002: Research Claude Code Value-Add

## Type
RESEARCH

## Objective
Determine whether Claude Code + Playwright MCP adds genuine value over existing mod managers, or if this is a solved problem. Be honest — if existing tools already do this well, say so.

## Steps
1. Review the FM24 proof of concept session:
   - What did Claude Code do that Vortex/MO2 can't?
   - What was painful about the manual Playwright approach? (rate limits, download waits, auth handling)
   - Was the AI layer necessary or was it just browser automation?
2. Identify unique Claude Code advantages:
   - Natural language mod discovery ("install the best graphics packs for FM24")
   - Cross-site navigation (sortitoutsi + fmscout + df11 in one session)
   - Intelligent conflict resolution (understanding what mods do, not just file conflicts)
   - Game-specific setup guidance (explaining load order, cache clearing, new game requirements)
   - Adaptive — handles site layout changes without hardcoded selectors
3. Identify disadvantages vs traditional mod managers:
   - Speed (Playwright downloads vs direct HTTP)
   - Reliability (browser automation is fragile)
   - Cost (Claude API usage for what could be a simple file manager)
   - No persistent state between sessions (mod manager remembers installed mods)
4. Assess: is this a harness or just a script?
   - Does it need kernel governance, hooks, protocol?
   - Or is it better as a simple command/skill within existing kernel?
5. Evaluate monetization potential:
   - Is anyone paying for mod management? (Nexus Premium, etc.)
   - Would gamers use a Claude-powered mod installer?
   - Portfolio/showcase value vs actual product

## Deliverable
`projects/universal-mod-installer-research/02-claude-code-value-add.md`

## Acceptance Criteria
- Honest assessment of Claude Code advantages AND disadvantages
- Clear answer: harness, skill, or don't build
- Monetization/market analysis
