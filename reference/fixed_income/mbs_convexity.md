# MBS Negative Convexity (Extension and Contraction Risk)

## One-line definition
An MBS's effective duration lengthens when rates rise (extension) and
shortens when rates fall (contraction) — the opposite of a normal bond's
convexity, which helps in both directions.

## Mechanism
When rates fall, `refinancing_incentive_cpr` rises (more prepayments) —
principal comes back faster, capping price appreciation and *shortening*
duration (contraction). When rates rise, prepayments floor at `base_cpr`
— principal comes back on the original schedule *plus* the pool now runs
longer than a bullet bond of the same duration would (extension). Either
way, the borrower's option to prepay works against the investor.

## What's demonstrable here, and what isn't
Compute `weighted_average_life` at a rate with an active refinancing
incentive versus one without, using `refinancing_incentive_cpr` to set the
prepayment speed at each rate first — WAL genuinely shortens as rates
fall and floors (stops shortening further) once rates rise past the
pool's coupon. That WAL shift *is* extension/contraction, and it's a
correct, verifiable result of this repo's simple prepayment model.

Full negative convexity **in price terms** is not demonstrated here.
Naively discounting the prepayment-adjusted cash flows at a flat market
rate does not reproduce it — that approach doesn't capture the actual
mechanism (principal is returned at *par*, capping upside versus what an
equivalent option-free bond would be worth at that rate), which requires
comparing against an option-free benchmark under a proper term-structure
model. That's exactly the OAS machinery this repo doesn't build — see
[OAS](oas.md).

## Why PMs care
A portfolio that looks duration-neutral against cash bonds can still be
short convexity if it holds MBS — it will underperform in both a big rally
(price capped) and a big selloff (duration extends right when you don't
want it to) relative to a position with normal convexity.

## Limitations
The `refinancing_incentive_cpr` model correctly signs the WAL/extension
effect but is not sophisticated enough to correctly price the option cost
— don't use it to argue about MBS *price* behavior, only *cash-flow
timing* behavior.

## Related
- [Prepayment models](prepayment_models.md)
- [Effective duration](effective_duration.md)
- [OAS](oas.md)
- [CMO/REMIC structuring](cmo_remic_structuring.md)
