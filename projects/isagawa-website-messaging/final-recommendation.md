# Final Recommendation — Homepage Copy Package

## Recommended Hero Copy

**Headline:** AI agents that follow the rules. Every time.

**Subheadline:** Isagawa is a drop-in enforcement framework for AI coding agents — mechanical quality gates, mandatory learning, and cryptographic attestation. No infrastructure required.

**Description:** AI agents drift. They skip quality checks after thousands of tokens, ignore instructions during complex work, and repeat the same mistakes across sessions. Isagawa solves this with enforcement gates at the tool-call boundary — not guidelines agents can ignore, but checks they physically cannot bypass. Every failure becomes a permanent lesson. Every output is cryptographically signed. The governance is a property of the system, not a layer on top of it.

**Primary CTA:** Get started in 5 minutes →
**Secondary CTA:** See the kernel →

**Rationale:** This hero synthesizes Variant B's business clarity (agent drift problem + "agents you can trust") with Variant A's technical precision (enforcement gates, tool-call boundary, cryptographic attestation). The headline is immediately understandable to all three audience segments. The subheadline packs three concrete capabilities and the "no infrastructure" hook for founders. The description leads with the problem, offers the solution, and closes with the architectural distinction.

## Recommended Subheader
"Not a platform for building agents. A framework for governing them."

This one-liner differentiates Isagawa from every competitor in the space (LangChain, CrewAI, AutoGen) by reframing the category. It positions Isagawa in unoccupied territory.

## Recommended Quick Start Micro-Section (NEW — add between hero and Section 01)

**VS Code + Claude Code + Python.**
No database. No Docker. No cloud infrastructure.
Clone the kernel. Run session-start. Your first enforcement gate fires in five minutes.

`git clone https://github.com/isagawa-co/isagawa-kernel` → Try it now

## Recommended Section Copy

### Section 01: The Kernel

"A minimal kernel — interlocking enforcement mechanisms that govern every agent action. The kernel scans your repo, builds its own protocol, and produces enforcement hooks that intercept every tool call. Governance becomes a property of the system, not a suggestion on top of it."

**Subsections:**
- **Anchor Token:** "Every N actions, the system re-reads its own protocol. Context drift becomes mechanically impossible."
- **Gate Enforcer:** "A hook at the tool-call boundary blocks writes until prerequisites are met. Quality checks are guaranteed, not suggested."
- **Learn Loop:** "Every failure is recorded as a permanent lesson. The protocol updates itself. The same mistake cannot recur."
- **Session Protocol:** "Start, anchor, work, complete. The same governed loop, every session, every agent."

CTA: Read the kernel docs →

### Section 02: Growth

"The kernel produced everything it now uses to operate — 30+ governed agents, a 12-step factory pipeline, governed workspaces. None of it was hand-coded. The kernel managed conversations that produced AI agents. Those agents learned new domains. A factory pipeline emerged to compile natural language into governed agents automatically. Every artifact was produced under enforcement."

Stats:
- "30+ governed agents produced from conversation"
- "12-step factory pipeline — natural language to governed agent"
- "Every workspace operates under the same enforcement loop"

### Section 03: Self-Extension

"The system now produces new capabilities from conversation — skills, commands, workflows — that become part of the system itself. Each new capability extends the range of what future conversations can build. 130+ backlogs captured as intent. 90+ pipeline executions completed autonomously. The factory is not just producing outputs. It is producing itself."

### Section 04: This Page

"You are looking at the output. This page was built by the system it describes. The kernel governed. The pipeline decomposed and built. The attestation signed the work. Three pipelines, 55 tasks, under two hours. Every claim on this page is mechanically verifiable. The attestation bundles below are real. Verify them yourself."

## Recommended CTAs

| Position | CTA Text | Target |
|----------|----------|--------|
| Hero (primary) | "Get started in 5 minutes →" | Quick start / GitHub repo |
| Hero (secondary) | "See the kernel →" | Kernel landing page |
| Quick Start section | "Try it now →" | GitHub clone command |
| Section 01 | "Read the kernel docs →" | Kernel documentation |
| Section 04 | "Verify the attestation →" | Rekor transparency log |

## Implementation Notes

### HTML Changes Needed
1. **Hero section:** Replace headline, subheadline, description, and CTAs
2. **Add Quick Start micro-section:** New section between hero and Section 01 with terminal-style display showing the clone command
3. **Section 01-04:** Update body copy and subsection text
4. **Stats in Section 02:** Update to governance-framed versions
5. **CTAs throughout:** Add "Get started" alongside existing "See kernel" links

### Alignment with Backlog 124 (Aesthetic Directive)
- Maintain dark theme, grain texture, monospace headings per established design tokens
- Quick Start section should use terminal/code styling consistent with existing badge elements
- New CTAs should match existing button styling (no new design elements)
- Subheader uses the same muted secondary text color as existing subsection text

### What NOT to Change
- Navigation structure (Home, Kernel, Feed, Products, The Story)
- Provenance section (attestation bundles are real artifacts)
- Footer structure
- Section numbering pattern (01, 02, 03, 04)
- Overall page architecture (scroll-down narrative arc)

## Audience Coverage Verification

| Audience | Addressed In | Evidence |
|----------|-------------|----------|
| AI Infrastructure Teams | Hero (enforcement gates), Section 01 (mechanisms), Section 03 (self-extension) | "tool-call boundary," "protocol re-reads," "enforcement loop" |
| Compliance/QA Teams | Hero (can't bypass), Section 01 (guaranteed checks), Section 04 (attestation) | "physically cannot bypass," "guaranteed not suggested," "verify them yourself" |
| Early-Stage Founders | Hero (no infrastructure), Quick Start (5 minutes), Section 02 (what's possible) | "no database, no Docker," "five minutes," "MIT license" |

All three audiences from backlog 138 are addressed. The hero speaks to all three simultaneously. Segment-specific depth comes in the sections.
