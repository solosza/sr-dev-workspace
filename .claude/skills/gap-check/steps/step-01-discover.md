# Step 1: Discover

## Purpose

Load all files in the target to build a complete file inventory before any analysis begins.

## Input

- Target path (command argument — folder or file)

## Output

- File inventory list: path, size, extension, last modified

## Acceptance Criteria

- [ ] Target path exists and is accessible
- [ ] All files globbed recursively for `.md`, `.json`, `.sql`, `.py`, `.xlsx` extensions
- [ ] File inventory built with path, size, extension, last modified
- [ ] Report printed: "Found N files in [target]"

## References

- -> design doc: [[gap-check/references/workflow.md]] — Step 1 procedure
- -> design doc: [[gap-check/references/corpus-detection.md]] — dependency traversal rules

## Procedure

1. If target is a file: read it, extract all path references (`→` links, wikilinks, backtick-quoted paths)
2. If target is a folder: glob recursively for `.md`, `.json`, `.sql`, `.py`, `.xlsx` files
3. **Dependency traversal:** For each reference found in any file:
   - If it points to a folder → glob that folder recursively, add all files to inventory
   - If it points to a file → add that file to inventory
   - Read newly added files and extract their references too (recursive, max depth 3)
4. Build file inventory: path, size, extension, last modified, discovery method (direct vs dependency)
5. Report: "Found N files (M direct, K via dependency traversal)"

**Rule:** The scope is the target PLUS everything it references, recursively. Don't filter by extension yet — Step 2 uses content to detect type.

## Verification

- At least 1 file found in target path
- All file paths are absolute
- No files missed (recursive glob covers subdirectories)

## Failure Recovery

| Condition | Action |
|-----------|--------|
| Target path doesn't exist | Report error, stop |
| Target is empty (0 files) | Report "No files found in [target]", stop |
| Permission error on file | Skip file with warning, continue |
