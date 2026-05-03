# Attestation Format — natural-language-session/v1

## Status
NEW

## Location
`workspace:.claude/state/attestations/`

## What It Does
Defines the JSON schema for attestation bundles that prove a kernel pipeline run was driven by natural language intent.

## Schema

```json
{
  "predicateType": "natural-language-session/v1",
  "predicate": {
    "invocation": {
      "configSource": "<SHA-256 of session transcript>",
      "parameters": "<SHA-256 of input prompt / backlog document>"
    },
    "output": {
      "artifacts": [
        {
          "path": "relative/path/to/file",
          "sha256": "<hash>"
        }
      ]
    },
    "timestamp": {
      "start": "ISO-8601",
      "end": "ISO-8601"
    },
    "metadata": {
      "pipeline_backlog": "docs/backlog/NNN-*.md",
      "task_folder": "tasks/folder-name/",
      "task_count": 0,
      "completed_count": 0,
      "skipped_count": 0
    }
  }
}
```

## Privacy Model
- `configSource` is a hash of the full session transcript — content stays private, hash is published
- `parameters` is a hash of the backlog document that drove the run — the backlog itself may be public or private
- Output artifact hashes are public (they can be verified against the actual files)
- No prompt text, conversation content, or proprietary information is ever included in the attestation

## Dependencies
- Hash collection component (must compute all hashes before format can be populated)
