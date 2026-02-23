# Generation Spec

## Interface Contract

```
GenerationInterface:
  method: generate(query: str, context: list[RetrievedChunk]) → GenerationResult
  method: generate_with_template(query: str, context: list[RetrievedChunk], template: str) → GenerationResult
```

## Data Types

### GenerationResult (output)
```
GenerationResult:
  answer: str                     # Generated response
  citations: list[Citation]       # Source references used
  model: str                      # Model used for generation
  prompt_tokens: int              # Tokens in prompt
  completion_tokens: int          # Tokens in response
  generation_time_ms: float       # Time taken
```

### Citation
```
Citation:
  chunk_id: str           # ID of the source chunk
  source: str             # Original document source
  content_preview: str    # First 100 chars of the chunk
  relevance_score: float  # Score from retrieval
```

## Provider Abstraction

```
GenerationInterface (abstract)
├── OpenAIGeneration       # GPT-4, GPT-4o
├── AnthropicGeneration    # Claude
├── LocalGeneration        # Ollama, llama.cpp
└── MockGeneration         # For testing (returns template-based responses)
```

## Prompt Template System

Templates are external files, not hardcoded strings:

```
prompts/
├── default.md             # Standard RAG prompt
├── concise.md             # Short answer format
├── detailed.md            # Comprehensive with citations
└── custom/                # User-defined templates
```

### Template Variables
```
{{query}}          # User's question
{{context}}        # Formatted retrieved chunks
{{citations}}      # Source references
{{instructions}}   # System-level instructions
```

## Context Formatting

Retrieved chunks are formatted into the prompt context:

```
[Source 1: filename.md, relevance: 0.92]
Chunk content here...

[Source 2: other.md, relevance: 0.87]
Another chunk...
```

## Configuration

```yaml
generation:
  provider: "openai"               # "openai", "anthropic", "local", "mock"
  model: "gpt-4o"                  # Provider-specific model
  template: "default"              # Template name (from prompts/)
  max_tokens: 1024                 # Max response length
  temperature: 0.1                 # Low for factual, high for creative
  include_citations: true          # Add citation references to response
```

## Rules

1. Generated answers MUST be grounded in provided context (no hallucination)
2. If context is insufficient, response MUST say so (not make up information)
3. Citations MUST reference actual chunks from the context (not fabricated sources)
4. Template switch MUST NOT require code changes
5. `MockGeneration` MUST return deterministic responses for testing
6. Token counts MUST be tracked for cost monitoring
