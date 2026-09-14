# Strategic and Tactical Asset Allocation

## One-line definition
Strategic asset allocation (SAA) is the long-run "policy portfolio" —
asset-class weights set from an investor's return objective, risk
tolerance, and long-run capital market expectations; tactical asset
allocation (TAA) is a deliberate, usually short-lived, deviation from
that policy portfolio to exploit a near-term view.

## Vocabulary
- **Policy portfolio**: SAA's other name — the weights an investor would
  hold absent any short-term view, the baseline everything else is
  measured against.
- **Active risk / active return from TAA**: TAA weights minus SAA
  weights is exactly an [active weight](../concepts/tracking_error.md)
  in the same sense a stock-picker's active weight is measured against a
  benchmark — the policy portfolio *is* the benchmark here.
- **Rebalancing**: distinct from TAA — rebalancing trades back *toward*
  the policy weights after market moves drift them away; TAA
  deliberately trades *away* from policy weights on a view.

## Why PMs care
This is the top-down decision that determines most of a multi-asset
portfolio's return and risk before any single-security selection
happens — the SAA/TAA split is exactly asking "how much of what we do is
a long-run structural bet (SAA) versus a shorter-run market-timing bet
(TAA)?" Every optimization tool already in this repo is the *engine* for
setting SAA: `efficient_frontier` and `max_sharpe` translate long-run
capital market expectations into policy weights the same way they'd
translate any other expected-return/covariance inputs into an optimal
portfolio; `black_litterman_posterior` is the standard way TAA views get
blended with the market-implied equilibrium prior without those views
dominating the whole portfolio; `risk_parity_weights` and
`scenario_robust_weights` are alternative approaches to setting the same
policy-level weights when point-estimate expected returns are
distrusted. Nothing new needs to be built here — SAA/TAA is a framing
for how this repo's existing optimization machinery gets used in
practice, not a separate calculation.

## Why this isn't a new `src/pm` function
There's no new formula: SAA is [mean-variance
optimization](mean_variance_optimization.md) (or
[Black-Litterman](black_litterman.md), [risk
parity](risk_parity.md), etc.) run once, at a long horizon, on
asset-class-level inputs; TAA is the same tools run again at a shorter
horizon with updated near-term views, then compared back against the SAA
weights the same way `active_weights` compares a portfolio to a
benchmark. Building a distinct "asset_allocation" function would just be
re-wrapping functions this repo already has under a new name.

## Common mistakes
- treating TAA as "the active part" and SAA as "the passive part" — SAA
  is itself an active decision (choosing *which* long-run weights), just
  a much lower-turnover one than TAA
- sizing TAA bets without reference to the SAA policy weights they're
  deviating from — a TAA tilt only means something relative to what the
  policy portfolio would otherwise hold
- confusing TAA with rebalancing — rebalancing restores policy weights
  after drift; TAA deliberately abandons them on a view. A portfolio can
  do both at the same time for different reasons

## Related
- [Mean-variance optimization](mean_variance_optimization.md)
- [Efficient frontier and tangency portfolio](efficient_frontier.md)
- [Black-Litterman](black_litterman.md)
- [Risk parity](risk_parity.md)
- [Liability-driven investing](liability_driven_investing.md)

## Free resources
- [Strategic Implementation Choices — AnalystPrep (CFA Level III)](https://analystprep.com/study-notes/cfa-level-iii/strategic-implementation-choices/) — the policy-portfolio framing and how TAA deviates from it
