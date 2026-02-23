# GTM Content Strategy

> Revenue streams, pricing, and monetization are in `services-strategy.md`.
> This doc covers content creation, platforms, and posting cadence.

---

## Platform Prioritization

### Tier 1 — Hit First (highest ROI for current stage)

| Platform | Why | Audience | Content Type |
|----------|-----|----------|--------------|
| **LinkedIn** | Direct pipeline to buyers (QA leads, eng managers, startups). DM conversions. | SDETs, QA leads, engineering managers, startups | Posts, articles, video clips |
| **Reddit** | Authentic technical community. High engagement. Multiple relevant subs. | Developers, QA engineers, AI builders | Text posts, code examples, AMAs |
| **X / Twitter** | Tech audience, vibe coders, AI builders. Viral potential. **PENDING: Create @isagawa account with Premium (business expense).** | Developers, vibe coders, founders | Threads, hot takes, clips |

### Tier 2 — Build Over Time

| Platform | Why | Audience | Content Type |
|----------|-----|----------|--------------|
| **YouTube** | Manual tester training content. Long shelf life. Course funnel. | Manual testers, junior devs, career switchers | Tutorials, demos, course previews |
| **Hacker News** | Category-defining posts. One viral HN post = massive awareness. | Engineers, founders, tech leaders | Show HN, articles |
| **Dev.to** | Cross-post articles. SEO. Technical credibility. | Developers | Articles (repurposed from LinkedIn) |

### Tier 3 — Opportunistic

| Platform | Why | Audience | Content Type |
|----------|-----|----------|--------------|
| **Facebook Groups** | QA groups, startup groups. Lower engagement but broad reach. | Manual testers, small team leads | Share posts, answer questions |
| **Product Hunt** | One-time launch event. Good for initial visibility. | Early adopters, product people | Launch listing |
| **Discord / Slack** | QA communities, Claude Code community, testing communities | Practitioners | Help people, drop links organically |

---

## How to Hit All Platforms at Once

**One piece of content, repurposed across platforms:**

```
LinkedIn Article (long-form, 1500-2000 words)
  │
  ├─→ LinkedIn Post (300 words, key insight + link to article)
  ├─→ X Thread (8-10 tweets, same structure as article)
  ├─→ Reddit Post (rewritten for each subreddit's tone)
  ├─→ Dev.to Article (cross-post, minor edits)
  ├─→ Hacker News (submit article link, or Show HN)
  ├─→ YouTube (talk through the same content on camera, or screen share)
  └─→ Facebook Groups (share with community-specific framing)
```

**Batch creation workflow:**
1. Write the LinkedIn article (source of truth)
2. Pull out the hook → X thread opener
3. Pull out the key insight → LinkedIn post
4. Rewrite intro for each Reddit sub (authentic tone, no marketing speak)
5. Cross-post to Dev.to
6. Record 5-10 min YouTube version (screen share + talk through it)
7. Share in Facebook groups with "thought this was relevant" framing

**Time investment:** ~3-4 hours per content batch. Produces 6-8 posts across all platforms.

---

## Content Pillars

| Pillar | Target Audience | Angle | Frequency |
|--------|----------------|-------|-----------|
| **QA Platform** | SDETs, QA leads | Open source, Screenplay-inspired architecture, demo clips | 1x/week |
| **Kernel / AI Execution Management** | Developers, eng managers | Category creation — governance vs execution management | 1x/week |
| **Structured Coding** | Everyone — devs, vibe coders, founders | Vibe coding v2 — category creation | 1x/week |
| **Manual Tester Path** | Manual QA, career switchers | Fastest path from manual to automation | 1x/week |

---

## Posting Cadence

### 3-4x per week on LinkedIn (primary platform)

| Day | Type | Pillar |
|-----|------|--------|
| **Monday** | Thought leadership | Structured coding OR AI execution management |
| **Wednesday** | Product / demo | QA platform — video clips, screenshots, code examples |
| **Friday** | Audience-specific | Manual testers OR startup pain points |
| **Saturday (optional)** | Personal / behind the scenes | Solopreneur journey, building in public |

### Other platforms: 2-3x per week (repurposed from LinkedIn)

- **X:** Mirror every LinkedIn post as a shorter version or thread
- **Reddit:** 1-2 posts per week, staggered across subreddits (no cross-posting same content)
- **YouTube:** 1x per week (tutorial OR talk-through of article)
- **Dev.to:** 1x per week (cross-post articles)
- **HN:** Only when you have a category-defining piece or Show HN moment

---

## Content Calendar — First 4 Weeks

### Week 1 (Launch)
- [x] LinkedIn: Video post + demo clip (done)
- [ ] LinkedIn: "AI can generate tests. But the output is inconsistent..." (structured coding teaser)
- [ ] LinkedIn: Manual tester angle — "You already know what to test."
- [ ] Reddit: r/QualityAssurance — open source announcement
- [ ] X: Thread — "Every dev team is building their own AI guardrails. All of them are static."

