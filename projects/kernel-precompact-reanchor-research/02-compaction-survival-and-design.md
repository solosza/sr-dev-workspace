# Compaction Survival Audit + Hook Design

## What Survives Compaction Today

### Reliably Survives (On-Disk State)
| Artifact | Mechanism | Survives Because |
|----------|-----------|-----------------|
| CLAUDE.md | Auto-discovered every turn | Loaded into system prompt; not part of conversation history |
| `session_state.json` | File on disk | Unaffected by context compaction; read on demand |
| `sr_dev_workflow.json` | File on disk | Same — persistent state independent of conversation |
| `actions.jsonl` | Append-only log | Same |
| Protocol + lessons files | Files on disk | Read during anchor ceremony, not conversation-dependent |
| `context` key in session_state | Structured JSON | Written by anchor, read by next anchor — disk roundtrip |

### Partially Survives (Compacted Summary)
| Artifact | Risk |
|----------|------|
| Task context | The compacted summary retains high-level task info but loses nuanced decisions, edge cases, specific code snippets reviewed |
| Rule applications | Which lesson rules were applied and how gets compressed; the agent may "forget" a relevant rule without re-reading |
| Protocol understanding | Freshly-read protocol details decay into summary; the agent acts on a compressed version of the rules |
| Direction changes | Mid-conversation pivots documented in conversation get flattened |

### Does Not Survive
| Artifact | Impact |
|----------|--------|
| Full conversation history | Gone by definition — replaced by summary |
| Concrete verification results | Specific test outputs, grep results, file contents read |
| Mental model depth | The agent's deep understanding of "why" behind decisions |

### Current Re-Centering Mechanism
The kernel's existing defense is the N-action anchor timer (`actions_limit: 30`). Every 30 actions, the hook blocks and forces a full `/kernel/anchor` — re-reading protocol, lessons, reviewing inter-anchor work, and persisting context. This works well for gradual context drift (the agent slowly forgetting rules over many actions) but does NOT fire on compaction events. After compaction, the agent could have 0 actions_since_anchor and proceed for up to 30 more actions on a degraded context.

The `context` key in `session_state.json` provides partial recovery when `/kernel/anchor` runs (Step 5: "restore conversation context"), but this only happens when the timer fires or the agent self-invokes anchor — there is no compaction-triggered re-anchor today.

## PreCompact-to-Anchor Flow Design

### Overview

When compaction fires, a PreCompact hook sets `anchored: false` in the workflow state. The next tool call hits Gate 3 in universal-gate-enforcer.py, which blocks until the agent runs a full `/kernel/anchor`. This reuses the existing infrastructure — no new gates, no new blocking mechanisms.

### Flow Diagram

```
Context approaches limit
    ↓
[AUTO] compaction triggers
    ↓
PreCompact hook fires
    ↓
Hook reads session_state.json
    ↓
Hook resolves workflow state file (agent-routed or domain)
    ↓
Hook sets anchored: false in workflow state
Hook writes compaction_anchor_reason to session_state.json
    ↓
Compaction executes (conversation summarized)
    ↓
Agent resumes with compacted context
    ↓
Agent's next Write/Edit/Bash tool call
    ↓
Gate 3 fires: "BLOCKED: Protocol not anchored"
    ↓
Agent runs /kernel/anchor (full ceremony)
    ↓
Protocol re-read, lessons re-read, context restored
    ↓
Agent proceeds with fresh protocol understanding
```

### State Fields

**PreCompact hook writes (workflow state):**
```json
{
  "anchored": false
}
```

**PreCompact hook writes (session_state.json, merge):**
```json
{
  "compaction_anchor_reason": "auto_compaction",
  "compaction_timestamp": "2026-07-21T20:00:00Z"
}
```

**After anchor completes (existing behavior):**
```json
{
  "anchored": true,
  "anchor_timestamp": "...",
  "actions_since_anchor": 0,
  "compaction_anchor_reason": null
}
```

