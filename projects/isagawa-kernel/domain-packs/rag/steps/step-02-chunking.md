# Step 2: Build Chunking Pipeline

## Goal

Implement document chunking that splits raw documents into semantic units with metadata.

## Spec Reference

→ `_reference/chunking-spec.md`

## Actions

1. **Read the chunking spec** — understand strategies, metadata requirements, and interface contract
2. **Implement `ChunkInterface`** — concrete class following the spec
3. **Support at least 2 document formats** (e.g., plain text, markdown)
4. **Attach metadata** to each chunk: source file, position index, token count, overlap info
5. **Respect max token limit** — configurable via config spec
6. **Write unit tests** — chunk size, metadata correctness, edge cases (empty docs, single-sentence docs)

## Key Decisions (Agent Makes During Build)

- Chunking strategy: fixed-size, semantic, recursive character split
- Overlap size: how much context carries between chunks
- Token counting method: tiktoken, character estimation, model-specific

## Gate

→ See `gate-contract.md` Step 2 criteria
