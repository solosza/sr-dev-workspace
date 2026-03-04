# Content Journal

Tracks all published and planned content for Isagawa QA Platform GTM.

## Published

| # | Date | Platform | Type | Title / Hook | Engagement |
|---|------|----------|------|-------------|------------|
| 1 | 2026-02-22 | LinkedIn | Post + Video | "I built a highly scalable, maintainable, enterprise-grade test automation platform powered by AI..." | TBD |
| X-1 | 2026-02-23 | X (@isagawa_co) | Post (pinned) | "AI can generate test scripts. But without enforcement, every test comes out different..." | TBD |
| 2 | 2026-02-23 | LinkedIn | Post | "The AI failed 10 times on a live production site. Each time, it got permanently smarter." | 942 impressions, 6 reactions, 1 comment |
| 3 | 2026-02-23 | LinkedIn + X | Post | "Every manual tester has the same fear: AI is going to replace me." | 193 impressions, 2 reactions |
| L-1 | 2026-02-24 | LinkedIn | Post + Video | "AI agents drift... So I built a leash." (Kernel governance loop, 48s video) | 67 impressions, 1 reaction, 1 repost |
| 4 | 2026-02-25 | LinkedIn | Post | "Everyone's talking about spec-driven development. I call it Self-Driven Development." | 45 impressions |
| 5 | 2026-02-25 | LinkedIn | Post | "I ran the same management system on two completely different tech stacks." | TBD |
| 6 | 2026-02-26 | LinkedIn | Post + Video | "Live demo found a real bug — full QA cycle in 41 minutes" | 7,488 impressions, 4,433 reached, 42 reactions, 2 comments, 3 reposts, 22 saves, 51 GitHub clicks, 2,820 video views, 24 followers gained. Demographics: 49% IT Services, 48% Senior, 29% 10K+ employees. **BEST POST — use as format template.** |
| 7 | 2026-02-26 | LinkedIn + X | Post + Video | "Vibe Coder Spec discovery phase — spec-driven development in action" | TBD |
| 8 | 2026-03-02 | LinkedIn | Post | "I automated 19 tests on a client's production app. Script generation alone: about 8 hours." | TBD |

## Ready to Publish

### Post #7: Vibe Coder Spec Discovery Phase (Video)

**Status:** Ready to publish
**Date:** 2026-02-26
**Platform:** LinkedIn + X
**Angle:** Spec-driven discovery — vague idea becomes full architecture before any code. Teases Vibe Coder Spec (coming soon) + Kernel (live now)
**Media:** Discovery phase screen recording, 3x speed

---

**LinkedIn:**

All I said was "I want to build a webhook that connects Gumroad to GitHub."

That's it. I didn't know the stack. I didn't know the architecture. I barely had the full idea fleshed out.

The agent didn't guess. It asked the right questions and recommended a stack for each decision — because the spec told it to. One product or many? Should refunds revoke access? Where does it run? How do you collect the buyer's GitHub username? Each question came with a recommendation and a clear explanation of the tradeoffs.

By the end of the conversation, we'd gone from a vague idea to a full picture — buyer purchases on Gumroad, gets collaborator access to my private repo. Multiple products mapped to different repos. Refunds revoke access. Node.js serverless on Vercel. Stateless — no database needed. GitHub tracks access, Gumroad tracks purchases.

I didn't come in knowing any of that. The spec-driven discovery phase pulled it out of me through the right questions and the right recommendations in the right order.

Full architecture, prioritized roadmap, and every decision documented — before a single line of code was written.

Two things made this work:

- **Isagawa Kernel** (open source now) — manages the agent. Enforces the spec, blocks the agent from skipping steps, keeps human in the loop.
- **Vibe Coder Spec** (coming soon) — drives the entire workflow. Discovery, stack decisions, architecture, roadmap, scaffold. You describe what you want in plain English. The spec tells the agent how to turn that into a working project.

Together, the kernel enforces the spec and the spec drives the agent. That's spec-driven development.

Kernel: https://github.com/isagawa-co/isagawa-kernel

The video is the full discovery phase at 3x speed.

#SpecDrivenDevelopment #AI #BuildInPublic #ClaudeCode #OpenSource

---

**X:**

All I said was "I want to build a webhook that connects Gumroad to GitHub." That's it.

The agent's spec told it what to ask and what to recommend. By the end of the conversation, we'd figured out the full picture — buyer purchases on Gumroad, gets access to my private repo. Multiple products, revoke on refund, serverless on Vercel, stateless, no database.

I didn't know any of that when I started. The spec-driven discovery asked the right questions and recommended the right stack.

