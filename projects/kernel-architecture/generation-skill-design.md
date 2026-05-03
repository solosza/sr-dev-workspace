# Generation Skill Architecture Design

## Overview

Architecture sketch for generation skills in the kernel. Generation skills transform structured data (design tokens, content specs, architecture specs) into deliverable artifacts (HTML, CSS, code, documents). They complement extraction skills, which transform sources (URLs, codebases) into structured data.

This design derives from the generation gap analysis and composability model produced by the kernel-architecture research.

---

## Input Contract

A generation skill receives structured data, not free-text instructions. Every generation skill declares its input in SKILL.md:

```
input:
  required:
    - tokens: path to JSON file (DesignTokens)
    - content: path to JSON file (ContentSpec)
  optional:
    - architecture: path to JSON file (ArchitectureSpec)
    - reference_screenshots: path[] (visual targets for QA)
    - constraints: path to JSON file (overrides, exclusions, fixed values)
```

### DesignTokens (produced by extraction skills)

```json
{
  "colors": { "primary": "#1a1a2e", "accent": "#e94560" },
  "typography": {
    "heading": { "family": "Inter", "weight": 700, "scale": [2.5, 2, 1.5, 1.25, 1] },
    "body": { "family": "Inter", "weight": 400, "size": "1rem", "line_height": 1.6 }
  },
  "spacing": { "section": "6rem", "element": "1.5rem", "grid_gap": "2rem" },
  "breakpoints": { "mobile": "375px", "tablet": "768px", "desktop": "1440px" }
}
```

### ContentSpec (authored by human or extracted from brief)

```json
{
  "sections": [
    {
      "id": "hero",
      "heading": "Isagawa",
      "subheading": "Provenance-first software engineering",
      "body": null,
      "cta": { "text": "View provenance chain", "target": "#provenance" }
    },
    {
      "id": "about",
      "heading": "About",
      "body": "Paragraph text here...",
      "cta": null
    }
  ],
  "metadata": {
    "title": "Isagawa — Portfolio",
    "description": "...",
    "lang": "en"
  }
}
```

### ArchitectureSpec (optional — defaults applied if absent)

```json
{
  "layout": "single-page-scroll",
  "grid": { "columns": 12, "max_width": "1200px" },
  "section_order": ["hero", "about", "work", "provenance", "contact"],
  "responsive_strategy": "mobile-first",
  "typography_strategy": "fluid-clamp"
}
```

**Key constraint:** Inputs must be files on disk, not context-window data. This enables composition with extraction skills (website-cloner writes tokens to disk, generation skill reads them) and survives process boundaries (one-shot agents can read the files).

---

## Output Contract

Every generation skill produces a directory with a manifest:

```
output:
  directory: [output-dir]/
  manifest: [output-dir]/manifest.json
  files:
    - index.html
    - styles.css
    - assets/          (copied/generated assets)
    - screenshots/     (QA screenshots per stage)
```

### manifest.json

```json
{
  "skill": "site-builder",
  "version": "1.0",
  "timestamp": "2026-04-26T14:00:00Z",
  "status": "success",
  "stages_completed": 6,
  "stages_total": 6,
  "files": {
    "html": "index.html",
    "css": "styles.css",
    "assets": "assets/"
  },
  "qa": {
    "screenshots": ["screenshots/stage-2-scaffold.png", "screenshots/stage-6-final.png"],
    "visual_comparison": "pass"
  },
  "errors": [],
  "input_manifest": "path/to/extraction/manifest.json"
}
```

**Key constraint:** The manifest is the interface contract. Downstream skills or orchestrators read the manifest, not the files directly. This decouples producers from consumers.

---

## Pipeline Stages

Generation follows a 6-stage pipeline, mirroring the extraction pipeline's shape. Each stage has defined input, output, and judgment points.

