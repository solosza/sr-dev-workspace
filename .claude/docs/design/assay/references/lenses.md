# Divergence Lenses (Step 1)

Generate candidate wedges from each abstraction rung. Generous — weird is fine; killing happens at the gates, not here.

| Lens | Move | Example |
|------|------|---------|
| adjacent | same capability, new market | RE video -> auto dealers, STR, e-commerce |
| transpose | the mechanism in a far domain (strip the artifact — keep the *mechanism*) | "find invisible-X, auto-build the fix, pitch it built" -> unclaimed Google profiles, bad marketplace listings, missing menus/booking, not just websites |
| recombine | mash with an asset already owned | + ALA data / kernel governance -> the compliant version nobody runs |
| invert / picks-and-shovels | sell TO the crowd, don't be one | be the compliance/disclosure layer the video crowd lacks |
| constraint-break | target who won't DIY; drop the assumed limit | serve the small business that won't touch SaaS |
| zoom | category-level tool <-> hyper-niche | one engine for all verticals vs one deep niche |
| payer-swap | same solution, a DIFFERENT buyer who has budget | don't only sell the cheap end-user — sell the capability to whoever the problem pains most: the platform, the DIY vendor (as leads/affiliate), the franchise HQ, a data buyer |

Each generated wedge records its `lens_origin` and `abstraction_rung` so the Decide step can show *where* an opening came from.

## Mandatory quotas (anti-anchoring)

Divergence fails silently when every wedge is just the input idea re-dressed. To force real distance:

- **transpose** MUST yield at least one wedge that changes the *artifact/mechanism domain* (not just the market) — or Step 1 logs an explicit `quota_miss: transpose` with the reason none was viable.
- **payer-swap** MUST yield at least one wedge that changes *who_pays* — or logs `quota_miss: payer_swap` with the reason.
- A run where every survivor shares the input's artifact AND payer is a **divergence-failure flag** surfaced at Decide (the engine under-explored; treat conclusions as low-confidence).
