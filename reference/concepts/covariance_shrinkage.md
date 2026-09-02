# Covariance Shrinkage (Robust Covariance)

## One-line definition
Blending the noisy sample covariance matrix with a more stable, structured
target to reduce estimation error, at the cost of some bias.

## Formula
`Sigma_shrunk = shrinkage * Target + (1 - shrinkage) * Sigma_sample`

This repo's `shrink_covariance` uses a diagonal target (correlations
shrunk to zero, variances preserved) — a simple, standard choice.

## Why PMs care
Sample covariance from a short history is noisy, especially for large
asset universes — `mean_variance`/`minimum_variance` optimizers are
notoriously sensitive to that noise, often producing extreme, unstable
weights ("optimizer error maximization"). Shrinkage is the cheapest fix.

## Common mistakes
- shrinking to 100% (shrinkage=1) and losing all correlation information,
  as blindly "safe" as full shrinkage feels
- not shrinking at all with a small sample and short history relative to
  the number of assets

## Limitations
This repo implements linear shrinkage to a diagonal target, chosen for a
fixed `shrinkage` value. The Ledoit-Wolf method (which *estimates* the
optimal shrinkage intensity from the data) is the more sophisticated
standard approach and is not implemented here.

## Related
mean-variance optimization, Black-Litterman, risk parity.
