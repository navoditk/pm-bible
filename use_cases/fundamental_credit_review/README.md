# Use Case — Fundamental Credit Review

## PM question
Two issuers are being screened for a new position: Issuer A ($200 debt,
$10 interest expense) and Issuer B ($400 debt, $30 interest expense),
both with $100 of EBITDA. Which is the stronger credit, and does the
CDX index they'd sit in look cheap or rich right now?

## Concepts
leverage ratio, interest coverage ratio, fixed-charge coverage ratio,
credit index intrinsic spread and basis.

## First exercise
Using `pm.fixed_income.credit.leverage_ratio` and
`interest_coverage_ratio`:

1. compute leverage and interest coverage for both issuers
2. Issuer A also carries $15 of mandatory term-loan amortization this
   year — recompute its coverage picture with
   `fixed_charge_coverage_ratio` and compare to interest coverage alone
3. decide: is Issuer B automatically the weaker credit just because it's
   more leveraged, or does its coverage tell a more specific story?

Then, using `index_intrinsic_spread` and `index_basis`: five single-name
CDS spreads (80, 90, 100, 70, 110 bp) trade equal-weighted under an
index quoted at 95bp — is the index cheap or rich relative to its
intrinsic value, and by how much?

## Extend
The central bank raises rates sharply. Issuer A's debt is a fixed-rate
bond; Issuer B's is a floating-rate term loan. Whose coverage ratio is
directly affected by the rate move alone, and whose isn't? See
`reference/fixed_income/leveraged_loans.md`.
