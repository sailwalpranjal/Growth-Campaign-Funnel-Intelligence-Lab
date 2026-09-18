"""
tests/test_funnel.py
--------------------
Unit tests for multi-stage acquisition funnel and drop-off rate calculations.
"""

import pytest
import pandas as pd
from src.metrics import safe_divide


def test_funnel_stage_transitions():
    impressions = 1000000
    clicks = 2000
    total_conv = 200
    approved_conv = 50
    
    # Step conversion rates
    step1_ctr = safe_divide(clicks, impressions)
    step2_enquiry = safe_divide(total_conv, clicks)
    step3_approval = safe_divide(approved_conv, total_conv)
    
    # Cumulative conversion rate
    cumulative_rate = safe_divide(approved_conv, impressions)
    
    assert step1_ctr == 0.002
    assert step2_enquiry == 0.10
    assert step3_approval == 0.25
    assert cumulative_rate == 0.00005
    
    # Mathematical identity: cumulative == product of step rates
    step_product = step1_ctr * step2_enquiry * step3_approval
    assert pytest.approx(cumulative_rate, rel=1e-6) == step_product


def test_funnel_drop_off_volumes_and_percentages():
    impressions = 500000
    clicks = 1000
    total_conv = 100
    approved_conv = 20
    
    drop_1 = impressions - clicks
    drop_2 = clicks - total_conv
    drop_3 = total_conv - approved_conv
    
    assert drop_1 == 499000
    assert drop_2 == 900
    assert drop_3 == 80
    
    drop_rate_1 = 1.0 - (clicks / impressions)
    drop_rate_2 = 1.0 - (total_conv / clicks)
    drop_rate_3 = 1.0 - (approved_conv / total_conv)
    
    assert pytest.approx(drop_rate_1, rel=1e-5) == 0.998
    assert pytest.approx(drop_rate_2, rel=1e-5) == 0.90
    assert pytest.approx(drop_rate_3, rel=1e-5) == 0.80
