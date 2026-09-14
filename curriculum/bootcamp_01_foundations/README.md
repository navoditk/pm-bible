# Bootcamp 01 — Five-Day PM/FICC Foundations

## Day 0 — Orientation (optional, for true beginners)

If you haven't taken a portfolio-theory or linear-algebra course before,
start here. If `w' Sigma w` is already second nature and your `pm`
package imports without error, skip straight to Day 1.

1. confirm your environment works
2. the PREDICT / MANUAL FIRST / HAND CALCULATION / ORAL CHECK learning cycle
3. vectors, dot products, and the quadratic form `w' Sigma w` by hand

Notebook:
- [00 Orientation](../../notebooks/foundations/00_orientation.ipynb)

Also see [reference/glossary.md](../../reference/glossary.md) — a
one-line-per-term cheat sheet for vocabulary used throughout the
curriculum.

## Day 1 — Portfolio mathematics and risk
1. portfolio process and vocabulary
2. returns and compounding
3. covariance/correlation
4. diversification
5. portfolio volatility
6. marginal/component risk
7. Sharpe and drawdown

Notebooks:
- [01 Returns and Compounding](../../notebooks/foundations/01_returns_and_compounding.ipynb)
- [02 Covariance and Diversification](../../notebooks/foundations/02_covariance_and_diversification.ipynb)
- [03 Risk Contribution](../../notebooks/foundations/03_risk_contribution.ipynb)
- [13 Sharpe, Drawdown, Benchmark](../../notebooks/foundations/13_sharpe_drawdown_benchmark.ipynb) (Sharpe ratio, drawdown, benchmark vocabulary)

## Day 2 — Portfolio theory and optimization
1. opportunity set
2. efficient frontier
3. global minimum variance
4. tangency / Sharpe
5. mean–variance utility
6. CVXPY
7. constraints
8. turnover/transaction-cost intuition
9. optimizer instability

Notebooks:
- [04 Efficient Frontier](../../notebooks/optimization/04_efficient_frontier.ipynb)
- [05 Constrained Optimization](../../notebooks/optimization/05_constrained_optimization.ipynb)

## Day 3 — Active management and risk models
1. benchmark-relative thinking
2. active weights
3. tracking error
4. information ratio
5. alpha / IC / breadth
6. factor models
7. active optimization

Notebooks:
- [06 Active Portfolio](../../notebooks/active/06_active_portfolio.ipynb)
- [07 Factor Risk](../../notebooks/active/07_factor_risk.ipynb)

## Day 4 — Fixed-income foundations
1. bond vocabulary and price
2. YTM
3. duration
4. DV01
5. convexity
6. yield curve vocabulary
7. key-rate duration
8. spread/spread duration
9. carry/roll introduction

Notebooks:
- [08 Bond Math](../../notebooks/fixed_income/08_bond_math.ipynb)
- [09 Duration and Curve Risk](../../notebooks/fixed_income/09_duration_curve_risk.ipynb)
- [10 Credit Spreads](../../notebooks/fixed_income/10_credit_spreads.ipynb)

## Day 5 — Scenario, attribution, integration
1. scenario design
2. risk-off scenario
3. attribution intuition
4. combined portfolio report
5. deterministic analytics/tool boundary
6. oral assessment

Notebooks:
- [11 Scenarios](../../notebooks/integration/11_scenarios.ipynb)
- [12 Attribution](../../notebooks/integration/12_attribution.ipynb)

## Daily rule

Never spend more than ~45 minutes searching for learning materials. Use the curated references and build.

## Extension — Day 6: Rates portfolio management

This sprint was originally scoped to five days. Phase 6 of `ROADMAP.md`
(rates portfolio management) extends it by one day, building on Day 4's
fixed-income foundations.

1. curve construction (bootstrapping), forward rates
2. curve trades: steepeners, flatteners, butterflies
3. scenario analysis on curve shocks
4. swaps, swap DV01, swap spreads
5. Treasury futures, hedge ratio
6. carry and rolldown, repo/specialness/on-the-run vs. off-the-run, TIPS
   and breakeven inflation

Notebooks:
- [14 Curve Construction and Forwards](../../notebooks/fixed_income/14_curve_construction_forwards.ipynb)
- [15 Curve Trades and Scenarios](../../notebooks/fixed_income/15_curve_trades_scenarios.ipynb)
- [16 Swaps and Swap Spreads](../../notebooks/fixed_income/16_swaps_and_swap_spreads.ipynb)
- [17 Futures and Hedging](../../notebooks/fixed_income/17_futures_and_hedging.ipynb)
- [31 Carry, Roll, and Financing](../../notebooks/fixed_income/31_carry_roll_and_financing.ipynb)

## Extension — Day 7: Risk models (VaR, ES, factor contribution)

Phase 4 of `ROADMAP.md` (risk models), building on Day 3's factor model.

1. factor variance vs. specific variance contribution
2. parametric VaR and expected shortfall
3. stress testing (reuses Day 5's `Scenario` mechanism — see
   `reference/concepts/stress_testing.md`)

Notebooks:
- [18 Factor Risk Contribution](../../notebooks/active/18_factor_risk_contribution.ipynb)
- [19 VaR and Expected Shortfall](../../notebooks/active/19_var_and_expected_shortfall.ipynb)

## Extension — Day 8: Credit

Phase 7 of `ROADMAP.md` (credit), building on Day 4's spread/spread
duration. OAS and rating migration are covered conceptually only — see
`reference/fixed_income/oas.md` and `credit_migration.md` for why they
aren't implemented as code here.

