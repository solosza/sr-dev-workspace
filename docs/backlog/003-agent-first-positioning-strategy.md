# Backlog 003: Agent-First Positioning Strategy

## Status
Open

## Priority
High — market timing is now

## Summary
Position Isagawa's kernel + spec ecosystem in the "agent infrastructure" category that Levie and the broader market are defining. We're already building in the governance/enforcement gap — now we need to articulate it clearly and show up where agents (and their builders) are looking.

## Market Context
Aaron Levie (Box CEO) published "Building for trillions of agents" (March 2026) calling out:
- Agents become primary users of all software → build API-first, agent-first
- Infrastructure gaps: identity, memory, governance, compute, coordination
- "Make something agents want" — agents pick tools on technical merit, not marketing
- Security/compliance/governance is a major unsolved problem for agents
- Seat-based pricing dies → consumption/volume-based wins

## Where We Fit
| Market Gap (Levie) | Isagawa Equivalent |
|--------------------|--------------------|
| "strict controls on what actions agents can take" | Hook enforcement layer (universal-gate-enforcer) |
| "govern and retain all the work agents did" | JSONL execution log (backlog 001), actions_log |
| "skills they leverage for repeated actions" | Domain specs (drop-in skill folders) |
| "long-term memory across sessions" | session_state.json + context persistence |
| "agents need identities to authenticate into services" | Domain identity via protocol (self-built per repo) |

## Competitive Landscape — GitHub Trending (March 2026)

The fastest-growing AI repos this week show every layer being rebuilt for agents — except governance:

| Repo | Stars | What It Does | Layer | Has Enforcement? |
|------|-------|-------------|-------|-----------------|
| **Agency Agents** | 35K | One command → 51 AI specialists across 9 departments | Orchestration | No — prompt routing, session-stateless |
| **Auto Research** (Karpathy) | 25K | Plans experiments, writes code, trains, evaluates, loops | Research loops | No — single-purpose, no cross-session memory |
| **Lightpanda** | 14K | Headless browser built from scratch for agents (11× faster) | Infrastructure (browser) | N/A — different layer |
| **llmfit** | 14K | Benchmarks every model against your hardware | Tooling | N/A — benchmarking tool |
| **CLI-Anything** (HKU) | 3.5K | Wraps any desktop app into agent-controllable tool (3 days old) | Desktop control | No — tool wrapping, no governance |

**The pattern:** every layer of the stack — orchestration, research loops, browsers, local models, desktop control, memory — is being rebuilt for agents simultaneously. But **nobody is building the enforcement/governance layer**.

**Where Isagawa sits:** We're the missing row in this table.

| **Isagawa Kernel** | — | Self-governing agent infrastructure: hooks, learn loops, specs, cross-session state | **Governance/Enforcement** | **Yes — hooks agents can't bypass, mandatory learn after failure, gate contracts** |

## What Nobody Else Has
Every repo above is about making agents **do more**. None of them address making agents **stay reliable under enforcement**. Our kernel is the governance layer the market hasn't built yet:
- Hooks agents can't bypass
- Self-improvement after every failure (learn loop)
- Cross-session state persistence with enforcement
- Spec-driven domain knowledge (agents teaching agents)

## Action Items

### Messaging
- [ ] Define one-liner positioning: "Self-governing agent infrastructure" or similar
- [ ] Write the "why enforcement matters" narrative — agents that self-correct vs agents that drift
- [ ] Create comparison matrix: Isagawa kernel vs Agency Agents vs Devin vs Claude Code vanilla

### Technical Proof Points
- [ ] Demo video: agent hits hook block → self-corrects → records lesson → never repeats mistake
- [ ] Demo video: drop spec into cognitive-agent → domain-setup → cycling builds full project
- [ ] Publish gate-contract verification results (spec factory output)

### Distribution
- [ ] cognitive-agent README rewrite — lead with governance/enforcement angle, not "another agent framework"
- [ ] Agent Skills marketplace listing (agentskills.io) — specs as discoverable skills
- [ ] Blog post or thread: "The missing layer in agent infrastructure: self-governance"
- [ ] Position QA platform as proof — production system running under kernel enforcement with paying customers

### Business Model
- [ ] Revisit QA platform pricing — per-test-run (consumption) not per-seat
- [ ] Spec marketplace pricing model — free specs + paid enterprise enforcement/governance layer?
- [ ] Explore: kernel-as-a-service for teams deploying agents at scale

## References
- Aaron Levie blog post: "Building for trillions of agents" (March 2026)
- Twitter thread: @levie March 8-9 2026
- GitHub trending repos analysis (Agency Agents, Auto Research, Lightpanda, llmfit, CLI-Anything)
- Backlog 001: Zep Cloud memory research (cross-session persistence)
