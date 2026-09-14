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

`posterior_cov` here is the covariance of the *estimated mean itself*, not
a posterior return covariance — don't pass it straight into an optimizer
in place of `Sigma` (it's smaller by roughly a factor of `tau`, which
would make the optimizer far too confident). Use `Sigma` itself, or
`Sigma + posterior_cov`, as the optimizer's covariance input.

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
- passing `black_litterman_posterior`'s second return value straight into
  an optimizer as the covariance — see the note above
- reverse-optimizing a prior with one `risk_aversion` and then
  re-optimizing with a *different* one — the round trip back to market
  weights only holds at the same `risk_aversion` on both sides, see
  [mean-variance optimization](mean_variance_optimization.md)

## Related
- [Covariance shrinkage](covariance_shrinkage.md)
- [Mean-variance optimization](mean_variance_optimization.md)
- [Risk parity](risk_parity.md)
