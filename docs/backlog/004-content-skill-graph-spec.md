# Backlog 004: Content Production Skill Graph (Domain Spec)

## Status
Open

## Priority
Medium — validates spec model for non-engineering domains, strong GTM signal

## Summary
Build a content production domain spec that manages multi-platform social media output from a single topic input. Inspired by the "skill graph" pattern trending on Twitter (30+ markdown files wired together as a content team). This is a natural fit for our spec architecture — it's what we already do, just pointed at content instead of code.

## Why This Matters
1. **Proves specs work beyond engineering** — every spec so far is BUILD-type (QA, DevOps, games). A content spec is OPERATE-type — ongoing workflow, not one-time build.
2. **GTM leverage** — content creators are a massive audience. "I replaced $8-12k/mo in content spend with a skill graph" is a compelling proof point for the spec marketplace.
3. **We already have the infrastructure** — SKILL.md, workflow.md, steps/, gate-contract.md. The content graph maps directly to our existing architecture.
4. **Validates the "agents teaching agents" thesis** — drop this spec into cognitive-agent, give it a topic, it produces 10 platform-native posts.

## Architecture Mapping

| Skill Graph (Twitter) | Isagawa Spec Equivalent |
|-----------------------|------------------------|
| `index.md` (entry point) | `SKILL.md` (identity, philosophy, file index) |
| `platforms/*.md` (x, linkedin, ig...) | `steps/step-01.md` through `step-10.md` (per-platform generation steps) |
| `voice/brand-voice.md` | `references/brand-voice.md` (config, not hardcoded) |
| `engine/hooks.md` | `references/hook-formulas.md` |
| `engine/repurpose.md` | `workflow.md` (1 input → 10 outputs pipeline) |
| `audience/*.md` | `references/audience-profiles.md` |
| `[[wikilinks]]` between files | File references in step files (same pattern we use) |
| No enforcement | `gate-contract.md` — verify each post meets platform specs |

## What We'd Build

```
.claude/skills/content-production/
├── SKILL.md                          ← Identity: multi-platform content system
├── workflow.md                       ← Pipeline: topic → research → draft → per-platform → review
├── gate-contract.md                  ← Gates: char limits, tone match, no cross-platform copy-paste
├── steps/
│   ├── pre-build.md                  ← Load brand voice, audience profiles, platform rules
│   ├── step-01.md                    ← Topic analysis and angle generation
│   ├── step-02.md                    ← X/Twitter (contrarian, hooks, 280 chars)
│   ├── step-03.md                    ← LinkedIn (narrative, professional, 1500 words)
│   ├── step-04.md                    ← Instagram (carousel, visual-first, bold claims)
│   ├── step-05.md                    ← TikTok (raw script, 45-sec format)
│   ├── step-06.md                    ← YouTube (SEO title, structured outline, 8-min)
│   ├── step-07.md                    ← Newsletter / email
│   ├── step-08.md                    ← Blog / long-form
│   ├── step-09.md                    ← Repurposing chain verification
│   └── on-failure.md                 ← Platform rule violations, tone drift
├── references/
│   ├── brand-voice.md                ← Configurable per user
│   ├── platform-rules.md             ← Char limits, format specs, posting frequency
│   ├── hook-formulas.md              ← Contrarian, question, stat-lead, story-lead
│   └── audience-profiles.md          ← Builders, casual, enterprise, etc.
└── config/
    └── content-config.json           ← Platforms enabled, posting schedule, voice settings
```

## What Makes Ours Better Than a Flat Skill Graph
1. **Enforcement** — gate-contract.md catches platform rule violations (char limits, tone drift, copy-paste across platforms). The skill graph has zero enforcement.
2. **Self-improvement** — kernel learn loop. If a post gets flagged or underperforms, lesson recorded, spec updated. Skill graph is static.
3. **Config-driven** — swap brand-voice.md and audience-profiles.md for a different client. Same spec, different output. The skill graph is hardcoded to one brand.
4. **Cycling support** — can batch-generate a week of content as tasks. Topic per task, cycling produces all platforms per topic.
5. **Composable** — stack with other specs. Content spec + analytics spec + scheduling spec = full content operation.

## Key Differentiator for GTM
The Twitter post says "one flat file gives you a tool, a graph gives you a team." Our pitch: **"a graph gives you a team, enforcement gives you a team that doesn't drift."** Static skill graphs degrade over time as the agent forgets rules or drifts from voice. Enforcement prevents that.

## Implementation Steps
- [ ] Research: audit 2-3 existing content skill graph repos for patterns
- [ ] Design: map to spec architecture (SKILL.md, workflow, steps, gates)
- [ ] Build: create spec via factory or manually
- [ ] Test: drop into cognitive-agent, generate content for Isagawa's own accounts
- [ ] Ship: publish to spec marketplace, write comparison blog post

## Factory Input (Ready to Run)

Run `/spec-factory-run content-production` from the factory repo and feed this:

**Domain:** Content Production (Multi-Platform Social Media)

**What the agent does:** Takes a single topic and produces platform-native posts for 10 social media accounts. Each post thinks about the topic differently — different angle, hook, voice, structure, format per platform. Not reformatting, rethinking.

**Platforms:** X/Twitter, LinkedIn, Instagram (carousels), TikTok (scripts), YouTube (outlines), Newsletter, Blog, Threads, Reddit, Facebook

**Core systems:**
- Brand voice engine (configurable per client)
- Hook formulas (contrarian, question, stat-lead, story-lead)
- Audience profiles (builders, casual, enterprise)
- Platform rules (char limits, format specs, posting frequency)
- Repurposing chain (1 topic → 10 outputs, each native)
- Content calendar / scheduling

**Workflow:** Topic input → angle generation → per-platform drafting → tone/rule verification → output

**LinkedIn format (proven — 99 likes, 12.8K impressions on QA autonomous cycling post):**
1. Hook — bold claim with specific numbers, no fluff ("I gave my AI agent 5 QA test tasks on a live production app and walked away.")
2. Story — chronological walkthrough, task by task, show the failures and fixes, be honest about what went wrong
3. Results — bullet list with concrete metrics (files generated, pass rates, zero human intervention)
4. Honest self-assessment — score yourself, acknowledge gaps ("4/5 on maintainability, 1 point deduction because...")
5. Takeaway — what it means, what's next ("Next step: point it at something that breaks")
6. CTA — repo links, open source callout, hashtags
- Tone: technical but accessible, first-person, no jargon walls
- Length: ~300-400 words, scannable paragraphs
- Key pattern: show vulnerability (failures, retries) alongside wins — builds credibility

**Quality gates:** No copy-paste across platforms, char limits enforced, tone matches brand voice, each post is native to its platform format

**Config-driven:** Brand voice, audience, platforms enabled, posting schedule — all swappable per client

## References
- Twitter thread: skill graph for 10 social media accounts (March 2026)
- @arscontexta Claude Code plugin (generates skill graph structure)
- Existing spec architecture: `.claude/skills/` pattern across all Isagawa repos
