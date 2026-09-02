# Risk Parity

## One-line definition
Weighting a portfolio so every asset contributes equally to total risk,
rather than equally to capital (equal-weight) or by expected return
(mean-variance).

## Formula
Solved via the standard convex reformulation (Maillard, Roncalli,
Teiletche 2010):

`minimize 0.5 * w'*Sigma*w - sum(log(w_i))`, then renormalize `w` to sum
to 1.

This is equivalent to equal component risk contribution
(`component_risk_contribution` from `reference/concepts/risk_contribution.md`)
without needing to solve the equal-contribution condition directly.

## Why PMs care
A capital-weighted 60/40 portfolio is not risk-balanced — equities
typically dominate total risk despite being a minority of capital
allocation. Risk parity is the explicit fix: lower-vol assets (like
bonds) get more capital weight so their risk contribution matches
higher-vol assets.

## Worked example
Verified in `tests/test_robust.py`: with two uncorrelated assets at equal
volatility, risk parity gives 50/50 weights (matches equal-weight, as
expected). With asset 2 at 2x the volatility of asset 1, risk parity
weights ~2:1 toward asset 1 — and the resulting component risk
contributions are equal, confirming the property.

## Common mistakes
- assuming risk parity means equal *weights* — it means equal risk
  *contribution*, which is only the same thing when assets have equal
  volatility and zero correlation
- ignoring that risk parity often implies leveraging lower-vol assets
  (like bonds) to bring their risk contribution up to match equities

## Related
risk contribution, mean-variance optimization, covariance shrinkage.
