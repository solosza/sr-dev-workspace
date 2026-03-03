# X Build-in-Public Series: Vibe Coder Pack

8-post series. Post 1 documents building the pack itself. Posts 2-8 document using it live to build a Gumroad → GitHub webhook.

**Account:** @isagawa_co
**Status:** Draft

---

## Post 1 — Building the Tool (the plan + output story)

**When:** Now — before the webhook build starts
**Attachment:** 30s video — scroll through the plan, then the output

Vibe coding builds fast. But without architecture, every file comes out different. No patterns, no tests, no conventions. It works once, then falls apart.

So I built a domain pack — a full set of specs that plug into my kernel. The kernel reads those specs and self-builds its own protocols, enforcement hooks, and quality gates from them. The agent writes its own rules, then the system makes it mechanically impossible to break them.

I described what I wanted the pack to do. The agent planned it, built it, and verified it. Here's the plan and the output. Next: using it to build something live.

---

## Post 2 — Discovery

**When:** After running /vibe (Phase 1)
**Screenshot:** /vibe discovery conversation

I told the AI "build me a webhook that connects Gumroad to GitHub."

Instead of writing code, it interviewed me. What problem does this solve? Who uses it? What data does it handle?

6 questions before a single line of code. That's not vibe coding. That's how a senior engineer starts a project.

---

## Post 3 — Stack Decisions

**When:** After Phase 2 decisions
**Screenshot:** Decision review output

The AI recommended my tech stack and explained every tradeoff in plain English.

"Option A: Express.js — RECOMMENDED. Best for simple APIs. Tradeoff: manual setup for everything beyond routing. Why I recommend this: your app is a single webhook endpoint."

It recommended. I chose. It recorded why. Then it moved on.

---

## Post 4 — Roadmap

**When:** After Phase 3 roadmap
**Screenshot:** Product roadmap output

Before writing a single line of code, the AI planned every feature in priority order.

P1 — webhook listener, signature validation. P2 — GitHub invite automation. P3 — error notifications, admin dashboard.

It told me what to build first and why. I approved. Then it started.

---

## Post 5 — Self-Binding (the money post)

**When:** After architecture.md is generated + scaffold
**Screenshot:** architecture.md + hook block message

This is the part that changes everything.

The AI generated its own architecture doc — file structure, naming conventions, patterns, anti-patterns. Then the system makes it mechanically impossible for the AI to violate those rules.

The agent wrote its own constraints. Now it enforces them on itself.

Same kernel that manages QA test automation across Selenium and Playwright. Same loop. Different domain.

---

## Post 6 — First Feature

**When:** After first feature completes
**Screenshot:** Feature spec + passing tests

First feature from the roadmap: Gumroad webhook listener.

The AI generated a feature spec before writing code. Files to create, files to modify, test cases. I approved the plan. Then it built — tests alongside the code, not after.

Full test suite runs after every feature. New tests + old tests. Catches regressions automatically.

---

## Post 7 — First Failure

**When:** After first failure + fix + learn
**Screenshot:** on-failure checkpoint + lesson recorded

It broke.

The AI explained why in plain English: "The webhook signature validation is checking the raw body but Express already parsed it as JSON."

It fixed it. Recorded the lesson. That exact failure mode is now documented and gated. The AI can never make that mistake again in this project.

Every failure makes the system permanently smarter. Not because the AI remembers — because the system won't let it forget.

---

## Post 8 — Results / CTA

**When:** After build is complete
**Screenshot:** None or deployed app

Working sales infrastructure. Built from "I need a webhook" to deployed code by an AI that was managing itself the entire time.

The tool that built it is open source:
github.com/isagawa-co/vibe-coder-pack

The kernel behind it:
github.com/isagawa-co/isagawa-kernel

You describe what you want. The AI handles the engineering. MIT license.

---

## LinkedIn — Full Story Recap (draft after build)

**When:** After build is complete, best screenshots selected
**Format:** One long-form post — polished recap of the full build arc
**Angle:** "Here's what happened when I used my own tool to build real infrastructure"
**Include:** Pack build (50 files) → live webhook build → failure learning → results
**Reference:** LinkedIn Post #2 format (942 impressions) — complete narrative with specific details

*(Draft this after the build when you have real screenshots and the actual failure story)*

---

## Notes

- Post 1 is the "how I built the tool" story — uses the plan + output from the actual session as proof
- Posts 5 and 7 are the strongest — self-binding and failure learning performed best historically (Post #2 got 942 impressions with the same failure-learning angle)
- Post 7 is a placeholder scenario — replace with the actual failure during the real build
- Post 4 (roadmap) is new — shows the SDLC discipline that separates this from raw vibe coding
- Screenshots are critical on X — every post should have one
- Post 1 goes out now, posts 2-7 go out as each milestone happens during the live build, post 8 after completion
