# Messaging Audit — Isagawa Homepage

## Current Copy

### Hero
The homepage leads with the brand name "Isagawa" and the tagline "An agent harness factory." The description explains intent-to-harness conversion but uses insider language ("structured runtimes," "governance baked in") that assumes the reader already understands what an agent harness is.

### Section Structure
Four sections tell a story arc: The Seed (kernel mechanics) → Growth (what it produced) → Self-Extension (recursive capability) → This Page (proof of concept). Each section has subsections with stats or mechanism descriptions.

### Tone
Technical, declarative, confident. Reads like a system describing itself. Minimal marketing language. No persuasion — pure exposition. This tone is distinctive but may alienate readers who need "what's in it for me" before "how it works."

### CTAs
Two CTAs exist: "See kernel →" (hero) and "Read the kernel landing page →" (Section 01). Both route to technical content. No CTA targets business outcomes, onboarding, or getting started.

## Kernel README Positioning

The README leads with "The self-improving harness for AI coding agents" — clearer than the homepage. It frames the problem (agent drift) and solution (mechanical enforcement) effectively. The README is better at articulating differentiation than the homepage.

Key README framing the homepage lacks:
- The agent drift problem (system prompts ignored, quality checks skipped)
- "Advisory vs enforceable" distinction
- Three-layer architecture (Kernel / Domain Spec / Agent-Generated)
- Quick start simplicity (just VS Code + Claude Code + Python)

## Competitive Landscape

Major competitors (LangChain, CrewAI, AutoGen, W&B) all position as agent engineering platforms focused on building, deploying, and monitoring agents. None address agent governance, mechanical enforcement, or self-improvement. This is Isagawa's unoccupied territory.

Competitor messaging patterns:
- Scale social proof (Fortune 500, millions of workflows)
- End-to-end lifecycle coverage
- Enterprise readiness and control
- Framework-agnostic compatibility

## Gaps

### Gap 1: No Problem Statement
The homepage never articulates WHY someone needs Isagawa. The README does this well (agent drift, advisory vs enforceable). The homepage should lead with the problem.

### Gap 2: Value Prop Buried in Mechanics
The homepage explains HOW the kernel works (anchor tokens, gate enforcers, learn loops) before explaining WHAT it does for the user. Most visitors need the outcome before the mechanism.

### Gap 3: No Audience Targeting
The homepage speaks to one audience: technical insiders who already understand agent governance. It doesn't address:
- Business stakeholders (what's the ROI?)
- Compliance/QA teams (how does this reduce risk?)
- Solo developers (how do I start?)

### Gap 4: "Factory" Framing is Opaque
"Agent harness factory" is precise but requires explanation. Visitors need to already know what an agent harness is AND what a factory metaphor means in this context. The README's "self-improving harness for AI coding agents" is immediately clearer.

### Gap 5: No Differentiation Statement
The homepage never says how Isagawa differs from LangChain, CrewAI, or other frameworks. The README's "advisory vs enforceable" distinction is powerful but absent from the homepage.

### Gap 6: No Getting Started Path
No "try it now" or quick start guide linked from the homepage. The README mentions it needs only VS Code + Claude Code + Python — this simplicity is a selling point that should be on the homepage.

## Tone Analysis

| Element | Current Tone | Desired Tone |
|---------|-------------|--------------|
| Hero | System self-describing | Problem-solution with clarity |
| Section 01 | Technical mechanism catalog | Architecture with business implications |
| Section 02 | Internal metrics | External proof points |
| Section 03 | Recursive abstraction | Concrete capability expansion |
| Section 04 | Meta-narrative | Proof of concept with call to action |

## Recommendations

1. **Lead with the problem** — agent drift, quality degradation, advisory-only governance
2. **Reframe the tagline** — from "agent harness factory" to something that communicates the outcome
3. **Add differentiation** — "not a platform for building agents, a framework for governing them"
4. **Include quick start** — show the 3-step simplicity (VS Code + Claude Code + Python)
5. **Add audience-specific messaging** — at least one line per audience segment
6. **Strengthen CTAs** — add "Get started in 5 minutes" alongside the kernel deep-dive
7. **Keep the tone** — the confident, declarative voice is distinctive; just add clarity before depth
