# Spread Duration

## One-line definition
Approximate price sensitivity to a change in credit spread.

## Approximation
`dP/P ≈ -SpreadDuration * dSpread`

## PM interpretation
A portfolio can be short Treasury duration yet long credit/spread duration.

## Limitations
Spread moves can coincide with Treasury moves, liquidity changes, default repricing, and convex effects.

`spread_pnl` in `src/pm/fixed_income/credit.py` takes spread duration as a
given input, the same way `key_rate_return_approximation` takes KRD as
given — nothing here derives spread duration from a bond's OAS
sensitivity to spread. A full treatment needs the same option-adjusted
machinery already called out as conceptual-only in `oas.md`.
