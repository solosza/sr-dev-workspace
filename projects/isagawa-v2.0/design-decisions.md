# Isagawa v2.0 — Design Decisions Log

**Status:** living capture (pre-thesis) · **Date:** 2026-07-28

Preserves the reasoning + decisions from the v2.0 design sessions before they compact, so either
build path can pick them up later. **This is not the thesis** — it is the scaffolding we build the
thesis *from*.

**Claim discipline (dogfooded here):** every item is tagged `[DECIDED]` / `[OPEN]` / `[HYPOTHESIS]`.
We don't let prose become canonical just because it's written down — the same rule the Validate gate
(§4) will enforce on the eventual corpus. If it's not proven, it's marked.

**Source:** the OpenAI "factory" chat at `.claude/docs/isagawa_co/isagawa v.2.0/my_long_factory_chat_openai.md`
+ the Claude design session that refined it (2026-07-28).

---

## 0. Frame

- `[DECIDED]` **Customer Zero = Isagawa itself.** The first build target is a real internal
  bottleneck, run through the loop. No external customer needed to start.
- `[DECIDED]` **Go-to-market (later): service-first → productize.** Deliver operating-model design as
  a service (kernel behind the curtain), extract the product from repeated delivery.
- `[HYPOTHESIS]` **One compiler generalizes across domains** (H1–H8 in the source chat). Unproven;
  it earns its way in one instance at a time. Do not market as fact.

## 1. The invariant loop

- `[DECIDED]` `Discover → Compile → Execute → Artifacts → Evidence → ↺`, three-phase:
  - **DISCOVER** — purpose · bottleneck · evidence · capability-evaluation
  - **COMPILE** — harness · operating model · workflows
  - **EXECUTE** — run workflows · produce artifacts · collect evidence
- `[DECIDED]` **Discover / Compile / Execute is the external verb-set** (what a user experiences).
  **Learn is internal** — a platform property, not a fourth user step.

## 2. Structure — harness vs workflow is a false binary

- `[DECIDED]` Everything governed is a **harness** (a node: identity, contract, state, lessons,
  authority). A **workflow** is not a rival kind of thing — it is the *wiring* (edges) between harnesses.
- `[DECIDED]` The real cut is **index-harness vs payload-harness**, and it IS the kernel's own
  tiered-indexing law applied to execution units:
  `coordinator : department  ::  index : payload  ::  routing-node : artifact-node`
  - **index-harness** (coordinator / orchestrator): holds routing + pointers, owns **no** artifact.
    Its output is a routing table + a blocker list. Nothing else.
  - **payload-harness** (capability): owns the actual artifact.
- `[DECIDED]` **Extraction rule = decomposition rule.** Split a capability into sub-capabilities by the
  same trigger you extract an index section — only when it grows too big. (Guards against premature
  departmentalization.)
- `[DECIDED]` **COMPILE emits:** operating model = capability graph (nodes + edges); harnesses =
  payload nodes; coordinator = index node; workflows = edges.

## 3. Invariants adopted from the source chat

- `[DECIDED]` **Capability owns work; executor performs it.** Executor (human / LLM / script / API) is
  replaceable; executor identity ≠ capability identity.
- `[DECIDED]` **Runtime never rewrites governance.** Runtime emits telemetry / lessons / proposals;
  changes to authority, gates, or purpose go through review + recompilation.
- `[DECIDED]` **Two evidence loops, distinct authority:**
  - *operational* — fast, autonomous, the harness gets better at its job
  - *architectural* — slow, HITL-gated, changes the factory / model / corpus, **cannot self-rewrite
    governance**. Collapsing the two is the governance-recursion risk.
- `[DECIDED]` **Ambiguity-triggered HITL.** Human review fires on ambiguity that is *material* AND
  *not authoritatively resolvable* — at any layer, not at fixed checkpoints. (The Vibe-Coder
  interaction pattern, generalized.)