Full architecture, prioritized roadmap, every decision documented. Before a single line of code.

Two things made this work — the Isagawa Kernel (open source now) manages the agent. The Vibe Coder Spec (coming soon) drives the discovery, decisions, and scaffold phases. Together, you describe what you want and the agent builds it right.

Kernel: github.com/isagawa-co/isagawa-kernel

Video is the full discovery phase at 3x speed.

#BuildInPublic #VibeCoding #SpecDrivenDevelopment #ClaudeCode

---

### Post #6: Live Demo Bug — Full QA Cycle in 41 Minutes

**Status:** Ready to publish
**Date:** 2026-02-26
**Platform:** LinkedIn
**Angle:** Real-world speed story — AI built the test, caught the bug live, dev team fixed in 21 min, retest confirmed in 18 seconds
**Media:** 18s defect video (bug happening live during demo)

---

I was demoing my QA platform to a colleague. The test script I built for the demo found a real bug — live, during the demo.

Here's what happened.

I pointed my AI test automation system at a client's production app — zentyant.app — and told it to generate a test for their Scheduled Tasks workflow. 20 minutes later I had a fully automated test script: login, navigate, create a scheduled task, verify success.

I ran it during the demo. It failed. The app's server returned HTTP 400 — their cron parser was broken. Every schedule preset, every manual cron input — all blocked. The platform caught it, took a screenshot automatically, and I had a full bug report with video evidence ready to send.

I sent the report to the dev team. 21 minutes later they pushed a fix and asked me to retest. I reran the exact same test the demo built.

Passed. 18.42 seconds. All steps green — login, navigation, task creation, success toast, schedule visible in the list.

The timeline:

- 20 minutes — AI built the test script
- 21 minutes — dev team fixed the bug
- 18 seconds — retest confirmed the fix

41 minutes from test creation to confirmed fix. On a real production app. With a real bug the team didn't know existed.

That's the full QA cycle — build, find, report, fix, verify — in under an hour. The test script that found the bug is the same one that confirmed the fix. Write it once, run it forever.

Side note: the attached video is the actual defect — 18 seconds of the bug happening live during the demo. This is what the dev team received along with the bug report.

Open source. MIT license.
https://github.com/isagawa-qa/platform

#TestAutomation #QA #AI #OpenSource #BugHunting #ClaudeCode

---

## Planned

| # | Target | Platform | Type | Angle | Notes |
|---|--------|----------|------|-------|-------|
| 9 | TBD | LinkedIn | Post + Video | Autonomous AI QA: 6 tasks, 13 files, 3 domains, 0 human intervention | Cycling run 2 results. Self-improvement curve, full autonomy, 4/5 maintainability. Source: `.claude/lessons/cycling-run-2.md` |
| 10 | TBD | LinkedIn | Post | "Monolithic specs get skipped. Here's why." | Tiered indexing, modular specs, 200-line threshold |
| 11 | TBD | LinkedIn | Post | "Why I don't let AI code alone" | HITL pair programming model — human approves every fix, 5-option failure protocol |
| 12 | TBD | LinkedIn | Post | "5 layers that make AI-generated tests maintainable" | Architecture deep-dive — Screenplay-inspired, reference implementations |
| 13 | TBD | LinkedIn | Post | "Most AI coding tools suggest. Mine enforces." | Competitive positioning — what makes enforcement different from instructions |
| 14 | TBD | Reddit | Posts | r/QualityAssurance, r/selenium, r/softwaretesting, r/ClaudeAI | Drafts in social-media.md |
| 15 | TBD | X/Twitter | Thread | 8-tweet thread on AI Execution Management | Draft in social-media.md. @isagawa_co account LIVE |
| 16 | TBD | Blog | Article | "AI Governance vs AI Execution Management" | blog-post.md (ready) |
| 17 | TBD | Product Hunt | Listing | Launch listing | Draft in social-media.md |

## Post Series Arc

1. **Post 1 (published 2/22):** Here's what it does — demo video on a live site
2. **Post 2 (published 2/23):** Here's how it learns — 10 failures on zentyent.app (best: 942 impressions)
3. **Post 3 (published 2/23):** Manual testers — AI replaces the gap, not you
4. **Post L-1 (published 2/24):** AI agents drift — "I built a leash" (kernel governance + video)
5. **Post 4 (published 2/25):** Claim SDD — Self-Driven Development philosophy
6. **Post 5 (published 2/25):** Portability proof — same kernel, two frameworks, two tech stacks
7. **Post 6 (published 2/26):** Live demo bug — full QA cycle in 41 minutes (real story + defect video)
8. **Post 7 (published 2/26):** Vibe Coder Spec discovery phase — SDD in action (video)
9. **Post 8 (published 3/2):** 19 tests on a client app, 8 hours codegen — business results story
10. **Post 9:** Autonomous AI QA — 6 tasks, 13 files, 3 domains, 0 human intervention. Self-improvement curve (3 iterations → 0 in 2 tasks). Full autonomy on live production app.
11. **Post 10:** Monolithic specs get skipped — tiered indexing, modular specs
12. **Post 11:** Why I don't let AI code alone (HITL)
13. **Post 12:** 5 layers that make AI-generated tests maintainable (architecture)
14. **Post 13:** Most AI coding tools suggest. Mine enforces. (competitive)

