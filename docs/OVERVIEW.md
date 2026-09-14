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
| Analytics code | 766 lines across 24 modules in `src/pm/` |
| Tests | 94 passing, 14 test files |
| Notebooks | 29, across 7 tracks (foundations, optimization, active, fixed income, FX/commodities, equity, integration) |
| Reference pages | 59 |
| Roadmap phases | 13 of 13 complete |
| Bootcamp curriculum | 14 days (5 core + 9 extension) |
| Use-case workflows | 7 |
| Curated resource files | 6, 172 lines total |
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
| 2 | Portfolio theory & optimization — efficient frontier, mean-variance optimization, shrinkage, Black-Litterman |
| 3 | Active management — active weights, tracking error, information ratio, factor models |
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

Fixed income (Phases 5–8) remains the deepest vein by page count and
code volume — rates, credit, and mortgages are each fully built out with
tested code, not left conceptual. Phase 13 (equity) closes what used to
be this repo's one clear gap: previously "equity" appeared only as a
generic example asset class, with no valuation, CAPM, or factor-investing
material anywhere.

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
and tested, not just described.

Remaining gaps to cover elsewhere: portfolio operations, compliance,
client reporting, and ESG content; live market data and desk-grade
tooling (Bloomberg PORT/Barra/Aladdin-equivalent workflows); and depth
beyond this repo's curated pointer list for whatever specific topics an
interview process tests hardest.
