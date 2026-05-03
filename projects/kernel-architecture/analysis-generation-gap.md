# Generation Skills Gap — Extraction vs Generation Asymmetry

## The Asymmetry

The kernel has mature extraction skills but zero generation skills. This gap is the single largest source of ad-hoc task volume.

| Capability | Skill Exists? | Maturity | Example |
|-----------|--------------|----------|---------|
| **Extraction** (URL → tokens) | Yes — website-cloner | High — 6-stage pipeline, fallback cascades, visual QA | `/clone https://example.com` → JSON tokens, screenshots, assets |
| **Generation** (tokens → site) | No | N/A — ad-hoc task instructions every time | 75 bespoke tasks across backlogs 047+053 |
| **Execution** (tasks → done) | Yes — task-builder, run-task.sh, autonomous cycling | High — decompose, gate, spawn, validate | `/kernel/task-builder Build X` → task files → one-shot agents |

The extraction pipeline is a proper skill: structured input (URL), structured output (JSON tokens + screenshots), reusable across any site, with documented fallback strategies and quality gates. The generation pipeline is invisible — it exists only as ad-hoc task instructions written fresh for each project.

## Current Extraction Skills: What's Mature

The website-cloner's 6-stage extraction pipeline:

| Stage | Input | Output | Judgment Required |
|-------|-------|--------|-------------------|
| 1. Navigate & screenshot | URL | Reference screenshots | Viewport selection, wait-for-hydration decision |
| 2. Extract structure | DOM snapshot | Section map, computed styles | Which sections matter, how to name them |
| 3. Extract tokens | Computed styles | JSON token files (colors, typography, spacing) | Which values are design tokens vs incidental |
| 4. Download assets | Image/font URLs | Local files in assets/ | Which assets to download, format conversion |
| 5. Assemble output | Extracted data | HTML + CSS + assets directory | How to organize, what to discard |
| 6. Visual QA | Clone vs reference screenshots | Iterative fixes | What "close enough" means, which discrepancies matter |

Key properties that make this a real skill:
- **Generic input:** Any URL works. No site-specific configuration.
- **Structured output:** Always the same shape (JSON tokens, screenshots, directory).
- **Documented fallbacks:** Canvas detection, SVG text, deferred hydration — written in prose but systematic.
- **Quality gate:** Stage 6 visual comparison loop catches regressions.

## Current Generation Pattern: What's Missing

When the kernel needs to generate output (a site, a document, a codebase), it relies on ad-hoc task instructions. There is no skill. The pattern observed across projects:

### Portfolio Site (backlogs 047 + 053)

75 generation tasks, zero skill coverage. Each task was a bespoke instruction like:
- "Merge Suero spacing tokens with Shader surface tokens, resolve conflicts manually"
- "Write hero section HTML with narrative content about Isagawa"
- "Create CSS for provenance section with Sigstore attestation display"
- "Apply `clamp()` fluid typography to headings at 5 breakpoints"

These instructions contain embedded domain knowledge (what the Isagawa narrative is, what Sigstore attestations look like, what "good" responsive typography means) but that knowledge is never captured for reuse. The next site build starts from scratch.

### Fraud Detector (backlog 025)

