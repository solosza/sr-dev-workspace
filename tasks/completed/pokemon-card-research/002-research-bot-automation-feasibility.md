# Research: Bot/automation tools and agentic buying feasibility

## Context
Research what tools smart buyers currently use to acquire Pokemon cards at retail before other buyers. Assess whether building a Playwright-based agentic buyer is feasible and worth the effort.

## Type
RESEARCH

## Execution
agent

## Requirements
- Use WebSearch to research: Pokemon card restock bots, auto-checkout tools, Discord stock monitors
- Identify the most popular tools/services (NowInStock, BrickSeek, Notibot, CardBot, etc.)
- Research anti-bot measures retailers use (CAPTCHA, queue systems, Cloudflare, purchase limits)
- Assess Playwright-based agent feasibility: can it monitor, detect restocks, auto-add-to-cart, and checkout?
- Identify technical barriers (CAPTCHA solving, account bans, IP blocking, shipping address limits)
- Compare cost-benefit: building a custom agent vs subscribing to existing alert/bot services
- Note legal/ethical considerations (TOS violations, state laws on bot purchases)

## Acceptance Criteria
- [ ] `projects/pokemon-card-research/02-bot-automation-feasibility.md` exists
- [ ] File lists at least 5 existing tools/services with descriptions
- [ ] File includes anti-bot countermeasures analysis
- [ ] File includes Playwright feasibility assessment with technical barriers
- [ ] File includes cost-benefit comparison (build vs buy)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
