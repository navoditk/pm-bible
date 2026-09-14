# Leveraged Loans

## One-line definition
Senior secured, floating-rate debt issued by below-investment-grade
borrowers — the bank-loan-market cousin of high-yield bonds, with a
different risk profile driven by that combination of secured status and
floating coupons.

## Key differences from high-yield bonds
- **Rate**: loans float (reference rate, typically SOFR, plus a fixed
  margin); high-yield bonds are almost always fixed-rate. A loan
  investor's income rises automatically as rates rise, but so does the
  borrower's interest bill — floating-rate exposure cuts both ways.
- **Seniority**: loans are typically senior secured (first claim on
  collateral); high-yield bonds are typically senior unsecured. This is
  the single biggest driver of loans' historically higher recovery
  rates in default.
- **Covenants**: loans traditionally carried maintenance covenants
  (tested every quarter regardless of issuer action); the rise of
  "covenant-lite" loans over the 2010s eroded much of that distinction,
  moving loan covenant packages closer to bonds' incurrence-only style
  — see [fundamental credit analysis](fundamental_credit_analysis.md).
- **Pricing convention**: loans are typically quoted on a **discount
  margin** basis (spread to the floating reference rate) rather than a
  fixed-rate yield or spread-to-Treasury, since their coupon already
  floats with the reference rate.

## Why PMs care
Rates going up is a genuinely different event for a loan book than a
high-yield bond book: loan coupons reset higher (helping loan holders'
income, but also raising the exact borrowers' debt-service burden that
[interest coverage](fundamental_credit_analysis.md) measures). A PM
choosing between the two isn't just picking a different point on the
credit curve — they're picking a different interest-rate exposure and a
different position in the capital structure for essentially the same
underlying company, in many cases the same issuer with both a loan and
a bond outstanding simultaneously.

## Why this isn't implemented in `src/pm`
The mechanics that differ from a fixed-rate bond — floating-rate
resets, discount-margin pricing, prepayment/call optionality specific to
loan documentation — are a materially different computation from this
repo's fixed-coupon bond-pricing functions, and the same "small
transparent function" discipline that keeps OAS and HRP conceptual-only
applies here: better to state the comparison clearly than ship an
under-tested loan pricer. The credit ratio functions in
[fundamental credit analysis](fundamental_credit_analysis.md) — leverage,
coverage, fixed-charge coverage — apply identically to a loan issuer as
to a bond issuer, since they're properties of the borrower, not the
instrument.

## Common mistakes
- assuming loans are always safer than high-yield bonds because of
  seniority alone — a loan and a bond from the *same* over-levered
  issuer are both exposed to that issuer's fundamental deterioration,
  seniority only changes the recovery outcome if default happens
- ignoring rate-reset risk in a rising-rate environment — a floating
  coupon protects the *investor's* income, but rising debt service can
  push a marginal borrower toward the exact covenant breach or default
  that erases the seniority advantage
- treating "covenant-lite" as a recent, minor development rather than a
  structural shift in the loan market's risk profile over the past
  decade-plus

## Related
- [Fundamental credit analysis](fundamental_credit_analysis.md)
- [Spread duration](spread_duration.md)
- [Credit curves](credit_curves.md)

## Free resources
- [Leveraged Lending and Collateralized Loan Obligations: Frequently Asked Questions — Congressional Research Service](https://www.congress.gov/crs-product/R46096) — a plain-language, non-industry-affiliated primer on the leveraged loan market and CLOs
- [Leveraged Credit Markets: Then and Now — Western & Southern / Fort Washington](https://www.westernsouthern.com/fortwashington/insights/leveraged-credit-markets) — loans vs. high-yield bonds, covenant-lite trends
