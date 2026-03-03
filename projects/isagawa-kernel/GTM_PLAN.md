# Isagawa Kernel — GTM Plan

**Date:** 2026-02-24
**Status:** Active

## Strategy

Release the kernel as open-source governance for SDD. Prove it with a case study. Name the methodology. Convert inbound to consulting.

## Three Moves

### 1. Release the Kernel (Now)

Push the repo public. The governance primitive — the piece nobody else has. Sits in the SDD conversation that Karpathy and AWS are already driving. Not selling a category, adding the missing piece to one with momentum.

### 2. Publish the Case Study (Next)

Article or video showing the kernel building the QA platform from a domain pack. Not "here's my product" — "here's the methodology in action."

The trace is the proof. Agent scans repo, builds its own protocol, enforces it, hits a failure, learns, improves, ships working tests.

Shows:
- Modular specs over monolithic ones
- Mechanical enforcement over advisory guidelines
- Self-improvement over static specs
- The kernel governing a real build end-to-end

Formats:
- Short video (5 min): Problem → loop → demo → result
- Long video (20-25 min): Full domain-setup → QA platform build → test scenario
- Written article: SDD methodology documented as a build log

### 3. Name the Methodology — Self-Driven Development (SDD)

**Self-Driven Development.** You provide the domain knowledge, the agent drives everything else — builds its own governance, enforces it, improves it.

Same acronym as spec-driven development. That's the point. This is what SDD should have been all along. Not specs the human writes and hopes the agent follows. Specs the agent builds, enforces, and evolves on its own.

- **Spec-driven development** = human writes specs, agent executes
- **Self-driven development** = human provides domain knowledge, agent manages itself

The kernel is the tool. Self-Driven Development is the methodology. The case study proves it works. The term is what people share.

## The GTM Loop

```
Kernel (open source, free)
  → Case study (proves it works)
    → Methodology article (names the idea)
      → Inbound from SDD community
        → Domain pack consulting (paid)
          → QA platform as flagship example
```

The kernel gets stars. The case study gets shares. The methodology gets cited. The consulting gets revenue.

## Outreach (Parallel)

### X/Twitter — Builder Engagement

Find builders shipping publicly on X. Genuine compliment, one-liner on value, drop the repo link. No demo ask, no pitch — let the repo sell itself.

**Template:**
> Looks good! If you ever want automated test coverage on [their product], I built an open source QA platform that can spin up scripts on your actual app. Standard workflows take about 30 mins to spit out maintainable, enterprise grade code. Check it out: https://github.com/isagawa-qa/platform

Started: Steven Pu / roro (@pusongqi)

### YC S25 — Direct Outreach

YC S25 batch is 8 months post-graduation — sweet spot for QA services outreach.

24 strong targets identified. Template:
- Ask how they're handling testing (manual/automated/both)
- Mention AI-native platform that 10x's test script development
- Offer quick demo on their web app
- Let the demo sell itself

Started: Bond (Flor Sanders), Den (Justin Lee), Mesmer (Lucas)

## Content Calendar

### Post 1: Claim SDD (LinkedIn — 2026-02-25)
Philosophy post, not a pitch. Plant the flag.

> Everyone's talking about spec-driven development. I've been thinking about it differently. I call it Self-Driven Development.
>
> Stop writing specs for the agent. Let the agent build its own. You provide the domain knowledge — your patterns, your reference code, your standards. The agent scans it, builds its own protocol, and enforces it on itself at runtime. When it fails, it records what went wrong and that mistake becomes permanently impossible.
>
> The human stays the source of truth. The agent handles the governance.
>
> Three principles:
> - Self-building — the agent creates its own enforcement from your references
> - Self-improving — every failure makes the system stronger
> - Safety-first — mechanical hooks the agent can't bypass, not guidelines it can ignore
>
> This isn't about replacing human judgment. It's about not relying on the agent's willingness to follow instructions. Structure it can't skip beats structure it's supposed to follow.
>
> I open sourced the implementation: https://github.com/isagawa-co/isagawa-kernel

### Post 2: Monolithic Specs Problem (LinkedIn — next)
Problem post. "Monolithic specs get skipped. Here's why." Break down tiered indexing, modular specs, 200-line threshold.

### Post 3: The Leash (X + LinkedIn — done 2026-02-24)
48s video clip of hook blocking agent at runtime. Attached to QA platform launch post.

## Competitive Landscape

### Direct SDD Competitors
- **Kiro (AWS)** — IDE with monolithic specs, no enforcement
- **Spec Kit (GitHub)** — CLI + templates, no enforcement
- **Tessl** — CLI + MCP, no enforcement

### Our Differentiation
- Agent builds its own specs (not human-authored)
- Mechanical enforcement via hooks (not advisory)
- Self-improving learning loop (not static)
- Modular markdown (not monolithic files)
- No tooling required (just files)

### Adjacent / QA Space
- **Docket** — AI agents for web testing (YC S25)
- **QualGent** — AI Mobile App QA Tester (YC S25)
- **Propolis** — Browser agent QA (YC S25)
- **Bluejay** — QA agency for voice/text AI (YC S25)