### Hook Configuration (settings.local.json)

```json
{
  "hooks": {
    "PreCompact": [
      {
        "matcher": "auto|manual",
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/precompact-reanchor.py"
          }
        ]
      }
    ]
  }
}
```

### Hook Script Design (`precompact-reanchor.py`)

```python
#!/usr/bin/env python3
"""PreCompact hook: invalidate anchor so the next action triggers re-anchor."""
import json, sys
from pathlib import Path

HOOK_DIR = Path(__file__).resolve().parent
WORKSPACE = HOOK_DIR.parent.parent
STATE_DIR = WORKSPACE / '.claude' / 'state'
SESSION_STATE = STATE_DIR / 'session_state.json'

def main():
    data = json.load(sys.stdin)
    
    # Read session state
    ss = json.loads(SESSION_STATE.read_text(encoding='utf-8'))
    domain = ss.get('domain')
    if not domain:
        sys.exit(0)
    
    # Route to correct workflow file (agent-aware)
    agent_id = ss.get('agent_id')
    if agent_id:
        wf_file = STATE_DIR / f'agent-{agent_id}-workflow.json'
        if not wf_file.exists():
            wf_file = STATE_DIR / f'{domain}_workflow.json'
    else:
        wf_file = STATE_DIR / f'{domain}_workflow.json'
    
    wf = json.loads(wf_file.read_text(encoding='utf-8'))
    
    # Invalidate anchor
    wf['anchored'] = False
    wf_file.write_text(json.dumps(wf, indent=2), encoding='utf-8')
    
    # Record reason in session state
    ss['compaction_anchor_reason'] = data.get('source', 'unknown')
    ss['compaction_timestamp'] = data.get('timestamp', '')
    SESSION_STATE.write_text(json.dumps(ss, indent=2), encoding='utf-8')
    
    sys.exit(0)  # Don't block compaction — let it proceed

if __name__ == '__main__':
    main()
```

## Compatibility with Existing Gate Enforcer

The design is fully compatible with the existing universal-gate-enforcer.py:

| Gate | Impact | Compatible? |
|------|--------|-------------|
| Gate 1 (session_started) | No change — session is already started | Yes |
| Gate 2 (needs_learn) | No change — learn state unaffected | Yes |
| Gate 3 (anchored) | **This is the trigger** — PreCompact sets `anchored: false`, Gate 3 blocks next action | Yes — existing mechanism |
| Gate 4 (actions counter) | Counter resets to 0 after the forced anchor | Yes |
| Gate 5 (anchor token) | Only generated when counter hits limit, not for Gate 3 blocks | Yes — no token needed for compaction re-anchor |
| One-shot guard | One-shot agents skip Gate 3, so compaction re-anchor doesn't fire for them | Yes — correct behavior (one-shot agents rarely compact) |

No modifications to universal-gate-enforcer.py are required. The PreCompact hook only writes to existing state fields (`anchored`) that Gate 3 already checks. The entire re-anchor mechanism rides on existing infrastructure.

### Edge Cases

1. **Concurrent agents:** If multiple agents share `sr_dev_workflow.json` and one hits compaction, the `anchored: false` write affects all agents using that workflow file. Per-agent workflow routing (`agent_id` → `agent-{id}-workflow.json`) mitigates this — each agent has its own anchored state.

2. **Counter reset interaction:** After compaction-triggered re-anchor, `actions_since_anchor` resets to 0. The agent gets a fresh 30-action window. This is correct — the full protocol re-read justifies a counter reset.

3. **Manual `/compact`:** The hook uses `matcher: "auto|manual"`, so user-triggered compaction also forces re-anchor. This is desirable — manual compaction also degrades context.

4. **Rapid compaction:** If compaction fires frequently (very long session), the agent spends more time anchoring. This is a feature, not a bug — frequent compaction means frequent context loss, which demands frequent re-centering.
