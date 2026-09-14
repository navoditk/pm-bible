# Regime-Aware Allocation

## One-line definition
Adjusting portfolio construction based on which market regime (e.g.
high/low volatility, risk-on/risk-off) is currently in effect, rather
than using one covariance/return estimate across all history.

## The easy 90% and the hard 10%
*Given* a regime label for each historical period, "regime-conditional
covariance" is nothing new — it's just `covariance()` computed on the
subset of returns matching that regime, then optimizing (via
`minimum_variance`, `risk_parity_weights`, etc.) with that regime-specific
input. No new machinery needed there.

## Why this isn't implemented in `src/pm`
The hard part — *detecting* which regime the market is currently in, or
was in historically — needs real statistical machinery (Hidden Markov
Models, Markov-switching models, or similar unsupervised regime
detection) that this repo doesn't build. Without that, "regime-aware"
degrades to manually labeling periods by hindsight, which isn't a usable
PM tool.

## Why PMs care
Correlations and volatilities are famously regime-dependent — the
"diversification" a covariance matrix promises in calm markets often
evaporates exactly when a portfolio needs it most, in a crisis regime
where correlations spike toward 1.

## Related
- [Covariance shrinkage](covariance_shrinkage.md)
- [Stress testing](stress_testing.md)
- [Scenario-robust optimization](scenario_robust_optimization.md)
