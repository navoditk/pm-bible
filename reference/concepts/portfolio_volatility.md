# Portfolio Volatility

## Formula
`sigma_p = sqrt(w^T Sigma w)`

## Why PMs care
It summarizes total portfolio return dispersion under the covariance model.

## Two-asset form
`sigma_p^2 = w1^2 sigma1^2 + w2^2 sigma2^2 + 2 w1 w2 rho12 sigma1 sigma2`

## Code recipe
```python
def portfolio_volatility(weights, covariance):
    w = np.asarray(weights, float)
    cov = np.asarray(covariance, float)
    return float(np.sqrt(w @ cov @ w))
```

## Invariant
Variance should be non-negative up to numerical tolerance.
