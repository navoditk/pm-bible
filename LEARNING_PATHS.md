# Learning Paths

## Path A — Five-Day Foundations Sprint

Use:
`curriculum/bootcamp_01_foundations/README.md`

Best for:
- fast PM foundations
- portfolio optimization
- fixed-income vocabulary
- initial FICC fluency

## Path B — FICC Deep Dive

Prerequisite: complete Foundations Day 1–3.

Sequence:
1. Fixed-income foundations — `curriculum/bootcamp_01_foundations/README.md` Day 4
2. Rates — `curriculum/bootcamp_01_foundations/README.md` Day 6 extension (built)
3. Credit — `curriculum/bootcamp_01_foundations/README.md` Day 8 extension (built; OAS and rating migration are conceptual-only, see `reference/fixed_income/oas.md` and `credit_migration.md`)
4. Mortgages/securitized — `curriculum/bootcamp_01_foundations/README.md` Day 9 extension (built; full price-based negative convexity/OAS and non-agency tranche waterfalls are conceptual-only, see `reference/fixed_income/oas.md`, `mbs_convexity.md`, and `non_agency_overview.md`)
5. FX — `curriculum/bootcamp_01_foundations/README.md` Day 10 extension (built)
6. Commodities — `curriculum/bootcamp_01_foundations/README.md` Day 10 extension (built)
7. FICC portfolio construction — not yet built
8. FICC scenarios and attribution — scenarios: Day 5 (`notebooks/integration/11_scenarios.ipynb`); attribution: `curriculum/bootcamp_01_foundations/README.md` Day 11 extension (built; liquidity-aware costs are conceptual-only, see `reference/concepts/liquidity.md`)

## Path C — Portfolio Construction Specialist

1. portfolio theory — Day 1-2
2. expected returns — Day 2 (`mean_variance`); Black-Litterman (below) is the more defensible way to build these
3. covariance/risk models — Day 1, Day 7 (VaR/ES/factor contribution); covariance shrinkage below
4. optimization — Day 2
5. constraints — Day 2 (`notebooks/optimization/05_constrained_optimization.ipynb`)
6. active risk — Day 3
7. transaction costs — Day 11 (`reference/concepts/transaction_costs_and_rebalancing.md`)
8. robust optimization — Day 12 (built: covariance shrinkage, risk parity, scenario-robust optimization)
9. Black–Litterman — Day 12 (built)
10. multi-period construction — conceptual only, see `reference/concepts/multi_period_optimization.md`

Use `curriculum/bootcamp_01_foundations/README.md` Days 1, 2, 3, 7, 11, and 12.

## Path D — Quick Reference

Start at:
`reference/index.md`

Each page follows:
definition → why PMs care → formula → units → intuition → worked example → code → common mistakes → related concepts → resources.

## Path E — Use-Case Driven

Start at:
`use_cases/index.md`

Use cases progressively connect multiple concepts.
