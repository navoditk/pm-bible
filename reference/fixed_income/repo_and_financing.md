# Repo, Specialness, and On-the-Run vs. Off-the-Run

## One-line definition
Repo (repurchase agreement) is how a bond position actually gets
financed — sell the bond today with an agreement to buy it back
tomorrow at a slightly higher price, the difference being the financing
rate. "Specialness" is what happens to that rate when the specific bond
being financed is unusually in demand to borrow.

## Vocabulary
- **General collateral (GC) repo**: financing where *any* similar bond
  is acceptable collateral — the baseline, roughly-risk-free short-term
  financing rate.
- **On-the-run**: the most recently auctioned Treasury of a given
  maturity — the current benchmark, most liquid issue.
- **Off-the-run**: every earlier issue of that same maturity — still
  tradable, but less liquid, and usually cheaper (higher yield) than the
  on-the-run issue for the same cash flows.
- **Special repo**: when a specific bond (almost always the on-the-run
  issue) is financed at a repo rate *below* GC, because short-sellers who
  need that exact bond to deliver are willing to lend cash cheaply to
  borrow it.

## Why PMs care
`carry_return` (see [carry and rolldown](carry_and_rolldown.md)) treats
"financing rate" as one input — in reality it's a market outcome that
depends on exactly which bond you hold. Owning a bond that's trading
special means your effective financing cost is *lower* than GC, boosting
realized carry beyond the naive calculation; being short a special bond
means the opposite — you may have to pay up hard to borrow it to cover
your short, sometimes eating most or all of a curve trade's expected
edge. On-the-run vs. off-the-run is also the classic curve relative-
value trade: two bonds with nearly identical cash flows, priced
differently purely on liquidity and financing, not credit or duration.

## Why this isn't implemented in `src/pm`
Repo specialness is a market-observed rate, not something derivable from
a bond's own cash flows or a yield curve — there's no formula to
compute it, only data to look up (or a market to trade in). The pieces
that *are* mechanical — turning a given financing rate into a carry
number — are exactly what `carry_return` already does; specialness is an
input to that function, not a separate calculation.

## Common mistakes
- treating repo rate as a fixed, uniform number across all bonds — GC
  and special rates for the same maturity can differ by tens of basis
  points, which is often larger than the carry edge a curve trade is
  trying to capture in the first place
- forgetting that a new on-the-run issue displaces the old one after
  each auction — a bond that was special can suddenly trade at GC (or
  even cheap) the moment a new issue takes over as the benchmark
- assuming off-the-run bonds are simply "worse" — for a buy-and-hold
  investor uninterested in trading liquidity, the extra yield on an
  off-the-run issue with equivalent cash flows can be a genuine pickup

## Related
- [Carry and rolldown](carry_and_rolldown.md)
- [Curve trades](curve_trades.md)
- [Treasury futures hedging](treasury_futures_hedging.md)

## Free resources
- [On the run (finance) — Wikipedia](https://en.wikipedia.org/wiki/On_the_run_(finance)) — on-the-run vs. off-the-run definitions and the liquidity premium
- [What's going on in the US Treasury market, and why does it matter? — Brookings](https://www.brookings.edu/articles/whats-going-on-in-the-us-treasury-market-and-why-does-it-matter/) — plain-language overview of Treasury market structure, including repo
- [Money Market Fund Repo and the ON RRP Facility — Federal Reserve](https://www.federalreserve.gov/econres/notes/feds-notes/money-market-fund-repo-and-the-on-rrp-facility-20231215.html) — how repo markets actually function, from the source that sets the policy rate repo trades around
