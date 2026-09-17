"""
src/metrics.py
--------------
Ratio-of-Sums aggregation engine and core growth metric definitions.
Enforces strict mathematical aggregation: SUM(numerator) / NULLIF(SUM(denominator)).
Prevents Simpson's paradox, row-averaging bias, and zero-division errors.
"""

from typing import Dict, List, Optional, Union
import numpy as np
import pandas as pd


def safe_divide(numerator: Union[float, int, np.ndarray, pd.Series], 
                denominator: Union[float, int, np.ndarray, pd.Series], 
                default: float = 0.0) -> Union[float, np.ndarray, pd.Series]:
    """
    Safely divide numerator by denominator, returning default when denominator is zero or NaN.
    """
    if isinstance(denominator, (pd.Series, np.ndarray)):
        denom_clean = np.where(denominator == 0, np.nan, denominator)
        res = numerator / denom_clean
        if isinstance(res, pd.Series):
            return res.fillna(default)
        return np.nan_to_num(res, nan=default)
    else:
        if denominator == 0 or pd.isna(denominator):
            return default
        return numerator / denominator


def calculate_ctr(clicks: Union[float, int], impressions: Union[float, int]) -> float:
    """Click-Through Rate = SUM(Clicks) / SUM(Impressions)."""
    return safe_divide(clicks, impressions)


def calculate_cpc(spent: Union[float, int], clicks: Union[float, int]) -> float:
    """Cost Per Click = SUM(Spent) / SUM(Clicks)."""
    return safe_divide(spent, clicks)


def calculate_cpm(spent: Union[float, int], impressions: Union[float, int]) -> float:
    """Cost Per Mille (Thousand Impressions) = (SUM(Spent) / SUM(Impressions)) * 1000."""
    return safe_divide(spent, impressions) * 1000.0


def calculate_conversion_rate(conversions: Union[float, int], clicks: Union[float, int]) -> float:
    """Click-to-Total-Conversion Rate = SUM(Total_Conversion) / SUM(Clicks)."""
    return safe_divide(conversions, clicks)


def calculate_click_to_approved_rate(approved: Union[float, int], clicks: Union[float, int]) -> float:
    """Click-to-Approved-Conversion Rate = SUM(Approved_Conversion) / SUM(Clicks)."""
    return safe_divide(approved, clicks)


def calculate_cost_per_total_conversion(spent: Union[float, int], conversions: Union[float, int]) -> float:
    """Cost Per Total Conversion (Enquiry) = SUM(Spent) / SUM(Total_Conversion)."""
    return safe_divide(spent, conversions)


def calculate_cost_per_approved_conversion(spent: Union[float, int], approved: Union[float, int]) -> float:
    """
    Cost Per Approved Conversion = SUM(Spent) / SUM(Approved_Conversion).
    NOTE: Not labeled CAC because this dataset does not track downstream customer lifecycle,
    blended organic acquisition, or paid-to-activation retention.
    """
    return safe_divide(spent, approved)


def calculate_metric_scorecard(df: pd.DataFrame) -> Dict[str, Union[int, float]]:
    """
    Calculate full ratio-of-sums scorecard for a given slice of ad data.
    """
    tot_imp = df["impressions"].sum()
    tot_clicks = df["clicks"].sum()
    tot_spent = df["spent"].sum()
    tot_conv = df["total_conversion"].sum()
    tot_app = df["approved_conversion"].sum()
    
    return {
        "impressions": int(tot_imp),
        "clicks": int(tot_clicks),
        "spent": round(float(tot_spent), 2),
        "total_conversions": int(tot_conv),
        "approved_conversions": int(tot_app),
        "ctr": calculate_ctr(tot_clicks, tot_imp),
        "cpc": round(calculate_cpc(tot_spent, tot_clicks), 4),
        "cpm": round(calculate_cpm(tot_spent, tot_imp), 4),
        "conversion_rate": calculate_conversion_rate(tot_conv, tot_clicks),
        "click_to_approved_rate": calculate_click_to_approved_rate(tot_app, tot_clicks),
        "cost_per_conversion": round(calculate_cost_per_total_conversion(tot_spent, tot_conv), 2),
        "cost_per_approved_conversion": round(calculate_cost_per_approved_conversion(tot_spent, tot_app), 2)
    }


