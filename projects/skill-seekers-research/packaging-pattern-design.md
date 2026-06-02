# Research Skill Packaging Pattern Design

**Date:** 2026-06-01
**Task:** 003 — Design the Packaging Pattern
**Input:** projects-survey.md (35 projects surveyed, 11 Tier 1 candidates)

---

## 1. What a Research SKILL.md Contains

A research skill wraps accumulated project findings into a callable, indexable knowledge unit. Structure:

```markdown
# [Topic] Research Skill

**Domain:** [topic-slug]
**Type:** Knowledge (read-only reference)
**Source:** projects/[project-dir]/
**Updated:** [date of last research update]

## Identity
One-sentence description of what this skill knows about.

## When to Invoke
- User asks about [topic area]
- Pipeline references [topic] as a dependency
- Decision requires [domain] knowledge

## Key Findings
| Finding | Recommendation | Confidence |
|---------|---------------|------------|
| [finding 1] | [action] | High/Med/Low |
| [finding 2] | [action] | High/Med/Low |

## Reference Files
| File | Contains |
|------|----------|
| `references/[file].md` | [what it covers] |

## Structured Data (optional)
- Go/No-Go decision: [GO | NO-GO | CONDITIONAL]
- Risk level: [LOW | MEDIUM | HIGH]
- Revenue estimate: [range or null]
- Timeline: [range or null]

## Limitations
What this research does NOT cover or where findings may be stale.
```

**Key design choices:**
- **Key Findings table** is the primary interface — an agent reads this first, dives into references only if needed
- **Structured Data** enables programmatic queries ("show me all GO decisions")
- **When to Invoke** tells the kernel/agent when to pull this skill's context
- References point to the original project files (no duplication)

---

## 2. Auto-Packaging Feasibility

### Minimum Structure for Auto-Packaging

A project directory is auto-packageable if it has:

1. **A synthesis file** matching one of: `research-report.md`, `final-report.md`, `gtm-recommendation.md`, `report.md`, `go-to-market-plan.md`
2. **At least 2 sub-topic files** (numbered or named)
3. **Headers with conclusions** — the synthesis file contains ## sections with actionable text

### Detection Algorithm

```python
def is_packageable(project_dir):
    files = list(project_dir.glob("*.md"))
    synthesis_names = {
        "research-report.md", "final-report.md",
        "gtm-recommendation.md", "report.md",
        "go-to-market-plan.md"
    }
    has_synthesis = any(f.name in synthesis_names for f in files)
    has_subtopics = len(files) >= 3  # synthesis + 2 topics minimum
    return has_synthesis and has_subtopics
```

### What Auto-Packaging Produces

A script could generate:
1. **SKILL.md** — from the synthesis file's headers and first paragraphs
2. **Key Findings table** — extracted from Go/No-Go sections, recommendation tables, or ## Summary sections
3. **Reference file index** — from the directory listing
4. **Structured Data** — parsed from Go/No-Go keywords in the synthesis

### Feasibility Assessment

**HIGH feasibility** for Tier 1 projects (11/35). The pattern is consistent enough that a ~100-line Python script could:
- Detect packageable projects (pattern match on synthesis file names)
- Extract key findings (regex on markdown headers + table content)
- Generate SKILL.md stubs with references

**LOW feasibility** for Tier 2-3 projects. Single-file projects and in-progress work lack the structure needed for automated extraction.

**Estimated effort:** 2-4 hours for the auto-packaging script. Manual review of each generated SKILL.md: ~5 min per project.

---

## 3. Invocation Model

Three models considered, in order of simplicity:

### Model A: Context Injection (MVP — Recommended)

The task file or pipeline includes a reference directive:

```markdown
## Context References
- → projects/hoi-an-knockoff-shirts/gtm-recommendation.md
- → projects/govcon-research/research-report.md
```

The agent reads these files at task start, incorporating findings into its working context. No new infrastructure needed — just a convention.

**Pros:** Zero new code. Works today. Agent already reads files referenced in tasks.
**Cons:** Manual — someone must know which project has relevant findings. No discovery.

### Model B: Skill Invocation

Research skills are registered in the protocol's reference table:

