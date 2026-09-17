"""
scripts/export_reports.py
-------------------------
Generates all export deliverables:
1. Clean CSVs in exports/
2. Formatted multi-tab Excel dashboard in sheets/growth_dashboard.xlsx
3. Markdown growth reports in reports/
"""

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
from src.report_generator import export_csv_data, create_excel_dashboard, generate_markdown_reports


def main():
    print("[*] Generating all reports and dashboard deliverables...")
    
    # 1. Load Data
    df_ads = load_raw_ad_campaigns()
    df_uci = load_raw_consumer_behavior()
    
    # 2. Build Analytical Tables
    scorecard_df = aggregate_campaign_scorecard(df_ads)
    
    # Audience breakdown (Age x Gender)
    audience_df = aggregate_by_dimension(df_ads, ["age", "gender"])
    
    # Segment Stability
    stability_df = analyze_segment_stability(df_ads, dimension="interest", thresholds=[10, 25, 50])
    
    # Mix Analysis
    mix_df = calculate_mix_adjustment(df_ads, segment_col="age", campaign_ids=[936, 1178])
    
    # Funnel Analysis
    funnel_rows = []
    for cid in sorted(df_ads["xyz_campaign_id"].unique()):
        c_sub = df_ads[df_ads["xyz_campaign_id"] == cid]
        imp = c_sub["impressions"].sum()
        clk = c_sub["clicks"].sum()
        tot = c_sub["total_conversion"].sum()
        app = c_sub["approved_conversion"].sum()
        funnel_rows.append({
            "campaign_id": cid,
            "stage_1_impressions": int(imp),
            "stage_2_clicks": int(clk),
            "stage_3_total_conversions": int(tot),
            "stage_4_approved_conversions": int(app),
            "step_1_to_2_ctr": round(safe_divide(clk, imp), 6),
            "step_2_to_3_enquiry_rate": round(safe_divide(tot, clk), 4),
            "step_3_to_4_approval_rate": round(safe_divide(app, tot), 4),
            "cumulative_imp_to_approved_rate": round(safe_divide(app, imp), 8)
        })
    funnel_df = pd.DataFrame(funnel_rows)
    
    # Consumer Behavior
    uci_results = analyze_consumer_behavior_diagnostics(df_uci)
    consumer_df = uci_results["visitor_type"]
    
    # Experiment Backlog
    backlog_df = get_experiment_backlog_df()
    
    # Data Quality
    quality_df = generate_full_quality_audit(df_ads, df_uci)
    
    # Metric Availability
    metric_avail_df = get_metric_availability_table()
    
    # 3. Efficiency Bridge
    decomp_dict = decompose_efficiency_bridge(scorecard_df, base_campaign_id=936, target_campaign_id=1178)
    
    # Dictionary of all exports
    exports_dict = {
        "campaign_scorecard": scorecard_df,
        "audience_analysis": audience_df,
        "segment_stability": stability_df,
        "mix_analysis": mix_df,
        "funnel_analysis": funnel_df,
        "consumer_behavior": consumer_df,
        "experiment_backlog": backlog_df,
        "data_quality": quality_df,
        "metric_availability": metric_avail_df
    }
    
    # 4. Export CSVs
    export_dir = os.path.join(root_dir, "exports")
    export_csv_data(exports_dict, export_dir)
    
    # 5. Build Excel Workbook
    sheets_dir = os.path.join(root_dir, "sheets")
    excel_path = os.path.join(sheets_dir, "growth_dashboard.xlsx")
    create_excel_dashboard(exports_dict, excel_path)
    
    # 6. Generate Markdown Reports
    reports_dir = os.path.join(root_dir, "reports")
    generate_markdown_reports(exports_dict, decomp_dict, reports_dir)
    
    print("[+] All deliverables successfully generated and exported.")


if __name__ == "__main__":
    main()
