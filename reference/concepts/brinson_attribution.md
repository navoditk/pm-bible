# Brinson Attribution

## One-line definition
Decomposes active return per segment (sector, country, ...) into
allocation (over/underweighting a segment), selection (picking better/worse
names within it), and interaction.

## Formula
`allocation = (w_p - w_b) * r_b`

`selection = w_b * (r_p - r_b)`

`interaction = (w_p - w_b) * (r_p - r_b)`

These three sum, segment by segment, to total active return
(`w_p·r_p - w_b·r_b`).

## Why PMs care
"We beat the benchmark by 130bp" is not actionable. "We beat it because we
were overweight tech (allocation) despite weak stock selection within
tech (negative selection)" tells a PM what actually worked and what to
fix.

## Common mistakes
- comparing segments that aren't defined identically in portfolio and
  benchmark (a sector taxonomy mismatch silently breaks the decomposition)
- ignoring interaction because it's usually small — it can matter when
  active weights and active returns are both large in the same segment

## Related
tracking error, active weights, fixed-income attribution.