### Week 2
- [ ] LinkedIn Article: "I Built a Production QA Platform Without Writing Code" (structured coding proof)
- [ ] LinkedIn Post: Kernel concept — "You're already doing this badly by hand. Here's the system."
- [ ] LinkedIn Post: Quick tip / code screenshot from the platform
- [ ] Reddit: r/selenium — 5-layer architecture with code examples
- [ ] Reddit: r/ClaudeAI — "Using Claude Code hooks to enforce how AI writes test code"
- [ ] X: Repurpose article as thread
- [ ] YouTube: Screen recording walkthrough of /qa-workflow

### Week 3
- [ ] LinkedIn Article: "AI Governance vs AI Execution Management" (category-defining)
- [ ] LinkedIn Post: Manual tester walkthrough — "60 minutes from zero to automated tests"
- [ ] LinkedIn Post: Behind the scenes — "Here's what happens when the AI makes a mistake"
- [ ] Reddit: r/softwaretesting — "Built a self-improving QA agent"
- [ ] X: Thread — "The $5.8B AI governance market is building the wrong thing"
- [ ] Hacker News: Submit article
- [ ] Dev.to: Cross-post Week 2 article

### Week 4
- [ ] LinkedIn Article: "Vibe Coding Is Dead. Structured Coding Is Next." (the manifesto)
- [ ] LinkedIn Post: "From Manual Tester to Automation Engineer — No Bootcamp Required"
- [ ] LinkedIn Post: Services case study or demo results
- [ ] Product Hunt: Launch (Tue-Thu)
- [ ] Reddit: r/startups or r/SaaS — services angle
- [ ] YouTube: "Manual Tester's Guide to AI-Powered Test Automation" (course preview)
- [ ] Dev.to: Cross-post Week 3 article

---

## Subreddit Targeting

| Subreddit | Angle | What NOT to do |
|-----------|-------|---------------|
| **r/QualityAssurance** | Architecture + enforcement, open source | No marketing speak |
| **r/selenium** | Screenplay-inspired architecture, BrowserInterface, code examples | No AI hype, focus on Selenium patterns |
| **r/softwaretesting** | Learning loop, HITL, self-improving agent | Don't bash manual testing |
| **r/ClaudeAI** | Kernel mechanics, hooks, commands, skills | Can go deeper on Claude Code specifics |
| **r/learnprogramming** | Manual tester path, career switching | Be helpful, not salesy |
| **r/startups** | Services model, solopreneur journey | Focus on business model, not tech |
| **r/SaaS** | Open source + services monetization | Business model discussion |

---

## Startup Services Targeting (PRIORITY — Fastest Path to Revenue)

Startups hiring SDETs are budgeting $120K-$180K/year for one hire they can't find. Your Trojan Horse demo replaces months of recruiting with a 60-minute proof. One deal = $15K-$50K.

### Where to find startup leads

#### Direct Outreach Channels

| Channel | How |
|---------|-----|
| **X / Twitter** | **PRIMARY outreach channel.** Higher response rates than LinkedIn for cold intros. See X Outreach Strategy below. |
| **LinkedIn** | Secondary — good for warm leads, but DMs get buried. Better for inbound (content → profile → DM). |
| **AngelList / Wellfound** | Search for startups posting QA/SDET roles |
| **Reddit r/startups** | Engage in discussions about QA pain, offer demo |
| **Indie Hackers** | Solopreneur/small team audience |
| **Local startup meetups** | Demo in person |

#### Incubator / Accelerator Lists (Gold Mine)

Startups that graduated incubators 6-18 months ago are the sweet spot — they've shipped a product, raised a round, are scaling, and now hitting QA pain they didn't plan for. Browse their portfolio lists and look for web-app companies.

| Source | What to Look For | URL |
|--------|-----------------|-----|
| **Y Combinator** | Current + past batch directories. Filter for B2B SaaS, fintech, healthtech — anything with complex web flows. W24/S24 batches are now at the "need real QA" stage. | ycombinator.com/companies |
| **Techstars** | Portfolio by city/vertical. Look for companies with 10-50 employees. | techstars.com/portfolio |
| **500 Global** | Large portfolio, many early-stage. Sort by recent batches. | 500.co/companies |
| **Antler** | Global, very early stage — may be too early for services but good for awareness. | antler.co/portfolio |
| **Launch House / On Deck** | Community-based, founders are active on X. Easy to engage. | — |
| **Google for Startups** | Regional accelerator programs worldwide. | startup.google.com |
| **Microsoft for Startups (Founders Hub)** | Large portfolio, many B2B SaaS. | microsoft.com/startups |
| **Local incubators** | Every city has them. Check your local university and city accelerators. | Google "[your city] startup incubator" |

**How to work incubator lists:**

1. Browse the portfolio directory (most are public)
2. Filter for companies with web apps (SaaS, platforms, marketplaces)
3. Check their careers page or LinkedIn — are they hiring QA/SDET? If yes, they have budget and pain.
4. Even if not hiring — if they have 10+ devs and no QA team, they need you
5. Find the founder/CTO on X (most incubator founders are active there)
6. Engage with their content first, then DM with the demo offer

