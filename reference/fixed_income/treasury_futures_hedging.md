# Treasury Futures Hedging

## One-line definition
Using Treasury futures to hedge portfolio rate risk without trading the
cash bond.

## Approximation
Futures DV01 per contract ≈ cheapest-to-deliver (CTD) bond's DV01 divided
by its conversion factor — `futures_dv01_per_contract` in
`src/pm/fixed_income/futures.py`. Then size the hedge with `hedge_ratio()`
same as any other instrument.

## Why PMs care
Futures are liquid and capital-efficient relative to trading the underlying
cash Treasury, making them a common first choice for duration hedges.

## Limitations
Ignores the delivery option value and the risk that the cheapest-to-deliver
bond changes as yields move — both make realized futures DV01 drift from
this static approximation.

## Related
- [Swap DV01](swap_dv01.md)
- [DV01](dv01.md)
