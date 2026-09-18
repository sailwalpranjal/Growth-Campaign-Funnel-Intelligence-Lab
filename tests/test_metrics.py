"""
tests/test_metrics.py
---------------------
Unit tests for ratio-of-sums metric aggregation, formulas, and zero-denominator handling.
"""

import pytest
import pandas as pd
import numpy as np
from src.metrics import (
    safe_divide,
    calculate_ctr,
    calculate_cpc,
    calculate_cpm,
    calculate_conversion_rate,
    calculate_click_to_approved_rate,
    calculate_cost_per_approved_conversion,
    aggregate_campaign_scorecard
)


def test_safe_divide_scalars():
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) == 0.0
    assert safe_divide(0, 10) == 0.0
    assert safe_divide(5, np.nan) == 0.0


def test_safe_divide_series():
    num = pd.Series([10, 20, 30])
    den = pd.Series([2, 0, 5])
    res = safe_divide(num, den)
    assert res.iloc[0] == 5.0
    assert res.iloc[1] == 0.0
    assert res.iloc[2] == 6.0


def test_ctr_formula():
    # CTR = SUM(clicks) / SUM(impressions)
    assert calculate_ctr(100, 10000) == 0.01
    assert calculate_ctr(0, 10000) == 0.0
    assert calculate_ctr(100, 0) == 0.0


def test_cpc_and_cpm_formulas():
    # CPC = Spend / Clicks
    assert calculate_cpc(500.0, 250) == 2.0
    assert calculate_cpc(500.0, 0) == 0.0
    
    # CPM = (Spend / Impressions) * 1000
    assert calculate_cpm(10.0, 10000) == 1.0
    assert calculate_cpm(10.0, 0) == 0.0


def test_conversion_rates():
    assert calculate_conversion_rate(25, 500) == 0.05
    assert calculate_click_to_approved_rate(10, 500) == 0.02
    assert calculate_cost_per_approved_conversion(1000.0, 20) == 50.0
    assert calculate_cost_per_approved_conversion(1000.0, 0) == 0.0


def test_ratio_of_sums_vs_row_averaging():
    """
    Demonstrate why ratio-of-sums avoids Simpson's Paradox.
    Row 1: 1 click / 10 impressions (10% CTR)
    Row 2: 10 clicks / 10,000 impressions (0.1% CTR)
    Average of row CTRs: (10% + 0.1%) / 2 = 5.05% (MISLEADING!)
    True Ratio of Sums: 11 clicks / 10,010 impressions = 0.10989%
    """
    test_df = pd.DataFrame({
        "xyz_campaign_id": [1, 1],
        "ad_id": [101, 102],
        "impressions": [10, 10000],
        "clicks": [1, 10],
        "spent": [2.0, 20.0],
        "total_conversion": [1, 2],
        "approved_conversion": [0, 1]
    })
    
    scorecard = aggregate_campaign_scorecard(test_df)
    row_ctr = scorecard.iloc[0]["ctr"]
    
    expected_ratio_of_sums = 11 / 10010
    row_average = (1/10 + 10/10000) / 2
    
    assert pytest.approx(row_ctr, rel=1e-5) == expected_ratio_of_sums
    assert row_ctr != pytest.approx(row_average, rel=1e-2)
