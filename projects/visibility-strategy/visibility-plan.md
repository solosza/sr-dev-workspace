# Visibility / Get-Known Plan (282)

Task: 002-build-channel-plan-goal-branched.md | Gate: VP-02
Built on: [[field-and-asset-notes.md]] (VP-01)

Premise (from backlog 282): the work is ahead of the public frontier; distribution, not quality, is the constraint. Goal branches: **career** (active job search, top AI-infra roles — most time-sensitive), **venture/clients**, **recognition/thought-leadership**.

---

## 1. Ranked Channel/Artifact Table (Goal-Branched)

Effort: S(mall) / M(edium) / L(arge). Leverage: 1 (low) – 5 (very high), goal-independent ceiling.

| Artifact | Effort | Leverage | Career rank | Venture rank | Recognition rank |
|---|---|---|---|---|---|
| **DEMO** — watchable meta-factory / governed-loop | M | 5 | **1** | 2 | **2** |
| **PAPERS-RESPONSE** — field report vs. arXiv 2605.25665 | M | 5 | 2 | 3 | **1** |
| **ESSAY** — "harness engineering + a meta-factory" | M/L | 4 | 3 | 4 | 3 |
| **X/HN posting** — distribution layer for the above | S | 4 (amplifier) | 4 | 6 | 4 |
| **OSS clean slice** — publish a decoupled kernel piece | L | 4 (compounds) | 5 | **1** | 5 |
| **Talk/CFP** | L (long lead) | 3 | 6 | 5 | 6 |

Bold = lead recommendation for that goal.

---

## 2. Per-Artifact Detail

### DEMO — watchable meta-factory / governed-loop
**What it reveals:** the kernel's self-build → gate-contract → learn loop running end-to-end — task-builder decomposing a goal, a gate failing, `/kernel/learn` firing, the loop self-correcting. Recorded against **Orderly** (clean-room demo app) or the **Kernel repo's own dev loop** — never against this workspace (`sr_dev_workspace`) or any client-adjacent directory, since backlog/GTM content and any HMSA-adjacent paths are confidential and must never appear on-screen, in a terminal history, or in a visible file tree during recording.
**IP-reveal check:** draws from Kernel (MIT — shareable) + Orderly (shareable) + domain-spec meta-factory (MIT/shareable). **Clears the boundary** — contingent on recording discipline above (no sr_dev_workspace paths/content visible, no QA-platform or HMSA directory in the terminal at any point).
**Why it leads Career:** most concrete, watchable proof-of-work — directly linkable from a resume/portfolio and usable as interview evidence without translation. Matches the operator's live job-search targets (AI-infra roles want to see a working harness, not a description of one).
**Goal stacking:** the single highest-leverage artifact — stacks **career + venture + recognition** simultaneously (portfolio evidence, sales/demo material, and shareable HN/X content all at once). Build this first.

