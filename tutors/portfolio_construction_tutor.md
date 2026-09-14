# Portfolio Construction Tutor

Coverage:
- mean–variance optimization
- expected returns
- covariance
- constraints
- active risk
- factor models
- transaction costs (`reference/concepts/transaction_costs_and_rebalancing.md`)
- robust construction: covariance shrinkage, Black-Litterman, risk parity,
  scenario-robust optimization (`reference/concepts/covariance_shrinkage.md`,
  `black_litterman.md`, `risk_parity.md`, `scenario_robust_optimization.md`)

Conceptual only, not implemented as code: hierarchical risk parity,
regime-aware allocation, multi-period optimization, strategic/tactical
asset allocation (SAA/TAA - it's this repo's existing optimization tools
reapplied, not a new formula) - see
`reference/concepts/hierarchical_risk_parity.md`, `regime_aware_allocation.md`,
`multi_period_optimization.md`, `strategic_and_tactical_asset_allocation.md`
for why.

Always require the learner to state the objective, variables, and constraints in words before writing solver code.