## Tracking Notes

- Update Engagement column after 48 hours (impressions, likes, comments, reposts, DMs)
- Note which hooks/angles generate the most engagement to inform future content

## Post Format Template (based on Post #6 — 7,488 impressions, best performer)

Every future post should follow this format. Post #6 is the reference.

**What works:**
1. **Real story** — something that actually happened, not a concept or philosophy
2. **Concrete numbers** — timelines, durations, counts (20 min, 21 min, 18 seconds, 41 minutes total)
3. **Stakes** — real production app, real bug the team didn't know existed, live demo
4. **Narrative arc** — setup ("I was demoing"), conflict ("It failed"), resolution ("Passed. 18.42 seconds.")
5. **Short video evidence** — 18s defect video attached, 2,820 views, 18s avg watch time (people watch the whole thing)
6. **Clear timeline/bullet summary** — scannable breakdown of what happened
7. **One-liner closer** — "The test script that found the bug is the same one that confirmed the fix."
8. **Open source CTA** — GitHub links at the end (51 clicks)

**What doesn't work (from other posts):**
- Philosophy posts (Post #4 SDD: 45 impressions)
- Abstract concepts without a story (Post L-1: 67 impressions)
- "Here's how it works" without "here's what happened" (Post #3: 193 impressions)

**Formula:** Real story + concrete numbers + video evidence + narrative arc = engagement

**Demographics that respond:** 49% IT Services, 48% Senior level, 29% at 10K+ companies. Write for senior QA/engineering leaders at enterprise companies.

---

## Post Drafts

### X Post #1: Introduction (Pinned)

**Status:** Published
**Date:** 2026-02-23
**Platform:** X (@isagawa_co)

---

AI can generate test scripts. But without enforcement, every test comes out different, it's inconsistent, unmaintainable, impossible to scale.

We built a system that manages how AI writes tests. Every script follows the same architecture. Industry grade, enterprise quality code, automatically.

Open source. MIT license.
github.com/isagawa-qa/platform

---

### Post #9: Autonomous AI QA — 6 Tasks, 0 Human Intervention

**Status:** Ready to publish
**Date:** 2026-03-03
**Platform:** LinkedIn
**Angle:** Full autonomy — the human left the room and it still worked. First post where the agent ran completely alone against a live production app.
**Media:** None (run too long for video). Consider screenshot of the final results table if possible.
**Source:** `.claude/lessons/cycling-run-2.md`

---

**LinkedIn:**

I gave my AI agent 5 QA test tasks on a live production app and walked away.

No supervision. No approvals. No "human reviews and approves the fix." Just the agent, the tasks, and a live app.

Here's what happened.

I built an autonomous cycling loop into my kernel — the agent picks up a task, builds the code, runs the test, fixes its own failures, records what it learned, and moves to the next task. No human in between. Just a queue of tasks and an agent that works through them.

I set up a clean instance of my Playwright/TypeScript platform — no previous test scripts, no prior lessons, no history. Just the framework, my kernel, and 5 tasks queued up. The agent logged into zentyent.app, navigated across multiple pages including cross-domain links, discovered page elements through the browser's accessibility tree, and started building test scripts. Page objects, task modules, roles, test files — 13 files total, following the same 5-layer architecture my framework enforces.

Task 1 passed after one fix — a marketing page had duplicate "Schedule a Live Demo" links and the agent had to figure out which one to click.

Task 2 was rough. The agent failed 3 times. Wrong selectors, a toast notification it couldn't find, strict mode violations from duplicate elements. Each time it failed, it fixed the issue and tried again. By the third fix, the test passed.

Then something happened.

Tasks 3, 4, and 5 — all passed on the first run. No failures. No retries. The agent had learned enough from its earlier mistakes to get them right the first time.

The results:

- 5 test tasks completed, 0 skipped
- 13 files generated (6 page objects, 2 task modules, 2 roles, 5 tests)
- Login flows, modals, dropdowns, toast notifications, cross-domain popups — all handled
- Tasks 3-5: first-run passes
- Human intervention: zero

I scored the output: 4/5 on maintainability. The architecture is clean — every file in the right layer, every locator centralized, every test following the same pattern. The 1 point deduction: we didn't have the methods the agent needed — like handling multiple matching elements. The fix is simple: wrap those patterns into reusable framework methods once, and every future test gets them for free.

The agent picked its own selectors — data-testid attributes and CSS selectors it discovered through the browser. Every test passes. And it got there faster by finding what works for this specific app through experience rather than following abstract best practices.

Previous posts showed human-in-the-loop — the human reviews every fix, approves every change. This run, the human wasn't in the loop. The agent fixed its own mistakes, recorded its own lessons, and kept going. 5 tasks, start to finish, alone.

Next step: point it at something that breaks. I want to see how the autonomous agent handles failure when nobody's there to help.

The autonomous cycling loop isn't in the repo yet — still testing. I've built this modularly, so it plugs right into the kernel when it's ready.

Open source. MIT license.
https://github.com/isagawa-co/isagawa-kernel
https://github.com/isagawa-qa/platform-playwright

#TestAutomation #QA #AI #Autonomy #OpenSource #ClaudeCode

---

**X:**

I gave my AI agent 5 QA test tasks on a live production app and walked away.

No supervision. No approvals. Just the agent, the tasks, and a live app.

I built an autonomous cycling loop — the agent picks up a task, builds the code, runs the test, fixes its own failures, records what it learned, and moves to the next task.

Task 2 failed 3 times. The agent fixed its own mistakes each time.

Tasks 3, 4, 5 — all passed on the first run. It learned enough from its earlier failures to get them right.

13 files generated. Login flows, modals, toasts, cross-domain popups — all handled. Human intervention: zero. Maintainability: 4/5.

Next: point it at something that breaks. I want to see how it handles failure when nobody's there to help.

The autonomous cycling loop isn't in the repo yet — still testing. Built modularly, so it plugs right into the kernel when ready.

github.com/isagawa-co/isagawa-kernel

#TestAutomation #QA #AI #Autonomy #ClaudeCode

---

### Post #3: Manual Testers

**Status:** Published
**Date:** 2026-02-23
**Platform:** LinkedIn + X (@isagawa_co)

---

Every manual tester has the same fear: "AI is going to replace me."
Here's what's actually happening, AI is replacing the gap between manual and automation testing.

You don't need to mass learn Python. You don't need a bootcamp. You don't need 2 years of writing test scripts from scratch.

You need to understand what a good test looks like and you already do. You've been writing test cases your entire career. You know the workflows, the edge cases, the places where things break.

The learning curve? Understanding selectors, how to find elements on a page, how to interact with grids, modals, iframes, dropdowns, dynamic tables. The stuff that AI even trips up on. That's what you learn instead of learning to code from scratch. That's only a fraction of the effort it used to take to learn test automation.

My platform lets you take that knowledge and turn it into automated test scripts. AI writes the code and the system enforces the architecture. You tell it what to test, guide it, review the output and approve it.

That's the shift, from writing tests manually to managing how AI writes them for you. The testers who figure this out first won't get replaced. They'll be the ones running automation for entire teams.

Open source. MIT license.
https://github.com/isagawa-qa/platform

---

### Post #2: The Learning Loop

**Status:** Published
**Date:** 2026-02-23
**Platform:** LinkedIn
**Engagement:** 942 impressions, 6 reactions, 1 comment

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

---

### Post #4: Self-Driven Development (SDD Philosophy)

**Status:** Published
**Date:** 2026-02-25
**Platform:** LinkedIn
**Engagement:** 45 impressions
**Angle:** Claim SDD methodology — philosophy post, not a pitch

---

Everyone's talking about spec-driven development. I've been thinking about it differently. I call it Self-Driven Development.

Stop writing specs for the agent. Let the agent build its own. You provide the domain knowledge — your patterns, your reference code, your standards. The agent scans it, builds its own protocol, and enforces it on itself at runtime. When it fails, it records what went wrong and that mistake becomes permanently impossible.

The human stays the source of truth. The agent handles the governance.

Three principles:
- Self-building — the agent creates its own enforcement from your references
- Self-improving — every failure makes the system stronger
- Safety-first — mechanical hooks the agent can't bypass, not guidelines it can ignore

This isn't about replacing human judgment. It's about not relying on the agent's willingness to follow instructions. Structure it can't skip beats structure it's supposed to follow.

I open sourced the implementation: https://github.com/isagawa-co/isagawa-kernel

---

### Post #5: Portability Proof (Two Frameworks, One Kernel)

**Status:** Published
**Date:** 2026-02-25
**Platform:** LinkedIn
**Angle:** Portability — same kernel manages agent across different tech stacks

---

I ran the same management system on two completely different tech stacks. It built its own enforcement both times.

First run — Selenium/Python. The kernel managed the agent through 17 tests across 4 business domains on a live client site.

This week — Playwright/TypeScript. Completely different framework. Same kernel. Same site.

The kernel scanned the new reference patterns — code examples that show the agent what good looks like. A login page object. A task module. A role. A test. It built a new protocol from scratch and started generating tests. It took 4 rounds of human-in-the-loop fixes before the first test passed. Each failure got recorded. Each fix became permanent.

Same loop both times:
1. Human writes the standards — architecture, patterns, reference code
2. Kernel scans it and builds its own protocol
3. Agent writes code, kernel enforces the protocol
4. Test fails — agent fixes and retries
5. Test passes — every failure gets recorded as a permanent lesson
6. Human reviews and approves
7. The agent never makes that mistake twice

Two frameworks. Two protocols. One kernel.

The management layer doesn't care what language you write in or what domain you're in. It reads your standards and makes sure the agent follows them. Every time. Give it React component patterns, API design rules, your spec-driven development standards — that's how we built this framework. Any domain where you have standards the agent should follow, the kernel can enforce them.

Both platforms are ready:
Selenium/Python — github.com/isagawa-qa/platform
Playwright/TypeScript — github.com/isagawa-qa/platform-playwright
Kernel — github.com/isagawa-co/isagawa-kernel

Open source. MIT license.

---

### Post #8: 19 Tests on a Client App — Business Results

**Status:** Published
**Date:** 2026-03-02
**Platform:** LinkedIn
**Angle:** Business results — real numbers, real client app, codegen speed, modular architecture, maintainability

---

I automated 19 tests on a client's production app. Script generation alone: about 8 hours.

Here's what happened.

A client's production app had no automated tests. I pointed my AI test automation platform at it and started building. One domain at a time, 25 minutes per test on average.

The first few tests were rough. The AI hardcoded XPath selectors — wrong element types, three failures in a row from the same mistake. The system caught all three, collapsed them into one permanent lesson: use element-agnostic selectors. The AI never made that mistake again.

By the third domain, the AI was writing tests that passed on the first or second try. Every past failure was already blocked — toast notifications that disappear before you can assert them, dynamic dropdowns that go stale between clicks, text matching patterns that break on nested elements. Twelve lessons total, each one permanent.

The result:

- 19 automated tests across 5 business domains
- ~8 hours total script generation
- 25 minutes average per test
- 12 permanent lessons the AI learned from its own failures
- 10 seconds average per test run

That's just codegen. Setup, test planning, bug reporting, retests, and maintenance are on top of that — the full QA workload that comes with any real engagement.

Goal Management, Task Management, Employee Management, Scheduled Tasks, Lead Capture. Each domain has its own role, task modules, and page objects. Each test within a domain shares common domain modules. And all domains share the same login module and the same enforced architecture. Change the login flow once, every domain picks it up. That's maintainability built into the structure, not bolted on after.

This isn't the entire app. It's a fraction of it. And every new test the AI writes is faster than the last because the lessons stack. The 19th test benefits from every mistake the 1st test made.

A manual tester writing these from scratch — weeks. An AI without enforcement — inconsistent, unmaintainable code every time. An AI with enforcement — 8 hours of codegen, consistent architecture, and it gets faster with every test.

The framework is open source with reference implementations included. Point it at your own app and start building.

https://github.com/isagawa-qa/platform

I also set up full QA infrastructure for teams — framework, config, credential management, and training. DM me or email alain@isagawa.co.

#TestAutomation #QA #AI #OpenSource #ClaudeCode

---

**X:**

I automated 19 tests on a client's production app. Script generation: about 8 hours. 25 minutes per test.

The first few tests failed — AI hardcoded XPath selectors, wrong element types, three failures in a row. The system caught all three, collapsed them into one permanent lesson. Never happened again.

By the third domain, tests were passing on the first or second try. Every past failure was already blocked. 12 lessons total, each one permanent.

19 tests. 5 business domains. 8 hours of codegen. 10 seconds average per test run. And it gets faster — the 19th test benefits from every mistake the 1st test made.

This is a fraction of the app. A manual tester writing these from scratch — weeks. AI without enforcement — inconsistent code every time. AI with enforcement — 8 hours, consistent architecture, gets faster with every test.

Open source. MIT license.
github.com/isagawa-qa/platform

#TestAutomation #QA #AI #OpenSource #ClaudeCode
