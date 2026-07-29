# Isagawa v2.0 (IOM): Architecture

> **isagawa** · _"Discover the system. Build the future."_  _(external)_
>
> _Internal only:_ _"Discover the system. Build the future. Always learning."_ Learn is the internal
> fourth part, kept **inside isagawa** (an implementation detail of the kernel: it continuously captures
> evidence and improves future discovery and compilation, with no user-facing "learning phase"). It never
> appears in the outward tagline. (Source: factory chat, "we keep learn inside isagawa"; "Always learning.")

_The overall design, current state. The **why** and the decision history live in
[design-decisions.md](design-decisions.md); this is the **what** and the **how**, now. Index-style:
this doc points to the real payloads (the skills, the contracts, the decisions), it does not duplicate them._

## What it is

IOM (Invariant Operating Model) is a private engine that turns a **purpose** into a **governed operating
model**. One invariant loop, applied at every scale:

```
DISCOVER  ->  COMPILE  ->  EXECUTE  ->  artifacts  ->  evidence  ->  (loop)
```

Discover / Compile / Execute is what a user experiences; Learn is internal.

> `[OPEN - naming]` **Compile vs Build for the middle phase.** The tagline uses "Build" ("Build the
> future"). Lean: keep **Compile** for the technical loop (it is the differentiating compiler word, and it
> avoids colliding with the `build` *capability* inside evaluate -> design -> build -> validate), and use
> **Build** outward-facing (the tagline). If you want one word everywhere, go all-Build and rename the
> `build` capability to `scaffold`. Not decided.

## How it is built (three rules)

- **Prose-primary.** The LLM is the orchestrator. Capabilities are PROSE (skills). Contracts are DATA
  (JSON). Code is HOOKS only (mechanical enforcement).
- **Index / payload = coordinator / capability.** A thin coordinator routes and holds no artifact; the
  capabilities own the work. The kernel's tiered-index law, applied to execution.
- **One primitive, self-similar.** Everything (the factory's steps, a harness, a workflow, the thing that
  builds them) is the same primitive: a command/skill + a contract, a hook only where enforcement is
  mechanical. No new abstraction layer.

## The factory

The compile engine. A thin coordinator wires four capabilities, each **pluggable per scope** by a data
contract (doc / command / code / ...):

```
evaluate  ->  design  ->  build  ->  validate
```

- Every capability begins with **discover** (a shared primitive): characterize the input, locate where
  its target lives, ambiguity-triggered HITL. It is invoked, not copy-pasted.
- New scope = a new contract, not a new capability.
- Contracts accumulate into a private **capability library** (the compounding moat, design-decisions §11).

## Status (hand-bootstrap)

| Capability | State | Where |
|-----------|-------|-------|
| `discover` (primitive) | built | `.claude/skills/discover/` |
| `validate` | built, dogfooded, gate-tested | `.claude/skills/validate/` + `.claude/hooks/validate-gate.py` |
| `evaluate` | built, dogfooded | `.claude/skills/evaluate/` |
| `design` / `build` | exist as v1 skills, to generalize | `.claude/skills/design-command/`, `build-command/` |
| coordinator | to generalize from the loop | `.claude/skills/execute-pipeline/` |

**The gate:** one generic hook (`validate-gate.py`) checks any register against its declared contract,
structurally. Semantic judgment stays with the LLM (the soft gate). One hook, every contract.

## Boundary (the moat)

- **Platform repo (private, not distributed):** kernel + factory + capability library. The IP.
- **Client repo (delivered):** their compiled operating model + a runtime-only kernel. Never the factory.
- Architectural change routes back to the engine (retention). Detail in design-decisions §8.

## Map

| Payload | What it is |
|---------|-----------|
| [design-decisions.md](design-decisions.md) | the decision log: why + history, every claim tagged |
| `.claude/skills/{discover,validate,evaluate}/` | the built capabilities (prose orchestrators + JSON contracts) |
| `.claude/hooks/validate-gate.py` | the one generic gate hook |
| IOM map / validate-flow | the visual explainers (Artifacts) |

Build sequence, IP boundary, capability library, and open items: design-decisions §7 through §12.

---

**Note on this doc:** kept thin and hand-written for now. When the doc-harness exists, the polished
canonical version (an RFC) gets *generated* from the decisions log + the built capabilities and validated
by the `validate` skill. This is the interim index until then.
