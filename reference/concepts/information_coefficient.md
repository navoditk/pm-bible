# Information Coefficient (IC)

## One-line definition
The correlation between a manager's return forecasts and what actually
happened — the standard measure of raw forecasting skill.

## Formula
`IC = corr(forecasts, realized_returns)`

computed cross-sectionally: one forecast score and one realized return
per asset in the universe, at a single point in time (not a time series
for one asset).

## Why PMs care
IC isolates skill from everything else that goes into a track record —
sizing, constraints, luck. It ranges from -1 (perfectly wrong) to +1
(perfectly right), with 0 meaning no forecasting skill at all. It's the
first term in the [Fundamental Law of Active Management](fundamental_law.md):
`IR ~= IC * sqrt(breadth) * transfer_coefficient` — so a given level of
skill can still produce a strong information ratio if applied across
enough independent bets.

## Worked example
Three stocks ranked 1 (most attractive) to 3 (least) by a signal, and
their realized returns come in in the same order the signal predicted
(highest-ranked stock does best). `information_coefficient([1,2,3],
[0.01,0.02,0.03]) = 1.0` — perfect forecasting skill on this sample.

## Common mistakes
- treating a small positive IC as weak — in practice, real-world ICs
  cluster around 0.02-0.10; even 0.05 is considered meaningful skill once
  applied across enough independent bets (see breadth)
- computing IC over too few names or too few periods and treating a
  noisy estimate as a stable skill measurement
- using raw (Pearson) correlation when forecasts are better thought of as
  rankings — a rank (Spearman) correlation is often the more honest
  measure of a ranking signal's skill, and isn't what this repo's
  `information_coefficient` computes

## Limitations
`src/pm/active.py::information_coefficient` computes Pearson correlation
only. It also assumes forecasts and realized returns are already aligned
one-to-one by asset — no ranking, deduplication, or universe-matching is
done for you.

## Related
- [Fundamental Law](fundamental_law.md)
- [Information ratio](information_ratio.md)

## Free resources
- [Information coefficient — Wikipedia](https://en.wikipedia.org/wiki/Information_coefficient) — short definition and the -1/0/+1 interpretation
- [Information Coefficient (IC) — Financial Edge Training](https://www.fe.training/free-resources/portfolio-management/information-coefficient-ic/) — Pearson vs. Spearman IC, typical real-world IC ranges, and limitations
