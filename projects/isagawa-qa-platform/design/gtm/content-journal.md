# Content Journal

Tracks all published and planned content for Isagawa QA Platform GTM.

## Published

| # | Date | Platform | Type | Title / Hook | File | Engagement |
|---|------|----------|------|-------------|------|------------|
| 1 | 2026-02-22 | LinkedIn | Post + Video | "I built a highly scalable, maintainable, enterprise-grade test automation platform powered by AI..." | social-media.md (Section 1) | TBD |

## Ready to Publish

| # | Date | Platform | Type | Title / Hook | File |
|---|------|----------|------|-------------|------|
| 2 | 2026-02-23 | LinkedIn | Post | "The AI failed 10 times on a live production site. Each time, it got permanently smarter." | See Post Drafts below |

## Planned

| # | Target | Platform | Type | Angle | Notes |
|---|--------|----------|------|-------|-------|
| 3 | TBD | LinkedIn | Post | "Why I don't let AI code alone" | HITL pair programming model — human approves every fix, 5-option failure protocol |
| 4 | TBD | LinkedIn | Post | "5 layers that make AI-generated tests maintainable" | Architecture deep-dive — Screenplay-inspired, reference implementations |
| 5 | TBD | LinkedIn | Post | "I automated 17 tests on a client site in [X] hours" | Business results story — zentyant.app, 4 domains, time savings |
| 6 | TBD | LinkedIn | Post | "Most AI coding tools suggest. Mine enforces." | Competitive positioning — what makes enforcement different from instructions |
| 7 | TBD | Reddit | Posts | r/QualityAssurance, r/selenium, r/softwaretesting, r/ClaudeAI | Drafts in social-media.md |
| 8 | TBD | X/Twitter | Thread | 8-tweet thread on AI Execution Management | Draft in social-media.md. Requires @isagawa account (PENDING) |
| 9 | TBD | Blog | Article | "AI Governance vs AI Execution Management" | blog-post.md (ready) |
| 10 | TBD | Product Hunt | Listing | Launch listing | Draft in social-media.md |

## Post Series Arc

1. **Post 1 (published):** Here's what it does — demo video on a live site
2. **Post 2 (ready):** Here's how it learns — 10 failures on zentyant.app
3. **Post 3:** Why I don't let AI code alone (HITL)
4. **Post 4:** 5 layers that make AI-generated tests maintainable (architecture)
5. **Post 5:** I automated 17 tests on a client site (business results)
6. **Post 6:** Most AI coding tools suggest. Mine enforces. (competitive)

## Tracking Notes

- Update Engagement column after 48 hours (impressions, likes, comments, reposts, DMs)
- Note which hooks/angles generate the most engagement to inform future content

---

## Post Drafts

### Post #2: The Learning Loop

**Status:** Ready to publish
**Date:** 2026-02-23
**Platform:** LinkedIn (post, not article)
**Character count:** ~2,800 / 3,000 limit

---

The AI failed 10 times on a live production site. Each time, it got permanently smarter.

I pointed my AI test automation system at zentyant.app — a real client's production app — and told it to generate Selenium tests.

It failed. A lot. And that was the point.

Failures 1-3: The AI hardcoded XPath selectors. //div[...], //li[...], //span[...]. Wrong tag each time. Three consecutive failures from the same mistake: assuming the DOM structure instead of using element-agnostic selectors.

The system captured all three, collapsed them into one lesson: "Always use element-agnostic selectors — //*[...] with @role or @data-testid."

Every test generated after that uses the correct pattern. Not because I told it to. Because the system won't let it forget.

Failure 7 was the one that changed everything.

The AI made a mistake it had already solved two sessions earlier. The fix was sitting right there in the system's own lessons file — but it didn't read it before writing new code.

Think of it like an employee who keeps making the same mistake because they never check the team's runbook.

So we added a rule: before the AI writes any new test code, it must first read every lesson it's learned from previous failures. If it skips this step, it's blocked. Can't proceed.

The result? The AI doesn't just learn from mistakes — it's required to review what it's learned before every new task. That's not a suggestion. It's enforced.

How the loop works:

1. AI writes test code
2. Test fails — hook detects failure automatically
3. AI is blocked from writing more code until it records what went wrong
4. Human reviews and approves the fix
5. Lesson is recorded — what broke, why, and how to prevent it
6. Block clears. AI resumes. That failure mode is now documented and gated.

After 10 lessons on one client site, the system had learned:

- Element-agnostic XPath selectors (3 failures, 1 compound lesson)
- Wait patterns for transient toast notifications
- contains(., ...) over contains(text(), ...) for text matching
- starts-with() over CSS ^= for partial attribute matching
- Don't duplicate modules across domains — reuse first
- Integration tests need different architectural rules than functional tests
- And that meta-lesson: read your own lessons before writing new code

The result: 17 automated tests across 4 business domains. Consistent 5-layer architecture. Code that gets better with every session — not because the AI is smarter, but because the system won't let it repeat mistakes.

Open source. MIT license.
https://github.com/isagawa-qa/platform

I also set up full QA infrastructure for teams — framework, config, credential management, and training. DM me or email alain@isagawa.co.

#TestAutomation #QA #Selenium #OpenSource #AI #ClaudeCode #AINative
