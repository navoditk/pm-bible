# Credit Indices (CDX / iTraxx)

## One-line definition
A credit default swap index is a standardized basket of single-name CDS
on a fixed list of reference entities — CDX for North American and
Emerging Market names, iTraxx for European, Asian, and other markets —
traded as one liquid instrument instead of assembling dozens of
individual CDS trades.

## Formula
Intrinsic value (this repo's simplified version):

`index_intrinsic_spread = weighted_average(constituent_spreads)`

(real intrinsic-value calculations PV01-weight the constituents; this
repo's version takes weights as given, equal-weighted by default — see
Limitations)

`index_basis = index_spread - intrinsic_spread`

## Why PMs care
A credit index is the fastest way to express (or hedge) a macro credit
view without picking individual names — buy protection on CDX.HY to
hedge a high-yield book, or sell protection on CDX.IG to add cheap
long-credit-beta exposure. The index basis is the standard relative-
value signal between the index and its constituents: when it strays
from zero, an arbitrage trade (sell protection on whichever side pays
more spread for the same risk, buy protection on the other) tends to
pull it back — that flow is a real part of why credit indices stay
tightly linked to their constituents even though they trade separately.

## Worked example
Five constituent CDS spreads (in bp): 80, 90, 100, 70, 110. Equal-
weighted intrinsic value: `index_intrinsic_spread([80,90,100,70,110]) = 90`.
If the index itself trades at 95bp, `index_basis(95, 90) = +5` — a 5bp
gap between the traded index and what its constituents would imply on
their own.

## Common mistakes
- treating CDX and iTraxx as interchangeable — they cover different
  regions/issuers and roll on different (though coordinated)
  semi-annual schedules
- forgetting the index basis has a sign, and that "which side is cheap"
  depends on that sign carefully, not just its magnitude — get this
  backwards and a relative-value trade is structured in the wrong
  direction entirely
- using the theoretical (par) spread interchangeably with the traded
  fixed-coupon convention most indices actually quote under — the two
  aren't the same number and index pricing reconciles them with an
  upfront payment

## Limitations
`index_intrinsic_spread` here uses simple (equal, unless given) weights.
Real intrinsic-value calculations PV01-weight each constituent — a name
with a longer effective maturity or higher spread contributes more to
the index's true sensitivity than a simple average captures. Treat this
repo's version as directionally correct for a quick estimate, not a
trading-desk-grade intrinsic-value calculation.

## Related
- [Fundamental credit analysis](fundamental_credit_analysis.md)
- [CDS and basis](cds_and_basis.md)
- [Credit curves](credit_curves.md)

## Free resources
- [Credit Default Swap Indices — Financial Edge Training](https://www.fe.training/free-resources/financial-markets/credit-default-swap-indices/) — CDX vs. iTraxx coverage and structural mechanics
- [Credit default swap index — Wikipedia](https://en.wikipedia.org/wiki/Credit_default_swap_index) — issuance, quotation conventions, and credit-event handling
