# Scanner Loop: Core Algorithm

## Status
NEW

## Purpose

The core scanning algorithm that reads a tiered-index structure, follows wikilinks to sub-indexes and payloads, and catalogs every payload file with its topic metadata.

## Input

- `reference_index_path`: Path to the project's root reference index (e.g., `reference/index.md`)

## Output

- `payload_catalog`: List of `{ path, topics[], source_index }` for every payload discovered

## Algorithm

1. **Read root index.** Parse the index file for:
   - Table rows with `| Topic | File | Contents |` structure
   - Wikilinks (`[[path]]` or `[text](path)`)
   - Each entry = a reference with a topic and a file path

2. **Classify each entry.** For each file path found:
   - If path points to another `index.md` → it's a sub-index, recurse into it
   - If path points to a payload file (`.md`, `.sql`, `.json`) → catalog it
   - Extract topic from the "Topic" column or from the filename/heading

3. **Follow sub-indexes recursively.** Apply the same parsing to sub-indexes. Track depth to prevent infinite loops (max depth = 5).

4. **Build catalog.** Each payload gets:
   ```json
   {
     "path": "references/test-workflow/references/rules.md",
     "topics": ["rules", "test-data-creation", "dos-overlap", "member-uniqueness"],
     "source_index": "references/test-workflow/index.md"
   }
   ```

5. **Topic extraction.** Topics come from:
   - The "Topic" or "Contents" column in index tables
   - Section headings within the payload (H2/H3)
   - Filename keywords (e.g., `rules.md` → "rules", `drg-to-mdc-mapping.md` → "drg-mapping")

## Edge Cases

- Payload referenced by multiple indexes → appears once, topics merged
- Broken wikilink (file doesn't exist) → skip with warning
- File over 200 lines → scan is fine, just catalog it (splitting is a separate concern)
- Non-markdown payloads (.sql, .json) → catalog path, topics from filename only

## Dependencies

- Tiered-index architecture must be followed by reference docs (index → payload pattern)
- No code dependencies — this is agent reasoning, not a script
