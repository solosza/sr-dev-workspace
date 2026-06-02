# Skill Seekers Pattern — Research Report

**Backlog:** 120 — Skill Seekers Pattern Research
**Date:** 2026-06-01
**Scope:** Design a pattern for auto-packaging accumulated research into callable kernel skills.

---

## Recommendation

### BUILD (MVP)

The workspace has 35 project directories containing accumulated research. 11 are well-structured (numbered sub-files + synthesis report) and ready for skill packaging today. The MVP requires ~2 hours of implementation with zero external dependencies — a Python script to generate SKILL.md stubs plus protocol registration.

---

## 1. Current State: Why projects/ Is Inert

The `projects/` directory holds research outputs from execute-pipeline runs, manual research, and strategic planning. These outputs are **write-once, never-referenced** — once a pipeline completes, the findings sit in markdown files that no future pipeline or task consults.

**The problem:** Research accumulates but doesn't compound. A pipeline researching "AI business models" doesn't know that govcon-research already concluded "CONDITIONAL GO" on government contracting, or that ai-business-formation already decided "form Wyoming LLC." Each pipeline starts from zero.

**Scale of the problem:**
- 35 project directories
- 11 well-structured with synthesis reports and actionable recommendations
- 8 single-file projects (valid but monolithic)
- 4 empty (currently being populated by parallel pipelines)
- 12 in-progress or partial structure

The structured projects follow an emergent pattern: numbered topic files → synthesis report → Go/No-Go recommendation. This pattern was never formally defined — it evolved through repeated execute-pipeline usage. Formalizing it makes future research structurally consistent.

---

## 2. Pattern Design: The Research Skill

A research skill is a co-located SKILL.md file inside the project directory that provides:

| Component | Purpose |
|-----------|---------|
| **Identity** | What this skill knows about |
| **When to Invoke** | Triggers for pulling this knowledge |
| **Key Findings table** | Primary interface — findings, recommendations, confidence |
| **Structured Data** | Go/No-Go, risk level, revenue estimate (machine-parseable) |
| **Reference Files index** | Pointers to detailed sub-topic files |
| **Limitations** | What the research doesn't cover |

The Key Findings table is the critical innovation — it gives an agent a 10-second summary without reading 6 sub-files. Deep dives use the reference index.

**Design choice: SKILL.md lives in `projects/[slug]/`, not `.claude/skills/`.** This keeps research outputs co-located with their source and avoids a parallel directory tree that must be kept in sync.

---

## 3. Auto-Packaging Feasibility

**HIGH for Tier 1 projects.** A ~100-line Python script can:
1. Scan `projects/*/` for directories matching the packageable pattern (synthesis file + 2+ sub-files)
2. Extract key findings from synthesis file headers and tables
3. Generate SKILL.md stubs with reference indices
4. Report which projects need manual curation

**Detection criteria:** Project has a file named `research-report.md`, `final-report.md`, `gtm-recommendation.md`, `report.md`, or `go-to-market-plan.md` — plus at least 2 additional markdown files.

**11/35 projects pass** this filter. The remaining 24 either lack structure (single-file), are empty (in-progress), or are non-research projects (design docs, fix scripts).

**Manual effort per project:** ~5 minutes to review and customize the auto-generated Key Findings table.

---

## 4. Invocation Model

Three models evaluated:

| Model | Mechanism | When to Use |
|-------|-----------|-------------|
| **A: Context Injection** | Task files include `→ projects/[slug]/SKILL.md` | MVP — works today, zero code |
| **B: Skill Registration** | Protocol table lists research skills, agent scans at anchor | When discovery becomes a bottleneck (~15+ active projects) |
| **C: Programmatic Index** | JSON catalog with metadata, queryable by script | Only if machine-queryable metadata is needed |

**Recommendation:** Start with Model A. The convention of referencing `→ projects/[slug]/SKILL.md` in task context sections costs nothing to implement and integrates with how the kernel already works (agents read referenced files).

Upgrade path: A → B when the number of research skills exceeds ~15 and agents can't efficiently find relevant prior research by scanning a flat list.

---

## 5. RAG Comparison

| Factor | Skill Index | RAG/Embeddings |
|--------|-------------|----------------|
| Setup cost | Zero | Embedding pipeline + vector DB |
| Precision | High (curated) | Medium (chunk-dependent) |
| Context efficiency | Excellent | Poor (noisy retrieval) |
| Dependencies | None | Python packages, API keys, vector store |
| Auditability | Full (readable markdown) | Low (opaque embeddings) |
| Scale ceiling | ~50-100 projects | 1000+ documents |
| Kernel fit | Native | Foreign pattern |

**Verdict:** Skill index wins for this workspace. The corpus is small, the kernel demands visible/auditable knowledge, and RAG adds complexity without proportional value. The break-even point where RAG becomes worthwhile is ~100+ research projects with significant topic overlap requiring semantic discovery.

---

## 6. MVP Specification

### Build These

1. **`scripts/generate-research-skills.py`** — Scans `projects/*/`, identifies packageable directories, generates SKILL.md stubs
2. **11 SKILL.md files** — One per Tier 1 project, auto-generated then manually reviewed
3. **Protocol section** — "Research Knowledge" reference table in sr_dev-protocol.md

### Do Not Build

- Vector database or embedding pipeline
- Separate `.claude/skills/research/` directory tree
- JSON metadata index
- Custom MCP server
- Orchestration/composition layer

### Implementation Estimate

| Step | Output |
|------|--------|
| Write generate-research-skills.py | Auto-gen script |
| Run script, review 11 outputs | 11 SKILL.md files with Key Findings |
| Add protocol section | Research skills discoverable at anchor |

### Success Criteria

- Agent finds relevant prior research by scanning protocol → research skills table
- Each SKILL.md has accurate Key Findings and reference index
- Zero external dependencies added
- Future pipelines reference prior research via `→ projects/[slug]/SKILL.md`

---

## 7. Strategic Value

This pattern has a compounding effect: every future execute-pipeline run produces output in the standard format, which is immediately packageable as a research skill. The workspace's knowledge base grows with every pipeline — and unlike a wiki or document store, each entry has a structured interface (Key Findings table) that makes it machine-consumable.

The auto-gen script becomes a one-time investment that pays dividends on every subsequent research pipeline. Combined with the emerging Model B (protocol registration), the kernel evolves from "agent that does research" to "agent that accumulates and reuses research."
