"""
tests/test_diagnostics.py
-------------------------
Unit tests for efficiency decomposition bridge, mix-adjustment math, and segment stability.
"""

import pytest
import pandas as pd
from src.metrics import aggregate_campaign_scorecard
from src.diagnostics import (
    decompose_efficiency_bridge,
    analyze_segment_stability,
    calculate_mix_adjustment
)


@pytest.fixture
def mock_campaign_df():
    """Create reproducible test campaign data with known variance."""
    data = []
    # Campaign A (Efficient, Low Scale)
    for i in range(10):
        data.append({
            "ad_id": 100 + i,
            "xyz_campaign_id": 936,
            "age": "30-34" if i < 5 else "35-39",
            "gender": "M" if i % 2 == 0 else "F",
            "interest": 10 + (i % 3),
            "impressions": 100000,
            "clicks": 50,
            "spent": 50.0,
            "total_conversion": 10,
            "approved_conversion": 5
        })
    # Campaign B (Inefficient, Scaled)
    for i in range(10):
        data.append({
            "ad_id": 200 + i,
            "xyz_campaign_id": 1178,
            "age": "30-34" if i < 3 else "45-49", # Demographic skew
            "gender": "M" if i % 2 == 0 else "F",
            "interest": 10 + (i % 3),
            "impressions": 500000,
            "clicks": 100,
            "spent": 200.0,
            "total_conversion": 8,
            "approved_conversion": 2
        })
    return pd.DataFrame(data)


def test_decomposition_bridge_mathematical_identity(mock_campaign_df):
    """
    Verify that the sequential substitution decomposition bridge sums to
    100.000% of the cost difference with zero residual error.
    """
    scorecard = aggregate_campaign_scorecard(mock_campaign_df)
    decomp = decompose_efficiency_bridge(scorecard, base_campaign_id=936, target_campaign_id=1178)
    
    cost_gap = decomp["cost_gap"]
    reconciled_sum = decomp["reconciled_sum"]
    error = decomp["reconciliation_error"]
    
    assert pytest.approx(cost_gap, rel=1e-6) == reconciled_sum
    assert error < 1e-6
    assert decomp["cpm_effect"] + decomp["ctr_effect"] + decomp["conv_effect"] == pytest.approx(cost_gap, rel=1e-6)


def test_segment_stability_thresholding(mock_campaign_df):
    """Verify segment stability classifications across sample thresholds."""
    stability_df = analyze_segment_stability(mock_campaign_df, dimension="interest", thresholds=[10, 25, 50])
    
    assert "stability_classification" in stability_df.columns
    assert "qualifies_t10" in stability_df.columns
    assert "qualifies_t25" in stability_df.columns
    assert "qualifies_t50" in stability_df.columns
    
    # Check that high click segments qualify for t50
    high_sample = stability_df[stability_df["total_clicks"] >= 50]
    for _, row in high_sample.iterrows():
        assert row["qualifies_t50"] is True
        assert "Stable" in row["stability_classification"]


def test_mix_adjustment_direct_standardization(mock_campaign_df):
    """Verify that mix-adjusted calculation isolates demographic composition."""
    mix_df = calculate_mix_adjustment(mock_campaign_df, segment_col="age", campaign_ids=[936, 1178])
    
    assert len(mix_df) == 2
    assert "raw_cost_per_approved" in mix_df.columns
    assert "mix_adjusted_cost_per_approved" in mix_df.columns
    assert "cost_gap_mix_effect" in mix_df.columns
    
    # Both campaigns should have valid positive rates
    assert (mix_df["mix_adjusted_cost_per_approved"] > 0).all()