| Stage | Name | Input | Output | Agent Judgment |
|-------|------|-------|--------|----------------|
| 1 | **Foundation** | DesignTokens | `styles.css` with custom properties, reset, grid system | Which tokens become CSS variables vs hard-coded values |
| 2 | **Scaffold** | ArchitectureSpec | `index.html` with semantic sections, no content | Section ordering, container nesting, landmark roles |
| 3 | **Populate** | ContentSpec + scaffold | HTML with real headings, text, CTAs, images | Content hierarchy, emphasis, where to truncate |
| 4 | **Style** | Tokens + populated HTML | Per-section CSS rules | Aesthetic judgment: spacing rhythm, color application, visual weight |
| 5 | **Responsive** | Breakpoints + styled page | Media queries, fluid typography, reflow rules | Which elements stack, reflow, or hide at each breakpoint |
| 6 | **Visual QA** | Generated output + reference screenshots | Iterative fixes | What "close enough" means, which discrepancies to fix vs accept |

### Stage Dependencies

```
DesignTokens ──→ [1. Foundation] ──→ styles.css
                                         ↓
ArchitectureSpec → [2. Scaffold] ──→ index.html (skeleton)
                                         ↓
ContentSpec ────→ [3. Populate] ──→ index.html (filled)
                                         ↓
                  [4. Style] ────→ styles.css (sections added)
                                         ↓
                  [5. Responsive] → styles.css (media queries)
                                         ↓
References ────→ [6. Visual QA] ──→ fixes → manifest.json
```

### Fallback Strategies

Each stage has documented fallbacks — unlike current ad-hoc generation where failures are handled improvisationally.

| Stage | Failure Mode | Fallback |
|-------|-------------|----------|
| 1. Foundation | Token conflict (two sources disagree on `--color-primary`) | Priority rules: later source wins, or merge with explicit override list |
| 2. Scaffold | Architecture spec missing or ambiguous | Apply defaults: single-column, natural section order from content spec |
| 3. Populate | Content too long for intended layout | Overflow strategy: truncate with visible indicator, or split into sub-sections |
| 4. Style | Visual weight feels wrong (too heavy, too sparse) | Apply spacing multiplier (0.8x or 1.2x) and re-evaluate; escalate to QA if still off |
| 5. Responsive | Element breaks at a breakpoint (overflow, overlap) | Stack to single-column at that breakpoint; log for QA |
| 6. Visual QA | Reference screenshot unavailable | Generate self-referencing screenshots (stage 2 vs stage 6 comparison) instead of external reference |

### Checkpoint Screenshots

The skill takes a screenshot after stages 2, 4, and 6. These serve as:
- **Build record:** What the output looked like at each stage (debugging aid)
- **QA anchors:** Stage 6 compares against stage 2 (structural integrity) and against references (visual fidelity)
- **Composability signal:** Downstream skills can inspect screenshots from the manifest without rendering the HTML themselves

---

## Composability with Extraction Skills

### The Extraction → Generation Pipeline

The primary composition pattern. Website-cloner extracts tokens from a reference site; generation skill builds a new site from those tokens plus new content.

```
[website-cloner]                    [site-builder]
  Input: URL                          Input: tokens + content + architecture
  Output: tokens/ + screenshots/      Output: site/ + manifest.json
       ↓                                    ↓
  manifest.json ──────────────────→ reads tokens path from manifest
```

### Connection Mechanism

Skills connect through **manifests on disk**, not shared state or context windows:

1. Extraction skill writes output directory with `manifest.json`
2. Orchestrator (execute-pipeline or manual) passes manifest path to generation skill
3. Generation skill reads manifest, resolves file paths, loads tokens
4. Generation skill writes its own output directory with its own manifest

This avoids:
- **State contention:** No shared `session_state.json` mutations between skills
- **Context overflow:** Tokens are files on disk, not in-context JSON blobs
- **Process coupling:** Skills can run in separate one-shot agents

### Token Validation Gate

