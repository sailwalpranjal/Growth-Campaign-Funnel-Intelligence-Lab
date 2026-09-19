"""
scripts/export_web_data.py
--------------------------
Exports all real analytical findings, scorecards, decomposition values,
and experiment backlogs into a structured JSON file for the visual web dashboard.
"""

import json
import os
import sys
import pandas as pd

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from src.data_loader import load_raw_ad_campaigns, load_raw_consumer_behavior
from src.metrics import aggregate_campaign_scorecard, aggregate_by_dimension, get_metric_availability_table, safe_divide
from src.diagnostics import (
    decompose_efficiency_bridge, 
    analyze_segment_stability, 
    calculate_mix_adjustment, 
    analyze_consumer_behavior_diagnostics
)
from src.experiment_engine import get_experiment_backlog_df
from src.validation import generate_full_quality_audit


def main():
    print("[*] Exporting verified analytical data to web/data/dashboard_data.json...")
    
    df_ads = load_raw_ad_campaigns()
    df_uci = load_raw_consumer_behavior()
    
    scorecard_df = aggregate_campaign_scorecard(df_ads)
    decomp_dict = decompose_efficiency_bridge(scorecard_df, base_campaign_id=936, target_campaign_id=1178)
    mix_df = calculate_mix_adjustment(df_ads, segment_col="age", campaign_ids=[936, 1178])
    stability_df = analyze_segment_stability(df_ads, dimension="interest", thresholds=[10, 25, 50])
    audience_df = aggregate_by_dimension(df_ads, ["age", "gender"])
    
    # Multi-stage funnel
    funnel_rows = []
    for cid in sorted(df_ads["xyz_campaign_id"].unique()):
        c_sub = df_ads[df_ads["xyz_campaign_id"] == cid]
        imp = int(c_sub["impressions"].sum())
        clk = int(c_sub["clicks"].sum())
        tot = int(c_sub["total_conversion"].sum())
        app = int(c_sub["approved_conversion"].sum())
        funnel_rows.append({
            "campaign_id": int(cid),
            "impressions": imp,
            "clicks": clk,
            "total_conversions": tot,
            "approved_conversions": app,
            "ctr": round(safe_divide(clk, imp), 6),
            "click_to_enquiry_rate": round(safe_divide(tot, clk), 4),
            "enquiry_to_approved_rate": round(safe_divide(app, tot), 4),
            "cumulative_rate": round(safe_divide(app, imp), 8),
            "drop_clicks_to_enquiry_pct": round(1.0 - safe_divide(tot, clk), 4)
        })
        
    uci_results = analyze_consumer_behavior_diagnostics(df_uci)
    backlog_df = get_experiment_backlog_df()
    quality_df = generate_full_quality_audit(df_ads, df_uci)
    metric_avail_df = get_metric_availability_table()

    audience_segments = []
    for _, r in audience_df.iterrows():
        audience_segments.append({
            "age": str(r["age"]),
            "gender": str(r["gender"]),
            "clicks": int(r["total_clicks"]),
            "spend": float(r["total_spend"]),
            "approved": int(r["approved_conversions"]),
            "cost_per_approved": float(r["cost_per_approved_conv"]) if pd.notnull(r["cost_per_approved_conv"]) else 0.0,
            "ctr": float(r["ctr"])
        })
    
    web_data = {
        "metadata": {
            "project_name": "Khatabook Growth Intelligence Platform",
            "target_company": "Khatabook",
            "role": "Growth Product Analyst / Merchant Intelligence",
            "author": "Pranjal Sailwal",
            "generated_at": pd.Timestamp.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        },
        "scorecard": scorecard_df.to_dict(orient="records"),
        "decomposition": decomp_dict,
        "mix_adjustment": mix_df.to_dict(orient="records"),
        "funnel": funnel_rows,
        "segment_stability": stability_df.to_dict(orient="records"),
        "audience": audience_df.to_dict(orient="records"),
        "audience_segments": audience_segments,
        "consumer_behavior": {
            "visitor_type": uci_results["visitor_type"].to_dict(orient="records"),
            "traffic_type": uci_results["traffic_type"].to_dict(orient="records"),
            "engagement_tier": uci_results["engagement_tier"].to_dict(orient="records")
        },
        "experiments": backlog_df.to_dict(orient="records"),
        "data_quality": quality_df.to_dict(orient="records"),
        "metric_availability": metric_avail_df.to_dict(orient="records")
    }
    
    web_dir = os.path.join(root_dir, "web", "data")
    os.makedirs(web_dir, exist_ok=True)
    out_path = os.path.join(web_dir, "dashboard_data.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(web_data, f, indent=2)

    # Also keep root data/dashboard_data.json in sync for zero-config root hosting
    root_data_dir = os.path.join(root_dir, "data")
    root_out_path = os.path.join(root_data_dir, "dashboard_data.json")
    with open(root_out_path, "w", encoding="utf-8") as f:
        json.dump(web_data, f, indent=2)
        
    print(f"[+] Successfully exported web data to {out_path} and {root_out_path} ({os.path.getsize(out_path):,} bytes)")


if __name__ == "__main__":
    main()
