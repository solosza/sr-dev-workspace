# Skill Composability Model — Can Skills Compose Like Unix Pipes?

## Current Skill Model: Standalone Invocation

Every kernel skill today is a **standalone monolith** invoked by a single command. Each skill owns its entire pipeline from input to output:

| Skill | Command | Input | Output | Steps |
|-------|---------|-------|--------|-------|
| website-cloner | `/clone <url>` | URL | HTML + CSS + assets/ | 6 |
| task-builder | `/kernel/task-builder <goal>` | Natural language goal | tasks/ folder + gate contract + validation report | 10 |
| execute-pipeline | `/kernel/execute-pipeline <input>` | Goal or backlog number | Executed tasks + validation report | 5 |
| autonomous-cycling | `/kernel/autonomous-cycle` | Workflow state (task_folder) | Completed tasks | Loop |
| prod-test | `/kernel/prod-test <repo>` | Repo path | Validation report | 8 |
| audit-workflow | `/kernel/audit-workflow` | Kernel state | Fix tasks + report | 8 |

Each skill reads its own references, manages its own state, and produces its own output. There is no concept of "plug skill A's output into skill B's input."

## Execute-Pipeline: The Existing Composition Pattern

Execute-pipeline is the closest thing to skill composition in the kernel today. It chains three capabilities:

```
backlog-creation → task-builder → run-task.sh
     (step 2)        (step 3)       (step 4)
```

But this isn't true composition — it's **orchestration**. Execute-pipeline is a meta-skill that calls other skills as subroutines within a single agent session. The key differences from Unix pipe composition:

| Property | Unix Pipes | Execute-Pipeline |
|----------|-----------|-----------------|
| Coupling | None — `ls` doesn't know about `grep` | Tight — step 3 knows task-builder's API, sets flags (`pipeline_mode`) |
| Data format | Text streams (universal) | JSON in session_state.json (proprietary per skill) |
| Failure handling | Exit code propagation | Custom retry logic per step |
| State | Stateless (each process independent) | Shared mutable state (session_state.json, workflow.json) |
| Process model | Separate processes, concurrent | Single agent, sequential steps |

Execute-pipeline's "composition" is more like a shell script calling functions than Unix pipes composing processes. The orchestrator has intimate knowledge of each step's internals.

## What True Skill Composability Would Look Like

### The Unix Pipe Model Applied to Skills

```
extractor | transformer | generator
   ↓            ↓            ↓
 URL → tokens  tokens →     tokens+spec →
               filtered      HTML+CSS
               tokens
```

For this to work, skills would need:

### 1. Input/Output Contracts

Each skill declares its input type and output type:

```
website-cloner:
  input:  { url: string }
  output: { tokens: DesignTokens, screenshots: Screenshot[], assets: Asset[] }

generation-skill (hypothetical):
  input:  { tokens: DesignTokens, content: ContentSpec, architecture: ArchitectureSpec }
  output: { html: string, css: string, assets: Asset[] }

task-builder:
  input:  { goal: string, context?: any }
  output: { task_folder: string, gate_contract: GateContract, validation: Report }
```

The pipe would work when skill A's output type matches skill B's input type (or a subset of it).

### 2. Intermediate Data Format

Unix pipes use text. Skills would need a universal intermediate format. Candidates:

| Format | Pros | Cons |
|--------|------|------|
| **JSON files on disk** | Already used (tokens, state). Inspectable. Survives process boundaries. | Schema enforcement is manual. Large payloads (screenshots). |
| **Directory convention** | Skills produce output dirs, next skill reads from there. Website-cloner already does this. | Loose contract — skill B must know skill A's directory structure. |
| **Typed manifests** | Each skill writes a `manifest.json` with typed fields + file pointers | New concept to build. But clean interface. |

The most natural fit for the kernel is **directory convention + manifest**: each skill writes its output to a directory, includes a `manifest.json` describing what's there, and the next skill reads from that manifest.

### 3. Piping Mechanism

Who connects skill A to skill B? Options:

| Approach | How It Works | Fits Kernel? |
|----------|-------------|--------------|
| **Shell-level piping** | `clone https://x.com \| generate --content spec.json` | No — skills are agent conversations, not CLI processes |
| **Orchestrator skill** | A meta-skill (like execute-pipeline) wires skills together | Yes — already proven with execute-pipeline |
| **Declarative pipeline** | YAML/JSON file declaring the chain: `[clone, transform, generate]` | Maybe — clean but adds configuration layer |
| **Implicit chaining** | Skills detect predecessor output in a known location and resume | No — too magical, violates "never assume" |

The orchestrator pattern is the most kernel-native. Execute-pipeline already proves it works. The question is whether to generalize it.

## Barriers to Composability

### 1. Shared Mutable State

The biggest barrier. Skills today share state through `session_state.json` and `workflow.json`. This creates coupling:

- Execute-pipeline writes `pipeline_state` that task-builder reads
- Task-builder writes `task_folder` that autonomous-cycling reads
- Prod-test reads `completed_tasks` that cycling writes

If skills were truly composable, each would own its own state. But the kernel's hook system (gate enforcement, anchor counter) assumes a single global state. Two skills running in parallel would corrupt state — this is exactly the contention bug documented in the state-contention lesson.

**Resolution path:** Scoped state per skill invocation, with the kernel's global state (anchor counter, learn obligations) as a separate layer. Each skill gets a `skill_state/[invocation-id].json` while kernel enforcement stays in `session_state.json`.

### 2. Context Window Limits

