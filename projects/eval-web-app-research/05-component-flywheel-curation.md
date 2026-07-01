# Component Flywheel and Curation

## The Growth Mechanism

The platform's core moat is the growing component library. When a user submits an artifact for evaluation, the agent checks existing components in the library. If a required component doesn't exist, the agent builds it from `_reference/` patterns. This new component is then a candidate for the shared library.

**Flywheel cycle:**
```
User submission requires new component
    → Agent builds component from _reference/ patterns
    → Component passes automated quality gates
    → Component enters human review queue
    → Approved component merges to master library
    → Next user benefits from the new component
    → Platform intelligence compounds
```

This is analogous to how Hugging Face Hub grew from community contributions: the Hub hosts 2.4M+ models because every contributor makes the platform more valuable for the next user. The key difference is that our contributions are automated (agent-generated) rather than manual, which removes the friction that slows community-driven registries.

## Automated Quality Gates

Every dynamically-created component must pass automated gates before entering the human review queue:

### Gate 1: Pattern Conformance
- Component follows `_reference/` patterns (file structure, naming, exports)
- Automated check: diff against reference template, verify required fields present
- Rejects components that deviate from established patterns

### Gate 2: Test Pass
- Component must pass the same test suite that existing components pass
- For metrics: does the metric compute correctly on known inputs?
- For validators: does the validator produce expected pass/fail on reference configs?
- For test patterns: does the generated test execute and produce a result?

### Gate 3: Code Quality
- Linting (ruff/eslint depending on language)
- No hardcoded values, no API keys, no user-specific data
- Complexity checks (no 500-line monolith components)
- Type hints present (Python) or typed (TypeScript)

### Gate 4: Deduplication
- Semantic similarity check against existing components
- Prevents library bloat from near-duplicate components
- Uses embedding similarity (threshold: 0.85) to flag potential duplicates
- Duplicates flagged for human decision: merge, keep both, or discard

**Estimated pass rate:** 60-70% of agent-generated components should pass all automated gates. The remaining 30-40% either fail tests (fixable by the agent in a retry loop) or are flagged as duplicates.

## Human Review Workflow

Automated gates catch structural issues; human review catches semantic and strategic issues:

### Review Queue Design
```
Component passes automated gates
    → Enters review queue with context:
        - Source submission (anonymized)
        - Which _reference/ pattern was used
        - Test results
        - Similarity report (near-duplicates)
    → Reviewer actions:
        - Approve → merge to staging → automated integration test → merge to main
        - Request changes → return to agent for modification
        - Reject → discard with reason (logged for pattern improvement)
        - Merge with existing → combine with near-duplicate
```

### Reviewer Qualifications
- **MVP:** Platform maintainers (internal team) review all components
- **Growth:** Community reviewers with reputation scores (like npm maintainers)
- **Scale:** AI-assisted review where a separate LLM evaluates the component and provides a recommendation, with human final approval

## Conflict Resolution Strategy

Concurrent users may trigger creation of similar components simultaneously:

### Optimistic Concurrency (Recommended)
- Both agents build their component independently
- First to pass automated gates enters the review queue
- Second component flagged as "potential duplicate" — reviewer decides
- No locking mechanism needed — duplicates are caught at the gate level

**Why not locking:** Locking introduces contention and latency. If User A's job must wait for User B's component to be reviewed before building, the UX degrades. Better to let both build independently and deduplicate at review time. The cost of reviewing an occasional duplicate is lower than the cost of job queue blocking.

### Merge Conflict Resolution
- Component library uses Git-based versioning
- Components are atomic files — merge conflicts are rare (each component is self-contained)
- If a structural conflict occurs (two components modify the same shared utility), the reviewer manually resolves

## Versioning Strategy

### Semantic Versioning for the Library
- **Major:** Breaking changes to component interfaces (rare — `_reference/` patterns define interfaces)
- **Minor:** New components added
- **Patch:** Bug fixes to existing components

### Per-Component Versioning
- Each component has a version field in its metadata
- Breaking changes to a component create a new version, old version preserved
- Container images pin to a specific library version — no surprise breakage mid-run

### Rollback Capability
- Git-based library means any version is recoverable
- If a merged component causes issues, revert the commit
- Affected container images are rebuilt automatically

## Operational Cost Analysis at Scale

### MVP Phase (0-100 submissions/month)
- **Human review:** ~30 components/month enter review (30% of submissions generate new components)
- **Reviewer time:** ~5 minutes per component = 2.5 hours/month
- **Cost:** Internal team absorbs — no dedicated reviewer needed

### Growth Phase (100-1,000 submissions/month)
- **Human review:** ~300 components/month
- **Reviewer time:** ~25 hours/month = ~0.6 FTE
- **Cost:** $3,000-5,000/month (part-time contractor or community incentive program)
- **Mitigation:** AI-assisted review reduces per-component time to ~2 minutes → 10 hours/month

### Scale Phase (1,000-10,000 submissions/month)
- **Human review:** ~3,000 components/month
- **Reviewer time (without AI):** ~250 hours/month = 1.5 FTE
- **Reviewer time (with AI assist):** ~100 hours/month = 0.6 FTE
- **Cost:** $5,000-10,000/month
- **Mitigation:** Increase automated gate strictness, auto-approve components with >95% confidence score from AI reviewer

### The Curation Bottleneck

This is the make-or-break operational challenge. If curation falls behind:
- Review queue grows → new components don't reach users → flywheel stalls
- Quality standards drop to clear backlog → bad components pollute library → user trust erodes
- Reviewers burn out → attrition → queue grows faster

**Mitigation strategy:**
1. **Strict automated gates** — reject more at the gate, less reaches human review
2. **AI-assisted review** — LLM evaluates component, provides confidence score and recommendation
3. **Tiered review** — auto-approve high-confidence components (>95%), human-review medium confidence (70-95%), auto-reject low confidence (<70%)
4. **Community incentives** — reputation system, early access to features, recognition for top reviewers
5. **Slow growth** — intentionally limit submissions per user to control queue growth until automation matures

**Comparison to open source ecosystems:** npm processes ~2,000 new packages/day with mostly automated checks. PyPI relies on namespace reservation and automated malware scanning. Docker Hub uses automated vulnerability scanning. All have quality problems at scale. Our advantage: components are generated from `_reference/` patterns, making automated quality checking more reliable than for arbitrary human-submitted code.

## Sources

- [Hugging Face Hub Documentation](https://huggingface.co/docs/hub/en/index)
- [Everything About the Hugging Face Model Hub](https://machinelearningmastery.com/everything-you-need-to-know-about-the-hugging-face-model-hub-and-community/)
- [What is Hugging Face? The 2026 Guide](https://www.metacto.com/blogs/what-is-hugging-face-a-guide-to-the-ai-community-and-its-tools)
