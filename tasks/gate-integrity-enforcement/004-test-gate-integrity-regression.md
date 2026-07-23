# Task 004: Gate-Integrity Regression
**Type:** TEST | **Gates:** GI-04
## Action
Write + RUN a live regression test for the three gate-integrity helpers.
## Spec
Throwaway fixtures under mktemp. Three cases: (a) SIMULATED/EMPTY gate evidence -> the classifier (001) REJECTS it (returns simulated/empty defect); (b) a fixture with a relative DATABASE_URL + no PYTHONPATH -> the linter (002) FLAGS it, and a 223-style portable fixture passes clean; (c) an HTML string with `max-width:100%` inside a <style> block -> strip_markup_then_grep (003) does NOT fire on it, but the SAME helper DOES fire on a real absolute claim ('100% accurate') in body text. Portable (absolute paths, explicit PYTHONPATH). LIVE runs, not simulations.
## Acceptance
3/3 regression cases pass live: simulated/empty rejected, relative-DB flagged, CSS-100% not-FP but real-claim caught.
