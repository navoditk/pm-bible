# Factor Risk

## One-line definition
Splitting portfolio variance into systematic (factor) risk and idiosyncratic (specific) risk.

## Formula
Given factor exposures `B` (assets x factors), factor covariance `F`, and
specific variances `d`:

`Sigma = B F B^T + diag(d)`

## Why PMs care
It explains *why* a portfolio is exposed to risk (value, momentum, rates,
credit) rather than just *how much*, and lets a PM budget/limit risk by
factor rather than by name.

## Code recipe
```python
def factor_model_covariance(exposures, factor_covariance, specific_variance):
    B = np.asarray(exposures, float)
    F = np.asarray(factor_covariance, float)
    d = np.asarray(specific_variance, float)
    return B @ F @ B.T + np.diag(d)
```

## Common mistakes
- double-counting risk already captured by a factor as specific risk
- treating factor exposures as static when they drift over time

## Related concepts
tracking error, risk contribution, factor risk contribution, mean-variance optimization.