def aggregate_campaign_scorecard(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute campaign-level scorecard using strict ratio-of-sums aggregation.
    """
    grouped = df.groupby("xyz_campaign_id").agg({
        "ad_id": "count",
        "impressions": "sum",
        "clicks": "sum",
        "spent": "sum",
        "total_conversion": "sum",
        "approved_conversion": "sum"
    }).reset_index()
    
    grouped = grouped.rename(columns={
        "xyz_campaign_id": "campaign_id",
        "ad_id": "total_ads",
        "impressions": "total_impressions",
        "clicks": "total_clicks",
        "spent": "total_spend",
        "total_conversion": "total_conversions",
        "approved_conversion": "approved_conversions"
    })
    
    grouped["ctr"] = safe_divide(grouped["total_clicks"], grouped["total_impressions"])
    grouped["cpc"] = safe_divide(grouped["total_spend"], grouped["total_clicks"])
    grouped["cpm"] = safe_divide(grouped["total_spend"], grouped["total_impressions"]) * 1000.0
    grouped["click_to_total_conv_rate"] = safe_divide(grouped["total_conversions"], grouped["total_clicks"])
    grouped["click_to_approved_conv_rate"] = safe_divide(grouped["approved_conversions"], grouped["total_clicks"])
    grouped["cost_per_total_conv"] = safe_divide(grouped["total_spend"], grouped["total_conversions"])
    grouped["cost_per_approved_conv"] = safe_divide(grouped["total_spend"], grouped["approved_conversions"])
    
    # Lever decomposition values
    grouped["cost_per_impression"] = safe_divide(grouped["total_spend"], grouped["total_impressions"])
    grouped["impressions_per_click"] = safe_divide(grouped["total_impressions"], grouped["total_clicks"])
    grouped["clicks_per_approved"] = safe_divide(grouped["total_clicks"], grouped["approved_conversions"])
    
    return grouped


def aggregate_by_dimension(df: pd.DataFrame, group_cols: List[str]) -> pd.DataFrame:
    """
    Aggregate ad performance by arbitrary audience or creative dimension(s).
    """
    grouped = df.groupby(group_cols).agg({
        "ad_id": "count",
        "impressions": "sum",
        "clicks": "sum",
        "spent": "sum",
        "total_conversion": "sum",
        "approved_conversion": "sum"
    }).reset_index()
    
    grouped = grouped.rename(columns={
        "ad_id": "ad_count",
        "impressions": "total_impressions",
        "clicks": "total_clicks",
        "spent": "total_spend",
        "total_conversion": "total_conversions",
        "approved_conversion": "approved_conversions"
    })
    
    grouped["ctr"] = safe_divide(grouped["total_clicks"], grouped["total_impressions"])
    grouped["cpc"] = safe_divide(grouped["total_spend"], grouped["total_clicks"])
    grouped["cpm"] = safe_divide(grouped["total_spend"], grouped["total_impressions"]) * 1000.0
    grouped["click_to_approved_rate"] = safe_divide(grouped["approved_conversions"], grouped["total_clicks"])
    grouped["cost_per_approved_conv"] = safe_divide(grouped["total_spend"], grouped["approved_conversions"])
    
    # Sample qualification classification
    grouped["qualification_state"] = np.select(
        [
            grouped["total_clicks"] >= 50,
            grouped["total_clicks"] >= 25,
            grouped["total_clicks"] >= 10
        ],
        [
            "Qualified (High Sample)",
            "Qualified (Medium Sample)",
            "Directional (Low Sample)"
        ],
        default="Unreliable (Sample < 10)"
    )
    
    return grouped


def get_metric_availability_table() -> pd.DataFrame:
    """
    Return formal Metric Availability & Boundary Table demonstrating growth analytical discipline.
    """
    records = [
        {"metric": "Impressions", "available": "Yes", "exact_formula": "SUM(Impressions)", "reason": "Directly recorded ad impression volume."},
        {"metric": "Clicks", "available": "Yes", "exact_formula": "SUM(Clicks)", "reason": "Directly recorded ad clicks."},
        {"metric": "Spend", "available": "Yes", "exact_formula": "SUM(Spent)", "reason": "Directly recorded ad media expenditure."},
        {"metric": "CTR", "available": "Yes", "exact_formula": "SUM(Clicks) / SUM(Impressions)", "reason": "Real top-of-funnel creative engagement rate."},
        {"metric": "CPC", "available": "Yes", "exact_formula": "SUM(Spent) / SUM(Clicks)", "reason": "Real media auction cost efficiency per click."},
        {"metric": "CPM", "available": "Yes", "exact_formula": "(SUM(Spent) / SUM(Impressions)) * 1000", "reason": "Real baseline media inventory pricing."},
        {"metric": "Cost per Approved Conversion", "available": "Yes", "exact_formula": "SUM(Spent) / SUM(Approved_Conversion)", "reason": "Real cost per verified end conversion."},
        {"metric": "CAC (Customer Acquisition Cost)", "available": "No (Unsupported)", "exact_formula": "N/A", "reason": "Lacks full marketing spend, blended organic acquisition, agency fees, and downstream retention."},
        {"metric": "ROAS (Return on Ad Spend)", "available": "No (Unsupported)", "exact_formula": "N/A", "reason": "No monetary transaction revenue exists in the ad dataset. Creating fake revenue violates analytical integrity."},
        {"metric": "Mobile App Installs", "available": "No (Unavailable)", "exact_formula": "N/A", "reason": "Web conversion tracking dataset; does not track SDK install attribution."},
        {"metric": "User Login / Retention", "available": "No (Unavailable)", "exact_formula": "N/A", "reason": "No user authentication or post-install cohort logs in public advertising dataset."}
    ]
    return pd.DataFrame(records)
