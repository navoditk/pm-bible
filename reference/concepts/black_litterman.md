# Black-Litterman

## One-line definition
A way to build expected returns by blending a market-implied equilibrium
(the "prior") with the PM's own views, weighted by how confident each view
is — rather than plugging raw historical-mean returns into an optimizer.

## Formula
Prior (market-implied, via reverse optimization):

`pi = risk_aversion * Sigma @ w_market`

Posterior (combining prior with views `P`, `Q`, `Omega`):

`posterior_cov = [(tau*Sigma)^-1 + P'*Omega^-1*P]^-1`

`posterior_mean = posterior_cov @ [(tau*Sigma)^-1 @ pi + P'*Omega^-1*Q]`

## Why PMs care
Feeding raw historical average returns straight into a mean-variance
optimizer is exactly what produces the extreme, unstable weights
`mean_variance` is known for — small differences in estimated returns
swing weights wildly. Black-Litterman anchors to a defensible market
prior and only tilts away from it where the PM has an actual view, sized
by how confident they are.

## Worked example
Verified in `tests/test_robust.py`: a view with near-infinite uncertainty
(`Omega` huge) leaves the posterior equal to the prior; a highly confident
view pulls the posterior toward the view (and spills over to correlated
assets through `Sigma`).

## Common mistakes
- setting `Omega` too small (overconfidence) and effectively overriding
  the market prior with an unvalidated view
- forgetting views on one asset spill over to correlated assets via
  `Sigma` — a single-asset view can move the whole posterior

## Related
covariance shrinkage, mean-variance optimization, risk parity.
