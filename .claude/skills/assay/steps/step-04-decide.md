# Step 4: Decide

## Purpose

Intersect the three verdicts and hand back a ranked shortlist for the human commit. This is the only HITL point: Assay presents, the human decides which wedge (if any) to actually pursue.

## Input

- Step 1 `Wedge[]` + Step 2 `BuildVerdict[]` + Step 3 `ValidationResult[]`
- Canonical reference: `.claude/docs/design/assay/references/io-contracts.md` (Decision)
- `.claude/docs/design/assay/references/state-schema.md` (the ledger record shape)
- Contract: `contracts/step-04-contract.json`

## Output

- `Decision` — `{ idea_ref, shortlist[], committed_wedge? }` — and the full run appended to `state/ledger.jsonl`.

## Acceptance Criteria

- [ ] Green light computed as market (survived Step 1) AND build (Step 2 = build) AND demand (Step 3 = pass) — all three
- [ ] Two-of-three = park, not go
- [ ] Shortlist ranked by (speed-to-first-dollar x defensibility x reuse-with-existing-builds)
- [ ] Each shortlisted wedge names one precondition to clear first
- [ ] Any ambiguous gate from Steps 1-3 surfaced for the human call
- [ ] Run persisted in ALL THREE layers: readable report in `projects/assay/runs/`, one appended line in `state/ledger.jsonl`, one row in `projects/assay/runs/INDEX.md` (a re-run never overwrites a prior report)
- [ ] No action taken — the commit is left to the human
- [ ] **Presented in PLAIN LANGUAGE for a non-technical reader** (see Output Style below) — the ledger keeps the typed/jargon form; the human-facing answer does not

## Output Style (human-facing — MANDATORY)

The typed `Decision`/contract shapes are for the ledger. What you SHOW the human must read like a sharp advisor talking to a smart non-technical founder — not a data dump.

Rules:
- **No jargon, no contract field names, no big grids of columns.** Say "the idea," "who'd pay," "why it wins or dies," "the cheapest way to find out."
- **Lead with the verdict in one plain sentence** ("Your original plan is too crowded to win; here's the one version that could.").
- For each idea worth keeping, write a short titled blurb: *what it is* (1 line a layperson gets) -> *why it could work* -> *the one thing that would kill it* -> *the cheapest test to know* (with a number and a deadline).
- Name the killed ideas in one line each with the plain reason ("everyone already does this, no way to stand out").
- End with **one clear question**: which one do you want to chase, park, or drop.
- Short sentences. A busy person should get the whole thing in under two minutes. Tables only if they genuinely make it *easier* to read (max 3-4 columns, plain words in the cells).

## References

- [[../references/INDEX]] -> design doc `references/io-contracts.md`, `references/state-schema.md`

## Procedure

1. **Green light** = market (survived Step 1) x build (Step 2 = build) x demand (Step 3 = pass). Two-of-three -> park.
2. **Rank** green-lit wedges by (speed-to-first-dollar x defensibility x reuse-with-existing-builds).
3. **PERSIST THE RUN (mandatory — 3 layers, so no run is ever lost):**
   a. **Readable report** -> `projects/assay/runs/<YYYY-MM-DD>-<idea-slug>.md`. Contains: (1) the full PLAIN-LANGUAGE writeup (per Output Style above); (2) a **"Every idea this run (good & bad)"** section — the COMPLETE list of wedges generated, survivors AND killed, each as a one-line pitch + verdict + plain reason (this is the content-fodder list — e.g. for a hustle round-up; never truncate it to just survivors); (3) a short "Under the hood" section (verdicts, boxed tests). This is the human artifact. If a report for the same date+slug exists (a re-run), suffix `-2`, `-3`, ... — never overwrite a prior run.
   b. **Ledger line** -> append ONE JSON record (idea incl. normalized, wedges, build_verdicts, validations, decision, committed_wedge, ts, and the report path) to `.claude/skills/assay/state/ledger.jsonl`. Machine index + the substrate the prior-art check (Step 1) reads.
   c. **Index row** -> append/update a row in `projects/assay/runs/INDEX.md` (table: date · idea · verdict · best wedge · link to the report). Create the file with a header if it doesn't exist.
   Write files with plain UTF-8 (no BOM). All three must land before presenting.
4. **Present** the ranked shortlist in plain language (Output Style) + each wedge's single precondition-to-clear-first, plus any ambiguous gate flagged upstream. Tell the human where the run was saved (the report path).
5. **HITL:** the human picks which wedge (if any) to actually pursue — the only real-world commit. Record the choice in `committed_wedge` (append the update; do not mutate the prior ledger record — append-only).

## Verification

- Output validates against `contracts/step-04-contract.json` (shape + three-of-three + ranked + precondition + no-act + ledger rules)
- All three persistence layers landed: the report file exists under `projects/assay/runs/`, the ledger has exactly one new appended record (with the report path), and INDEX.md has a matching new row
- The human-facing presentation is plain-language (no contract field names / jargon dumps)

## Failure Recovery

- If the ledger append fails, the run is not complete — retry the append before presenting (the audit trail is mandatory).
- If nothing green-lights, present the parked/killed set with reasons — a clean "no go" is a valid, useful outcome.
- If the human defers, leave `committed_wedge: null`; the shortlist persists in the ledger for a later commit.
