"""Build a single-file, searchable HTML preview of the curriculum for
publishing as a Claude Artifact - a companion to the full MkDocs site
(docs/OVERVIEW.md explains why both exist) for readers who can't reach
GitHub Pages at all. Covers reference pages, curriculum, and use cases;
notebooks and code live in the full docs site and the repo itself.

Refresh manually when content changes meaningfully:
  python scripts/build_artifact_preview.py
Output is a gitignored build artifact; publish the resulting file with
the Artifact tool.
"""
import json
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "site_src" / "_artifact_preview.html"

MD_EXTENSIONS = ["tables", "fenced_code", "sane_lists", "toc"]

# Titles kept in sync with mkdocs.yml's nav labels for the same pages.
TITLES = {
    "reference/concepts/portfolio_return.md": "Portfolio Return",
    "reference/concepts/covariance.md": "Covariance",
    "reference/concepts/portfolio_volatility.md": "Portfolio Volatility",
    "reference/concepts/risk_contribution.md": "Risk Contribution",
    "reference/concepts/sharpe_ratio.md": "Sharpe Ratio",
    "reference/concepts/drawdown.md": "Drawdown",
    "reference/concepts/benchmark_basics.md": "Benchmark Basics",
    "reference/concepts/tracking_error.md": "Tracking Error",
    "reference/concepts/mean_variance_optimization.md": "Mean-Variance Optimization",
    "reference/concepts/factor_risk.md": "Factor Risk",
    "reference/concepts/factor_risk_contribution.md": "Factor Risk Contribution",
    "reference/concepts/value_at_risk.md": "Value at Risk",
    "reference/concepts/stress_testing.md": "Stress Testing",
    "reference/concepts/brinson_attribution.md": "Brinson Attribution",
    "reference/concepts/fixed_income_attribution.md": "Fixed-Income Attribution",
    "reference/concepts/transaction_costs_and_rebalancing.md": "Transaction Costs and Rebalancing",
    "reference/concepts/liquidity.md": "Liquidity",
    "reference/concepts/covariance_shrinkage.md": "Covariance Shrinkage",
    "reference/concepts/black_litterman.md": "Black-Litterman",
    "reference/concepts/risk_parity.md": "Risk Parity",
    "reference/concepts/scenario_robust_optimization.md": "Scenario-Robust Optimization",
    "reference/concepts/hierarchical_risk_parity.md": "Hierarchical Risk Parity",
    "reference/concepts/regime_aware_allocation.md": "Regime-Aware Allocation",
    "reference/concepts/multi_period_optimization.md": "Multi-Period Optimization",
    "reference/concepts/agentic_pm_analytics.md": "Agentic PM Analytics",
    "reference/fixed_income/bond_pricing.md": "Bond Pricing",
    "reference/fixed_income/duration.md": "Duration",
    "reference/fixed_income/dv01.md": "DV01",
    "reference/fixed_income/convexity.md": "Convexity",
    "reference/fixed_income/key_rate_duration.md": "Key-Rate Duration",
    "reference/fixed_income/spread_duration.md": "Spread Duration",
    "reference/fixed_income/curve_construction.md": "Curve Construction",
    "reference/fixed_income/forward_rates.md": "Forward Rates",
    "reference/fixed_income/curve_trades.md": "Curve Trades",
    "reference/fixed_income/swap_dv01.md": "Swap DV01",
    "reference/fixed_income/swap_spread.md": "Swap Spread",
    "reference/fixed_income/treasury_futures_hedging.md": "Treasury Futures Hedging",
    "reference/fixed_income/z_spread.md": "Z-Spread",
    "reference/fixed_income/oas.md": "OAS",
    "reference/fixed_income/credit_curves.md": "Credit Curves",
    "reference/fixed_income/default_recovery.md": "Default and Recovery",
    "reference/fixed_income/cds_and_basis.md": "CDS and Basis",
    "reference/fixed_income/credit_migration.md": "Credit Migration",
    "reference/fixed_income/pass_throughs.md": "Pass-Throughs",
    "reference/fixed_income/prepayment_models.md": "Prepayment Models",
    "reference/fixed_income/effective_duration.md": "Effective Duration",
    "reference/fixed_income/mbs_convexity.md": "MBS Convexity",
    "reference/fixed_income/non_agency_overview.md": "Non-Agency Overview",
    "reference/equity/dividend_discount_model.md": "Dividend Discount Model",
    "reference/equity/relative_valuation_multiples.md": "Relative Valuation Multiples",
    "reference/equity/capm_and_beta.md": "CAPM and Beta",
    "reference/equity/equity_factor_investing.md": "Equity Factor Investing",
    "reference/equity/active_share.md": "Active Share",
    "reference/equity/shareholder_yield.md": "Shareholder Yield",
    "reference/fx/spot_and_forward.md": "Spot and Forward",
    "reference/fx/cross_currency_basis.md": "Cross-Currency Basis",
    "reference/fx/fx_carry.md": "FX Carry",
    "reference/commodities/roll_yield.md": "Roll Yield",
}

