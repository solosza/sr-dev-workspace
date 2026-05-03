# Research Flight 1: Haneda → Ho Chi Minh City

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001

## Requirements
- Search for one-way flights from Haneda (HND), Japan to Ho Chi Minh City (SGN), Vietnam
- Must arrive at SGN by 5/13 1:00 PM local time (ICT, UTC+7)
- Find the best price + best airline combination
- Check multiple sources: Google Flights, Skyscanner, Kayak, airline direct
- Compare: price, airline, departure time, arrival time, layovers, duration
- Write results to `projects/vietnam-trip/flight1-hnd-sgn.md` with:
  - Top 3-5 options in a comparison table
  - Airline, flight number, departure time, arrival time, layovers, price
  - Recommendation for best value option

## Acceptance Criteria
- [ ] `test -f "projects/vietnam-trip/flight1-hnd-sgn.md"` exits 0
- [ ] File contains at least 3 flight options with pricing
- [ ] All options arrive at SGN by 1:00 PM local on 5/13

## Gates Satisfied
- RESEARCH-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
