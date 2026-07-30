---
name: assay
type: skill
version: 0.1
date_created: 2026-07-30
status: draft
purpose: Take any idea and surface the revenue streams the operator can actually capture — an adversarial, kill-by-default, self-sharpening research engine.
---

# Assay — Design Doc

Idea in (mine or from the internet) -> a **ranked shortlist of capturable revenue wedges** out, each with a build verdict, a demand test, and a logged trail. Metaphor: idea = ore; assay it for value + extractability; output = the lode or a fast kill.

**Invocation:** `/assay <idea>` (skill + command in this workspace).
**v1 scope:** triggered core — Loops 1-3 + Decide + the ledger. Ambient loops (Source/Scan, Learn/Meta) are v2 roadmap; v1 lays the ledger they consume.

## Skill Identity
Assay is an adversarial, self-sharpening research engine that takes any idea and surfaces the revenue streams the operator can *actually capture* — climbing the abstraction ladder, fanning out to non-obvious angles, then killing all but the rare survivors and handing back a ranked, build-verified, demand-tested shortlist.

## Philosophy
1. **Diverge wide, converge hard.** Generation is generous (weird welcome); gates are adversarial. Keep the two modes separate or it becomes a rationalization machine.
2. **Kill by default.** The value is fast kills + the rare survivor. A gate that can't confidently keep, kills (or escalates) — never auto-passes.
3. **Climb the ladder.** Evaluate each abstraction rung; the opening usually lives 1-2 rungs above the literal idea.
4. **Capturable, not just possible.** Rank by realizability — speed-to-first-dollar, defensibility, reuse with what the operator already owns — not cleverness.
5. **Research, not action.** Assay never spends, contacts, or commits. It produces verdicts; humans act downstream.
6. **Self-sharpening.** Every run is logged; outcomes + the live internet recalibrate the gates each pass (v2).

## Vocabulary
| Term | Meaning |
|------|---------|
| idea / ore | raw input (mine or from the internet), pre-evaluation |
| wedge | a candidate revenue angle at a specific abstraction rung |
| lode | a wedge that clears all gates — capturable + buildable + demand-validated |
| lens | one of 6 divergence moves that generate candidate wedges |
| gate | one adversarial, kill-by-default check |
| verdict | a loop's typed output (Wedge / BuildVerdict / ValidationResult / Decision) |
| green light | the intersection: viable market x buildable-with-edge x validated demand |
| anti-library | log of kill-reasons; "everyone dies on X" -> X is the opening (v2) |

## Critical Rules
1. **Diverge and converge are separate modes.** Never let a gate strangle generation; never let generation skip the gates.
2. **Kill-by-default.** An uncertain gate kills or escalates to the human — never silent-passes.
3. **Assay never acts.** No spend, outreach, or commit inside the engine. HITL only at (a) the terminal commit and (b) ambiguity escalation.
4. **Every run is logged to the ledger** — idea, per-loop verdicts, final decision (audit + future calibration).
5. **Green light requires all three:** market x build x validated demand. Two of three = park, not go.

## Workflow Summary
| Step | Responsibility | Output | HITL |
|------|----------------|--------|------|
| 1. Opportunity | normalize -> abstract -> DIVERGE (6 lenses) -> adversarial gates -> rank | `Wedge[]` | no |
| 2. Buildability | per surviving wedge: can WE build+automate+govern with an edge | `BuildVerdict[]` | no |
| 3. Validate | cheapest real demand test per build-viable wedge | `ValidationResult[]` | no |
| 4. Decide | intersect market x build x demand -> ranked shortlist + preconditions | `Decision` | **YES** (commit) |

> Step specs: [[references/workflow]]. The Loop-2 picks-and-shovels variant re-enters Step 1's diverge, bounded to 1 hop.
> **v2 (roadmap, not built now):** Source/Scan (ambient internet idea + "why-now" catalyst hunt) and Learn/Meta (outcome + internet recalibration of gates/lenses) — the self-sharpening tier.

## Design Documents
| Document | Purpose |
|----------|---------|
| [[references/workflow]] | Per-step Purpose + Procedure (Loops 1-3 + Decide) |
| [[references/lenses]] | The 6 divergence lenses |
| [[references/gates]] | The adversarial gate battery |
| [[references/io-contracts]] | Typed object schemas (Idea / Wedge / BuildVerdict / ValidationResult / Decision) |
| [[references/state-schema]] | Ledger (v1) + v2 stores (anti-library, world-model, registry) |
| [[references/contracts]] | Per-step contract definitions (soft + mechanical validation rules) |

## Complete File Structure
```
.claude/
  commands/
    assay.md                        # /assay <idea> entry point
  skills/assay/
    SKILL.md
    workflow.md
    gate-contract.md
    steps/
      step-01-opportunity.md
      step-02-buildability.md
      step-03-validate.md
      step-04-decide.md
    references/
      lenses.md
      gates.md
      io-contracts.md
      state-schema.md
    contracts/
      step-01-contract.json
      step-02-contract.json
      step-03-contract.json
      step-04-contract.json
    state/
      ledger.jsonl                  # append-only run log (created at runtime)
```
