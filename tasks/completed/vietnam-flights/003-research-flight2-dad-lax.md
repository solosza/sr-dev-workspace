# Research Flight 2: Da Nang → Los Angeles

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001

## Requirements
- Search for one-way flights from Da Nang (DAD), Vietnam to Los Angeles (LAX) on 5/21
- Preferred: Starlux Airlines flight 704 (DAD → LAX)
- Check Starlux direct (https://www.starlux-airlines.com) for pricing and availability
- If Starlux 704 available: get exact price, departure/arrival times, any layover details
- Also check alternatives: Google Flights, Skyscanner, Kayak for comparison
- Write results to `projects/vietnam-trip/flight2-dad-lax.md` with:
  - Starlux 704 details and pricing (if available)
  - Top 3-5 alternative options in a comparison table
  - Airline, flight number, departure time, arrival time, layovers, price
  - Clear recommendation: Starlux 704 if reasonably priced, or best alternative

## Acceptance Criteria
- [ ] `test -f "projects/vietnam-trip/flight2-dad-lax.md"` exits 0
- [ ] File contains Starlux 704 pricing/availability OR explanation of why unavailable
- [ ] File contains at least 2 alternative options with pricing

## Gates Satisfied
- RESEARCH-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
