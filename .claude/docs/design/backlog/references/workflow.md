# Workflow: Steps 1-8

---

## Step 1: Parse Input

**Purpose:** Extract the core idea, tag, verb, scope, and priority from user's natural language description.

**Procedure:**
1. Read the argument — extract the core idea
2. Determine the tag: `kernel`, `domain`, `market`, `test`, or new tag if needed
3. Determine the verb: `research`, `build`, `fix`, `test`, `add`, `define`
4. Determine scope: BUILD, RESEARCH, TEST, or REFACTOR
5. Infer priority from context (High/Medium/Low) — ask only if genuinely ambiguous

**Output:** Parsed intent: tag, verb, object (kebab-case), scope, priority.

---

## Step 2: Get Next Number

**Purpose:** Determine the next sequential backlog number.

**Procedure:**
1. Scan `docs/backlog/*.md` for the highest existing number
2. Also scan `docs/backlog/done/*.md` for numbers there
3. Next number = highest found + 1

**Output:** Three-digit number (NNN) for the new backlog item.

---

## Step 3: Record Intent

**Purpose:** Create an append-only intent log entry for traceability.

**Procedure:**
1. Run: `python lib/attestation/intent.py record NNN "the raw argument text" docs/backlog/NNN-tag-verb-object.md`
2. For **new items** (file doesn't exist yet): run BEFORE writing the file. `record_intent` handles missing `backlog_path` by hashing an empty string.
3. For **updates to existing items**: run AFTER the file is written so `backlog_hash_after` captures the updated content.

**Output:** Intent chain entry appended to `.claude/state/intents/NNN-intent-chain.jsonl`.

---

## Step 4: Assess Complexity

**Purpose:** Determine whether the backlog item is simple or complex.

**Procedure:**
1. **Simple** — single deliverable, few requirements, fits in one file (<80 lines)
2. **Complex** — multiple components/phases, detailed requirements, would exceed 80 lines

**Output:** Complexity decision: `simple` or `complex`.

**Rule:** When in doubt, decompose. A wall of text is harder to task-build from than an index with sub-documents.

---

## Step 5: Write File (Simple Items)

**Purpose:** Apply the simple item template and write the backlog file.

**Procedure:**
1. Apply the simple item template — see [[backlog/references/templates#Simple Item Template]]
2. Populate all sections: Title, Status (Open), Priority, Summary, Requirements, References, Task Builder Input
3. Write to `docs/backlog/NNN-[tag]-[verb]-[object].md`

**Output:** Single backlog file on disk.

**Rule:** Task Builder Input section is MANDATORY — deliverable, location, scope, constraints.

---

## Step 6: Decompose (Complex Items)

**Purpose:** Create an index file + sub-documents for multi-component backlog items.

**Procedure:**
1. Create companion folder: `docs/backlog/NNN-[tag]-[verb]-[object]/`
2. Write one sub-document per component/phase/major concern
3. Each sub-document includes: Status, Location, What it does, Dependencies, enough detail for task-builder
4. Main file becomes an index with: Status, Priority, Summary, Design Documents table (wikilinks), Architecture diagram, Requirements, References, Task Builder Input
5. Verify companion folder name matches backlog filename (minus `.md`)

**Output:** Index file + N sub-documents.

**Sub-document naming:** Name by what they describe (`source-file-analyzer.md`, `llm-integration.md`), not by number.

**Design Documents table format:**
```markdown
## Design Documents

| Document | Purpose |
|----------|---------|
| [[NNN-tag-verb-object/component-name]] | One-line description |
```

---

## Step 7: Set Location

**Purpose:** Auto-resolve the deliverable location using the decision tree.

**Procedure:** Apply the decision tree — see [[backlog/references/templates#Location Decision Tree]]:

1. "spec", "domain spec", "test repo", "testing platform" → `new-repo:D:\my_ai_projects\project_test_repos\[name]`
2. "app", "repo", "tool", "pipeline", "platform", "library" → `new-repo:D:\my_ai_projects\[name]`
3. Change to existing workspace files → `workspace` or `workspace:[subpath]`
4. Research, notes, multi-file non-code → `subproject:[name]`
5. Fallback: `workspace`

**Output:** Location field populated in Task Builder Input.

**Rule:** NEVER ask the user for paths. Auto-resolve deterministically.

---

## Step 8: Report

**Purpose:** Summarize what was created.

**Output:**
```
BACKLOG ITEM CREATED

File: docs/backlog/NNN-[tag]-[verb]-[object].md
Title: [title]
Priority: [priority]
Scope: [scope]
Structure: [simple | decomposed (N sub-documents)]

Ready for /kernel/execute-pipeline.
```
