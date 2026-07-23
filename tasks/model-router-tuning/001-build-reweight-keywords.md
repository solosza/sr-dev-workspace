# Task 001: Re-weight Router Keywords
**Type:** BUILD | **Gates:** MR-01
## Action
Edit lib/model-routing-config.json so build/authoring verbs route to SONNET and Haiku is mechanical-only.
## Spec
READ lib/model-routing-config.json + lib/model-router.sh first (understand the current keyword sets + how they map to tiers). Re-weight: the SONNET tier keyword set gains build/implement/write/author/design/create/generate (real authoring). The HAIKU tier keyword set is restricted to MECHANICAL verbs only: copy, scaffold, rename, move, stub, register, index, list. The OPUS tier keeps the hardest work (architecture, multi-file, gate, verify, synthesize). Do NOT touch the resolved model IDs (opus-4-8/sonnet-5/haiku-4.5). Motivation: 247/001 + 257/001 authoring tasks routed to Haiku — fix that class.
## Acceptance
Config re-weighted: build/authoring -> sonnet; haiku mechanical-only; opus hardest; model IDs unchanged.