### PAPERS-RESPONSE — field report vs. arXiv 2605.25665
**What it reveals:** a practitioner response to "Meta-Engineering Harnesses for AI-Native Software Production" (Sengupta/Briggs/Myshakivskyi, 2026-05-25) — mapping the paper's proposed architecture (contract-driven, role-specialized routing, adversarial verification, self-improvement via failure classification) directly onto the kernel's shipped equivalents (gate-contract.md, task-builder's BUILD/TEST split, orchestrator re-validation lessons #37–#44, `/kernel/learn` + lessons.md), with arXiv 2606.04455's finding (meta-agents rarely match human-engineered baselines) used as a foil to sharpen the claim: this is not "agent designs an agent from scratch," it's "agent builds and mechanically enforces its own governance scaffold" — a narrower slice that already clears the harder paper's bar in this operator's own runs.
**IP-reveal check:** draws only from Kernel/meta-factory internals (MIT/shareable) plus public arXiv sources. No client, QA-platform, or HMSA content required to make the argument. **Clears the boundary.**
**Why it leads Recognition:** "practitioner-response-to-a-named-academic-paper" is rare, high-signal content — it reads to both an academic audience (cites correctly, engages the paper's own framing) and an industry audience (shows a real deployed system, not a toy). Rare content gets disproportionate attention.
**Goal stacking:** strong career secondary — research-literate infra roles (the OpenAI/Google/Anthropic-adjacent targets in the active search) specifically value engineers who read and respond to the literature, not just ship code. Stacks **career + recognition**, weaker on venture (prospective clients care less about academic positioning than working proof).

### ESSAY — "harness engineering + a meta-factory"
**What it reveals:** connects Fowler/Boeckeler's April-2026 "harness engineering" framing (Agent = Model + Harness, five-layer maturity model) and Spec Kit's mainstream scale (120k+ stars) to the kernel's independent, pre-dated implementation — the kernel matches the five-layer model point for point and sits one layer deeper than Spec Kit (mechanical runtime enforcement + a learn-from-failure loop, not just spec authoring).
**IP-reveal check:** draws from Kernel (MIT) + public field sources (Faros, Cobus Greyling, Visual Studio Magazine, star-history.com) — no client/proprietary content needed. **Clears the boundary.**
**Why it ranks mid-tier everywhere:** solid thought-leadership piece but slower to produce (M/L effort, careful citation work) and less concrete than the demo or papers-response — best framed as the connective narrative that LINKS the other artifacts together, not a standalone lead.
**Goal stacking:** career + recognition (a well-argued technical essay is portfolio-adjacent signal); weakest on venture (prospective clients respond better to seeing the system than reading about the category it belongs to).

### X/HN posting
**What it reveals:** nothing new on its own — it is the **distribution layer**, not a content artifact. Its job is to carry the DEMO, ESSAY, or PAPERS-RESPONSE to an audience (Hacker News, X/LinkedIn) rather than stand alone.
**IP-reveal check:** neutral by itself; inherits whatever it links to. **Clears the boundary only if** the linked artifact does — re-verify the link target has zero confidential content before posting, every time.
**Why it's ranked as an amplifier, not competing directly:** Low effort (S), fast, keeps the job-search pipeline visibly active (recruiters see engagement) — but has no standalone leverage without a linked artifact. Treat as mandatory companion to DEMO/PAPERS-RESPONSE/ESSAY releases, not a separate initiative.
**Goal stacking:** amplifies whatever it's attached to; ranked low on Venture specifically because cold HN/X traffic rarely converts to client relationships directly (OSS + direct outreach do that job better).

### OSS clean slice
**What it reveals:** a genuinely decoupled, standalone-installable piece of the kernel/task-builder pattern, published as open source (kernel is already MIT) — proof that the governance pattern works outside this operator's own workspace, not just narrated.
**IP-reveal check:** draws from Kernel (MIT) + domain-spec meta-factory (MIT/shareable). **Clears the boundary in principle**, but requires active de-risking work before publish: strip any workspace-specific state, paths, or extension code that references client/QA-platform context; verify no `sr_dev_workspace`-specific backlog/GTM content leaks in via commit history if extracted via `git filter` from this workspace. This is the one artifact where the IP check is a **process gate**, not just a content check.
**Why it leads Venture:** mirrors the exact motivating business model of arXiv 2605.25665 itself ("CTO-as-a-service" via continuously-evolving infra) — a working OSS artifact IS the credibility proof a prospective client or collaborator can inspect directly, higher trust than a demo video or essay.
**Goal stacking:** venture-primary, recognition-secondary (stars/adoption compound over time, but slowly — this is not a week-1 shippable). Weakest on career fit given the active search's urgency; treat as a background/ongoing effort, not the lead move.

### Talk/CFP
**What it reveals:** same underlying content as the essay/demo, formatted for a conference audience and a live Q&A.
**IP-reveal check:** same boundary as ESSAY/DEMO — clears if the same recording/content discipline holds.
**Why it ranks last everywhere:** CFP lead times (months, typically) and travel/prep overhead make this the slowest-payoff artifact — directly conflicts with the "smallest legible slice for fastest real audience contact" discipline this plan is built around (gate-contract.md, ship-don't-polish rule). Keep on the roadmap, not the critical path.
**Goal stacking:** highest prestige ceiling for Recognition long-term, but sequenced after the faster artifacts prove the material resonates.

---

## 3. Lead Recommendation Per Goal

- **Career (highest urgency, active search in flight):** ship the **DEMO** first — record this week against Orderly/Kernel only, link from portfolio/resume. Follow with **PAPERS-RESPONSE** as the differentiator for research-adjacent infra roles. Use X/HN as the ongoing amplifier for both, not a separate project.
- **Venture/clients:** **OSS clean slice** is the lead artifact (credibility proof matching 2605.25665's own business model), but it is the slowest to de-risk and publish — sequence it as a background effort that starts now and lands after the career-priority artifacts ship. DEMO doubles as venture-facing sales material in the meantime.
- **Recognition/thought-leadership:** **PAPERS-RESPONSE** leads (rarest, highest-signal content), DEMO close second (most shareable), ESSAY provides the connective narrative between them. Talk/CFP stays on the roadmap for after the faster artifacts validate the material.

**Where goals stack (build once, serves multiple):** DEMO → career + venture + recognition (build first). PAPERS-RESPONSE → career + recognition. X/HN → amplifies everything, costs almost nothing, ship alongside every other artifact's release.

---

## 4. Papers-Response Assessment: Entry-Point Verdict

Task: 003-build-papers-response-and-sequence.md | Gate: VP-03
Built on: Sections 1-3 above (VP-02) + [[field-and-asset-notes.md]] (VP-01, arXiv 2605.25665 + 2606.04455 citations)

**Question:** is a field report responding to the arXiv papers the highest-credibility ENTRY move, or is the demo the better first move?

**Format options considered:**
- **Blog post** (informal narrative) — fastest to produce, widest general readership, weakest academic credibility; reads as opinion, not evidence.
- **arXiv-style writeup** (formal abstract, citations, related-work section) — highest credibility ceiling with a research audience, but slowest to produce and invites the deepest scrutiny of every claim — risk of overclaiming rigor the piece doesn't actually have (this is practitioner analysis, not peer review).
- **Annotated comparison** ("they propose X; here it is in production") — quotes/paraphrases the paper's specific proposed components side-by-side with the kernel's shipped equivalent (a gate-contract.md excerpt, an actual lessons.md entry, a task-builder BUILD/TEST split example). Medium effort, faster than an arXiv-style paper, more credible than a pure blog opinion because every claim is anchored to a specific external quote AND a specific internal artifact rather than an assertion.

**Verdict: annotated-comparison format — but the DEMO still ships first; the papers-response follows in the same sprint, not instead of it.**

Reasoning:
- The papers-response has a higher credibility *ceiling* (rare content, engages the literature directly) but a higher activation cost — it only lands with a reader who already cares about the arXiv framing, and needs a live audience-contact hook (X/HN, or the right research-adjacent recruiter seeing it) to travel at all. Published in isolation, it can sit unread indefinitely.
- The DEMO is legible with zero required context — watchable in under 60 seconds by a recruiter, hiring manager, prospective client, or HN reader alike — and it IS the evidence that makes the papers-response's central claim ("here it is in production") credible in the first place. Publishing the papers-response before the demo exists asks the reader to take that claim on faith.
- This does not contradict Section 3's DEMO-first career ranking — it sharpens *why* demo-first is correct even when judged from inside the papers-response angle itself: DEMO creates the audience contact and the evidence base; PAPERS-RESPONSE (annotated-comparison format) converts that contact into rare, differentiated content within the same sprint.

**What it can claim without leaking IP** (per field-and-asset-notes.md's asset table, Section 2):
- Eligible to cite: gate-contract-driven verification exists and runs; role-specialized routing (task-builder's BUILD/TEST split) exists and runs; self-improvement via structured failure classification is real, with a citable example pulled from lessons.md (e.g., the 2026-07-15 AST-semantics false-positive lesson — it demonstrates the loop without touching any client content); adversarial/independent re-validation exists (orchestrator re-validation pattern, lessons #37-#44).
- Not eligible, ever: any specific client engagement, any HMSA/healthcare-adjacent detail, any proprietary QA-platform architecture or internals, any RT-automation venture material, any usage metric that would imply client-scale deployment data. Every example must trace to the Kernel, Orderly, or the meta-factory tooling itself — never to this workspace's backlog/GTM content.
- Framing discipline: describe the kernel as "an independently-built, running instance of [the paper's] architecture pattern." Never imply the paper's authors influenced, reviewed, or endorsed the work — there is no such relationship; the convergence is independent and should be stated as such.

**Credibility-vs-exposure tradeoff verdict:** LOW exposure risk, HIGH credibility upside, conditional on discipline. The IP boundary is enforced by construction — only MIT/shareable rows in the asset table are eligible source material — so the real risk isn't leaking confidential material, it's *overclaiming* (implying scale, endorsement, or peer-review status that doesn't exist). **Verdict: proceed**, annotated-comparison format, gate every specific claim against the asset table before publishing, and explicitly disclose the piece as independent practitioner analysis, not peer-reviewed or author-endorsed.

---

## 5. 30/60/90-Day Sequence

Dated from **2026-07-22** (today).

### Week 1 shippable — by 2026-07-29
A **90-120 second screen-recorded clip** (not the full DEMO artifact, not the papers-response) showing one concrete cycle: task-builder decomposing a small goal → a gate failing → `/kernel/learn` firing → the loop self-correcting. Recorded against Orderly or the Kernel repo's own dev loop only, per Section 2's recording-discipline constraint (no `sr_dev_workspace` paths/content, no QA-platform or HMSA directory visible at any point). Post to X/LinkedIn with a 2-3 sentence caption, link the portfolio site.
**Effort: S** (1-2 focused sessions — script the cycle, record, trim, caption).
This is deliberately smaller than Section 1's full "DEMO" artifact — a teaser/proof-of-life clip chosen for "smallest legible slice, fastest real audience contact," not "most complete artifact."

### 30-day milestone — by 2026-08-21
- Full polished DEMO artifact (Section 1's version — complete governed-loop walkthrough, 5-8 min, voiceover or captions per layer). **Effort: M.**
- Portfolio site updated with the demo embedded + a one-paragraph "what is this" framing. **Effort: S.**
- PAPERS-RESPONSE first draft, annotated-comparison format (this section's verdict), citing 2605.25665 + 2606.04455 with specific side-by-sides against gate-contract.md / lessons.md / the task-builder BUILD-TEST split. **Effort: M.**

### 60-day milestone — by 2026-09-20
- PAPERS-RESPONSE published + distributed (X/HN, demo linked as evidence). **Effort: S** (distribution, on top of the 30-day draft).
- Begin ESSAY draft (harness-engineering + meta-factory connective narrative, Section 1). **Effort: L** (careful citation work — Fowler/Boeckeler framing + Spec Kit scale + the kernel).
- Begin OSS clean-slice de-risking (strip workspace-specific paths/state, per Section 1's process-gate note) — background effort, does not block career-track artifacts. **Effort: L, ongoing.**

### 90-day milestone — by 2026-10-20
- ESSAY published + distributed.
- OSS clean slice published if de-risking is complete, or status-reported honestly if still in progress — never force a rushed IP-boundary check to hit a date.
- Retrospective checkpoint: review which artifacts generated real audience contact (interview requests, client inquiries, meaningful engagement) vs. which didn't, and re-rank Section 1's table on real data rather than projected leverage. **Effort: S.**

### Named personal decisions the operator must make to start
1. **Real name vs. reserved/pseudonymous.** Publish under the operator's real name (recommended given the career branch's active-search urgency — portfolio/interview linkage needs real-name attribution) vs. a reserved/pseudonymous handle. Must be decided before Week 1 — the demo caption and portfolio link depend on it.
2. **Time budget.** How many focused hours/week are actually available for this track alongside the active job search (pipeline 029). The sequence above assumes roughly 3-5 hours/week; if less, the sequence should slip in date, not compress in scope — never cut the recording-discipline or IP-boundary review steps to save time.
3. **Primary goal weighting.** Confirm career stays the primary weighting (as Section 3 assumes, given active-search urgency) vs. re-weighting toward venture or recognition — this changes whether Week 1's clip is captioned toward recruiters/hiring managers or toward a broader technical/academic audience.
4. **Comfort with public exposure.** Explicit go/no-go on recording and publishing video content publicly (voice, and optionally face, on camera). If not comfortable with video, Week 1's shippable should be re-scoped to a written/annotated-screenshot walkthrough instead of a screen recording — this changes the effort estimate (S → S/M) and the "watchable" leverage claim in Section 1.
