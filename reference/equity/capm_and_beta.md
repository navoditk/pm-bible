# CAPM and Beta

## One-line definition
The Capital Asset Pricing Model prices a stock's required return as the
risk-free rate plus its beta (systematic risk relative to the market)
times the equity risk premium.

## Formula
`beta = Cov(r_stock, r_market) / Var(r_market)`

`E[r] = r_f + beta * (E[r_market] - r_f)`

Jensen's alpha: realized return minus what CAPM predicted — the standard
risk-adjusted skill measure.

## Why PMs care
Beta is the equity analog of duration: a single number summarizing how
much of the market's risk a position carries. CAPM's expected return is
the standard required-return input into the DDM and justified-P/E
formulas elsewhere in this folder, and Jensen's alpha is a first-pass
"did this manager add value beyond just taking market risk" check.

## Common mistakes
- confusing beta (systematic risk only) with total volatility — a
  high-beta stock can have lower total vol than a low-beta,
  high-idiosyncratic-vol stock (see `factor_model_covariance` in
  `src/pm/factors.py` for the systematic/specific split)
- estimating beta over an unstable or too-short window and then treating
  it as fixed going forward

## Limitations
`beta()` here is a plain OLS regression coefficient over whatever return
series you pass in — no shrinkage toward 1.0 (as Bloomberg-style adjusted
betas do), no multi-factor decomposition. See `equity_factor_investing.md`
for the fuller multi-factor picture CAPM is a special (one-factor) case
of.

## Related
Dividend discount model, equity factor investing, factor risk
(`reference/concepts/factor_risk.md`).
