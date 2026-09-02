# Use Case — Treasury Futures Hedge

## PM question
The portfolio's DV01 is too high going into an event risk window. Hedge it
with liquid Treasury futures instead of trading cash bonds.

## Concepts
futures DV01, conversion factor, hedge ratio.

## First exercise
Portfolio DV01 = +$120,000/bp.
CTD bond DV01 per contract = $145/bp, conversion factor = 0.92.

Hand-calculate:
1. `futures_dv01 = futures_dv01_per_contract(ctd_dv01_per_contract, conversion_factor)`
2. `contracts = hedge_ratio(portfolio_dv01, futures_dv01)`

## Extend
The cheapest-to-deliver bond changes as yields move. Re-run the hedge with
a different CTD DV01/conversion factor and show how many contracts of
hedge drift result — purely from the CTD switch, with no trading.

## Relevant reference pages
`reference/fixed_income/treasury_futures_hedging.md`
