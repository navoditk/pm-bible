# Use Case — Swap DV01 Hedge

## PM question
The portfolio needs to shed 5 years of duration without selling cash bonds
(liquidity, tax, or index-tracking constraints). Size a pay-fixed swap to
do it.

## Concepts
swap DV01, hedge ratio, swap spread.

## First exercise
Portfolio DV01 = +$200,000/bp.
5-year swap DV01 = $43/bp per $1mm notional (from `swap_dv01`, `data/mock_curve.csv`'s 5Y `swap_rate`).

Hand-calculate the pay-fixed notional needed:
`notional_mm = hedge_ratio(portfolio_dv01, swap_dv01_per_mm)`

## Extend
Add the swap spread move as a second scenario: if swap spreads widen 10bp
while Treasury yields are unchanged, does the hedge's basis risk help or
hurt versus a Treasury-future hedge for the same DV01?

## Relevant reference pages
`reference/fixed_income/swap_dv01.md`  
`reference/fixed_income/swap_spread.md`
