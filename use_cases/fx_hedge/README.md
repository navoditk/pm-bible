# Use Case — FX Hedge

## PM question
A USD-based fund holds €10,000,000 of EUR-denominated bonds. Should the
currency exposure be hedged back to USD, and what does that hedge cost?

## Concepts
covered interest parity, FX forward rate, FX carry, hedge sizing.

## First exercise
Spot = 1.10 (USD/EUR), `r_USD = 5%`, `r_EUR = 3%`, hedge horizon = 1 year.

Hand-calculate:
1. the 1-year forward rate (`pm.fx.fx_forward_rate`)
2. the carry given up by hedging (`pm.fx.fx_carry`) — is it positive or
   negative for a USD investor here, and why?
3. the forward notional needed to fully hedge the €10,000,000 exposure
   (reuse `pm.fixed_income.duration.hedge_ratio` — for a 1:1 forward
   contract, the "hedge instrument DV01" is just 1 unit of notional, so
   the hedge ratio reduces to the exposure itself)

## Extend
Reprice the hedge if `r_EUR` rises to 4.5% (EUR rates catching up to USD)
— does the forward rate move toward or away from spot, and what happens
to the cost of staying hedged? See `reference/fx/spot_and_forward.md` and
`fx_carry.md`.
