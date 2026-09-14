import numpy as np
import pytest

from pm.active import (
    active_return,
    active_weights,
    effective_breadth,
    fundamental_law_ir,
    information_coefficient,
    information_ratio,
    tracking_error,
    transfer_coefficient,
)


def test_active_weights_sum_zero_when_both_fully_invested():
    p=np.array([.6,.4]); b=np.array([.5,.5])
    assert np.isclose(active_weights(p,b).sum(),0)

def test_zero_active_weights_zero_te():
    w=np.array([.5,.5]); cov=np.eye(2)*.04
    assert np.isclose(tracking_error(w,w,cov),0)

def test_active_return_hand_example():
    assert np.isclose(active_return(0.08, 0.05), 0.03)

def test_information_ratio_hand_example():
    # active returns = [0.02, 0.03, 0.01]; mean=0.02, sample std=0.01
    portfolio = [0.03, 0.05, 0.02]
    benchmark = [0.01, 0.02, 0.01]
    ir = information_ratio(portfolio, benchmark, periods_per_year=1)
    assert np.isclose(ir, 2.0)

def test_information_ratio_matches_direct_active_return_computation():
    rng = np.random.default_rng(0)
    portfolio = rng.normal(0.01, 0.02, 24)
    benchmark = rng.normal(0.008, 0.015, 24)
    active = portfolio - benchmark
    expected = active.mean() / active.std(ddof=1) * np.sqrt(12)
    assert np.isclose(information_ratio(portfolio, benchmark, periods_per_year=12), expected)

def test_information_ratio_zero_when_portfolio_tracks_benchmark_exactly():
    p = [0.01, 0.02, -0.01, 0.03]
    with pytest.raises(ValueError, match="must be positive and finite"):
        information_ratio(p, p)

def test_information_ratio_rejects_mismatched_shapes():
    with pytest.raises(ValueError, match="same shape"):
        information_ratio([0.01, 0.02], [0.01, 0.02, 0.03])

def test_information_coefficient_perfect_forecast_is_one():
    forecasts = [1, 2, 3]
    realized = [0.01, 0.02, 0.03]
    assert np.isclose(information_coefficient(forecasts, realized), 1.0)

def test_information_coefficient_inverted_forecast_is_negative_one():
    forecasts = [1, 2, 3]
    realized = [0.03, 0.02, 0.01]
    assert np.isclose(information_coefficient(forecasts, realized), -1.0)

def test_information_coefficient_rejects_constant_forecasts():
    with pytest.raises(ValueError, match="nonzero variance"):
        information_coefficient([1, 1, 1], [0.01, 0.02, 0.03])

def test_effective_breadth_uncorrelated_bets_equals_n():
    assert np.isclose(effective_breadth(100, average_correlation=0.0), 100.0)

def test_effective_breadth_fully_correlated_bets_collapses_to_one():
    assert np.isclose(effective_breadth(100, average_correlation=1.0), 1.0)

def test_effective_breadth_hand_example():
    # 10 bets, average pairwise correlation 0.5 -> 10 / (1 + 9*0.5) = 10/5.5
    assert np.isclose(effective_breadth(10, average_correlation=0.5), 10 / 5.5)

def test_effective_breadth_decreases_with_correlation():
    low = effective_breadth(50, average_correlation=0.1)
    high = effective_breadth(50, average_correlation=0.6)
    assert high < low

def test_transfer_coefficient_perfectly_aligned_bets_is_one():
    unconstrained = [0.10, -0.05, 0.03, 0.02]
    actual = unconstrained  # no constraints bind: identical weights
    assert np.isclose(transfer_coefficient(actual, unconstrained), 1.0)

def test_transfer_coefficient_is_scale_invariant():
    # TC is a correlation, so uniformly shrinking every active weight by
    # the same constraint (e.g. a leverage cap) still gives TC=1 - it
    # measures whether constraints changed the *direction* of the bets,
    # not whether they reduced their size. See reference page Limitations.
    unconstrained = np.array([0.10, -0.05, 0.03, 0.02])
    actual = 0.5 * unconstrained
    assert np.isclose(transfer_coefficient(actual, unconstrained), 1.0)

def test_transfer_coefficient_unrelated_bets_near_zero():
    unconstrained = [0.10, -0.05, 0.03, 0.02, 0.01, -0.02]
    actual = [0.01, 0.02, -0.03, 0.10, -0.05, 0.03]
    tc = transfer_coefficient(actual, unconstrained)
    assert abs(tc) < 0.5

def test_fundamental_law_hand_example():
    # IR ~= IC * sqrt(BR) * TC = 0.05 * sqrt(100) * 1.0 = 0.5
    assert np.isclose(fundamental_law_ir(0.05, 100, 1.0), 0.5)

def test_fundamental_law_default_transfer_coefficient_is_unconstrained():
    assert np.isclose(fundamental_law_ir(0.05, 100), fundamental_law_ir(0.05, 100, 1.0))

def test_fundamental_law_scales_linearly_with_transfer_coefficient():
    full = fundamental_law_ir(0.05, 100, transfer_coefficient_value=1.0)
    half = fundamental_law_ir(0.05, 100, transfer_coefficient_value=0.5)
    assert np.isclose(half, 0.5 * full)

def test_fundamental_law_composes_with_effective_breadth():
    # Doubling breadth with zero correlation is a straightforward
    # substitution; the composed call should match calling the law
    # directly with that same effective breadth.
    br = effective_breadth(400, average_correlation=0.0)
    assert np.isclose(fundamental_law_ir(0.05, br), fundamental_law_ir(0.05, 400))

def test_fundamental_law_correlated_bets_reduce_expected_ir():
    ic = 0.05
    independent = fundamental_law_ir(ic, effective_breadth(100, average_correlation=0.0))
    correlated = fundamental_law_ir(ic, effective_breadth(100, average_correlation=0.3))
    assert correlated < independent