**Why 6-18 months post-graduation is the sweet spot:**
- Too early (0-6 months): still building MVP, no QA budget
- Sweet spot (6-18 months): shipped product, have users, hitting quality problems, have funding
- Too late (2+ years): probably already have QA team or vendor in place

#### Job Board Mining

Companies posting QA roles are pre-qualified — they've already decided to spend money on this.

| Job Board | Search Terms |
|-----------|-------------|
| **Y Combinator Work at a Startup** | "SDET", "QA Engineer", "Test Automation" |
| **LinkedIn Jobs** | "Senior Test Automation Engineer" at companies with 10-100 employees |
| **Wellfound (AngelList)** | "QA" or "SDET" at funded startups |
| **Indeed / Glassdoor** | "Selenium" or "test automation" at startups (filter by company size) |
| **Hacker News Who's Hiring** | Monthly thread — search for "QA", "testing", "SDET" |

**Outreach angle for job postings:** "Before you fill that role — want to see working automated tests on your site in 60 minutes? You keep the code either way."

### X Outreach Strategy (Create @isagawa account first)

**Why X beats LinkedIn for outreach:**
- LinkedIn DMs are a graveyard — everyone gets pitched there
- X is conversational, less formal, higher response rates for cold intros
- Founders and CTOs are more active and responsive on X

**Setup (Day 1 — 10 minutes, $8/month):**
1. Create @isagawa X account
2. Subscribe to Premium (business expense — blue check, longer posts, analytics)
3. Pin your demo video as first tweet
4. Bio: "AI Execution Management for QA | Open source | I build working tests on your site in 60 min"

**Week 1 — Build credibility (don't cold DM yet):**
- Zero followers = looks like a bot if you DM immediately
- Reply to 5-10 threads per day where founders/CTOs discuss:
  - Hiring SDETs / QA engineers
  - AI-generated code maintenance problems
  - Test automation pain
  - Vibe coding regrets / technical debt
- Add value in replies, not pitches. Show expertise.
- Post 2-3 original tweets (from your drafted thread)

**Week 2+ — Warm outreach:**
- DM founders you've already interacted with in threads
- They've seen your replies, know you're legit
- Short, specific DM (see message templates below)

**Search queries to find pre-qualified leads:**
- `"hiring SDET"` or `"hiring QA engineer"`
- `"AI generated code" maintenance` or `"AI generated code" unmaintainable`
- `"test automation" mess` or `"test automation" broken`
- `"vibe coding" regret` or `"vibe coding" technical debt`
- `"need QA"` or `"no QA team"`
- `"selenium" frustrated` or `"tests keep breaking"`

These people are publicly complaining about the exact problem you solve. A reply with your demo offer hits different than a cold DM.

### Outreach messages

**X DM (after engaging in thread):**

```
Hey — saw your thread about [QA hiring / test maintenance / etc].

Quick question: would it be useful if I built working automated tests
on your site in 60 min? You keep the code either way.

I do this as a free demo — open source framework, enterprise-grade,
your team can maintain it long-term.

No catch. Just takes an hour. Interested?
```

**X reply to "hiring SDET" tweet:**

```
Before you fill that role — have you considered an AI-powered
framework that generates tests your team can maintain?

I can build working tests on your site in 60 minutes (free demo).
You keep the code. DM me if you want to see it.
```

**LinkedIn DM (for warm leads / inbound):**

```
Hey [name] — saw you're hiring for a senior test automation engineer.

Before you fill that role, want to see something? I can build working
automated tests on your site in 60 minutes. You keep the code whether
we work together or not.

The framework is open source, enterprise-grade, and your team can
maintain it long-term. Happy to show you — just takes an hour.
```

### Phased targeting

| Phase | Target | Why |
|-------|--------|-----|
| **Now** | **Startups hiring SDETs** — founders, eng managers, CTOs | Fastest close. Budget exists (they're already spending on hiring). |
| Month 1-3 | Individual SDETs, QA engineers | Champions who advocate internally |
| Month 3-6 | Startups (Series A-B), small teams (5-20 devs) | Need tests, no QA team |
| Month 6-12 | Mid-size companies (50-500 devs) | Have QA team, want to scale |
| Year 2+ | Enterprises, regulated industries | Compliance requirements, premium pricing |

---

## Key Messages by Platform

| Platform | Tone | Lead With |
|----------|------|-----------|
| **X / Twitter** | Sharp, conversational, value-first replies | Outreach to founders hiring SDETs. Engage in QA/AI pain threads. |
| **LinkedIn** | Professional, first person, solopreneur | Inbound content — "AI execution management" category creation |
| **Reddit** | Technical, helpful, no marketing | Code examples, architecture details, answer questions |
| **YouTube** | Educational, walkthrough | "Let me show you how this works" — demos + tutorials |
| **Hacker News** | Technical depth, contrarian | "Why AI governance is the wrong abstraction" |
| **Facebook** | Conversational, helpful | "Has anyone else dealt with this?" — pain point discussions |