Skills consume significant context window space. The website-cloner needs DOM snapshots, computed styles, and screenshots in context. The task-builder needs goal text, template file maps, and path mappings. Chaining two skills means both contexts must fit — or one must be summarized/externalized before the next starts.

Execute-pipeline handles this by running task-builder in the same session but run-task.sh in separate processes (one-shot agents). This is a **process boundary as context reset** — each one-shot agent gets a fresh context window with only the task file loaded.

**Resolution path:** Skill output goes to disk (not just context window). Next skill reads from disk, not from the prior skill's context. The manifest pattern handles this naturally.

### 3. Tool Availability

Different skills need different tools. Website-cloner needs Playwright MCP. Prod-test needs Docker. Task-builder needs file I/O. A composable pipeline would need to ensure tool availability at each stage.

**Resolution path:** Tool requirements declared in skill manifest. Orchestrator verifies all tools are available before starting the pipeline. Fail fast, not mid-pipeline.

### 4. Error Propagation

Unix pipes propagate errors via exit codes and `set -o pipefail`. Kernel skills have richer failure modes:

- Task-builder: design-level failure (wrong decomposition) vs execution-level failure (test failed)
- Website-cloner: extraction failure (site uses canvas) vs generation failure (CSS doesn't match)
- Prod-test: infrastructure failure (Docker down) vs test failure (L3 gate failed)

A composable system needs typed errors that the next skill or orchestrator can reason about, not just pass/fail.

**Resolution path:** Skill output manifests include a `status` field with error classification. Orchestrator has a retry decision tree (like task-builder's existing one) that applies across skill boundaries.

## Design: What Composability Would Actually Look Like

### Skill Interface Specification

```
# In each SKILL.md, add:

## Interface

input:
  required:
    - tokens: DesignTokens (path to JSON file)
    - content: ContentSpec (path to JSON file)
  optional:
    - reference_screenshots: Screenshot[] (paths)

output:
  directory: [output-dir]/
  manifest: [output-dir]/manifest.json
  files:
    - index.html
    - styles.css
    - assets/

errors:
  - type: extraction_failure
    recoverable: true
    fallback: "retry with simplified extraction"
  - type: token_conflict
    recoverable: true
    fallback: "use priority rules from input spec"
```

### Pipeline Definition

```json
{
  "pipeline": "extract-and-generate",
  "steps": [
    {
      "skill": "website-cloner",
      "input": { "url": "$URL" },
      "output_dir": "pipeline/step-1-extraction/"
    },
    {
      "skill": "token-transformer",
      "input": {
        "tokens": "pipeline/step-1-extraction/manifest.json#tokens",
        "filter": "typography+color"
      },
      "output_dir": "pipeline/step-2-transform/"
    },
    {
      "skill": "generation-skill",
      "input": {
        "tokens": "pipeline/step-2-transform/manifest.json#tokens",
        "content": "$CONTENT_SPEC",
        "architecture": "$ARCH_SPEC"
      },
      "output_dir": "pipeline/step-3-generation/"
    }
  ]
}
```

### Orchestrator Generalization

Execute-pipeline today is a specific orchestrator: backlog → task-builder → run-task.sh. A generalized orchestrator would:

1. Read pipeline definition (JSON or inline)
2. Verify all skills exist and tools are available
3. Execute each step sequentially (or parallel where declared safe)
4. Pass output manifests as input to next step
5. Handle errors per the retry decision tree
6. Produce a pipeline-level validation report

This is a natural evolution of execute-pipeline, not a replacement.

## Assessment: Should We Build This?

### Arguments For

- **Extraction → generation pipeline** is the most common multi-skill pattern (website-cloner + hypothetical generation skill)
- **Execute-pipeline already proves** the orchestrator pattern works
- **Manifest-on-disk** is trivial to implement (JSON files)
- **Skill interface specs** would improve documentation even without piping
- **Error classification** would improve retry logic across all skills

### Arguments Against

- **Only one composition exists today** (execute-pipeline). Building a general system for one use case is premature.
- **Shared state is the real problem**, and composability doesn't solve it — state scoping does.
- **Context window limits** mean skills can't truly "stream" data to each other. Each step reads from disk anyway, so the "pipe" metaphor is misleading.
- **Agent judgment doesn't compose linearly.** Unix pipes compose deterministic transforms. Agent skills involve judgment at every stage. Chaining judgment calls amplifies uncertainty — each skill's aesthetic/architectural choices constrain the next skill's options in ways that are hard to specify in an interface contract.
- **YAGNI.** The kernel has 6 skills. The likely next addition is one generation skill. Building a composition framework for 7 skills is over-engineering.

### Verdict

**Not yet. But prepare the ground.**

The kernel doesn't need a general-purpose skill composition framework today. It needs:

1. **Skill interface specs** added to each SKILL.md (input/output types, error classifications) — useful regardless of composition
2. **Manifest-on-disk pattern** standardized for skills that produce artifacts (website-cloner, future generation skill) — useful for inspection and debugging
3. **State scoping** to eliminate shared mutable state contention — prerequisite for any composition

When a second composition pattern emerges (beyond execute-pipeline), that's when to generalize the orchestrator. Until then, execute-pipeline's hardcoded orchestration is simpler, more debuggable, and sufficient.

The Unix pipe analogy is inspiring but misleading. Skills are not stateless text transforms — they are judgment-mediated, context-heavy, state-mutating agent behaviors. The right composition model is closer to **microservices with message passing** than Unix pipes: each skill has a defined API, communicates through structured artifacts on disk, and an orchestrator handles sequencing and error recovery.
