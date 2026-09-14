# Covariance

## One-line definition
Covariance measures how two return series move together in absolute return units.

## Why PMs care
Portfolio risk depends on cross-asset covariance, not only standalone volatility.

## Formula
`Cov(X,Y) = E[(X-E[X])(Y-E[Y])]`

Correlation normalizes covariance:
`rho_xy = Cov(X,Y)/(sigma_x sigma_y)`

## Units
Covariance has squared-return units; correlation is unitless.

## Core PM intuition
Diversification is produced by imperfect co-movement.

## Code recipe
```python
cov = returns.cov()
corr = returns.corr()
```

## Common mistake
Treating a large number of holdings as synonymous with diversification.

## Related
- [Portfolio volatility](portfolio_volatility.md)
- [Risk contribution](risk_contribution.md)
