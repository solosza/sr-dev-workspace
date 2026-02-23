# LinkedIn Post #2: The Learning Loop

**Status:** Draft — ready for publish
**Date:** 2026-02-23
**Platform:** LinkedIn (post, not article)
**Character count:** ~2,917 / 3,000 limit
**Accompanies:** No video (standalone text post)
**Series:** Post 2 (Post 1: demo video, Post 2: learning loop)

---

The AI failed 10 times on a live production site. Each time, it got permanently smarter.

I pointed my AI test automation system at zentyant.app — a real client's production app — and told it to generate Selenium tests.

It failed. A lot. And that was the point.

Failures 1-3: The AI hardcoded XPath selectors. //div[...], //li[...], //span[...]. Each one broke when the DOM shifted. Three consecutive failures, same root cause.

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

Next, I'll show what happens when you stop prompting AI and start giving it structure.

Open source. MIT license.
https://github.com/isagawa-qa/platform

I also set up full QA infrastructure for teams — framework, config, credential management, and training. DM me or email alain@isagawa.co.

#TestAutomation #QA #Selenium #OpenSource #AI #ClaudeCode #AINative
