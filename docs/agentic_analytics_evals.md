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
| "What's the OAS of this callable bond?" | none — conceptual only | — | should say plainly that OAS isn't implemented, and point to `reference/fixed_income/oas.md` rather than approximating one |

## What a passing run looks like

- Every numeric row: the skill actually executes the cited function (via
  `python -c` or similar) rather than stating a number from reasoning.
- The OAS row: the skill declines to fabricate a number and explains why,
  citing the conceptual-only reference page — this is as important a pass
  condition as getting the numeric rows right.
- Every answer names the specific function/module used.
