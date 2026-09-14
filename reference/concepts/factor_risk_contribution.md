# Factor Risk Contribution

## One-line definition
How much of total portfolio variance comes from factor (systematic) exposure
versus specific (idiosyncratic) risk.

## Formula
Portfolio factor exposure: `e = w^T B`

Factor variance contribution: `e^T F e`

Specific variance contribution: `sum(w_i^2 * d_i)`

These two sum to total portfolio variance under the [factor model](factor_risk.md).

## Why PMs care
Two portfolios with identical total volatility can have very different
splits — one dominated by factor bets, the other by idiosyncratic,
single-name risk. That split changes how you'd hedge or diversify it.

## Code recipe
```python
def portfolio_factor_exposure(weights, exposures):
    return np.asarray(weights, float) @ np.asarray(exposures, float)

def factor_variance_contribution(weights, exposures, factor_covariance):
    e = portfolio_factor_exposure(weights, exposures)
    F = np.asarray(factor_covariance, float)
    return float(e @ F @ e)

def specific_variance_contribution(weights, specific_variance):
    w = np.asarray(weights, float)
    return float(np.sum(w**2 * np.asarray(specific_variance, float)))
```

## Common mistakes
- forgetting the two contributions only sum to total variance under the
  same `exposures`/`factor_covariance`/`specific_variance` used to build
  the portfolio's covariance matrix in the first place
- comparing factor exposure across portfolios without checking they share
  the same factor definitions

## Related
- [Factor risk](factor_risk.md)
- [Risk contribution](risk_contribution.md)
- [Tracking error](tracking_error.md)
