---
name: assay
version: 1.0
status: draft
type: skill
design_doc: .claude/docs/design/assay/index.md
design_doc_hash: 1a469d56e2d12f94511afb69069cae5d71b5c6de78dcd40b64987398fba256dc
---

# Assay — Skill

## Identity

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

## Workflow

Triggered core (v1): one idea in -> Loops 1-3 + Decide -> a ranked, logged shortlist out. Sequential and autonomous; the only HITL is the terminal commit at Step 4. See `workflow.md` for phases, checkpoints, and state.

| Step | What It Does |
|------|-------------|
| 1. Opportunity | normalize -> abstract -> DIVERGE (6 lenses) -> adversarial gates -> rank -> `Wedge[]` |
| 2. Buildability | per surviving wedge: can WE build+automate+govern with an edge -> `BuildVerdict[]` |
| 3. Validate | cheapest real demand test per build-viable wedge -> `ValidationResult[]` |
| 4. Decide | intersect market x build x demand -> ranked shortlist + preconditions -> `Decision` (HITL commit) |

## Critical Rules

1. **Diverge and converge are separate modes.** Never let a gate strangle generation; never let generation skip the gates.
2. **Kill-by-default.** An uncertain gate kills or escalates to the human — never silent-passes.
3. **Assay never acts.** No spend, outreach, or commit inside the engine. HITL only at (a) the terminal commit and (b) ambiguity escalation.
4. **Every run is logged to the ledger** — idea, per-loop verdicts, final decision (audit + future calibration).
5. **Green light requires all three:** market x build x validated demand. Two of three = park, not go.

## File Index

| File | Purpose |
|------|---------|
| `SKILL.md` | This file — orchestrator |
| `workflow.md` | Phase definitions, checkpoints, state schema, HITL stops |
| `gate-contract.md` | Phase gates + per-step output validation |
| `steps/step-01-opportunity.md` | Normalize -> abstract -> diverge -> gate -> rank wedges |
| `steps/step-02-buildability.md` | Score build/automate/govern edge per wedge |
| `steps/step-03-validate.md` | Pick the cheapest decision-changing demand test |
| `steps/step-04-decide.md` | Intersect verdicts, rank, log, present for HITL commit |
| `references/INDEX.md` | Reference index — links to design doc references |
| `contracts/step-01-contract.json` | Wedge[] output validation |
| `contracts/step-02-contract.json` | BuildVerdict[] output validation |
| `contracts/step-03-contract.json` | ValidationResult[] output validation |
| `contracts/step-04-contract.json` | Decision output validation + ledger append |
| `state/ledger.jsonl` | Append-only run log (created at runtime) |

## Render the result (final step, optional)

After Step 4 (Decide), render the ranked shortlist as a live, question-able board via [[../render/steps/step-serve-and-watch]]: pass the decide output through the adapter [[../render/adapters/INDEX]] (`to_items`), then serve-and-watch. Standalone and modular — assay still runs headless without it. Plain vocabulary, rank on merit, fit shown as a tag only, and no em dashes are already baked into the adapter.
