# Sovereign and Emerging Market Debt

## One-line definition
Government bonds issued outside the developed-market Treasury/Gilt/Bund
universe this repo's curve and credit machinery already assumes — split
into hard-currency debt (issued in USD/EUR, credit risk without direct
FX exposure) and local-currency debt (issued in the sovereign's own
currency, currency risk layered on top of credit risk).

## Vocabulary
- **Hard-currency (external) debt**: denominated in a major reserve
  currency (usually USD), settled internationally. The investor takes
  sovereign credit/default risk but not direct currency risk — the same
  [CDS and basis](cds_and_basis.md) and [credit
  curves](credit_curves.md) machinery already built for corporate credit
  applies, with the issuer being a government instead of a company.
- **Local-currency debt**: denominated and often settled in the
  sovereign's own currency, requiring local custody. Adds currency
  depreciation and inflation risk on top of credit risk — this is where
  [FX carry](../fx/fx_carry.md) and [FX spot/forward](../fx/spot_and_forward.md)
  become directly relevant to a sovereign-debt position, not just a
  separate FX overlay.
- **EMBI / GBI-EM**: the standard benchmark index families (J.P. Morgan)
  for hard-currency and local-currency EM sovereign debt respectively —
  the practitioner's reference point the same way a Treasury or
  aggregate-bond index is for developed-market fixed income.

## Why PMs care
The hard-currency-vs-local-currency choice is a genuinely different risk
decision, not just a labeling detail: a hard-currency sovereign bond PM
is making a credit call (will this government default or restructure?)
largely insulated from that currency's day-to-day moves, while a
local-currency PM is making a combined credit-and-currency call, with
currency risk often the larger swing factor. A PM choosing between the
two isn't choosing "safer vs. riskier" in one dimension — they're
choosing which risk (credit vs. currency) they want to underwrite, and
in which combination.

## Why this isn't implemented in `src/pm`
Sovereign credit analysis (assessing a government's fiscal position, debt
sustainability, external reserves, and political risk) is a different
discipline from corporate fundamental credit analysis
([leverage/coverage ratios](fundamental_credit_analysis.md) don't apply
the same way to a country), and this repo doesn't have sovereign
fiscal/reserves data to build a tested model against. The mechanical
pieces that *do* apply directly — CDS/basis pricing for hard-currency
credit risk, FX carry/forward pricing for local-currency risk — are
already implemented and reused here rather than duplicated.

## Common mistakes
- assuming hard-currency debt is "safe" because it removes FX risk — a
  government can still default or restructure hard-currency debt (many
  historical EM defaults were on USD-denominated bonds specifically)
- assuming local-currency debt's higher historical volatility means it's
  strictly worse risk-adjusted — its low correlation to other fixed
  income (via the FX component) is a real diversification benefit that a
  volatility number alone doesn't capture
- treating "emerging markets" as one homogeneous risk bucket — a 1.5%
  yielding EM sovereign and a 13-14% yielding EM sovereign in the same
  local-currency index are pricing in very different fiscal and currency
  outlooks

## Related
- [Credit curves](credit_curves.md)
- [CDS and basis](cds_and_basis.md)
- [FX carry](../fx/fx_carry.md)
- [Municipal bonds](municipal_bonds.md)

## Free resources
- [Emerging market debt: Local or hard currency? — Robeco](https://www.robeco.com/en-int/insights/2025/10/emerging-market-debt-local-or-hard-currency) — the risk/return trade-off between the two, from a practitioner's perspective