USE_CASE_TITLES = {
    "duration_hedging": "Duration Hedging",
    "curve_positioning": "Curve Positioning",
    "spread_shock": "Spread Shock",
    "benchmark_relative": "Benchmark-Relative Risk",
    "swap_dv01_hedge": "Swap DV01 Hedge",
    "treasury_futures_hedge": "Treasury Futures Hedge",
    "equity_factor_tilt": "Equity Factor Tilt",
}

SECTIONS = [
    ("concepts", "Portfolio Concepts", "reference/concepts"),
    ("fixed_income", "Fixed Income", "reference/fixed_income"),
    ("equity", "Equity", "reference/equity"),
    ("fx", "FX", "reference/fx"),
    ("commodities", "Commodities", "reference/commodities"),
]


def md_to_html(text):
    return markdown.markdown(text, extensions=MD_EXTENSIONS)


def strip_h1(text):
    lines = text.lstrip().split("\n")
    if lines and lines[0].startswith("# "):
        return "\n".join(lines[1:]).lstrip("\n")
    return text


def build_pages():
    pages = []

    overview = (ROOT / "docs" / "OVERVIEW.md").read_text()
    pages.append({
        "id": "overview",
        "section": "Start Here",
        "title": "Repository Overview",
        "html": md_to_html(strip_h1(overview)),
    })

    curriculum = (ROOT / "curriculum" / "bootcamp_01_foundations" / "README.md").read_text()
    pages.append({
        "id": "curriculum",
        "section": "Start Here",
        "title": "Curriculum (14-Day Bootcamp)",
        "html": md_to_html(strip_h1(curriculum)),
    })

    for slug, label, reldir in SECTIONS:
        for path in sorted((ROOT / reldir).glob("*.md")):
            rel = str(path.relative_to(ROOT))
            title = TITLES.get(rel, path.stem.replace("_", " ").title())
            pages.append({
                "id": f"{slug}-{path.stem}",
                "section": label,
                "title": title,
                "html": md_to_html(strip_h1(path.read_text())),
            })

    for path in sorted((ROOT / "use_cases").glob("*/README.md")):
        slug = path.parent.name
        title = USE_CASE_TITLES.get(slug, slug.replace("_", " ").title())
        pages.append({
            "id": f"usecase-{slug}",
            "section": "Use Cases",
            "title": title,
            "html": md_to_html(strip_h1(path.read_text())),
        })

    return pages


PAGE_TEMPLATE = Path(__file__).with_name("_artifact_preview_template.html").read_text()


def render(pages):
    data_json = json.dumps(pages)
    # Neutralize "<" so the JSON can never contain a literal "</script>"
    # (or any tag) - < is a valid JSON escape, decoded correctly by
    # JSON.parse, so this is safe and standard for embedding JSON in HTML.
    safe_json = data_json.replace("<", "\\u003c")
    return PAGE_TEMPLATE.replace("__PAGES_JSON__", safe_json)


def main():
    pages = build_pages()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(pages))
    print(f"Wrote {OUT} ({len(pages)} pages, {OUT.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
