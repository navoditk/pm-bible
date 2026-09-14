# Equity Factor Investing

## One-line definition
Explaining and targeting stock returns through style characteristics —
value, size, momentum, quality, low-volatility — rather than, or in
addition to, single-market beta.

## Why PMs care
CAPM's single market factor explains only part of the cross-section of
stock returns; style factors explain much of the rest, and are exactly
the exposures a long-only active manager is usually taking, intentionally
or not. `style_tilt` in `src/pm/equity/factors.py` measures an active bet
on one factor the same way `active_share` measures the whole portfolio's
total active bet.

## What's implemented here
Given factor scores you already have (e.g. a value z-score per holding),
reuse `pm.factors.portfolio_factor_exposure(weights, factor_scores)` to
get the portfolio's exposure to one style factor, then
`style_tilt(portfolio_exposure, benchmark_exposure)` for the active bet
versus benchmark. `pm.factors.factor_model_covariance` /
`factor_variance_contribution` — the same functions used for the generic
Phase 4 risk-model work — then price the risk of that tilt once you have
a factor covariance matrix.

## Why the factor *scores themselves* aren't computed here
Turning raw fundamentals (P/B, trailing 12-month return, ROE, realized
vol, market cap) into clean, cross-sectionally comparable factor scores
needs winsorization, sector-neutralization, and standardization choices
that are judgment calls, not a single formula — and a real multi-factor
risk model (Barra/Axioma-style) additionally needs a cross-sectional
regression to estimate factor returns each period. That's materially
bigger than this repo's other "small transparent function" building
blocks, in the same class as
[hierarchical risk parity](../concepts/hierarchical_risk_parity.md) — a
conceptual placeholder here, not a shaky implementation.

## Common mistakes
- treating "factor investing" as only value/growth — momentum, quality,
  and low-volatility are equally standard style factors with their own
  well-documented premia and drawdowns
- forgetting that a large `active_share` and a large single-factor
  `style_tilt` are different things: a portfolio can be very active while
  still roughly factor-neutral, or vice versa

## Related
- [Active share](active_share.md)
- [CAPM and beta](capm_and_beta.md)
- [Factor risk](../concepts/factor_risk.md)
- [Factor risk contribution](../concepts/factor_risk_contribution.md)
