"""
tests/test_quality.py
---------------------
Unit tests for data quality audit rules, anomaly detection, and hygiene validation.
"""

import pytest
import pandas as pd
from src.validation import audit_ad_campaign_data, audit_consumer_behavior_data


def test_clean_data_passes_critical_checks():
    """Verify clean dummy ad dataset passes all critical data quality checks."""
    df_clean = pd.DataFrame({
        "ad_id": [1, 2, 3],
        "xyz_campaign_id": [936, 936, 1178],
        "impressions": [1000, 2000, 3000],
        "clicks": [10, 20, 30],
        "spent": [15.0, 30.0, 45.0],
        "total_conversion": [2, 4, 6],
        "approved_conversion": [1, 2, 3]
    })
    
    audit_res = audit_ad_campaign_data(df_clean)
    critical_fails = audit_res[(audit_res["status"] == "FAILED") & (audit_res["severity"] == "CRITICAL")]
    assert critical_fails.empty


def test_anomaly_clicks_exceed_impressions():
    """Verify that clicks > impressions is flagged as CRITICAL FAILED."""
    df_anomaly = pd.DataFrame({
        "ad_id": [1],
        "xyz_campaign_id": [936],
        "impressions": [10],
        "clicks": [50], # Impossible
        "spent": [15.0],
        "total_conversion": [1],
        "approved_conversion": [1]
    })
    
    audit_res = audit_ad_campaign_data(df_anomaly)
    failed_check = audit_res[audit_res["check_name"] == "Clicks Exceed Impressions"]
    assert failed_check.iloc[0]["status"] == "FAILED"
    assert failed_check.iloc[0]["flagged_count"] == 1


def test_anomaly_approved_exceeds_total():
    """Verify approved > total conversions is flagged as CRITICAL FAILED."""
    df_anomaly = pd.DataFrame({
        "ad_id": [1],
        "xyz_campaign_id": [936],
        "impressions": [100],
        "clicks": [10],
        "spent": [15.0],
        "total_conversion": [2],
        "approved_conversion": [5] # Impossible
    })
    
    audit_res = audit_ad_campaign_data(df_anomaly)
    failed_check = audit_res[audit_res["check_name"] == "Approved Exceeds Total Conversion"]
    assert failed_check.iloc[0]["status"] == "FAILED"
    assert failed_check.iloc[0]["flagged_count"] == 1


def test_duplicate_ad_ids_flagged():
    df_dups = pd.DataFrame({
        "ad_id": [1, 1], # Duplicate primary key
        "xyz_campaign_id": [936, 936],
        "impressions": [100, 100],
        "clicks": [5, 5],
        "spent": [10.0, 10.0],
        "total_conversion": [1, 1],
        "approved_conversion": [0, 0]
    })
    
    audit_res = audit_ad_campaign_data(df_dups)
    dup_check = audit_res[audit_res["check_name"] == "Duplicate Ad IDs"]
    assert dup_check.iloc[0]["status"] == "FAILED"
    assert dup_check.iloc[0]["flagged_count"] == 1


def test_consumer_behavior_null_revenue_flagged():
    df_uci = pd.DataFrame({
        "session_id": [1, 2],
        "administrative_duration": [10.0, 20.0],
        "informational_duration": [0.0, 5.0],
        "product_related_duration": [100.0, 200.0],
        "bounce_rates": [0.01, 0.02],
        "exit_rates": [0.02, 0.04],
        "revenue": [True, None] # Null label
    })
    
    audit_res = audit_consumer_behavior_data(df_uci)
    null_rev = audit_res[audit_res["check_name"] == "Missing Revenue Labels"]
    assert null_rev.iloc[0]["status"] == "FLAGGED"
    assert null_rev.iloc[0]["flagged_count"] == 1
