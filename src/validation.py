"""
src/validation.py
-----------------
Data quality and audit verification module.
Performs rigorous data hygiene checks on raw advertising and consumer behavior datasets.
"""

from typing import Dict, List, Any
import pandas as pd


def audit_ad_campaign_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform a comprehensive audit of the advertising campaign dataset.
    Returns a structured DataFrame of all audit checks, counts, and status.
    """
    records = []
    
    # Check 1: Missing values in critical fields
    critical_cols = ["ad_id", "xyz_campaign_id", "impressions", "clicks", "spent", "total_conversion", "approved_conversion"]
    missing_counts = df[critical_cols].isnull().sum().to_dict()
    total_missing = sum(missing_counts.values())
    records.append({
        "dataset": "Dataset A (Ad Campaigns)",
        "check_category": "Completeness",
        "check_name": "Missing Values Check",
        "flagged_count": int(total_missing),
        "status": "PASSED" if total_missing == 0 else "FAILED",
        "severity": "CRITICAL",
        "details": f"Missing values across critical columns: {missing_counts}"
    })
    
    # Check 2: Duplicate Ad IDs
    dup_count = int(df["ad_id"].duplicated().sum())
    records.append({
        "dataset": "Dataset A (Ad Campaigns)",
        "check_category": "Uniqueness",
        "check_name": "Duplicate Ad IDs",
        "flagged_count": dup_count,
        "status": "PASSED" if dup_count == 0 else "FAILED",
        "severity": "CRITICAL",
        "details": f"Found {dup_count} duplicate ad_id records."
    })
    
    # Check 3: Negative Numeric Values
    neg_imp = int((df["impressions"] < 0).sum())
    neg_clicks = int((df["clicks"] < 0).sum())
    neg_spent = int((df["spent"] < 0).sum())
    neg_total = neg_imp + neg_clicks + neg_spent
    records.append({
        "dataset": "Dataset A (Ad Campaigns)",
        "check_category": "Range / Validity",
        "check_name": "Negative Metric Values",
        "flagged_count": neg_total,
        "status": "PASSED" if neg_total == 0 else "FAILED",
        "severity": "CRITICAL",
        "details": f"Negative rows: impressions={neg_imp}, clicks={neg_clicks}, spent={neg_spent}"
    })
    
    # Check 4: Funnel Logic Violation: Clicks > Impressions
    clicks_gt_imp = int((df["clicks"] > df["impressions"]).sum())
    records.append({
        "dataset": "Dataset A (Ad Campaigns)",
        "check_category": "Funnel Logic",
        "check_name": "Clicks Exceed Impressions",
        "flagged_count": clicks_gt_imp,
        "status": "PASSED" if clicks_gt_imp == 0 else "FAILED",
        "severity": "CRITICAL",
        "details": f"Records where clicks > impressions (physically impossible): {clicks_gt_imp}"
    })
    
    # Check 5: Conversion Logic: Approved > Total Conversions
    app_gt_tot = int((df["approved_conversion"] > df["total_conversion"]).sum())
    records.append({
        "dataset": "Dataset A (Ad Campaigns)",
        "check_category": "Business Logic",
        "check_name": "Approved Exceeds Total Conversion",
        "flagged_count": app_gt_tot,
        "status": "PASSED" if app_gt_tot == 0 else "FAILED",
        "severity": "CRITICAL",
        "details": f"Records where approved_conversion > total_conversion: {app_gt_tot}"
    })
    
    # Check 6: Zero Clicks with Positive Spend
    zero_click_spend = int(((df["clicks"] == 0) & (df["spent"] > 0)).sum())
    spend_wasted = float(df.loc[(df["clicks"] == 0) & (df["spent"] > 0), "spent"].sum())
    records.append({
        "dataset": "Dataset A (Ad Campaigns)",
        "check_category": "Efficiency / Hygiene",
        "check_name": "Zero-Click Spend Ads",
        "flagged_count": zero_click_spend,
        "status": "FLAGGED" if zero_click_spend > 0 else "PASSED",
        "severity": "WARNING",
        "details": f"{zero_click_spend} ads spent positive budget (${spend_wasted:.2f}) without generating a single click."
    })
    
    # Check 7: Zero Impressions
    zero_imp = int((df["impressions"] == 0).sum())
    records.append({
        "dataset": "Dataset A (Ad Campaigns)",
        "check_category": "Delivery",
        "check_name": "Zero Impression Ads",
        "flagged_count": zero_imp,
        "status": "PASSED" if zero_imp == 0 else "FLAGGED",
        "severity": "INFO",
        "details": f"Ads with zero impressions: {zero_imp}"
    })
    
    # Check 8: Low Sample Records (< 10 Clicks)
    low_clicks = int((df["clicks"] < 10).sum())
    pct_low = (low_clicks / len(df)) * 100
    records.append({
        "dataset": "Dataset A (Ad Campaigns)",
        "check_category": "Statistical Reliability",
        "check_name": "Low-Sample Ad Records (< 10 Clicks)",
        "flagged_count": low_clicks,
        "status": "FLAGGED",
        "severity": "WARNING",
        "details": f"{low_clicks} of {len(df)} records ({pct_low:.1f}%) have <10 clicks, requiring ratio-of-sums aggregation to prevent noise."
    })
    
    return pd.DataFrame(records)


def audit_consumer_behavior_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform audit checks on the UCI Consumer Behavior dataset.
    """
    records = []
    
    # Check 1: Missing conversion outcome (Revenue is null)
    null_rev = int(df["revenue"].isnull().sum())
    records.append({
        "dataset": "Dataset B (UCI Consumer Behavior)",
        "check_category": "Completeness",
        "check_name": "Missing Revenue Labels",
        "flagged_count": null_rev,
        "status": "FLAGGED" if null_rev > 0 else "PASSED",
        "severity": "WARNING",
        "details": f"{null_rev} records have NULL Revenue. Filtered out before behavioral analysis."
    })
    
    # Check 2: Negative Durations
    duration_cols = ["administrative_duration", "informational_duration", "product_related_duration"]
    neg_dur = int(((df[duration_cols] < 0).any(axis=1)).sum())
    records.append({
        "dataset": "Dataset B (UCI Consumer Behavior)",
        "check_category": "Range / Validity",
        "check_name": "Negative Session Durations",
        "flagged_count": neg_dur,
        "status": "PASSED" if neg_dur == 0 else "FAILED",
        "severity": "CRITICAL",
        "details": f"{neg_dur} records with negative duration values."
    })
    
    # Check 3: Bounce and Exit Rate Range [0, 1]
    rate_out_of_bounds = int(((df["bounce_rates"] < 0) | (df["bounce_rates"] > 1.0) | 
                             (df["exit_rates"] < 0) | (df["exit_rates"] > 1.0)).sum())
    records.append({
        "dataset": "Dataset B (UCI Consumer Behavior)",
        "check_category": "Range / Validity",
        "check_name": "Bounce / Exit Rate Boundaries [0, 1]",
        "flagged_count": rate_out_of_bounds,
        "status": "PASSED" if rate_out_of_bounds == 0 else "FAILED",
        "severity": "CRITICAL",
        "details": f"{rate_out_of_bounds} records with bounce or exit rate outside [0, 1]."
    })
    
    return pd.DataFrame(records)


def generate_full_quality_audit(df_ads: pd.DataFrame, df_uci: pd.DataFrame) -> pd.DataFrame:
    """Run all quality audits across both datasets and return combined audit log."""
    ads_audit = audit_ad_campaign_data(df_ads)
    uci_audit = audit_consumer_behavior_data(df_uci)
    return pd.concat([ads_audit, uci_audit], ignore_index=True)