```markdown
## Research Skills
| Skill | SKILL.md |
|-------|----------|
| Business Formation | `.claude/skills/research/ai-business-formation/SKILL.md` |
| Govcon Feasibility | `.claude/skills/research/govcon-research/SKILL.md` |
```

Agent invokes by reading SKILL.md, which points to reference files.

**Pros:** Discoverable via protocol. Consistent interface. Agent can scan the table.
**Cons:** Requires creating SKILL.md files + registering in protocol. Maintenance burden.

### Model C: Programmatic Search

A `research-index.json` file catalogs all research findings with metadata (topic, decision, confidence, date). A script or the agent queries it:

```json
{
  "projects": [
    {
      "slug": "govcon-research",
      "decision": "CONDITIONAL_GO",
      "topics": ["government", "contracting", "SAM.gov"],
      "synthesis": "projects/govcon-research/research-report.md"
    }
  ]
}
```

**Pros:** Programmatically queryable. Supports filtering by topic/decision.
**Cons:** Requires maintaining a JSON index. Adds a build step.

### Recommendation

**Start with Model A (context injection)** — it works today with zero new code. Evolve to **Model B (skill invocation)** when the number of research projects exceeds ~15 active ones and discovery becomes a bottleneck. Skip Model C unless the workspace needs machine-queryable research metadata.

---

## 4. Comparison: Skill Index vs RAG/Vector Search

| Dimension | Skill Index | RAG/Embeddings |
|-----------|-------------|----------------|
| **Setup cost** | Zero (markdown files) | Requires embedding pipeline, vector DB |
| **Maintenance** | Update SKILL.md when findings change | Re-embed on every change |
| **Precision** | High — curated key findings | Medium — depends on chunk quality |
| **Context efficiency** | Excellent — agent reads only relevant findings | Poor — retrieves chunks that may miss context |
| **Dependencies** | None (pure markdown) | Python packages, vector store, API keys |
| **Discovery** | Protocol table scan | Semantic similarity search |
| **Scale ceiling** | ~50-100 projects before table gets unwieldy | 1000+ documents |
| **Fits kernel philosophy?** | Yes — visible, auditable, no external deps | No — opaque embeddings, external service |

**Verdict:** Skill index is the right choice for this workspace. The research corpus is small (~35 projects, ~11 structured), the kernel philosophy demands visible/auditable knowledge, and RAG adds complexity without proportional value at this scale. If the workspace grows past ~100 research projects, a lightweight search layer (grep-based, not vector) would be the next step before considering embeddings.

---

## 5. Minimum Viable Pattern (MVP)

### What to Build

1. **Convention:** Every Tier 1 research project gets a `SKILL.md` in its project directory (not in `.claude/skills/` — keeps research outputs co-located with their source)
2. **Auto-gen script:** `scripts/generate-research-skills.py` scans `projects/*/`, identifies packageable directories, generates SKILL.md stubs
3. **Protocol registration:** Add a "Research Knowledge" section to the protocol's reference table pointing to `projects/*/SKILL.md`
4. **Invocation convention:** Task files reference research via `→ projects/[slug]/SKILL.md` directives

### What NOT to Build

- No vector database or embedding pipeline
- No separate `.claude/skills/research/` directory tree (avoid duplication)
- No JSON index (premature for 11 projects)
- No custom MCP server or API
- No orchestration layer for skill composition

### Implementation Effort

| Step | Effort | Output |
|------|--------|--------|
| Write generate-research-skills.py | ~1 hour | Script that produces SKILL.md stubs |
| Review + customize 11 SKILL.md files | ~1 hour | Accurate key findings per project |
| Add protocol section | ~10 min | Research skills discoverable |
| Total | ~2 hours | 11 research projects indexed as skills |

### Success Criteria

- Agent can find relevant research by scanning protocol → research skills table
- Each SKILL.md has accurate Key Findings table and reference index
- No external dependencies added
- Research findings are reusable in future pipelines via context injection

---

## Summary

The packaging pattern is: **co-located SKILL.md files with curated key findings, auto-generated from structured research outputs, discoverable via protocol table, invoked via context injection.** This is the simplest pattern that makes research reusable without adding infrastructure. The auto-gen script handles the 11 Tier 1 projects; new research produced by execute-pipeline will follow the same structure automatically (since the pipeline already produces numbered files + synthesis reports).
