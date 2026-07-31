# Venture-Loop System — Extraction Manifest

Everything needed to move the venture-loop system (the "assay" family) into its own repo. Paste this into the new repo and have the agent run the transfer script. Structure is preserved (same relative paths land in the new repo).

**Source** (SRC): `D:/my_ai_projects/project_test_repos/sr_dev_workspace`
**Dest** (DEST): the new repo root.

Verified against the filesystem on 2026-07-31 (commit 4a7517e). Counts exclude `__pycache__` and runtime `state/`.

## What moves (the corpus — 150 files)

| Group | Paths | Files |
|-------|-------|-------|
| Loop commands (27) | `.claude/commands/kernel/<unit>.md` | 27 |
| Loop skills (27) | `.claude/skills/<unit>/` (minus `state/`, `__pycache__`) | 70 |
| Design docs (3) | `.claude/docs/design/{assay,render,review-queue}/` | 16 |
| System data | `projects/assay/` source-of-truth (see below) | 37 |
| **Total** | | **150** |

### The 27 units (each has a command + a skill)
```
source assay competition deep-dive offer gtm launch operate sharpen
trends pain arbitrage assets gaps bookmarks
expand small lateral
data distribution platform productize license stack adjacent
render review-queue
```
- 9 spine loops: `source assay competition deep-dive offer gtm launch operate sharpen`
- 6 source hunters: `trends pain arbitrage assets gaps bookmarks`
- 3 reframe loops: `expand small lateral`
- 7 expansion angle-loops: `data distribution platform productize license stack adjacent`
- 2 infrastructure: `render` (the board engine) + `review-queue` (its consumer)

### projects/assay/ — what to keep vs drop
KEEP (source of truth):
- `projects/assay/roadmap.md`, `projects/assay/assay-design.md`, `projects/assay/loop-candidates.jsonl`
- `projects/assay/ventures/` (cross-loop venture records + INDEX)
- `projects/assay/EXTRACTION-MANIFEST.md` (this file)
DROP for a fresh start (run history — regenerated at runtime), or keep for continuity:
- `projects/assay/<loop>/runs/` and their `INDEX.md`

## What does NOT move (exclude)

- `**/state/` and `**/*ledger.jsonl` — per-loop run history (12 files). New repo creates fresh ledgers at runtime.
- `.claude/state/*` — runtime state (`render-session.json`, `render-sessions/`, `review-status.json`, etc.). Created on first run. The render + review-queue skills reference these paths; they self-create.
- `**/__pycache__`, `**/*.pyc`.
- Any `projects/competition/`, `projects/deep-dive/` stray run dirs (pre-consolidation leftovers) — superseded by `projects/assay/<loop>/`.

## CRITICAL — re-encode these outside the repo (they do NOT travel with a file copy)

