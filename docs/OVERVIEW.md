# Repository Overview

A quick-read summary of what this repository actually contains, for
anyone (including a future you) who wants the state of things without
reading every file. For the day-to-day entry point, use
[docs/README.md](./README.md) instead — this page is a snapshot, not a
workflow guide.

## What this is

pm-bible is a build-first PM/FICC-and-equity learning and analytics
repository. It runs three modes at once — learn (curriculum and
notebooks), look up (reference pages), apply (use cases) — under one
discipline, stated in the root README:

> Read → predict → derive → type code yourself → test → compare with
> reference → explain

Financial logic must be documented, unit-aware, and tested
(`AGENTS.md`). Deterministic functions are preferred over opaque
frameworks, and manual reasoning comes before asking an agent.

## Browse without cloning

- **[Docs site](https://navoditk.github.io/pm-bible/)** — every
  reference page, notebook, and use case as a searchable static site,
  rebuilt automatically from `main` on every push
- **[Artifact preview](https://claude.ai/code/artifact/902379a8-c198-4970-aca8-4cb71e2a3d5c)**
  — a lighter single-page version for a quick look or if the docs site
  above isn't reachable; refreshed manually, not on every push

## At a glance

| | |
|---|---|
| Analytics code | 1,443 lines across 29 modules in `src/pm/` |
| Tests | 183 passing, 16 test files |
| Notebooks | 35, across 8 tracks (foundations, optimization, active, fixed income, FX/commodities, derivatives, equity, integration) |
| Reference pages | 80 (including a glossary) |
| Roadmap phases | 14 of 14 complete |
| Bootcamp curriculum | 16 days (5 core + 11 extension) |
| Use-case workflows | 7 |
| Curated resource files | 7, 275 lines total |
| Claude Code skills | `/tutor`, `/pm-query`, `/master` |

Module size is small by design — the median `src/pm` module is roughly
30 lines: a formula made concrete, tested, with its assumptions stated
in a one-line docstring where they aren't obvious. This is a mechanics
trainer, not a desk-grade risk system — no live data feeds, no
production-grade curve or optimization engine beyond notebook exercises.

## Coverage by phase

| Phase | Topic |
|---|---|
| 1 | Portfolio foundations — returns, covariance, diversification, risk contribution, Sharpe, drawdown |
| 2 | Portfolio theory & optimization — efficient frontier, tangency portfolio (max Sharpe), minimum tracking error, mean-variance optimization, shrinkage, Black-Litterman |
| 3 | Active management — active weights, tracking error, information ratio, information coefficient, breadth, transfer coefficient, the Fundamental Law, factor models |
| 4 | Risk models — factor covariance, marginal/component risk, VaR/ES, stress testing |
| 5 | Fixed-income foundations — price, yield, duration, DV01, convexity, key-rate duration |
| 6 | Rates portfolio management — curve bootstrapping, forwards, curve trades, swaps, futures |
| 7 | Credit portfolio management — Z-spread, spread duration, credit curves, CDS, default/recovery |
| 8 | Securitized/mortgages — agency MBS, CPR/PSA prepayment, effective duration, extension/contraction |
| 9 | FX & commodities — spot/forward, covered interest parity, carry, roll yield |
| 10 | Attribution & implementation — Brinson decomposition, FI carry/curve/spread attribution, rebalancing |
| 11 | Advanced portfolio construction — robust covariance, risk parity, scenario-robust optimization |
| 12 | Agentic PM analytics — tool schemas, `/pm-query`, `/tutor`, evals, grounding & guardrails |
| 13 | **Equity portfolio management** — DDM, relative valuation, CAPM/beta, factor investing, active share, shareholder yield |
| 14 | **Derivatives and options** — Black-Scholes, the Greeks, put-call parity, implied volatility, Black-76, swaptions/caps/floors and option strategies (conceptual) |

Fixed income (Phases 5–8) remains the deepest vein by page count and
code volume — rates, credit, and mortgages are each fully built out with
tested code on the *pricing and risk mechanics* (duration, DV01,
convexity, Z-spread, CDS, CPR/PSA prepayment). A follow-up audit found
that claim overstated on the practitioner/market-structure layer,
though: carry-and-rolldown was listed as a Phase 5 roadmap bullet and
never implemented, and TBA/dollar roll, repo specialness, TIPS
breakevens, credit indices, and fundamental credit analysis had zero
coverage anywhere. All three gaps are now closed —
`carry_and_rolldown.md`, `repo_and_financing.md`, and
`tips_and_breakevens.md` for rates; `fundamental_credit_analysis.md`,
`credit_indices.md`, and `leveraged_loans.md` for credit;
`tba_and_dollar_roll.md`, `specified_pools.md`, and
`cmo_remic_structuring.md` for mortgages — each with tested `src/pm`
code (where the math is genuinely codeable), a notebook, and real
external sources. Phase 13 (equity) closes what used to
be this repo's one clear gap: previously "equity" appeared only as a
generic example asset class, with no valuation, CAPM, or factor-investing
material anywhere. Phase 3 (active management) was similarly incomplete
for a time — `src/pm/active.py` had only active weights and tracking
error, while a reference page pointed readers at information ratio, IC,
breadth, and the Fundamental Law as if they already existed there. All
four are now implemented, tested, and referenced from real external
sources (Wikipedia, CFA Institute, Financial Edge Training).

A repo-wide curriculum-completeness audit (distinct from the fixed-income-
specific one above) found the single biggest remaining hole: zero
options/volatility coverage anywhere, despite deep coverage of linear
instruments. Phase 14 (derivatives and options) closes it —
`src/pm/options.py` implements Black-Scholes call/put pricing, all five
Greeks (each independently verified against a finite-difference bump of
the pricing function, not just the closed-form formula), implied
volatility (solved numerically), and Black-76 (options on forwards,
verified to reproduce Black-Scholes exactly at the matching forward
price) — with swaptions/caps/floors and option strategies (covered call,
protective put, collar) covered conceptually, since a real swaption needs
a curve-based annuity factor and a strategy payoff is a composition of
already-priced legs, not new formulas.

A correctness-fix pass also caught and fixed several bugs surfaced by a
detailed audit: a Black-Litterman round-trip that silently returned the
wrong weights due to a risk-aversion convention mismatch, NaN silently
propagating from `simple_returns` into every downstream metric, every
optimizer returning `None` instead of raising on an infeasible problem,
and a few MBS prepayment domain errors. Each fix shipped with a
regression test that fails against the old code.

The same audit flagged the optimizer as the thinnest, most-promised part
of the repo — `notebooks/optimization/04_efficient_frontier.ipynb` was
titled "Efficient Frontier" but never computed one, and matplotlib was a
paid-for dependency used nowhere. `src/pm/optimization.py` now has
`efficient_frontier`, `max_sharpe` (tangency portfolio), and
`min_tracking_error`; notebook 04 actually traces and plots a frontier
with the GMV and tangency points marked and a capital market line drawn.
A parallel gap in risk analytics — everything was ex-ante (covariance-
based) with no way to check realized risk against a risk model's
prediction, no way to see *which* position drives tracking error rather
than just the total, and no way to decompose risk by group instead of
by individual position — closed with `realized_volatility`,
`downside_deviation`, `realized_tracking_error`, marginal/component
contribution to tracking error, and `group_risk_contribution`; notebook
19 (VaR/ES) now plots the shaded VaR/ES tail and demonstrates checking a
risk model's assumed volatility against what a sample actually realized.

A pedagogy review of all 29 notebooks found a quality cliff at notebook
13: the earliest notebooks — the ones a true beginner hits first — were
the thinnest (5/12 template compliance on average, no plots anywhere
despite matplotlib being a dependency, zero `assert`-based self-checks
across all 29 notebooks, five with broken imports that had never been
executed). Notebooks 02, 03, 05, 07, 11, and 12 are rebuilt to the
standard the later notebooks already met — self-check asserts on every
`MANUAL FIRST` cell, plots where the audit specifically flagged one
missing, PREDICT questions moved before their code cells. `notebooks/foundations/00_orientation.ipynb`
is a new Day 0 for readers starting from zero: environment setup, the
PREDICT/MANUAL FIRST/ORAL CHECK cycle explained, and a linear-algebra
primer building `w' Sigma w` by hand before it appears "for real" in
notebook 02. `reference/glossary.md` is a one-line-per-term cheat sheet
across the whole curriculum. `notebooks/integration/30_capstone_portfolio_review.ipynb`
is a real capstone — using `data/mock_portfolio.csv`, `mock_benchmark.csv`,
and `mock_bonds.csv` (previously unused by any notebook) to compose risk
decomposition, active risk, bond-level DV01, a rates and a credit
scenario, and Brinson attribution into the one-page summary a PM would
actually read, closing out notebook 12's stub "Capstone" section that
was never built out.

## What's implemented vs. conceptual-only

The repository is deliberately explicit about this split — a reference
page for a harder topic states *why* it wasn't coded, rather than
shipping a shaky implementation. Examples: hierarchical risk parity,
regime-aware allocation, multi-period optimization, full OAS/MBS
negative-convexity pricing, non-agency tranche waterfalls, credit rating
migration matrices, and full multi-factor equity risk-model estimation
(Barra/Axioma-style). Each has a page explaining the specific machinery
that would be needed and why it's a materially bigger project than this
repo's "small transparent function" style. Treat those pages as
interview-ready conceptual fluency, not working code.

## Resources used

`resources/` is a short, curated pointer list (172 lines across 6
files), not a syllabus — its own instructions say "use the shortest
relevant resource first; do not turn resource discovery into the
learning task." Priority order: PIMCO (fixed-income framing), MIT
OpenCourseWare (mathematical intuition), CFA Institute (PM frameworks),
Aswath Damodaran / Kenneth French Data Library (equity valuation and
factor data), U.S. Treasury/FRED (public data), official Python docs.
The actual depth comes from the derive-code-test cycle, not from
reading.

## Mastering the curriculum

Starting from zero? Open `notebooks/foundations/00_orientation.ipynb`
first and keep `reference/glossary.md` open as a look-up while you work
— see "A pedagogy review..." above for what else changed to support
this. For rates, credit, and mortgages specifically, [Rates, credit, and
mortgages: zero to hero](./rates_credit_mortgages_roadmap.md) sequences
every reference page, notebook, and verified resource end to end.

- `/tutor <topic>` — a live, adaptive Socratic session on one concept,
  grounded in this repo's own reference pages, notebooks, and tests.
  Tracks per-concept status in `docs/mastery.md`.
- `/pm-query <question>` — a direct answer computed by actually running
  the relevant `src/pm` function, cited and logged.
- `/master` — a single, self-contained trainer covering the *entire*
  curriculum: `/master` teaches the next weak-or-untested concept in
  curriculum order, `/master quiz` runs 10 rapid multiple-choice checks
  (`/master quiz 20` for a bigger round), `/master scenario` applies
  confirmed concepts to a real use case, `/master exam` runs a
  multi-concept assessment ladder, and `/master status` gives a one-line
  progress readout. Use it to drive a full pass through the repository
  instead of picking topics one at a time — see
  [docs/mastery-guide.md](./mastery-guide.md) for a walkthrough.

## Fit for a bank → asset management move

Strongest for fixed-income, rates, credit, or multi-asset AM seats — the
FICC depth maps directly onto that background, and the portfolio-theory
layer (MVO, Black-Litterman, risk parity, tracking error, factor risk,
VaR/ES, Brinson attribution) supplies the buy-side vocabulary a
sell-side trading background often lacks. With Phase 13, equity
valuation, CAPM, factor investing, and active-share/shareholder-yield
mechanics are now covered the same way fixed income is — derived, coded,
and tested, not just described. Phase 14 closes what a repo-wide
completeness audit flagged as the single biggest remaining hole:
options/volatility, previously absent despite deep linear-instrument
coverage.

Remaining gaps the same audit found, still to close: asset allocation
framing (SAA/TAA, liability-driven investing) on top of the existing
optimization machinery; performance-measurement fundamentals
(time-weighted vs. money-weighted return, GIPS); narrower asset-class
coverage (municipal bonds, sovereign/EM debt, convertibles, preferred
securities); alternatives/private markets and ESG content. Also:
portfolio operations, compliance, and client reporting; live market data
and desk-grade tooling (Bloomberg PORT/Barra/Aladdin-equivalent
workflows); and depth beyond this repo's curated pointer list for
whatever specific topics an interview process tests hardest.
