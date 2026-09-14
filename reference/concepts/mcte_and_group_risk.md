# Marginal/Component Contribution to Tracking Error, and Group Risk Decomposition

## One-line definition
Marginal contribution to tracking error (MCTE) is how much tracking error
changes per unit of active weight in one asset; component contribution
(CCTE) scales that by the active weight actually held, so the components
sum exactly to total TE. Group risk contribution aggregates the analogous
absolute-risk breakdown (`component_risk_contribution`) by sector,
country, or any other grouping — the form a real risk report takes.

## Formula
Let `a = w_p - w_b` (active weights) and `TE = sqrt(a'Sigma*a)`:

`MCTE = (Sigma @ a) / TE`

`CCTE = a * MCTE`  (sums to `TE`)

Group risk contribution: partition `component_risk_contribution(w, Sigma)`
by a `groups` label per asset and sum within each group; the group totals
still sum to total portfolio volatility.

## Why PMs care
Tracking error is one number; MCTE/CCTE answer "which position is
actually driving it," which is what you act on to cut risk. This is
mathematically the same idea as `marginal_risk_contribution` /
`component_risk_contribution` in [risk contribution](risk_contribution.md)
— just evaluated at active weights against tracking error instead of raw
weights against total volatility, because a benchmark-relative mandate is
managed against active risk, not absolute risk. Group risk contribution
is the practical form both show up in: nobody reads a 500-line
position-by-position risk report, they read "62% of our risk is in Tech."

## Worked example
Portfolio `[35%, 65%]` vs. benchmark `[25%, 75%]` (active weights
`[+10%, -10%]`) with `Sigma = [[0.04, 0.01], [0.01, 0.09]]`:
`TE = sqrt(a'Sigma*a)`, `MCTE = (Sigma @ a) / TE` — see
`tests/test_active.py::test_mcte_hand_example` for the exact numbers.

## Common mistakes
- confusing MCTE (the sensitivity — how much TE moves per unit of
  additional active weight) with CCTE (the actual current contribution,
  which also depends on how much active weight is already held) — a name
  with a small active weight but huge MCTE is a risk to watch, not
  necessarily a risk that's currently large
- computing marginal contribution to *active risk* with each asset's raw
  volatility/correlation (MCAR) instead of its covariance *against the
  benchmark specifically* (MRCAR) — the two can rank positions
  differently, especially for low-volatility holdings like cash; see the
  COVER article below
- forgetting `group_risk_contribution` requires the *same* `weights` and
  `covariance` used to build the portfolio's risk in the first place —
  mixing in a different group's covariance silently breaks the
  sums-to-total identity

## Limitations
`marginal_contribution_to_tracking_error` raises rather than returning a
value when active weights are all zero (TE=0, so MCTE is an undefined
0/0) — matching `marginal_risk_contribution`'s guard on zero portfolio
volatility. `group_risk_contribution` does simple label-based summation
of `component_risk_contribution`; it doesn't implement the MRCAR-style
benchmark-relative refinement described in the COVER article below.

## Related
- [Risk contribution](risk_contribution.md)
- [Tracking error](tracking_error.md)
- [Factor risk contribution](factor_risk_contribution.md)

## Free resources
- [Tracking the (marginal) error — COVER](https://www.cover.co.za/news/tracking-the-marginal-error) — MCAR vs. MRCAR, and why raw-volatility marginal contribution can undervalue low-vol positions like cash
- [Risk Budgeting in Portfolio Management — AnalystPrep (CFA Level III)](https://analystprep.com/study-notes/cfa-level-iii/risk-budgeting/) — absolute vs. active risk budgeting and how contributions get allocated across a portfolio