- `[DECIDED]` **Self-hosting.** Isagawa designs itself through the same governed loop it offers every
  domain — no separate informal process for its own architecture. This is the kernel motto
  (self-building / self-improving / safety-first) extended from runtime to the whole system.

## 4. The first target — the factory, extracted not guessed

- `[DECIDED]` **The real first bottleneck is the FACTORY** (the thing that compiles harnesses), because
  every harness shares the loop-model. The leverage is build-once-emit-many.
- `[DECIDED]` **The factory is EXTRACTED, not guessed.** The v2.0 factory = the *generalization* of the
  existing v1 factory (`domain-setup` + `task-builder` + `execute-pipeline` + `prod-test`). We are rich
  in **v1** instances (deal engine, basketball sim, QA platform, research pipelines) but have **zero
  v2-native** ones.
- `[DECIDED]` **The factory and the first v2 harness CO-EMERGE.** Build the reference harness *through*
  the (extended) factory; every gap the factory can't fill = the factory's own build work. The factory
  is built **by** the loop — it is itself a harness, not an exception to the loop.
- `[DECIDED]` **Reference instance #1 = the canonical-doc harness** (produces the thesis / RFC / ADR
  corpus). Chosen because the corpus is the current real bottleneck AND it forces the honesty gate early.
- `[DECIDED]` **Doc-harness shape:** one coordinator (index) wiring three payload-harnesses —
  **Research / Author / Validate** — which are NOT doc-specific: they are the reusable core every
  future domain reuses.
