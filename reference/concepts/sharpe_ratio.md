# Sharpe Ratio

## One-line definition
Excess return per unit of total volatility.

## Formula
`Sharpe = (mean(r) - rf) / std(r)`

Annualized: multiply by `sqrt(periods_per_year)`.

## Units
Dimensionless (a ratio), typically quoted annualized.

## Why PMs care
It is the standard single-number summary of risk-adjusted performance, used to compare strategies with different volatility.

## Worked example
Annual returns of 2%, 4%, 3% against a 0% risk-free rate:

`mean = 0.03`, `std = 0.01` (sample, ddof=1) -> `Sharpe = 3.0`

## Code recipe
```python
import numpy as np

def sharpe_ratio(returns, risk_free_rate=0.0, periods_per_year=12):
    r = np.asarray(returns, float)
    excess = r - risk_free_rate / periods_per_year
    std = excess.std(ddof=1)
    return float(excess.mean() / std * np.sqrt(periods_per_year))
```

## Common mistakes
- mixing annualized and periodic risk-free rates
- using population std (`ddof=0`) inconsistently across tools
- comparing Sharpe ratios computed over different sampling frequencies without annualizing both

## Limitations / approximations
- Penalizes upside volatility the same as downside volatility.
- Unstable with few observations or fat-tailed/skewed return distributions.
- Says nothing about drawdown path or tail risk — pair with [drawdown](drawdown.md).

## Related
- [Portfolio volatility](portfolio_volatility.md)
- [Drawdown](drawdown.md)

## Free resources
- MIT OCW Portfolio Theory I–III
- [Portfolio foundations resources](../../resources/portfolio_foundations.md)
