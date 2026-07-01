# Design Decisions: DeepEval L3 Testing

## Status
NEW

## Resolved Decisions

### DD-001: L3 Detection Method
**Decision:** Auto-detect via contracts/ folder existence
**Rationale:** Contracts are the bridge between skill definitions and evaluation. If a skill has contracts/, it has declared expected behaviors that can be evaluated. No flags or config needed.
**Alternatives rejected:**
- `--l3-deepeval` flag: requires user to remember to pass it
- Config file: extra file to maintain, easy to forget

### DD-002: Pipeline Type for Kernel Commands
**Decision:** Agent pipeline (ToolCorrectness + TaskCompletion + custom GEval)
**Rationale:** Kernel commands use tools (Read, Write, Edit, Bash, openpyxl), follow multi-step protocols, and produce structured output. This matches DeepEval's Agent pipeline type exactly. GEval adds protocol faithfulness which Agent pipeline doesn't cover natively.

### DD-003: Golden Dataset Source
**Decision:** Mechanical translation from contract JSONs, enriched with real TC data when available
**Rationale:** Contracts already define expected behaviors declaratively. Translation eliminates manual fixture creation. Real TC data from xlsx makes goldens realistic. Synthetic fallback ensures minimum 20 goldens even without real data.

### DD-004: Agent Output Capture
**Decision:** Hybrid — state diff for correctness metrics, agent trace for faithfulness metrics
**Rationale:** State diff (before/after files) is reliable and deterministic — good for ToolCorrectness and TaskCompletion. Agent trace (reasoning text) is needed for GEval faithfulness ("did the agent mention checking the exclusion list?"). Both are captured, different metrics use different sources.

### DD-005: Score Persistence Location
**Decision:** Source repo's eval/results/ (not test repo)
**Rationale:** Test repo gets recreated each prod-test run. Score history must persist across runs to enable progression tracking. Source repo is the right home — scores describe the source's quality.

### DD-006: Composition vs. Monolith
**Decision:** Compose existing systems (prod-test + platform-deepeval), don't rebuild
**Rationale:** Both systems are mature. prod-test handles isolation, task generation, execution. platform-deepeval handles metric selection, eval suite generation, scoring. The gap is composition — Step 6 L3 needs to wire them together. Building from scratch would duplicate working code.

## Open Decisions

### OD-001: Score History Format
**Question:** JSON file vs. SQLite vs. JSONL (append-only)?
**Considerations:**
- JSON: simple, readable, but requires full-file rewrite each pass
- SQLite: queryable, handles concurrent access, but adds dependency
- JSONL: append-only like actions.jsonl, but harder to read progression
**Leaning:** JSON for now (simple, matches existing patterns). Migrate to SQLite if scale requires it.

### OD-002: Minimum Golden Count Strategy
**Question:** How to reach 20 goldens when a contract has few rules?
**Options:**
- Generate variations (different member counts, edge dates, boundary conditions)
- Combine goldens across contracts for the same command
- Lower the minimum for small contracts
**Leaning:** Generate variations. Each rule gets positive + negative + 2-3 edge cases. For a contract with 3 rules: 3 × (2 + 3) = 15, need 5 more variations.

### OD-003: GEval Criteria Authoring
**Question:** Auto-generate GEval criteria from contract rules, or hand-write them?
**Considerations:**
- Auto-generate: mechanical, consistent, but may miss nuance
- Hand-write: higher quality, but doesn't scale
- Hybrid: auto-generate baseline, allow manual override
**Leaning:** Auto-generate from `soft_validation_rules[].description` + `.check` fields. Allow manual `geval_criteria` field in contract JSON for overrides.

### OD-004: Test Repo Cleanup
**Question:** Delete test repo after L3 scores are captured, or preserve for debugging?
**Considerations:**
- Delete: clean, no disk bloat
- Preserve: enables debugging failed evaluations
- Preserve with TTL: auto-delete after N days
**Leaning:** Preserve latest test repo only. Delete previous on next run.
