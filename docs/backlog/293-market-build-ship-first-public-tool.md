# Ship the Governed Isagawa Kernel as a First Public Tool

## Status
Open — asset chosen (2026-07-23): the governed autonomous-build workflow. Blocked-soft on the reliability set (290/291) landing so "governed" is true, not aspirational.

## Priority
High — the visibility play made concrete. Benchmarking against 5 elite engineers (Kun Chen, Huntley, Gauthier/aider, Steinberger, Amp) gave one consistent verdict: deeper than all of them on governance/abstraction, behind all of them on **distribution**. Shipping this is the lever.

## The product (decided)
The public tool = the workflow the owner actually uses: **`/backlog "what I want"` → `/execute-pipeline` → autonomous governed build.** Positioned as **"ralph, governed"** — an autonomous coding loop that (unlike a raw while-loop) can't lie about finishing, write outside its lane, or clobber your repo. Name stays **Isagawa Kernel** ("ralph" is only the pitch, never the product name). One-liner: *"Describe the work, run one command, it builds it autonomously — governed."*

**Headline features = the reliability set** (this is why reliability-first IS ship-prep):
1. **Can't lie about finishing** — completion-truth (281 ✓ + 291).
2. **Can't write outside its lane** — output-sandbox hook (290).
3. **Can't clobber your repo** — isolation (292 ✓).

## Key finding — it's assemble + decouple, NOT publish-canonical
The workflow is **sr_dev-only**, not in `kernel-minimal`:
- `/backlog`, `/execute-pipeline`, `/autonomous-cycle` + `task-builder`/`execute-pipeline` skills — not in the canonical.
- `/backlog` needs the intent chain (`lib/attestation`) — not in the canonical.
- `task-builder` references the **factory/platforms in 7 files** — coupled to the private moat.

So shipping = curate + decouple, not just flip the canonical public. Every piece exists; it's cutting coupling, not new building.

## Requirements (the assemble plan)
1. **New public repo** `isagawa-kernel`; copy the governed loop + governance from the canonical (`run-task.sh`, session-start/anchor/complete, hooks, `lib/common.sh` verification primitives, tests).
2. **Port the workflow** `/backlog` + `/execute-pipeline` + `task-builder` — and **strip task-builder's 7 factory/platform references** so it is domain-agnostic (no HMSA/factory/platform vocab).
3. **Intent chain decision:** ship a lean version or drop it for v1 (backlog can work without Sigstore/Rekor attestation to start).
4. **Cut** `/fix`, `/learn`, `/reset` (owner doesn't use them) + keep the factory/spec-generation/platforms **private** (the moat).
5. **README** translating insider vocab (anchor, gates, domain-setup) → "describe → autonomous build"; five-minute quickstart; one clear job.
6. **Demo** (gif/asciinema): `/execute-pipeline` building something, and a guardrail **catching a false-complete** a raw loop would ship (the shareable moment). Then **clean-room sweep → publish public** + a launch post (ties [[282-...visibility-strategy]]).

## References
- Benchmark findings 2026-07-23 (Kun + Huntley/Gauthier/Steinberger/Amp): deeper on governance, behind on distribution → ship.
- Product shape defined via render boards 2026-07-23. Substrate: reliability set (290/291) + 281/292 (done).
- Owner note: "what I use the most is the backlog and execute pipeline; the latter kicks off run-task.sh."

## Task Builder Input
- **Deliverable:** One public `isagawa-kernel` repo = the governed autonomous-build workflow (backlog + execute-pipeline + governed loop + guardrails), decoupled from the factory/platforms, `/fix /learn /reset` cut, with README + demo, clean-room verified + a launch post.
- **Location:** new-repo:D:\my_ai_projects\isagawa-kernel-public
- **Scope:** BUILD
- **Constraints:** Assemble + DECOUPLE (strip the 7 factory/platform refs in task-builder). Clean-room (no client/moat leakage). Distribution-first — ship the smallest thing that works. Best AFTER 290/291 land so the 3 headline features are all real.
