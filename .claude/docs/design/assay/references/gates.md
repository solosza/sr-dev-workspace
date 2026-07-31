# Adversarial Gate Battery (Step 1)

**Kill-by-default.** Each gate defaults to KILL; a candidate survives only on clear evidence. An uncertain gate does NOT silent-pass — it flags the wedge for ambiguity escalation at the Decide step.

| Gate | Kills the wedge if |
|------|--------------------|
| legal / reg | requires a license/registration the operator lacks, or the model is illegal / ToS-violating |
| unit economics | no realistic path to positive margin |
| saturation | crowded with funded incumbents + generic tools, and no seam left |
| timing / why-now | no catalyst (new tool / reg / platform shift) opening a window |
| moat | pure commodity; no defensible edge available |
| fit-to-me | **NOT A KILL - displayed only (calibration 2026-07-31).** How well the idea matches the operator's assets/skills/channels. Shown as a tag (high / cond / low); it NEVER kills and NEVER multiplies ranking at Step 1. Fit is a **Decide-stage** factor only (finite-resource allocation), applied consciously by the human. A strong idea survives on its own merits at fit:low - the operator can build, partner, or acquire the capability. The bias this fixes: fit-as-a-gate funnels every assessment back to what the operator already does. |
| speed + cost to first dollar | too slow or too expensive to reach revenue |
| recurring vs one-shot | one-and-done with no repeat (soft: down-ranks, does not auto-kill) |
| TAM / demand-density | too few reachable buyers in a servable unit (e.g. per metro/niche) to sustain the model — forces a rough count, not a vibe. A wedge that exhausts a geography in a week fails unless it scales cheaply across geos |
| reachability | you cannot actually *reach* the buyer through a channel you can run. Watch the self-selection trap: if the target is defined by low digital engagement (no website/profile), digital outreach selects against the very people you must reach |
| guru-source / doer-vs-seller | the idea's loudest promoters make their money **selling the blueprint** (course/community/coaching), not **running the business** — a strong tell the business is harder / less lucrative than pitched. **DOWN-WEIGHTS, never hard-kills alone** — hype != bad (a hyped space can still be real, esp. with a genuine edge the crowd lacks; see fit-to-me / moat). The real money in a guru-hyped space is often the picks-and-shovels — so a guru-source hit should *trigger the picks-and-shovels / payer-swap reframe*, not just a kill. |

Survivors carry a per-gate score (`gate_scores`) used for ranking in Steps 1 and 4. **Rank on absolute opportunity merit** (real pain + why-now + defensibility + size) — NOT on fit-to-me. A great business is great whether or not it's the operator's.

**UNBIASED by default (calibration 2026-07-31).** The engine's job is to surface the best ideas *period*, not the best ideas *for the operator*. Fit-to-me is displayed, never a gate or a ranker (see the fit row). **Bias-check:** if a run's survivors all cluster around the operator's existing assets/domain, raise a **bias-failure flag** ("everything funneled back to what I already do — under-explored") and force genuinely distant ideas via `/lateral`, `/transpose`, and `/arbitrage` into unfamiliar domains. The engine must be willing to rank #1 a fantastic business the operator would have to build/partner/learn from scratch. Calibrated through iteration (`/sharpen`).

**Reachability is often the hidden killer.** "Compliant to contact" (legal gate) is not the same as "possible to contact" — a target with no email/website may be unreachable by any channel you can automate. Force this question explicitly; it is the gate most often skipped.

**Calibration — gates cause MISSED OPPORTUNITIES if they over-fire (avoid false kills).** A kill-by-default battery trades false-positives (bad ideas that slip through) against **false-negatives (good ideas wrongly killed)** — and a wrongly-killed opportunity is silent and expensive. Two safeguards:
1. **Every kill is revisitable, never permanent.** A kill records *which gate* killed it + the reason (in the ledger). Kills are re-examinable, not deleted.
2. **`/sharpen` periodically re-checks kills against the world** (see its calibration step): did a killed idea later succeed for someone else? does a gate kill an unusually high share? → that gate is **over-firing → loosen it**. The guru-source and saturation gates are the likeliest over-firers (hype and "crowded" both routinely hide real openings), so they get re-checked first. Run `/sharpen` on a cadence (e.g. weekly) so an over-tight gate is caught in days, not after a year of missed openings.

**Design intent for build-command:** each gate becomes a soft_validation_rule in the step-01 contract (judgment call, logged with rationale), except `legal/reg` which may also carry a mechanical_validation where a hard signal exists (e.g., a known license requirement). Note: `fit-to-me` is NOT a validation rule at all anymore — it is a *displayed tag*, computed and shown, never gating.
