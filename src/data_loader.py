"""
src/data_loader.py
------------------
Data loading, hash validation, and SQL database synchronization module.
"""

import hashlib
import json
import os
import sqlite3
from typing import Dict, Optional, Tuple
import pandas as pd


def get_project_root() -> str:
    """Return the absolute path to the project root directory."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def compute_sha256(filepath: str) -> str:
    """Compute the SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def verify_provenance(raw_dir: Optional[str] = None) -> bool:
    """Verify that raw files match the recorded SHA-256 checksums."""
    root = get_project_root()
    raw_dir = raw_dir or os.path.join(root, "data", "raw")
    meta_path = os.path.join(raw_dir, "provenance_metadata.json")
    
    if not os.path.exists(meta_path):
        print(f"[!] Provenance metadata not found at {meta_path}. Run scripts/download_data.py first.")
        return False
        
    with open(meta_path, "r", encoding="utf-8") as f:
        metadata = json.load(f)
        
    for name, info in metadata.get("datasets", {}).items():
        filepath = os.path.join(raw_dir, info["filename"])
        if not os.path.exists(filepath):
            print(f"[!] File missing: {filepath}")
            return False
        current_hash = compute_sha256(filepath)
        if current_hash != info["sha256"]:
            print(f"[!] Hash mismatch for {info['filename']}: expected {info['sha256']}, got {current_hash}")
            return False
            
    return True


def load_raw_ad_campaigns(raw_dir: Optional[str] = None) -> pd.DataFrame:
    """Load the raw Kaggle Clicks Conversion Tracking CSV into a DataFrame."""
    root = get_project_root()
    raw_dir = raw_dir or os.path.join(root, "data", "raw")
    filepath = os.path.join(raw_dir, "KAG_conversion_data.csv")
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Raw ad dataset not found at {filepath}. Run scripts/download_data.py first.")
        
    df = pd.read_csv(filepath)
    # Standardize column names
    rename_dict = {
        "Impressions": "impressions",
        "Clicks": "clicks",
        "Spent": "spent",
        "Total_Conversion": "total_conversion",
        "Approved_Conversion": "approved_conversion"
    }
    df = df.rename(columns=rename_dict)
    return df


def load_raw_consumer_behavior(raw_dir: Optional[str] = None) -> pd.DataFrame:
    """Load the raw UCI Online Shoppers Purchasing Intention CSV into a DataFrame."""
    root = get_project_root()
    raw_dir = raw_dir or os.path.join(root, "data", "raw")
    filepath = os.path.join(raw_dir, "online_shoppers_intention.csv")
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Raw consumer behavior dataset not found at {filepath}. Run scripts/download_data.py first.")
        
    df = pd.read_csv(filepath)
    # Add explicit 1-indexed session_id primary key if not present
    if "session_id" not in df.columns:
        df.insert(0, "session_id", range(1, len(df) + 1))
        
    # Standardize column names to snake_case matching SQL schema
    uci_rename = {
        "Administrative": "administrative",
        "Administrative_Duration": "administrative_duration",
        "Informational": "informational",
        "Informational_Duration": "informational_duration",
        "ProductRelated": "product_related",
        "ProductRelated_Duration": "product_related_duration",
        "BounceRates": "bounce_rates",
        "ExitRates": "exit_rates",
        "PageValues": "page_values",
        "SpecialDay": "special_day",
        "Month": "month",
        "OperatingSystems": "operating_systems",
        "Browser": "browser",
        "Region": "region",
        "TrafficType": "traffic_type",
        "VisitorType": "visitor_type",
        "Weekend": "weekend",
        "Revenue": "revenue"
    }
    df = df.rename(columns=uci_rename)
    df.columns = [c.strip().lower() for c in df.columns]
    return df


def init_database(db_path: Optional[str] = None) -> sqlite3.Connection:
    """Initialize local SQLite database, stage raw tables, and execute SQL analytical views."""
    root = get_project_root()
    proc_dir = os.path.join(root, "data", "processed")
    os.makedirs(proc_dir, exist_ok=True)
    db_path = db_path or os.path.join(proc_dir, "growth_analytics.db")
    
    conn = sqlite3.connect(db_path)
    
    # Load raw data
    df_ads = load_raw_ad_campaigns()
    df_uci = load_raw_consumer_behavior()
    
    # Run 01_staging.sql
    sql_dir = os.path.join(root, "sql")
    with open(os.path.join(sql_dir, "01_staging.sql"), "r", encoding="utf-8") as f:
        staging_sql = f.read()
    conn.executescript(staging_sql)
    
    # Ingest data into staging tables
    df_ads.to_sql("stg_ad_campaigns", conn, if_exists="append", index=False)
    df_uci.to_sql("stg_consumer_behavior", conn, if_exists="append", index=False)
    
    # Run subsequent SQL view and metric definitions
    sql_scripts = [
        "02_clean.sql",
        "03_metrics.sql",
        "04_audience.sql",
        "05_mix_analysis.sql",
        "06_funnel.sql",
        "07_quality.sql"
    ]
    for script_name in sql_scripts:
        script_path = os.path.join(sql_dir, script_name)
        with open(script_path, "r", encoding="utf-8") as f:
            sql_text = f.read()
        conn.executescript(sql_text)
        
    return conn
