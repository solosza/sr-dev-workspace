# Write Booking Recommendation

## Type
BUILD

## Execution
inline

## Dependencies
- 002, 003

## Requirements
- Read `projects/vietnam-trip/flight1-hnd-sgn.md` and `projects/vietnam-trip/flight2-dad-lax.md`
- Write `projects/vietnam-trip/recommendation.md` with:
  - Summary of recommended flight for each leg
  - Total estimated cost (both legs combined)
  - Booking platform recommendation for each flight
  - Any time-sensitive notes (price trends, seat availability)
  - Action items for the user (what to book, where, by when)

## Acceptance Criteria
- [ ] `test -f "projects/vietnam-trip/recommendation.md"` exits 0
- [ ] File contains recommended flight for both legs
- [ ] File contains total estimated cost

## Gates Satisfied
- BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
