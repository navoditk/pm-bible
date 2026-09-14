# Agentic Analytics Evals

Manually-run checklist for `/pm-query` (`.claude/skills/pm-query/SKILL.md`).
There is no automated harness for skill-routing behavior — that needs a
live agent test rig this repo doesn't have — so this stays an honest,
human-runnable checklist rather than a fake `pytest` suite. Each row's
expected output was computed and verified directly against `src/pm`
(not hand-derived) before being written here.

To run: ask `/pm-query` each question, and confirm (a) it calls the
listed function with the listed inputs, (b) the output matches, and
(c) it cites the function/module and a reference page, not just a bare
number.

| Query | Expected function | Inputs | Expected output |
|---|---|---|---|
| "DV01 of a 5-year 5% semiannual bond at a 4% yield?" | `pm.fixed_income.duration.dv01` | `ytm=0.04, face=100, coupon_rate=0.05, years=5, frequency=2` | `0.04609` (≈) |
| "Sharpe ratio of returns 2%, 4%, 3%, risk-free 0%, annual periods?" | `pm.returns.sharpe_ratio` | `returns=[0.02,0.04,0.03], risk_free_rate=0.0, periods_per_year=1` | `3.0` |
| "95% parametric VaR of a $1,000,000 portfolio with 2% daily vol?" | `pm.risk.parametric_var` | `portfolio_value=1_000_000, volatility=0.02, confidence=0.95` | `32897.07` (≈) |
| "1-year FX forward for spot 1.10, USD rate 5%, EUR rate 3%?" | `pm.fx.fx_forward_rate` | `spot=1.10, domestic_rate=0.05, foreign_rate=0.03, years=1` | `1.121359` (≈) |
| "Risk-parity weights for two uncorrelated assets at 20% and 10% vol?" | `pm.robust.risk_parity_weights` | `covariance=[[0.04,0],[0,0.01]]` | `[0.3333, 0.6667]` (≈) |
| "Roll yield if the near contract is $80 and the far contract is $78?" | `pm.commodities.roll_yield` | `near_price=80, far_price=78` | `0.02564` (≈, backwardation) |
| "Gordon growth value of a stock with a $2 next dividend, 9% required return, 4% growth?" | `pm.equity.valuation.gordon_growth_value` | `dividend_next=2.0, required_return=0.09, growth_rate=0.04` | `40.0` |
| "Beta of a stock whose returns move 1.5x the market's?" | `pm.equity.capm.beta` | `stock_returns=[0.015,0.03,-0.015,0.045,0.0], market_returns=[0.01,0.02,-0.01,0.03,0.0]` | `1.5` |
| "Information ratio if portfolio returns are 3%/5%/2% and benchmark returns are 1%/2%/1%, unannualized?" | `pm.active.information_ratio` | `portfolio_returns=[0.03,0.05,0.02], benchmark_returns=[0.01,0.02,0.01], periods_per_year=1` | `2.0` |
| "Expected information ratio for a manager with a 0.05 IC and 100 independent bets, no constraints?" | `pm.active.fundamental_law_ir` | `information_coefficient_value=0.05, breadth_value=100, transfer_coefficient_value=1.0` | `0.5` |
| "Unconstrained tangency portfolio for two uncorrelated assets, mu=[8%,5%], vol=[20%,10%], risk-free 2%?" | `pm.optimization.max_sharpe` | `expected_returns=[0.08,0.05], covariance=[[0.04,0],[0,0.01]], risk_free_rate=0.02, long_only=False` | `[0.3333, 0.6667]` (≈) |
| "Carry on a 5Y bond yielding 4.00% financed at 3.00% repo, held 1 year?" | `pm.fixed_income.carry.carry_return` | `coupon_income=4.0, price=100.0, financing_rate=0.03, horizon_years=1.0` | `0.01` |
| "Breakeven inflation with nominal 4.5% and TIPS real yield 2.0%?" | `pm.fixed_income.linkers.breakeven_inflation` | `nominal_yield=0.045, real_yield=0.02` | `0.025` |
| "Leverage ratio for an issuer with $300M debt and $100M EBITDA?" | `pm.fixed_income.credit.leverage_ratio` | `total_debt=300, ebitda=100` | `3.0` |
| "Index basis if 5 CDS constituents (80,90,100,70,110bp) trade equal-weighted and the index itself trades at 95bp?" | `pm.fixed_income.credit.index_intrinsic_spread` then `index_basis` | `constituent_spreads=[80,90,100,70,110]` → `intrinsic=90.0`; `index_basis(95, 90)` | `5.0` |
| "Implied financing rate on a dollar roll: $1,000,000 face, 5% coupon, near price 101.00, far price 100.625, 1-month roll?" | `pm.fixed_income.mbs.dollar_roll_implied_financing_rate` | `coupon_income=4166.6667, drop_income=3750.0, near_amount=1010000.0, horizon_years=1/12` | `0.004950` (≈, 0.495%) |
| "What's the OAS of this callable bond?" | none — conceptual only | — | should say plainly that OAS isn't implemented, and point to `reference/fixed_income/oas.md` rather than approximating one |

## What a passing run looks like

- Every numeric row: the skill actually executes the cited function (via
  `python -c` or similar) rather than stating a number from reasoning.
- The OAS row: the skill declines to fabricate a number and explains why,
  citing the conceptual-only reference page — this is as important a pass
  condition as getting the numeric rows right.
- Every answer names the specific function/module used.
