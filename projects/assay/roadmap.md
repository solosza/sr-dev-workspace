# Venture Loops — Roadmap (one screen)

Family of governed, kill-by-default loops that take a business from idea → money. Each: typed steps, one HITL commit, compact persist, prior-art check. **Output = quickest view to the pertinent info, never long docs.**

```
/source → /assay → /competition → /deep-dive → /offer → /gtm → /launch → /operate → /sharpen
  ✅        ✅          ✅              ✅           ✅       ✅       ✅          ✅          ✅
  └─────── FULL FAMILY BUILT ─ every loop standalone + modular (callable alone or by another loop) ──────┘
```

| Loop | Command | Question it answers | Status |
|------|---------|--------------------|--------|
| Source/Scan | `/source` | Which ideas even enter? (feeds assay) | ✅ built |
| Assay | `/assay` | Which idea is worth capturing? | ✅ built |
| Competition (A) | `/competition` | Can I win this arena? | ✅ built |
| Deep-Dive (B) | `/deep-dive` | Is it real + the plan? (calls A) | ✅ built |
| Offer/Pricing | `/offer` | How do I package + charge to max capture? | ✅ built |
| Go-to-Market | `/gtm` | How do I actually get customers? | ✅ built |
| Build/Launch | `/launch` | Ship the first sellable asset | ✅ built |
| Operate/Run | `/operate` | Run it, HITL-governed | ✅ built |
| Learn/Meta | `/sharpen` | Did the verdicts pan out? upgrade the engines | ✅ built |

**Two phases (design principle):**
- **Before GO** (assay → competition → deep-dive): light, adversarial, kill-fast. Burn ideas, not money. Cheap + disposable by design.
- **GO line** = deep-dive's go/no-go = the real commitment to pursue.
- **After GO** (offer/pricing → GTM → build → operate): the "serious stuff" — real time + real money. Carries HEAVIER HITL governance because every step now spends something. This is what the kernel is really for. *(Build later.)*

**Venture record (BUILT):** `projects/assay/ventures/<slug>.md` ties ONE business's runs across all loops into a single journey (Stage · Verdict · Next-action + a Journey table linking each loop's run). Dashboard: `projects/assay/ventures/INDEX.md`. Every loop's persist step now updates it. This is how the pipeline output is captured end-to-end.

**Home:** all loop output lives under `projects/assay/` (assay/competition/deep-dive runs + ventures + this roadmap). Designed to lift out into its own governed repo when the family grows — see "Future: own repo" below.

## Generative family — the reframe trio + angle-loops
The adversarial pipeline *converges* (kill/validate/gate/govern). The generative side *reframes*:
- **`/expand`** — think BIGGER (empire). Dispatches angle-loops: `/data` · `/distribution` · `/platform` · `/productize` · `/license` · `/stack` · `/adjacent` (adjacent ventures → `/assay`).
- **`/small`** — think SMALLER (smallest viable / narrowest / fastest-to-cash).
- **`/lateral`** — think OUT OF THE BOX (invert the assumption, contrarian, weird recombination).

Reframe big / small / sideways; the adversarial loops test what survives.

## Source family — idea provision (the proactive front)
The system was reactive (you bring an idea). `/source` is now a **dispatcher** that *provides* ideas: **you give a seed, the loop takes it from there.** It runs 6 hunters, each finding ideas a different way, cross-references for multi-signal winners (pain × why-now × fit), and auto-feeds the top into `/assay`:

`/trends` (why-now) · `/pain` (real demand) · `/arbitrage` (proven-elsewhere) · `/assets` (your moat) · `/gaps` (underserved) · `/bookmarks` (your saves)

Runs on demand (any seed) + a **weekly ambient drop**. `/sharpen`'s learnings steer the hunters. This is also the content engine for a "vetted business ideas" channel.

## Self-extending
Loops **capture their own blind spots**: spot a monetization/expansion path with no loop -> append to `projects/assay/loop-candidates.jsonl` (never dropped). `/sharpen` reads the register and, when a candidate recurs (>=2x), **proposes scaffolding it into a new loop**. The system grows new loops by noticing what it's missing — add angle-loops anytime without touching the rest.

## Future: own governed repo
When the loops grow, extract this whole system into its own repo — a kernel-governed **spec** (like the QA platform): loops = commands, kill-by-default gates + HITL commits = the protocol, venture records + ledgers = the state. Frees this workspace for other dev work. Don't extract prematurely — grow + stabilize here first.

**Status:** all 9 loops built (compact skills, lean output, standalone + modular, persist + venture-record wired). Next isn't building — it's *using* them (run a real venture through the chain) + hardening from real runs via `/sharpen`. Deeper design docs / contracts per loop can come later if a loop needs more rigor; today they're lean single-file skills.
