# Scenario-Robust (Minimax) Optimization

## One-line definition
Instead of optimizing against a single expected-return estimate,
maximize the portfolio's worst-case return across a set of specified
scenarios.

## Formula
Given `R` (n_scenarios x n_assets, each row a scenario's asset returns):

`maximize t subject to R @ w >= t, sum(w) = 1, w >= 0`

## Why PMs care
Mean-variance optimization is only as good as its expected-return input,
which is usually the least reliable part of the model. Scenario-robust
optimization sidesteps that by optimizing directly against a small set of
PM-defined, defensible scenarios (e.g. from `src/pm/scenarios.py`)
instead of a single fragile point estimate.

## Worked example
Verified in `tests/test_robust.py`: two assets, two symmetric scenarios
(each favoring one asset over the other), gives an equal-weight 50/50
solution where both scenarios bind at the same worst-case return — the
minimax solution can't do better in one scenario without doing worse in
the other.

## Common mistakes
- using too few scenarios, which can produce weights overfit to those
  specific shocks rather than genuinely robust
- forgetting that minimax is inherently conservative — it optimizes for
  the worst case, not the expected case

## Related
stress testing, mean-variance optimization, Black-Litterman.
