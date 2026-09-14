# Value at Risk (VaR) and Expected Shortfall (ES)

## One-line definition
VaR: the loss not expected to be exceeded over a horizon at a given
confidence level. ES: the average loss *given* that VaR is breached.

## Formula (parametric / Gaussian)
`VaR = PortfolioValue * sigma * z`

`ES = PortfolioValue * sigma * phi(z) / (1 - confidence)`

where `z = norm.ppf(confidence)`, `phi` is the standard normal density, and
`sigma` is portfolio volatility over the same horizon as the desired VaR.

## Units
Currency, over the same horizon as `sigma` (e.g. daily volatility gives
daily VaR).

## Why PMs care
VaR/ES turn a distribution of possible outcomes into a single risk-limit
number a mandate or regulator can cap.

## Worked example
`PortfolioValue = $1,000,000`, daily `sigma = 2%`, `confidence = 95%`:

`z ≈ 1.6449` → `VaR ≈ $32,897`

`ES ≈ $41,254` (always larger than VaR at the same confidence — it's an
average over the worse tail, not a single percentile).

## Common mistakes
- treating VaR as the worst-case loss — by construction, 5% of outcomes
  (at 95% confidence) are worse than VaR
- mixing volatility and confidence horizons/periods that don't match
- ignoring fat tails: real return distributions breach parametric VaR more
  often than the Gaussian assumption predicts

## Limitations
This is the parametric (delta-normal) method only. It assumes returns are
normally distributed with no autocorrelation — historical simulation and
Monte Carlo VaR relax that assumption but aren't implemented here.

## Related
- [Portfolio volatility](portfolio_volatility.md)
- [Stress testing](stress_testing.md)
