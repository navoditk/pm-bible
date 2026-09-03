# Convexity

## One-line definition
The second-order (curvature) term in the price-yield relationship —
duration alone is the tangent line; convexity is how much the actual
curve bows away from that line.

## Formula
`dP/P ≈ -D_mod*dy + 0.5*C*dy^2`

`convexity(ytm, face, coupon_rate, years, frequency)` in
`src/pm/fixed_income/duration.py` computes `C` in closed form from the
bond's cash flows (verified against a finite-difference second
derivative of `bond_price` in `tests/test_fixed_income.py`).

## Interpretation
For a normal (option-free) bond, convexity is positive: it adds to price
gains when yields fall and cushions price losses when yields rise — pure
upside relative to a duration-only estimate. The `dy^2` term means this
effect is small for small yield moves and grows quickly for large ones.

## Why PMs care
Two bonds with the same duration can have different convexity — the more
convex one performs better in both a big rally and a big selloff, all
else equal, which is why the market prices convexity (more convex bonds
trade at a yield premium, i.e. lower yield, for the same duration).

## Common mistakes
- using duration alone for large yield shocks (>50-100bp), where the
  convexity term is no longer negligible
- assuming all instruments have positive convexity — MBS is the classic
  counterexample (`reference/fixed_income/mbs_convexity.md`)

## Related
duration, DV01, MBS negative convexity, curve trades.