- `[DECIDED]` **Validate gate / claim-discipline** (because prose is the least self-verifying artifact —
  it can't fail a test):
  - claim-register: every assertion tagged `prior-art` / `synthesis` / `hypothesis` / `demonstrated`
  - every hypothesis carries a falsification criterion
  - citations are fetched + verified, never generated
- `[DECIDED]` **capability-evaluation (in DISCOVER) is the load-bearing make-vs-reuse-vs-adapt gate** —
  it is what makes the output a capability GRAPH (reuse existing nodes) instead of a tree (rebuild every
  time). The anti-duplication mechanism.

## 4.1 Factory architecture — the v1 parts already exist (extracted, not invented)

The factory's COMPILE stage is **already implemented in v1, scoped to commands.** Generalize it; don't reinvent it.

- `[DECIDED]` **The v1 compile pair.** `/design` (`.claude/docs/design/design-command/`) = the
  Discovery+Design capability (intent → interview/HITL → a spec that passes an input-contract).
  `/build-command` (`.claude/docs/design/build-command/`) = the Build capability (spec → mechanically
  scaffold structure; it calls itself *"the loop that builds other loops"*). Together = Design→Build,
  the creative/mechanical separation.
- `[DECIDED]` **They already encode our invariants:** spec-is-source-of-truth ("design doc wins on
  conflict") = runtime≠governance; "flag missing, don't fill" = don't-guess/escalate; the 7-section
  **input-contract** = the gate between design and build; "loop that builds loops" = self-hosting meta-harness.
- `[DECIDED]` **The factory = generalize the pair + a thin coordinator.** Four payload-capabilities in
  order: `evaluate → design → build → validate`, wired by an index-harness coordinator.
  - `evaluate` (NEW) — the capability-evaluation reuse gate (§4). Consulted first; makes output a graph.
  - `design` — generalize `/design`.
  - `build` — generalize `/build-command`.
  - `validate` — the gate; **structural** for commands, **semantic** for docs (claim-register /
    falsification / citations). Pluggable per scope.
  - **coordinator** — generalize `execute-pipeline`. **Thin:** routes, tracks, closes the evidence loop;
    **never designs or builds** (stays an index).
- `[DECIDED]` **"Generalize" = make three things pluggable-per-scope, held as DATA (a `scope → contract`
  map), not baked into the coordinator:** (1) the output contract (command-skill-pattern / domain-pack /
  doc-corpus-pattern), (2) the validate gate (structural vs semantic), (3) the design completeness contract.
- `[DECIDED]` **The one genuinely-new orchestration behavior:** the evidence-close — after build, collect
  "did it work?" and route to operational vs architectural learning (§3). v1 `execute-pipeline` stops at
  "pipeline complete."
- `[DECIDED]` **Scope instances to generalize FROM:** `/design`+`/build-command` (command scope),
  `domain-setup` (domain scope). The doc-harness adds a new scope (`doc-corpus`), which *proves* the
  pluggability. The 5 deltas get filled by emitting the doc-harness — friction, not abstract design.
- `[CAVEAT]` `/design` and `/build-command` are **draft** design docs (v1.0, 2026-06-20). Verify they're
  actually built/working before relying on them as tools (vs. only as the pattern to generalize).

## 5. Guardrails / discipline

- `[DECIDED]` **5–10 hour rule.** No harness/capability exists until it replaces real hours. Build from
  felt bottlenecks, never from an org chart.
- `[DECIDED]` **Keep the graph flat.** Departments are a *view* over capabilities, not a build target.
  No sub-agent org-chart cosplay until friction forces a split.
- `[DECIDED]` **Scope discipline.** Narrow the circle; widen it only with proof. Don't assert the
  horizontal claim as fact.
- `[DECIDED]` **Proof is a working artifact or a paying customer — a corpus is not evidence.**
  (Dogfooded: this doc is *tagged*, not asserted.)

## 6. Build path (both apply — this is the point)

- `[DECIDED]` These decisions describe **what** to build, not **how**, so either build path consumes them:
  - `backlog → execute-pipeline` (the loop) for a harness that fits task-builder decomposition, OR
  - the **domain-spec factory** for a harness that is a full governed domain.
  Pick per harness, whichever is more applicable. The decisions above are the shared input to either.

## 7. Open / not yet decided

- `[DECIDED → §4.1]` **The v1→v2 factory delta is now specified** — `evaluate` reuse-gate +
  semantic-`validate` + pluggable per-scope contracts + evidence-close, over a generalized
  `execute-pipeline` coordinator. What remains is *executing* the generalization, proven by emitting the
  doc-harness.
- `[OPEN — in progress]` **v2.0 repo structure.** Working thesis (2026-07-28): the operating model is
  itself the root harness; the platform (kernel substrate + factory + reusable capabilities) gets its own
  repo whose boundary enforces the domain-independent-core invariant; domains (deal engine, RT, …) stay in
  their own repos and depend on it. See §8.
- `[OPEN]` **The thesis / RFC / ADR corpus itself** (RFC-000 …). The eventual deliverable, produced by
  the doc-harness once it exists.
- `[DECIDED]` **Methodology name = Invariant Operating Model (IOM).** The company stays **Isagawa**; do
  **not** rename it. IOM names the *methodology* (the invariant `Discover → Compile → Execute` + the
  governance invariants that hold while everything else changes). Structural component names (Systems
  Compiler / Capability Factory / harness / coordinator) remain `[OPEN]`.

## 8. Repo & boundary architecture

### 8.1 The platform repo (the seed)

- `[DECIDED]` **One private platform repo = the IOM engine.** Composition:
  - kernel-minimal (hooks + state + session-start/anchor/learn/complete/fix + CLAUDE.md + protocol),
    **including domain-setup**
  - `backlog` (+ `lib/attestation/intent.py`)
  - `execute-pipeline` (+ `task-builder` + `run-task.sh`)
  - generalized `/design` + `/build-command` (+ `command-skill-pattern` + `tiered-index-architecture` + contracts)
  - the unifying **factory** (`evaluate` + semantic-`validate` + `scope→contract` map + evidence-close +
    the generalized coordinator)
- `[DECIDED]` **execute-pipeline, domain-setup, and /design+/build-command are the factory's v1
  instances**, not peers of it: `domain-setup` = domain scope, `/design`+`/build-command` = command
  scope, `execute-pipeline` = the coordinator. The factory is their **unification** (one coordinator +
  pluggable scope-contracts), which subsumes them over time.

### 8.2 Bootstrap

- `[DECIDED]` **Seed hand-built once; self-hosting thereafter.** The factory can't compile the first
  factory from nothing (bootstrap paradox) — the platform seed is hand-assembled by extracting the v1
  pieces into the repo. After that, every future version is a spec the factory builds. (GCC's first
  compiler wasn't written in C.)
- `[DECIDED]` **The platform ships pre-governed** (its own protocol + hooks committed — stable, not
  re-discovered each clone). `domain-setup` is the tool run to **wrap governance around each new domain
  instantiated**, not to re-bootstrap the platform.

### 8.3 Distribution & IP boundary (the moat)

- `[DECIDED]` **The v2 platform repo is PRIVATE and NOT distributed.** It is Isagawa's workspace/engine
  and its core IP / competitive advantage. The factory (the compiler) never leaves it.
- `[DECIDED]` **Clients' operating models are compiled into their OWN repos, OUTSIDE the platform repo.**
  The output (client repo) is the deliverable; the engine stays home. This is the service→product flow:
  every engagement = (privately) clone + run the engine → deliver the client's compiled operating model.
- `[DECIDED]` **The repo boundary = the IP boundary = the domain-independent-core invariant, physically
  enforced.** Platform repo = domain-independent core (private); client repos = domain instances
  (delivered). Domain-specifics never contaminate the core; the core (factory) never ships to the client.
- `[DECIDED]` **Delivery = the runtime-ships model.** A client repo carries their compiled operating
  model (harnesses + workflows + custom primitives) + a **runtime-only kernel** (enforcement substrate:
  hooks / anchor / learn / state) — and **never the factory or its build-time tooling** (`domain-setup`,
  `/design`, `/build-command`, `backlog`, `execute-pipeline`, `task-builder`).
- `[DECIDED]` **Two "minimals," don't confuse them.** *platform-minimal* (the engine repo, §8.1)
  INCLUDES the build tools; *client-minimal* (shipped) is runtime-only, factory-stripped. The client ship
  must **exclude `domain-setup`** — it is itself a factory instance.
- `[DECIDED]` **The two-loop split crosses the service boundary.** The client's runtime handles the
  OPERATIONAL loop (lessons within existing harnesses); ARCHITECTURAL change (new harnesses, model
  evolution) has no compiler client-side, so it routes back to Isagawa's factory — the retention mechanism.
- `[NOTE]` SaaS-hosted (nothing ships) remains the strongest-protection option for later; runtime-ships
  is the default delivery.
- `[NOTE]` Secrecy alone is not the moat (cf. [[alaindustries-competitive-positioning]]): the advantage
  is the private engine **plus** compounding refinement via Customer Zero (Isagawa itself) + real client
  evidence + operational know-how. The boundary protects the engine; the dogfooding compounds it.

## 9. Build sequence (how we execute)

- `[DECIDED]` **Sequence:** build doc-harness (instance one) → factory crystallizes as the reusable
  residue → extract `{seed + factory}` into the private platform repo → bootstrap governance.
- `[DECIDED]` **Where:** build in the sr_dev workspace (already-governed env with all v1 pieces), then
  extract. Guard the §8.3 boundary by hand meanwhile — generalize ONLY domain-independent pieces; never
  let the factory reference a domain.
- `[DECIDED]` **Don't over-build the factory for instance one.** Build just enough to produce the
  doc-harness; the pluggable multi-scope factory is the EXTRACTED residue, not a prerequisite.

### 9.1 Instance-one specifics to nail (resolve while building — co-emergence)

- `[OPEN]` **Doc-harness shape.** Confirm it decomposes into command-shaped capabilities (Research /
  Author / Validate as skills + an `execute-pipeline` coordinator) so the EXISTING v1 loop bootstraps
  most of it — leaving only two genuinely-new parts: the semantic-Validate gate + the doc output contract.
- `[OPEN]` **Build the semantic Validate gate FIRST, not last.** claim-tag enforcement + citation
  fetch/verify. If Research+Author ship before Validate, you generate a corpus you can't yet check
  (backwards). This gate is what separates a proof from a plausible-prose generator — it is the hard,
  risky deliverable of instance one.
- `[OPEN]` **Define instance-one INPUT + DONE.** Input = this design-decisions doc + the source chat →
  RFC-000. Done = RFC-000 produced AND passes the claim-gate (every claim tagged; every hypothesis has a
  falsification criterion; every citation resolves). Without a done-criterion, "prose can't fail a test" bites.
- `[NOTE]` `evaluate` (reuse gate) is trivially moot at instance one (empty capability library → always
  "build new"); it earns its value at instance two+.

## 10. Build model: prose-primary, self-similar, hand-bootstrapped

- `[DECIDED]` **The platform is prose-primary (LLM-orchestrated).** Corrects a drift. The LLM is the
  orchestrator/executor. Capabilities are PROSE (commands / skills / references). Contracts are DATA
  (JSON). **Code = hooks only** (mechanical enforcement). This is how the whole repo is already built;
  the factory follows it, not generic scripting.
- `[DECIDED]` **One primitive, one build-machinery, recursive (self-similar).** The single primitive is a
  command/skill (prose + a contract; a hook only where enforcement is mechanical). The single machinery
  that produces it is the loop (`/kernel/backlog` → `/kernel/execute-pipeline` → task-builder → design/build
  → run-task.sh). The factory's four steps, a harness, a workflow, and the thing that builds them are ALL
  that same primitive. **No new abstraction layer** — a new layer would break the self-similarity.
- `[DECIDED]` **"Identify / generalize my existing assets" = the `evaluate` step on our own assets**, not a
  layer above. Inventory kernel · spec-factory · design/build · execute-pipeline · domain-setup ·
  tiered-index-architecture; per asset decide reuse / adapt / generalize. That catalog IS the factory's
  parts list. The loop evaluating its own parts is the self-hosting.
- `[DECIDED]` **Generalize per capability as you build, not in one big upfront pass** (the upfront pass is
  the guess-the-factory trap). Build one capability; where the machinery can't handle it, that gap is the
  generalization work, surfaced by real friction.
- `[DECIDED]` **`validate` is a SKILL, not a script.** The LLM is the validator: it reads a claim, decides
  the authoritative corpus, checks reality via its tools, judges, and EMITS A CONTRACT (a claim-register:
  per claim `{tag, verdict, source, evidence}`). That contract is **gated for correctness** (a mechanical
  check / hook — the one place code belongs). Same shape as `/design` → doc → gated by `/build-command`'s
  input-contract. Token spend is warranted here (verifying reality is the value); spend in proportion to
  how checkable / load-bearing a claim is.
- `[SUPERSEDED]` `projects/isagawa-v2.0/validate/validate.py` was the wrong artifact (a generic Python
  validator). Superseded by the `validate` skill + claim-register contract; its reference-resolution logic
  may fold into the optional gate hook. Kept as scaffolding for now, not the validator.
- `[DECIDED]` **The factory (the bootstrap) is HAND-BUILT manually, NOT run through backlog/execute-pipeline.**
  You cannot use the loop to build the loop from nothing (bootstrap paradox, §8.2). Hand-build the factory
  live and fix blockers in place as they arise. Once the factory exists, future harnesses (and future
  factory changes) go through the loop.

## 11. The capability library (accumulating private asset)

- `[DECIDED]` **Every generalized contract is KEPT and accumulates into a private capability library** —
  not just validate-contracts, but ANY generalized contract (scope-contracts, capability specs, the
  reusable commands/skills themselves). The library is the **compounding moat**: every engagement leaves
  the engine more capable for the next.
- `[DECIDED]` **A new client usually REUSES or ADAPTS an existing contract, not builds fresh** (the
  `evaluate` gate: reuse / adapt / build-new). Reuse dominates as the library grows — you build LESS as
  it gets bigger. A genuinely-new client contract, once built, becomes a reusable asset: **client work
  FEEDS the library** (the Customer-Zero + client-evidence compounding of §8.3).
- `[DECIDED]` **The library is PRIVATE (§8.3).** It is the IP. Clients get their compiled output +
  runtime, never the contract library. "Scope increases" = the *private engine* gets more capable.
- `[DECIDED]` **Curate as a graph, not a pile.** Reuse-first (`evaluate`) + periodic **consolidation**:
  when N client contracts are variations of one thing, generalize them into one parameterized contract
  (many specifics → one general + params) + tiered-index the library itself. Otherwise scope-increase
  becomes scope-sprawl (the graph-explosion risk).
- `[DECIDED]` **Contract format = JSON (data); judgment = prose.** Corrects a drift (scope contracts were
  briefly `.md`). A contract is DATA the gate checks (schemas, enums, thresholds, required fields, pass
  conditions) → JSON, per command-skill-pattern Layer 5. The reasoning it triggers (how to unitize,
  determine authority, judge) is PROSE in the skill's `steps/`. Structural checks = hard gate (hook reads
  JSON); semantic checks = soft gate (LLM follows steps, fills the register the JSON then validates).

## 12. Capability conventions (discovered while building)

- `[DECIDED]` **Every capability begins with DISCOVER** — characterize the input and locate WHERE the
  relevant target lives (the scope/contract for an artifact; where candidate capabilities live for a
  need). Do NOT hardcode the location. This is the loop's DISCOVER (§1) at capability scope, self-similar.
- `[DECIDED]` **Discover is a shared PRIMITIVE, not copy-pasted.** `.claude/skills/discover/` — a skill any
  capability invokes as its step-01 (the `reference-scanner` "Step 0" pattern). Extracted on its 2nd use
  (validate + evaluate) per §11 consolidate-on-repeat; both step-01 files now INVOKE it.
- `[DECIDED]` **Discover uses ambiguity-triggered HITL** (§3): material + unresolvable → one bounded
  question; else best reading, recorded.
- `[DECIDED]` **validate kept distinct from gap-check** (the evaluate dogfood surfaced the overlap):
  validate verifies claims against an EXTERNAL authority and emits a gated register; gap-check checks
  INTERNAL consistency / coverage. Adjacent shells, different jobs.
- `[NOTE]` The evaluate dogfood corrected a stale belief: `design-command` and `build-command` are BUILT
  skills (`.claude/skills/`), not just draft design docs.
- `[DECIDED]` **Factory capabilities built so far** (hand-bootstrap): `discover` (primitive), `validate`
  (+ `validate-gate.py` hook), `evaluate`, `coordinator` (thin router, copy-tailored from execute-pipeline).
  Remaining: v2 `design`/`build` (adapt by-copy from design/build-command).

## 13. v1 -> v2 method: adapt-by-copy, never mutate the working kernel

- `[DECIDED]` **Generalize v1 assets by COPY-tailor, not in-place refactor.** The workspace's v1 kernel
  (`execute-pipeline`, `design`/`build-command`, `domain-setup`) is LOAD-BEARING; mutating it to build v2
  risks breaking the repo's own loop, for no benefit (the v2 asset lives in a different repo anyway). The
  v2 platform assets are COPIES tailored for the platform; the workspace originals keep running. The copies
  ARE the extraction taking shape (§8/§9). Encoded in `evaluate` as `adapt_mode: by-copy` (default for
  load-bearing targets).
- `[DECIDED]` **Per-asset decisions (the `evaluate` output for the v1 factory):**
  - `execute-pipeline` → adapt by-copy → the new `coordinator` (thin router). **Built.**
  - `design-command` / `build-command` → adapt by-copy → v2 `design`/`build` (scope-pluggable output). Pending.
  - `domain-setup` → **reuse as-is** (the bootstrap tool; ships unchanged, §8.2).
- `[DECIDED]` **"Copy-tailor" = reference + build lean**, not clone-then-gut. The coordinator is far
  thinner than `execute-pipeline`; use the original as the pattern reference and build the small tailored version.
