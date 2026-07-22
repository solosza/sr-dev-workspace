# Spec Kit / SDD Interop — Standards Alignment Without Losing Hard Enforcement

## Status
Open

## Priority
Medium-High — strategic. The industry is converging on GitHub Spec Kit as the spec-driven-development interop layer (93k+ stars by May 2026, agent-agnostic, 30+ agents). The kernel is fully bespoke — more control, but zero community leverage and all maintenance on us. Decide how (and whether) to interoperate before the standard hardens further.

## Summary
Spec-driven development is becoming table stakes, and Spec Kit is the emerging standard: a `constitution.md` governance doc + a command surface (`/speckit.constitution → specify → plan → tasks → implement`) that every supported agent respects. The kernel already does SDD — and does it *harder* (hook-enforced gates vs Spec Kit's soft "agent respects the constitution" + checklists) and *deeper* (the domain-spec-factory auto-generates specs; Spec Kit has humans write them). Research whether to expose a Spec-Kit-compatible surface (import/export a `constitution.md` ⇄ protocol, map the command vocab) so the kernel gains interop + community leverage while keeping its non-bypassable enforcement as the differentiator.

## Requirements
- **Map the two models:** Spec Kit's constitution/specify/plan/tasks/implement + its extensions (Security Review, Architecture Guard, governance/cost-tracking entries) against the kernel's protocol + gate-contract + backlog→task-builder→run-task.sh + attestation. Where do they align, where does the kernel exceed it, where is it behind?
- **Enforcement gap analysis:** Spec Kit governance is soft (respected + checklisted); the kernel's is hard (hook-blocked). Assess whether a `constitution.md`-compatible export could carry the kernel's hard gates to Spec-Kit-native agents, or whether hardness is inherently lost at the boundary.
- **Interop options + recommendation:** (a) import Spec Kit specs into a kernel domain, (b) export a kernel protocol as a `constitution.md` for interop, (c) adopt Spec Kit's command vocab as an alias layer, (d) stay fully bespoke. Give a clear recommendation with the maintenance-vs-leverage tradeoff quantified.
- **Positioning:** how the kernel's differentiators (hard enforcement, autonomous spec construction, attestation) are framed relative to a Spec-Kit-standardized world — is the kernel a superset, a competitor, or a governance layer on top?

## References
- GitHub Spec Kit: visualstudiomagazine.com/articles/2026/05/12/github-spec-kit-takes-off...; marktechpost.com/2026/05/08/meet-github-spec-kit...; truefoundry.com/blog/spec-driven-development-ai-agents (governing specs)
- Microsoft AI coding governance approach: softwareseni.com/github-speckit-and-the-microsoft-approach-to-ai-coding-governance
- Kernel: `.claude/protocols/`, `.claude/commands/kernel/`, `.claude/skills/spec-factory/` (domain-spec-factory), attestation/intent chain

## Task Builder Input
- **Deliverable:** Research report in `projects/speckit-interop/` — model mapping, enforcement-gap analysis, interop options with a clear go/no-go recommendation and (if go) a proposed compatibility surface; positioning of the kernel's differentiators vs the emerging standard.
- **Location:** subproject:speckit-interop
- **Scope:** RESEARCH
- **Constraints:** Web research required (Spec Kit evolves fast — cite source + date). The kernel's hard, hook-enforced governance is the crown jewel — any interop must PRESERVE it, not dilute to Spec Kit's soft model. No code in this backlog; produce the recommendation + proposed surface for a separate BUILD backlog if go.
