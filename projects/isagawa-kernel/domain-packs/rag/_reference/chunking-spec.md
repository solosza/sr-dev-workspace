# Chunking Spec

## Interface Contract

```
ChunkInterface:
  method: chunk(document: Document) → list[Chunk]
  method: chunk_batch(documents: list[Document]) → list[Chunk]
```

## Data Types

### Document (input)
```
Document:
  content: str          # Raw text content
  source: str           # File path or URL
  format: str           # "text", "markdown", "html", "pdf"
  metadata: dict        # Arbitrary key-value pairs (date, author, category)
```

### Chunk (output)
```
Chunk:
  id: str               # Unique identifier (hash of content + source + position)
  content: str           # Chunk text
  token_count: int       # Token count (model-specific or estimated)
  metadata:
    source: str          # Original document source
    position: int        # Index within document (0-based)
    total_chunks: int    # Total chunks from this document
    overlap_before: int  # Characters of overlap with previous chunk
    overlap_after: int   # Characters of overlap with next chunk
    format: str          # Original document format
    custom: dict         # Inherited from document metadata
```

## Strategies

The implementation MUST support at least one strategy, SHOULD support two:

### Fixed-Size (required)
- Split by token count (configurable: default 512)
- Configurable overlap (default 50 tokens)
- Respects sentence boundaries when possible

### Recursive Character Split (recommended)
- Split by separators in priority order: `\n\n` → `\n` → `. ` → ` `
- Recursively split chunks that exceed max token limit
- Better semantic coherence than fixed-size

### Semantic (optional)
- Split by topic/meaning boundaries
- Uses embedding similarity to detect topic shifts
- Highest quality but slowest and most complex

## Configuration

```yaml
chunking:
  strategy: "fixed_size"          # "fixed_size", "recursive", "semantic"
  max_tokens: 512                  # Maximum tokens per chunk
  overlap_tokens: 50               # Overlap between adjacent chunks
  min_chunk_tokens: 50             # Minimum chunk size (avoid tiny fragments)
  separators: ["\n\n", "\n", ". ", " "]  # For recursive strategy
```

## Rules

1. No chunk may exceed `max_tokens`
2. Chunks under `min_chunk_tokens` must merge with adjacent chunk
3. Every chunk MUST have complete metadata (no nulls for required fields)
4. Chunk IDs must be deterministic (same input = same ID)
5. Document format detection must be automatic (by extension or content)
