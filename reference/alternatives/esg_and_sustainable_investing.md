# ESG and Sustainable Investing

## One-line definition
Incorporating environmental, social, and governance factors into
investment analysis and portfolio construction — a family of distinct
approaches, not one technique, ranging from purely values-driven
exclusions to return-focused risk integration.

## Vocabulary
- **Negative screening**: excluding specific industries, companies, or
  practices from the investable universe entirely (e.g. tobacco,
  weapons, thermal coal).
- **Best-in-class / positive screening**: selecting the strongest ESG
  performers within each industry group while keeping sector weights
  comparable to a benchmark — unlike negative screening, this doesn't
  remove any sector outright.
- **ESG integration**: systematically incorporating material ESG factors
  into standard fundamental analysis and portfolio construction alongside
  traditional financial metrics, without necessarily excluding anything —
  the most widely used approach in practice, and the one CFA Institute's
  curriculum centers.
- **Thematic investing**: targeting a specific ESG-related theme directly
  (renewable energy, water scarcity, gender diversity) rather than
  screening or integrating across a broad universe.
- **Engagement / active ownership**: using shareholder rights (proxy
  voting, direct dialogue with management) to influence a company's
  ESG-related behavior, rather than avoiding or favoring it based on
  current practice.
- **Impact investing**: targeting measurable, beneficial social or
  environmental outcomes *alongside* financial return — the only
  approach here where the non-financial outcome is an explicit,
  measured objective rather than a lens on financial risk/return.
- **Value-based vs. values-based**: value-based ESG treats ESG factors as
  financially material risk/return inputs (the same logic as any other
  fundamental factor); values-based investing screens or tilts based on
  an investor's own convictions independent of whether it's
  return-relevant. The two are often conflated but are analytically
  distinct motivations.

## Why PMs care
"ESG" gets used as if it's one strategy, but a mandate built on negative
screening, one built on ESG integration, and one built on impact
investing can hold almost entirely different portfolios and have almost
nothing in common except the acronym. A PM needs to know which of these
a given mandate actually specifies — the implementation, benchmark
construction, and even what counts as "success" differ materially across
approaches. ESG integration in particular is framed by CFA Institute and
most practitioners as a *risk lens* on standard fundamental analysis
(does a governance red flag predict a future blow-up the way a leverage
red flag does?) rather than a separate, competing discipline from the
credit and equity analysis already covered throughout this repo.

## Why this isn't implemented in `src/pm`
There's no universally agreed-upon formula for "ESG score" — different
data providers (MSCI, Sustainalytics, Bloomberg) use different
methodologies and frequently disagree on the same company, and building
a genuinely defensible scoring model requires licensed data this repo
doesn't have access to. What *is* codeable — screening a universe against
a rule (include/exclude by sector, by a numeric threshold) — is just
filtering, not new financial math, so it doesn't warrant a dedicated
`src/pm` function.

## Common mistakes
- treating ESG integration as inherently return-sacrificing — the
  value-based framing argues the opposite (ESG factors as financially
  material risk information), though empirical evidence on ESG and
  performance is genuinely mixed and approach-dependent
- assuming one company's ESG rating is comparable across data providers —
  low correlation between different vendors' ESG scores for the same
  company is a well-documented, real methodological problem, not a
  minor detail
- conflating negative screening (excluding on principle) with ESG
  integration (using ESG factors as financial risk inputs) — a portfolio
  can do either, both, or neither, and they answer different questions

## Related
- [Alternative investments overview](alternatives_overview.md)
- [Fundamental credit analysis](../fixed_income/fundamental_credit_analysis.md)
- [Liquidity](../concepts/liquidity.md)

## Free resources
- [ESG Investment Approaches — AnalystPrep (CFA Level 1)](https://analystprep.com/cfa-level-1-exam/corporate-issuers/environmental-social-and-governance-investment-approaches/) — the six standard approaches with definitions