A critical gap identified in the generation gap analysis: no quality gate between extraction output and generation input. The generation skill adds an **input validation stage** (stage 0, implicit):

```
Before stage 1:
  - Read tokens from extraction manifest
  - Verify required fields exist (colors.primary, typography.heading, spacing.section)
  - Verify values are valid CSS (no NaN, no empty strings, no duplicate custom properties)
  - If validation fails: report missing/invalid fields, do not proceed
```

This prevents the scenario where extraction produces incomplete tokens and generation fails 30 tasks later.

### Extraction → Transform → Generation

When tokens from multiple sources need merging or filtering before generation:

```
[website-cloner A] → manifest-A.json ─┐
                                       ├→ [token-transformer] → merged-manifest.json → [site-builder]
[website-cloner B] → manifest-B.json ─┘
```

The token-transformer is a lightweight skill (or utility stage) that:
- Reads N token manifests
- Applies merge rules (priority, override, weighted average)
- Writes a single merged token file + manifest
- Reports conflicts for human review

This pattern emerged from the portfolio build where Suero spacing tokens and Shader surface tokens needed merging — done ad-hoc in task instructions, but formalized here.

---

## Example: "site-builder" Skill

### SKILL.md (Sketch)

```markdown
# Site Builder — Generation Skill

## Identity
Transforms design tokens + content spec + architecture spec into a static website.

## Interface

input:
  required:
    - tokens: DesignTokens (JSON path, from extraction or manual)
    - content: ContentSpec (JSON path)
  optional:
    - architecture: ArchitectureSpec (JSON path, defaults applied if absent)
    - references: Screenshot[] (paths for visual QA)

output:
  directory: site/
  manifest: site/manifest.json
  files: index.html, styles.css, assets/, screenshots/

## Step Table

| Step | Action | Reference |
|------|--------|-----------|
| 1 | Validate inputs | references/step-01-validate.md |
| 2 | Build foundation (tokens → CSS) | references/step-02-foundation.md |
| 3 | Scaffold HTML structure | references/step-03-scaffold.md |
| 4 | Populate content | references/step-04-populate.md |
| 5 | Apply section styles | references/step-05-style.md |
| 6 | Add responsive behavior | references/step-06-responsive.md |
| 7 | Visual QA loop | references/step-07-qa.md |
```

### Invocation

```
# Standalone
/build-site --tokens tokens.json --content content.json

# Composed with extraction
/clone https://reference-site.com
/build-site --tokens cloned-sites/reference-site/manifest.json#tokens --content content.json

# Via execute-pipeline
/kernel/execute-pipeline "Clone reference-site.com, merge tokens with brand guide, build portfolio"
```

### How It Differs from Ad-Hoc Generation

| Dimension | Ad-Hoc (75 tasks) | Site-Builder Skill |
|-----------|-------------------|-------------------|
| Input | Free-text task instructions | Structured JSON contracts |
| Process | Invented per task | 7-step pipeline, same every time |
| Fallbacks | Agent improvises | Documented per stage |
| Quality gates | None until final QA pass | Checkpoint screenshots at stages 2, 4, 7 |
| Token validation | None — failures discovered during styling | Stage 1 validates before generation starts |
| Reusability | Zero — process dies with conversation | Full — same skill, any tokens + content |
| Composability | None — standalone tasks | Reads extraction manifests, writes generation manifests |

---

## Open Questions

1. **How much of the content spec can be extracted vs authored?** The extraction pipeline produces tokens but not content. A "content extraction" skill (scrape copy from a reference site, extract section structure) would further reduce ad-hoc generation.

2. **Should stage 6 (visual QA) be a shared skill?** Both extraction and generation end with visual comparison. Factoring this into a standalone QA skill reduces duplication but adds a composition dependency.

3. **What's the minimum viable generation skill?** The full 7-step pipeline is the target. But an MVP could be stages 1-4 only (foundation + scaffold + populate + style), with responsive and QA added later. This reduces scope while proving the architecture.