1. **Auto-memory rules.** The loops reference `[[loop-output-lean]]`, `[[plain-vocabulary]]`, `[[render-board-responses]]`, `[[render-board-legend]]`. These live in per-project auto-memory (`~/.claude/projects/<proj>/memory/`), NOT in the repo. Without them the loops lose their hard rules. Re-encode into the new repo, e.g. a `.claude/references/venture-loop-conventions.md` (or the new repo's CLAUDE.md), stating:
   - Lean output: quickest view to the pertinent info, never long docs.
   - Plain vocabulary in all human-facing output (no jargon like fit/GO-IF/assay/wedge).
   - NO em dashes anywhere (a hard rule).
   - Respond through render boards (per-item Build / Test-first / Don't-build + a question box); every board carries a legend.
   - Unbiased ranking: fit-to-you is a displayed tag, never a ranker; rank on merit.

2. **`/acquire` is a parked candidate, not a bug.** It appears only in `sharpen/state/ledger.jsonl` as a self-extend candidate (count 1, queued for 2x promotion). No `/acquire` command/skill exists yet, by design. If you drop the sharpen ledger (run history), this reference goes with it. Do not "fix" it as a dead ref.

## Kernel dependency — one decision to make

The loops run as plain skills, but they were designed to run INSIDE a kernel session (anchor/hooks/gate enforcement). Two options:

- **Option A (corpus into an existing kernel repo):** the new repo already has, or will get, a kernel. Just drop the 150 corpus files in. Simplest.
- **Option B (self-contained kernel-governed repo):** also stand up a kernel. Do NOT copy this workspace's loaded kernel (it carries the QA domain protocol, QA lessons, and the `sr_dev` gate). Start from a FRESH minimal kernel (`D:/my_ai_projects/isagawa-kernel`) and add the corpus on top. Then the venture loops need at most a light domain protocol + the standard hooks.

The render engine itself (server + templates + adapter + launcher) is pure Python stdlib and needs no kernel.

## Transfer script (the new-repo agent runs this)

Set DEST to the new repo root, then run. Bash (Git Bash) version:

```bash
SRC="D:/my_ai_projects/project_test_repos/sr_dev_workspace"
DEST="<NEW_REPO_ROOT>"
UNITS="source assay competition deep-dive offer gtm launch operate sharpen trends pain arbitrage assets gaps bookmarks expand small lateral data distribution platform productize license stack adjacent render review-queue"

mkdir -p "$DEST/.claude/commands/kernel" "$DEST/.claude/skills" "$DEST/.claude/docs/design" "$DEST/projects/assay"

# 1. commands + skills (skills minus state/ and __pycache__)
for u in $UNITS; do
  cp "$SRC/.claude/commands/kernel/$u.md" "$DEST/.claude/commands/kernel/$u.md"
  mkdir -p "$DEST/.claude/skills/$u"
  (cd "$SRC/.claude/skills/$u" && find . -type f ! -path './state/*' ! -path '*/__pycache__/*' ! -name '*.pyc' \
     -exec sh -c 'mkdir -p "$2/$(dirname "$1")" && cp "$1" "$2/$1"' _ {} "$DEST/.claude/skills/$u" \;)
done

# 2. design docs (3)
for d in assay render review-queue; do
  mkdir -p "$DEST/.claude/docs/design/$d"
  (cd "$SRC/.claude/docs/design/$d" && find . -type f ! -path '*/__pycache__/*' ! -name '*.pyc' \
     -exec sh -c 'mkdir -p "$2/$(dirname "$1")" && cp "$1" "$2/$1"' _ {} "$DEST/.claude/docs/design/$d" \;)
done

# 3. projects/assay source of truth (roadmap, design, candidates, ventures, this manifest)
cp "$SRC/projects/assay/roadmap.md" "$SRC/projects/assay/assay-design.md" \
   "$SRC/projects/assay/loop-candidates.jsonl" "$SRC/projects/assay/EXTRACTION-MANIFEST.md" "$DEST/projects/assay/"
cp -r "$SRC/projects/assay/ventures" "$DEST/projects/assay/ventures"

# 4. (OPTIONAL) run history for continuity — omit for a fresh start
# for u in source assay competition deep-dive offer gtm launch operate sharpen expand small lateral; do
#   [ -d "$SRC/projects/assay/$u" ] && cp -r "$SRC/projects/assay/$u" "$DEST/projects/assay/$u"
# done

echo "Transfer done. Verify: 27 commands, 27 skill dirs, 3 design docs, projects/assay data."
```

Windows-native alternative (more reliable on Windows, run in cmd): use `robocopy "%SRC%\.claude\skills\%u" "%DEST%\.claude\skills\%u" /E /XD __pycache__ state /XF *.pyc` per unit, plus `copy` for the command files.

## Post-transfer verification (run in the new repo)

```bash
echo "commands: $(ls .claude/commands/kernel/ | grep -cE '^(source|assay|competition|deep-dive|offer|gtm|launch|operate|sharpen|trends|pain|arbitrage|assets|gaps|bookmarks|expand|small|lateral|data|distribution|platform|productize|license|stack|adjacent|render|review-queue)\.md$') (expect 27)"
echo "skill dirs: $(for u in source assay competition deep-dive offer gtm launch operate sharpen trends pain arbitrage assets gaps bookmarks expand small lateral data distribution platform productize license stack adjacent render review-queue; do [ -d .claude/skills/$u ] && echo x; done | wc -l) (expect 27)"
echo "design docs: $(ls -d .claude/docs/design/{assay,render,review-queue} 2>/dev/null | wc -l) (expect 3)"
# render engine smoke test (pure stdlib, no kernel needed):
python .claude/skills/render/templates/leaderboard/generate.py <(echo '{"title":"t","lead":"l","items":[]}') /tmp/rtest && echo "render generate: OK"
```
