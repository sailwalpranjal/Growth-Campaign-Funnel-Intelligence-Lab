"""
scripts/prepare_data.py
-----------------------
Prepares staging data, initializes local SQL database, executes all SQL view definitions,
and validates data pipeline integrity.
"""

import os
import sys

# Add project root to sys.path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from src.data_loader import verify_provenance, init_database, load_raw_ad_campaigns, load_raw_consumer_behavior
from src.validation import generate_full_quality_audit


def main():
    print("[*] Starting Data Preparation & SQL Pipeline...")
    
    # 1. Verify Provenance
    print("[*] Verifying data provenance and SHA-256 checksums...")
    if not verify_provenance():
        print("[!] Provenance check failed. Run python scripts/download_data.py first.")
        sys.exit(1)
    print("[+] Provenance verified successfully.")
    
    # 2. Initialize SQL Database and execute SQL scripts
    print("[*] Initializing SQLite / SQL staging tables and views...")
    conn = init_database()
    print("[+] Executed sql/01_staging.sql through sql/07_quality.sql successfully.")
    
    # 3. Run Data Quality Audit
    print("[*] Running comprehensive Data Quality Audit...")
    df_ads = load_raw_ad_campaigns()
    df_uci = load_raw_consumer_behavior()
    audit_df = generate_full_quality_audit(df_ads, df_uci)
    
    # Check for critical failures
    critical_fails = audit_df[(audit_df["status"] == "FAILED") & (audit_df["severity"] == "CRITICAL")]
    if not critical_fails.empty:
        print(f"[X] Critical data quality check failed:\n{critical_fails}")
        sys.exit(1)
        
    print(f"[+] Data quality audit complete: {len(audit_df)} checks executed. Zero critical failures.")
    
    # 4. Save processed parquet snapshots for fast access
    proc_dir = os.path.join(root_dir, "data", "processed")
    os.makedirs(proc_dir, exist_ok=True)
    df_ads.to_parquet(os.path.join(proc_dir, "clean_ad_campaigns.parquet"), index=False)
    df_uci.to_parquet(os.path.join(proc_dir, "clean_consumer_behavior.parquet"), index=False)
    print(f"[+] Saved clean snapshots to {proc_dir}")
    print("[+] Data preparation complete.")


if __name__ == "__main__":
    main()
