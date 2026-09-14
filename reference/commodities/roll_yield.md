# Commodity Futures Curves: Contango, Backwardation, Roll Yield

## One-line definition
Roll yield is the return earned (or lost) from replacing an expiring
futures contract with the next-dated one, driven by whether the futures
curve is upward-sloping (contango) or downward-sloping (backwardation).

## Formula
`roll_yield = (near_price - far_price) / far_price`

Positive in backwardation (`near_price > far_price`), negative in
contango (`near_price < far_price`).

## Why PMs care
Unlike a bond or equity, a commodity futures index's total return isn't
just spot price change — it's spot return *plus* roll yield. Two
commodities with identical spot performance can have very different
total returns if one curve is steeply contangoed and the other
backwardated.

## Worked example
Near contract at $80, far contract at $78 (backwardation):

`roll_yield = (80 - 78) / 78 ≈ +2.56%` — the position gains from rolling.

## Common mistakes
- evaluating a commodity investment on spot price alone and ignoring roll
- assuming a curve shape (contango vs. backwardation) is permanent —
  it reflects current storage costs, convenience yield, and near-term
  supply/demand, and can flip

## Related
- [FX carry (the FX analogue)](../fx/fx_carry.md)
- [Forward rates](../fixed_income/forward_rates.md)
