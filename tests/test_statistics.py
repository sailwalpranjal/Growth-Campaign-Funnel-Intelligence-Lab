"""
tests/test_statistics.py
------------------------
Unit tests for two-proportion hypothesis testing, confidence intervals,
sample size planning, and growth decision frameworks.
"""

import pytest
import math
from scipy import stats
from src.statistics import two_proportion_z_test, calculate_sample_size_required


def test_two_proportion_z_test_calculation():
    """Verify z-test against manual analytical formulas."""
    # Control: 100 conversions / 1000 visitors (10%)
    # Treatment: 130 conversions / 1000 visitors (13%)
    res = two_proportion_z_test(
        control_conversions=100,
        control_sample=1000,
        treatment_conversions=130,
        treatment_sample=1000
    )
    
    assert res["control_rate"] == 0.10
    assert res["treatment_rate"] == 0.13
    assert pytest.approx(res["absolute_lift"], rel=1e-4) == 0.03
    assert pytest.approx(res["relative_lift"], rel=1e-4) == 0.30
    
    # Manual z-score
    p_pool = (100 + 130) / 2000
    se = math.sqrt(p_pool * (1 - p_pool) * (2 / 1000))
    expected_z = 0.03 / se
    expected_p = 2.0 * (1.0 - stats.norm.cdf(expected_z))
    
    assert pytest.approx(res["z_score"], rel=1e-3) == expected_z
    assert pytest.approx(res["p_value"], rel=1e-3) == expected_p
    assert res["is_statistically_significant"] is True
    assert res["decision"] == "Promote cautiously"


def test_underpowered_test_decision():
    """Verify that small samples are not prematurely declared winners or nulls."""
    # 5 conversions / 50 visitors vs 8 conversions / 50 visitors
    res = two_proportion_z_test(
        control_conversions=5,
        control_sample=50,
        treatment_conversions=8,
        treatment_sample=50
    )
    assert not res["is_statistically_significant"]
    assert "Run longer" in res["decision"]


def test_sample_size_calculation():
    """Verify sample size required for given MDE and baseline."""
    # Baseline 5%, MDE 20% relative (p2 = 6%), alpha=0.05, power=0.80
    n = calculate_sample_size_required(
        baseline_conversion_rate=0.05,
        minimum_detectable_effect=0.20,
        alpha=0.05,
        power=0.80
    )
    # Standard Evan Miller sample size is ~7,500 - 8,000 per variant
    assert 7000 <= n <= 8500


def test_invalid_parameters():
    with pytest.raises(ValueError):
        two_proportion_z_test(10, 0, 10, 100)
    with pytest.raises(ValueError):
        calculate_sample_size_required(0.0, 0.1)
    with pytest.raises(ValueError):
        calculate_sample_size_required(0.1, 0.0)
