# Vertical Plugin System

## Overview

The platform serves multiple testing verticals (LLM Eval, Compliance, QA) from one infrastructure by swapping which platform spec loads into the execution container. Each vertical is a plugin — a platform spec repo that conforms to a standard interface, registered in a vertical registry, and packaged into a pre-baked container image.

First vertical: **LLM Eval** using platform-deepeval. Additional verticals added via the expansion protocol below.

## 1. Plugin Architecture

### Platform Spec Interface Contract

Every platform spec must provide:

| Artifact | Purpose | Example (platform-deepeval) |
|----------|---------|----------------------------|
| `_reference/` directory | Patterns the agent uses to build missing test components | Metric definitions, test fixtures, eval templates |
| `FRAMEWORK.md` | Framework identity, capabilities, known limitations | DeepEval framework description + metric catalog |
| Metric definitions | Named metrics with scoring logic | `answer_relevancy`, `faithfulness`, `hallucination` |
| Test fixtures | Sample inputs/outputs for each metric | Golden datasets, expected score ranges |
| Quality gates | Pass/fail thresholds per metric | `answer_relevancy >= 0.7`, `hallucination <= 0.3` |

The agent reads `_reference/` patterns during evaluation. If a component is missing for the submitted artifact, the agent builds it from the reference patterns — this is the dynamic component creation mechanism that differentiates the platform.

### Spec Discovery and Loading

1. Container starts with kernel + one platform spec pre-installed
2. Kernel runs `/kernel/domain-setup` (pre-compiled in pre-baked images) which reads the platform spec's `_reference/` to generate protocol + hooks
3. The compiled protocol defines what the agent can test, how it scores, and what quality gates apply
4. No runtime spec discovery needed — each container image is bound to exactly one platform spec

### Spec Versioning

- Container images pin to a specific platform spec commit SHA
- Image tag format: `{vertical}-{spec-version}-{kernel-version}` (e.g., `deepeval-v1.2.0-k0.9.1`)
- Spec updates trigger image rebuilds via CI (see Container Image Build Pipeline below)

## 2. Vertical Registry

### Vertical Metadata Schema

```yaml
vertical:
  name: "LLM Eval"
  slug: "llm-eval"
  description: "Evaluate LLM agents, harnesses, and skills"
  platform_spec_repo: "isagawa-qa/platform-deepeval"
  container_image: "gcr.io/{project}/eval-platform-deepeval:v1.2.0-k0.9.1"
  supported_artifacts:
    - "claude-code-harness"
    - "claude-code-skill"
    - "agent-loop"
  status: "active"          # active | beta | planned
  launch_date: "2026-Q3"
```

### Registered Verticals

| Vertical | Platform Spec | Status | Timeline |
|----------|--------------|--------|----------|
| LLM Eval | platform-deepeval | Active (first vertical) | Launch |
| Compliance Testing | platform-ssh-verify | Planned | 6-12 months post-launch |
| QA Generation | platform-selenium | Planned | 12-18 months post-launch |

The registry is stored in PostgreSQL. The API reads it to populate the vertical selector in the submission UI and to route jobs to the correct container image.

## 3. Container Image Build Pipeline

### Image Composition

```
Layer 1: Base image
  - Node.js 22 LTS + Python 3.12
  - Claude Agent SDK
  - Common utilities (git, jq, curl)

Layer 2: Kernel layer
  - Isagawa Kernel (commands, hooks, skills)
  - Kernel version pinned per image

Layer 3: Vertical layer (per platform spec)
  - Platform spec repo contents (_reference/, FRAMEWORK.md, metrics, fixtures)
  - Pre-compiled protocol + hooks (domain-setup output)
  - Vertical-specific dependencies (e.g., deepeval pip package for LLM Eval)
```

### Image Tagging and Versioning

- Tag format: `{vertical}-{spec-semver}-{kernel-semver}`
- `latest` tag per vertical points to most recent stable build
- Immutable tags for production (never overwrite a versioned tag)

### Rebuild Triggers

| Trigger | Action |
|---------|--------|
| Platform spec commit to main | Rebuild vertical layer, new spec version tag |
| Kernel release | Rebuild all vertical images with new kernel version |
| Base image security patch | Rebuild all images from new base |
| Manual trigger | For hotfixes or config changes |

CI pipeline (GitHub Actions or Cloud Build) runs on each trigger: clone spec → run domain-setup → compile protocol → build image → push to registry → update vertical registry with new image tag.

## 4. Vertical Isolation

### Namespace Isolation

- Each vertical has its own component library namespace in PostgreSQL (e.g., `components.llm_eval.*`, `components.compliance.*`)
- Components contributed via one vertical cannot leak into another vertical's evaluation
- Component IDs are scoped: `{vertical_slug}/{component_name}/{version}`

### Quality Gate Isolation

- Each vertical defines its own curation quality gates (from the platform spec's `_reference/` patterns)
- LLM Eval gates: metric accuracy, golden dataset coverage, scoring consistency
- Compliance gates: rule correctness, STIG/CIS mapping accuracy, false positive rate
- Gates are evaluated by the vertical's own agent (using the vertical's compiled protocol)

### Shared Infrastructure

Verticals share:
- Cloud Run (job execution)
- PostgreSQL (job records, user accounts, component library)
- Job queue (Cloud Tasks)
- Frontend (submission UI, results dashboard)
- Authentication and billing

Verticals do NOT share:
- Domain state (protocols, hooks, evaluation logic)
- Component libraries (separate namespaces)
- Container images (separate per vertical)
- Quality gates (separate curation criteria)

## 5. Expansion Protocol

To add a new vertical:

| Step | Action | Duration |
|------|--------|----------|
| 1 | Create platform spec repo with `_reference/`, `FRAMEWORK.md`, metrics, fixtures | 1-2 weeks |
| 2 | Run `/kernel/domain-setup` against the new spec to verify protocol compilation | 1 day |
| 3 | Build container image (base + kernel + new spec) | 1 day |
| 4 | Add vertical entry to registry (metadata, image tag, supported artifacts) | 1 day |
| 5 | Pre-seed component library with 50-100 components from spec test suites | 1 week |
| 6 | Add vertical to submission UI selector and results dashboard | 2-3 days |
| 7 | Beta test with internal artifacts, validate curation pipeline | 1 week |

**Estimated total: 3-4 weeks per new vertical** after MVP infrastructure is proven with the first vertical. This matches 158's research estimate.

The architecture makes vertical expansion a configuration operation, not a product rebuild — swap the platform spec, build the image, register the vertical.

## References

- `projects/eval-web-app-research/01-idea-validation.md` — First vertical recommendation (LLM Eval with platform-deepeval), multi-vertical timing (Compliance 6-12mo, QA 12-18mo)
- `projects/eval-web-app-research/02-competitive-landscape.md` — Existing platform specs (platform-deepeval, platform-ssh-verify, platform-selenium), differentiation via dynamic component creation
- `projects/eval-web-app-research/03-tech-stack.md` — Pre-baked container images per vertical, base image composition (Node.js + Python + Claude Agent SDK), Cloud Run for execution
- `projects/eval-web-app-research/05-component-flywheel-curation.md` — Component library growth mechanism, pre-seed with 50-100 components
- `projects/eval-web-app-research/09-go-no-go-recommendation.md` — GO (Conditional): start single vertical, validate flywheel before expanding
- `projects/eval-platform-design/prerequisite-gate.md` — Conditions carried forward into this design