39 tasks, all generation, but generating *code* not *content*. The task-builder decomposed the problem and the agent generated Python files. No generation skill was involved — the task instructions specified what each file should contain. The agent's code generation ability is implicit (it's an LLM) not codified (there's no "code generation skill" with stages, quality gates, and fallbacks).

### What Ad-Hoc Generation Looks Like in Practice

```
Task instruction (ad-hoc):
  "Write the hero section with: heading 'Isagawa', subheading about
   provenance, CTA button, dark gradient background using --bg-primary"

What the agent does:
  1. Reads the instruction
  2. Recalls extracted tokens from context window
  3. Makes aesthetic judgment calls (font size, spacing, layout)
  4. Writes HTML + CSS
  5. Hopes it looks good (no visual QA until polish phase)
```

There is no structured input contract. No fallback strategy for when tokens don't match intent. No quality gate between "wrote the section" and "moved to next section." The agent's judgment is the entire pipeline — and unlike extraction, that judgment isn't documented anywhere.

## What a Generation Skill Would Need

### Structured Input

A generation skill needs a defined input contract, not free-text instructions:

```
Generation Input:
  design_tokens:     JSON file (colors, typography, spacing, breakpoints)
  content_spec:      Structured content (sections, headings, body text, CTAs)
  architecture_spec: Layout intent (grid structure, section ordering, responsive behavior)
  reference_assets:  Screenshots or mood boards (optional, for visual QA)
```

The extraction skill already produces `design_tokens`. The missing pieces are `content_spec` and `architecture_spec` — these are currently embedded in task instructions as free text.

### Staged Pipeline (Analogous to Extraction)

| Stage | Input | Output | Judgment |
|-------|-------|--------|----------|
| 1. Foundation | Tokens → CSS variables | `styles.css` with custom properties, reset, grid | Which tokens become variables vs constants |
| 2. Scaffold | Architecture spec → HTML skeleton | `index.html` with semantic sections, no content | Section ordering, container nesting, landmark roles |
| 3. Populate | Content spec → filled sections | HTML with real headings, text, CTAs | Content hierarchy, emphasis, truncation |
| 4. Style | Tokens + scaffold → section CSS | Per-section styles | Aesthetic judgment: spacing, typography scale, color application |
| 5. Responsive | Breakpoints → media queries | Responsive behavior | Which elements reflow, stack, or hide |
| 6. QA | Generated output vs reference | Iterative fixes | Visual comparison (same as extraction stage 6) |

This mirrors the extraction pipeline's shape: 6 stages, structured I/O per stage, documented judgment points, visual QA at the end.

### Fallback Strategies (Currently Absent)

Extraction has documented fallbacks (canvas detection → SVG text → hydration wait). Generation has none. What would generation fallbacks look like?

| Problem | Current Behavior | Skill Fallback |
|---------|-----------------|----------------|
| Token conflict (two sources disagree) | Agent picks one ad-hoc | Priority rules: source A > source B, or compute weighted average |
| Content too long for layout | Agent truncates or rewrites | Overflow strategy: truncate with ellipsis, or reflow to 2-column |
| Typography scale doesn't work at small viewports | Agent adds `clamp()` after the fact | Fluid typography by default, with floor/ceiling from tokens |
| Section looks wrong but passes structural checks | Not caught until QA phase | Visual checkpoint after each section (screenshot + compare) |

## Comparison to Template Engines

Template engines (Jinja2, Handlebars, React components) solve a related but different problem:

| Dimension | Template Engine | Agent Generation Skill |
|-----------|----------------|----------------------|
| **Input** | Structured data (JSON/DB) | Structured data + aesthetic intent |
| **Logic** | Conditionals, loops, filters | Judgment calls, aesthetic decisions |
| **Output** | Deterministic (same input → same output) | Variable (agent makes different choices) |
| **Edge cases** | Pre-programmed (if/else) | Handled by agent reasoning |
| **Customization** | New template file | Same skill, different input spec |
| **Quality** | Guaranteed structure, no aesthetic judgment | Structure + aesthetics, but non-deterministic |

The critical difference: template engines are **deterministic transforms** — data in, HTML out, no judgment. Agent generation is **judgment-mediated transforms** — the agent makes choices about how to apply tokens, what looks good, where to add emphasis. This is why generation can't be reduced to a template engine. The agent's judgment IS the value.

But what a generation skill captures is the **process around the judgment**: what inputs to gather, what order to build in, where to check quality, what fallbacks to try when judgment calls don't land. The website-cloner proves this works — extraction judgment (what's a hero section? what CSS values matter?) is guided by the skill's staged process without being deterministic.

## The Gap's Cost

Evidence from the portfolio build:

- **75 ad-hoc generation tasks** with no skill coverage = 75 tasks where the process was invented from scratch
- **Build 2 (053) exists entirely because of the extraction-generation boundary gap** — extracted tokens weren't validated before generation started, so 25 tasks were needed to fix aesthetic failures
- **No quality gate between extraction and generation** — the website-cloner's visual QA covers extraction output but nothing validates "these tokens are sufficient to generate a good site"
- **Zero reusability** — the next site build can't reuse any of the generation process. It will be another 50-75 ad-hoc tasks.

## Conclusion

The extraction-generation asymmetry is the kernel's most significant architectural gap. Extraction is a mature skill with structured I/O, staged pipelines, fallback strategies, and quality gates. Generation is invisible — no skill, no stages, no fallbacks, no gates. The agent's generation ability is powerful (it built a fraud detector and a portfolio site) but uncaptured (the process dies with each conversation).

A generation skill wouldn't make generation deterministic — that's template engines. It would make generation *repeatable*: same stages, same quality gates, same fallback strategies, different content. The website-cloner proves this model works for extraction. The question is whether the same model can work for the judgment-heavier generation process.
