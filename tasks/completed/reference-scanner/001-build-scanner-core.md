# Build Scanner Core

## Type
BUILD

## Phase Gate
None (first task).

## Deliverable
`.claude/skills/reference-scanner/scanner.py`

## Instructions
1. Read the scanner-loop design doc: `docs/backlog/153-kernel-build-reference-scanner/scanner-loop.md`
2. Create `.claude/skills/reference-scanner/scanner.py` implementing:
   - `scan_index(index_path)` — reads a tiered-index markdown file
   - Parse table rows with `| Topic | File | Contents |` structure
   - Parse wikilinks (`[[path]]` and `[text](path)`)
   - Classify each entry as sub-index (another index.md) or payload file
   - Recurse into sub-indexes (max depth 5)
   - Build and return `payload_catalog`: list of `{ path, topics[], source_index }`
3. Topic extraction from: table columns, section headings (H2/H3), filename keywords
4. Handle edge cases: broken wikilinks (skip with warning), duplicate payloads (merge topics), non-markdown payloads (catalog path, topics from filename only)

## Verification
- File exists at `.claude/skills/reference-scanner/scanner.py`
- Contains `scan_index` function
- Handles recursive sub-index traversal