1. Z-spread
2. credit curves, IG/HY
3. default, recovery, hazard rate
4. CDS and CDS-bond basis
5. portfolio credit scenarios (reuses Day 5's `Scenario` mechanism and
   `use_cases/spread_shock/README.md`)

Notebooks:
- [20 Z-Spread and Credit Curves](../../notebooks/fixed_income/20_z_spread_and_credit_curves.ipynb)
- [21 Default, Recovery, and CDS](../../notebooks/fixed_income/21_default_recovery_and_cds.ipynb)

## Extension — Day 9: Securitized / mortgages

Phase 8 of `ROADMAP.md` (securitized/mortgages). Full price-based negative
convexity/OAS and non-agency tranche waterfalls are conceptual only — see
`reference/fixed_income/oas.md`, `mbs_convexity.md`, and
`non_agency_overview.md` for why they aren't implemented as code here.

1. agency MBS pass-throughs, amortization
2. CPR / SMM / PSA prepayment
3. effective duration (technique)
4. extension and contraction (WAL response to rates)
5. non-agency / ABS / CMBS overview

Notebooks:
- [22 Pass-Throughs and Prepayment](../../notebooks/fixed_income/22_pass_throughs_and_prepayment.ipynb)
- [23 Effective Duration and Convexity](../../notebooks/fixed_income/23_effective_duration_and_convexity.ipynb)

## Extension — Day 10: FX and commodities

Phase 9 of `ROADMAP.md` (FX and commodities).

1. FX spot/forward, covered interest parity
2. cross-currency basis
3. FX carry and hedging
4. commodity futures curves: contango, backwardation, roll yield

Notebooks:
- [24 FX and Commodities](../../notebooks/fx_commodities/24_fx_and_commodities.ipynb)

## Extension — Day 11: Attribution and implementation (deep dive)

Phase 10 of `ROADMAP.md`, extending Day 5's attribution intuition into a
real Brinson decomposition plus transaction costs/rebalancing. Liquidity
is conceptual only — see `reference/concepts/liquidity.md`.

1. Brinson attribution (allocation, selection, interaction)
2. fixed-income carry/curve/spread decomposition
3. transaction costs
4. rebalancing trades

Notebooks:
- [25 Brinson and Rebalancing](../../notebooks/integration/25_brinson_and_rebalancing.ipynb)

## Extension — Day 12: Advanced portfolio construction

Phase 11 of `ROADMAP.md`, building on Day 2's mean-variance optimization.
Hierarchical risk parity, regime-aware allocation, and multi-period
optimization are conceptual only — see `reference/concepts/hierarchical_risk_parity.md`,
`regime_aware_allocation.md`, and `multi_period_optimization.md` for why.

1. covariance shrinkage (robust covariance)
2. Black-Litterman
3. risk parity
4. scenario-robust (minimax) optimization

Notebooks:
- [26 Shrinkage and Black-Litterman](../../notebooks/optimization/26_shrinkage_and_black_litterman.ipynb)
- [27 Risk Parity and Robust Optimization](../../notebooks/optimization/27_risk_parity_and_robust_optimization.ipynb)

## Extension — Day 13: Agentic PM analytics

Phase 12 of `ROADMAP.md`, the final FICC roadmap phase. No notebook —
this is the agent layer over everything built in Days 1–12, not new
financial math. Read `reference/concepts/agentic_pm_analytics.md` first;
it maps every roadmap bullet to the concrete artifact that satisfies it.

1. tool schemas — `docs/tool_schema.json`
2. natural-language query layer — `/pm-query` (`.claude/skills/pm-query/SKILL.md`)
3. tutor agents — `/tutor` (`.claude/skills/tutor/SKILL.md`, built earlier)
4. evals — `docs/agentic_analytics_evals.md`
5. grounding, guardrails, explainability, observability — see how both
   skills apply `AGENTS.md`'s rules and cite/log every answer

## Extension — Day 14: Equity portfolio management

Phase 13 of `ROADMAP.md`, the first phase to extend the repo beyond
`docs/FICC_TAXONOMY.md`'s fixed-income/currencies/commodities scope into
equities. Full multi-factor risk-model estimation (Barra/Axioma-style) is
conceptual only — see `reference/equity/equity_factor_investing.md` for
why.

1. dividend discount models (Gordon growth, two-stage)
2. relative valuation multiples (justified P/E, PEG)
3. CAPM, beta, equity risk premium, Jensen's alpha
4. active share and style tilt
5. shareholder yield, buybacks, total shareholder return

Notebooks:
- [28 Equity Valuation and CAPM](../../notebooks/equity/28_equity_valuation_and_capm.ipynb)
- [29 Active Share, Factors, Shareholder Yield](../../notebooks/equity/29_active_share_factors_and_shareholder_yield.ipynb)

## Extension — Day 15: Capstone

The last day. Less hand-holding on purpose — this is where you compose
concepts from across the whole curriculum on one realistic portfolio
(using `data/mock_portfolio.csv`, `mock_benchmark.csv`, and
`mock_bonds.csv`, previously unused by any notebook) instead of learning
a new one.

1. absolute risk decomposition by group
2. active risk: tracking error, MCTE/CCTE, information ratio
3. ex-ante vs. ex-post — did the risk model match reality?
4. bond-level duration/DV01, a rates scenario, a credit scenario
5. Brinson attribution
6. writing the one-page PM summary

Notebook:
- [30 Capstone: Full Portfolio Risk and Attribution Review](../../notebooks/integration/30_capstone_portfolio_review.ipynb)
