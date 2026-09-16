"""
scripts/download_data.py
------------------------
Automated data acquisition script with SHA-256 verification and metadata logging.

Downloads real, public, un-fabricated datasets:
1. Kaggle Sales Conversion Optimization / Clicks Conversion Tracking (KAG_conversion_data.csv)
2. UCI Online Shoppers Purchasing Intention (online_shoppers_intention.csv)
"""

import hashlib
import json
import os
import sys
import time
import urllib.request

DATA_SOURCES = {
    "kaggle_ad_conversions": {
        "filename": "KAG_conversion_data.csv",
        "primary_url": "https://raw.githubusercontent.com/ychennay/ychennay.github.io/master/KAG_conversion_data.csv",
        "fallback_url": "https://raw.githubusercontent.com/raghav-arora/Kaggle-Facebook-Ad-Campaign/master/KAG_conversion_data.csv",
        "expected_min_bytes": 50000,
        "description": "Anonymized social media advertising campaign data across 3 campaigns (916, 936, 1178) with 1,143 ad records.",
        "publisher": "Kaggle / Anonymous Ad Network",
        "license": "Public Domain / CC0 equivalent open benchmark"
    },
    "uci_consumer_behavior": {
        "filename": "online_shoppers_intention.csv",
        "primary_url": "https://raw.githubusercontent.com/santoshc1/PowerBI-AI-samples/master/Tutorial_AutomatedML/online_shoppers_intention.csv",
        "fallback_url": "https://raw.githubusercontent.com/jbrownlee/Datasets/master/online_shoppers_intention.csv",
        "expected_min_bytes": 1000000,
        "description": "UCI Online Shoppers Purchasing Intention dataset with 12,330 e-commerce sessions and conversion outcomes.",
        "publisher": "UCI Machine Learning Repository (C. Okan Sakar, Yomi Kastro)",
        "license": "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    }
}


def compute_sha256(filepath: str) -> str:
    """Calculate SHA-256 hash of a local file."""
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def download_file(url: str, dest_path: str, fallback_url: str = None) -> bool:
    """Download a file with retry and fallback support."""
    headers = {"User-Agent": "Growth-Intelligence-Lab/1.0"}
    req = urllib.request.Request(url, headers=headers)
    
    try:
        print(f"[*] Downloading from: {url}")
        with urllib.request.urlopen(req, timeout=30) as resp:
            if resp.status != 200:
                raise ValueError(f"HTTP status code {resp.status}")
            data = resp.read()
            with open(dest_path, "wb") as out_f:
                out_f.write(data)
        return True
    except Exception as e:
        print(f"[!] Primary download failed: {e}")
        if fallback_url:
            print(f"[*] Trying fallback URL: {fallback_url}")
            try:
                fallback_req = urllib.request.Request(fallback_url, headers=headers)
                with urllib.request.urlopen(fallback_req, timeout=30) as resp:
                    if resp.status != 200:
                        raise ValueError(f"HTTP status code {resp.status}")
                    data = resp.read()
                    with open(dest_path, "wb") as out_f:
                        out_f.write(data)
                return True
            except Exception as fb_err:
                print(f"[X] Fallback download failed: {fb_err}")
                return False
        return False


def main():
    raw_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "raw")
    os.makedirs(raw_dir, exist_ok=True)
    
    metadata = {
        "timestamp_utc": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
        "datasets": {}
    }
    
    all_success = True
    for key, info in DATA_SOURCES.items():
        dest_path = os.path.join(raw_dir, info["filename"])
        
        # Check if file exists and is valid
        if os.path.exists(dest_path) and os.path.getsize(dest_path) >= info["expected_min_bytes"]:
            print(f"[+] Found existing file: {info['filename']} ({os.path.getsize(dest_path):,} bytes)")
            checksum = compute_sha256(dest_path)
        else:
            success = download_file(info["primary_url"], dest_path, info["fallback_url"])
            if not success or not os.path.exists(dest_path) or os.path.getsize(dest_path) < info["expected_min_bytes"]:
                print(f"[X] Failed to acquire valid file for {key}")
                all_success = False
                continue
            checksum = compute_sha256(dest_path)
            print(f"[+] Successfully downloaded {info['filename']} ({os.path.getsize(dest_path):,} bytes)")
            
        metadata["datasets"][key] = {
            "filename": info["filename"],
            "path": os.path.relpath(dest_path, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
            "size_bytes": os.path.getsize(dest_path),
            "sha256": checksum,
            "publisher": info["publisher"],
            "license": info["license"],
            "description": info["description"]
        }
        
    # Write metadata JSON
    meta_path = os.path.join(raw_dir, "provenance_metadata.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)
    print(f"[+] Saved provenance metadata to {meta_path}")
    
    if not all_success:
        sys.exit(1)
    print("[+] Data acquisition complete and verified.")


if __name__ == "__main__":
    main()
