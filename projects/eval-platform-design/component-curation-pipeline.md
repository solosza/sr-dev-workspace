# Component Curation Pipeline

The platform's core moat is its self-extending component library. When a user submits an artifact for evaluation, the agent checks existing components. If a required component doesn't exist, the agent builds it from `_reference/` patterns. That new component becomes a candidate for the shared library — every submission makes the platform smarter for the next user.

## Flywheel Architecture

The growth mechanism is automated contribution with human quality control:

```
User submission requires missing component
    → Agent builds component from _reference/ patterns
    → Component enters automated quality gate pipeline (4 gates)
    → Passes automated gates → enters human review queue
    → Approved → merges to staging → integration test → merges to main library
    → Next user benefits from the new component
    → Platform intelligence compounds
```

This is analogous to how Hugging Face Hub grew to 2.4M+ models through community contributions. The key difference: contributions are agent-generated rather than manual, removing the friction that slows community-driven registries. Every evaluation job potentially adds to the library without any user effort.

## Automated Quality Gates

Every dynamically-created component must pass all 4 gates before entering human review. Estimated overall pass rate: 60-70%. The remaining 30-40% either fail tests (fixable by the agent in a retry loop) or are flagged as duplicates.

### Gate 1: Pattern Conformance

Automated diff against `_reference/` template. Verifies:
- File structure matches reference pattern
- Required fields and exports present
- Naming conventions followed

Rejects components that deviate from established patterns. This is a structural check — does the component look right?

### Gate 2: Test Pass

Component must pass the same test suite that existing components pass:
- **Metrics:** Does the metric compute correctly on known inputs?
- **Validators:** Does the validator produce expected pass/fail on reference configs?
- **Test patterns:** Does the generated test execute and produce a result?

This is a functional check — does the component work?

### Gate 3: Code Quality

Automated linting and complexity analysis:
- Linting (ruff for Python, eslint for TypeScript)
- No hardcoded values, no API keys, no user-specific data
- Complexity checks — no 500-line monolith components
- Type hints present (Python) or typed (TypeScript)

This is a hygiene check — is the component maintainable?

### Gate 4: Deduplication

Semantic similarity check against existing library components:
- Embedding similarity threshold: 0.85
- Components above threshold flagged as potential duplicates
- Duplicates forwarded to human review for decision: merge, keep both, or discard

This prevents library bloat from near-duplicate components that do the same thing with different names.

## Human Review Workflow

Automated gates catch structural issues. Human review catches semantic and strategic issues — is this component genuinely useful? Does it overlap with something we already have?

### Review Queue Design

Components that pass all 4 automated gates enter the review queue with full context:

| Context Provided | Purpose |
|-----------------|---------|
| Source submission (anonymized) | What triggered the component creation |
| Which `_reference/` pattern was used | Template conformance verification |
| Test results | Functional correctness evidence |
| Similarity report (near-duplicates) | Deduplication decision support |

### Reviewer Actions

| Action | Effect |
|--------|--------|
| **Approve** | Component merges to staging → automated integration test → merges to main library |
| **Request changes** | Returns to agent for modification and re-submission through gates |
| **Reject** | Discard with logged reason (feeds back into pattern improvement) |
| **Merge with existing** | Combine with a near-duplicate component already in the library |

### Reviewer Scaling

| Phase | Reviewer Model |
|-------|---------------|
| **MVP** | Internal team reviews all components |
| **Growth** | Community reviewers with reputation scores (like npm maintainers) |
| **Scale** | AI-assisted review — separate LLM evaluates and provides confidence score, human final approval |

## Conflict Resolution

Concurrent users may trigger creation of similar components simultaneously.

**Approach: Optimistic concurrency (no locking)**

Both agents build their component independently. First to pass automated gates enters the review queue. Second component flagged as "potential duplicate" — reviewer decides whether to merge, keep both, or discard.

Why not locking: locking introduces contention and latency. If User A's job must wait for User B's component to be reviewed before building, the UX degrades. The cost of reviewing an occasional duplicate is lower than the cost of job queue blocking.

**Merge conflict resolution:** The component library uses Git-based versioning. Components are atomic files — merge conflicts are rare since each component is self-contained. If a structural conflict occurs (two components modify the same shared utility), the reviewer manually resolves.

## Versioning Strategy

### Library Versioning (Semantic)

| Change Type | Version Bump | Example |
|------------|-------------|---------|
| Breaking changes to component interfaces | Major | Rare — `_reference/` patterns define interfaces |
| New components added | Minor | Most common — flywheel output |
| Bug fixes to existing components | Patch | Agent-generated fix or human correction |

### Per-Component Versioning

Each component carries a version field in its metadata. Breaking changes to a component create a new version; the old version is preserved. Container images pin to a specific library version — no surprise breakage mid-run.

### Rollback

Git-based library means any version is recoverable. If a merged component causes issues, revert the commit. Affected container images are rebuilt automatically.

## Scaling Plan

### MVP (0-100 submissions/month)

- ~30 components/month enter review (30% of submissions generate new components)
- ~5 minutes per review = 2.5 hours/month
- Internal team absorbs — no dedicated reviewer needed

### Growth (100-1,000 submissions/month)

- ~300 components/month enter review
- Without AI: ~25 hours/month (0.6 FTE, $3,000-5,000/month)
- With AI-assisted review: ~2 minutes per component → 10 hours/month

### Scale (1,000-10,000 submissions/month)

- ~3,000 components/month enter review
- Without AI: ~250 hours/month (1.5 FTE)
- With AI assist: ~100 hours/month (0.6 FTE, $5,000-10,000/month)
- Auto-approve components with >95% AI confidence score

## Curation Bottleneck Mitigation

This is the make-or-break operational challenge. If curation falls behind: review queue grows → new components don't reach users → flywheel stalls → quality standards drop to clear backlog → bad components pollute library → user trust erodes → reviewers burn out.

**Five mitigation strategies:**

1. **Strict automated gates** — reject more at the gate, less reaches human review
2. **AI-assisted review** — LLM evaluates component, provides confidence score and recommendation
3. **Tiered review** — auto-approve high-confidence (>95%), human-review medium confidence (70-95%), auto-reject low confidence (<70%)
4. **Community incentives** — reputation system, early access to features, recognition for top reviewers
5. **Controlled growth** — intentionally limit submissions per user to control queue growth until automation matures

**Comparison to open source ecosystems:** npm processes ~2,000 new packages/day with mostly automated checks. PyPI relies on namespace reservation and automated malware scanning. Our advantage: components are generated from `_reference/` patterns, making automated quality checking more reliable than for arbitrary human-submitted code.

## References

- `projects/eval-web-app-research/05-component-flywheel-curation.md` — flywheel cycle, automated quality gates, human review workflow, conflict resolution, versioning strategy, operational cost analysis, curation bottleneck mitigation
- `projects/eval-platform-design/vertical-plugin-system.md` — vertical-specific component requirements
- `projects/eval-platform-design/execution-pipeline.md` — container lifecycle that produces components
