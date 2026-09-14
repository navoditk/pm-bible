# Fundamental Credit Analysis

## One-line definition
The qualitative and ratio-based work of deciding whether a borrower can
actually service its debt — the layer underneath spread, Z-spread, and
default-probability math that decides *which* bonds a credit PM wants to
own in the first place.

## Formula
`leverage_ratio = total_debt / EBITDA` (lower is safer; often a
covenant's *maximum*)

`interest_coverage_ratio = EBITDA / interest_expense` (higher is safer;
often a covenant's *minimum*)

`fixed_charge_coverage_ratio = EBITDA / (interest_expense + mandatory_principal_payments)`
— stricter than interest coverage, since scheduled amortization has to
be paid in cash too, not just refinanced indefinitely.

## Why PMs care
Everything else this repo's credit modules compute —
[spread duration](spread_duration.md), [Z-spread](z_spread.md),
[default and recovery](default_recovery.md) — takes a spread or a
default probability as *given*. Fundamental analysis is how a credit
analyst actually forms that view: is this issuer's leverage
deteriorating, does it generate enough EBITDA to cover its interest and
scheduled principal, and what happens to the bondholder if it doesn't.

## Covenants
Covenants are the contractual triggers tied to these same ratios.
**Incurrence covenants** (typical in public high-yield bonds) are only
tested when the issuer takes a specific action — "you may not issue more
senior debt if leverage would exceed 4.0x after the issuance." **Maintenance
covenants** (typical in bank loans and leveraged finance) are tested
periodically regardless of any action — "leverage must stay below 4.0x
at every quarterly reporting date." Maintenance covenants give lenders
an earlier warning and more leverage to force a renegotiation before
things get worse; their absence ("covenant-lite") is exactly what let
leveraged loans converge toward high-yield-bond-style protections over
the 2010s (see [leveraged loans](leveraged_loans.md)).

## Rating agencies
S&P, Moody's, and Fitch each publish their own ratings methodology, but
all three build on the same core inputs this page covers: leverage,
coverage, and cash-flow-based measures (e.g. FFO/Debt), adjusted
issuer-by-issuer for industry, business-risk, and structural factors a
pure ratio calculation misses. A rating downgrade is frequently the
market-moving event even when the underlying ratios only moved
gradually — see [credit migration](credit_migration.md) for the
portfolio-risk side of that.

## Common mistakes
- treating EBITDA as a cash-flow measure — it ignores working-capital
  changes, capex, and taxes, all of which can leave a "well-covered"
  borrower on paper without enough actual cash to pay its bills
- comparing leverage ratios across industries without adjusting — an
  asset-heavy, stable-cash-flow business (utilities) can safely carry
  leverage that would be dangerous for a cyclical, capex-light one
- reading a single quarter's ratio in isolation instead of the trend —
  deteriorating coverage over several quarters is a much stronger signal
  than one weak print

## Limitations
`leverage_ratio`, `interest_coverage_ratio`, and
`fixed_charge_coverage_ratio` are pure ratio calculations from inputs
you supply — this repo doesn't parse financial statements or forecast
EBITDA. Real credit work spends most of its effort on exactly that:
building and stress-testing the EBITDA/debt projections that go into
these formulas.

## Related
- [Spread duration](spread_duration.md)
- [Default and recovery](default_recovery.md)
- [Credit migration](credit_migration.md)
- [Leveraged loans](leveraged_loans.md)
- [Credit indices](credit_indices.md)

## Free resources
- [Financial Ratios for Credit Analysis — AnalystPrep (CFA Level 1)](https://analystprep.com/cfa-level-1-exam/fixed-income/financial-ratios-credit-analysis/) — leverage and coverage formulas, verified against this page's worked examples
- [An Introduction to Covenants in Leveraged Finance Debt — CredCore](https://credcore.com/insights/an-introduction-to-covenants-in-leveraged-finance-debt) — incurrence vs. maintenance covenants explained
