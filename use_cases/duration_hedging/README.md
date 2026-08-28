# Use Case — Duration Hedging

## PM question
The portfolio has excess rate sensitivity. How much DV01 must be removed?

## Concepts
duration, DV01, hedge instrument DV01, hedge ratio.

## First exercise
Portfolio DV01 = +$120,000/bp.
Hedge instrument DV01 = +$80/bp per unit.

Hand-calculate required short units:
`units = portfolio_DV01 / hedge_DV01_per_unit`

## Extend
Add key-rate durations and show why a single-duration hedge can leave curve basis risk.
