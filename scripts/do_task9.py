import os
import json

def do_task9():
    path = "scripts/export_web_data.py"
    with open(path, "r") as f:
        content = f.read()

    # Modify export_web_data.py so it preserves the new keys and writes to both locations
    replace_str = """
    # Merge existing data to preserve market_intelligence, growth_os, metric_dictionary
    data_path = os.path.join(root_dir, "data", "dashboard_data.json")
    if os.path.exists(data_path):
        with open(data_path, "r") as f:
            existing = json.load(f)
            if "market_intelligence" in existing: web_data["market_intelligence"] = existing["market_intelligence"]
            if "growth_os" in existing: web_data["growth_os"] = existing["growth_os"]
            if "metric_dictionary" in existing: web_data["metric_dictionary"] = existing["metric_dictionary"]

    web_data_dir = os.path.join(root_dir, "web", "data")
    os.makedirs(web_data_dir, exist_ok=True)
    out_path_web = os.path.join(web_data_dir, "dashboard_data.json")
    
    data_dir = os.path.join(root_dir, "data")
    os.makedirs(data_dir, exist_ok=True)
    out_path_data = os.path.join(data_dir, "dashboard_data.json")
    
    with open(out_path_web, "w") as f:
        json.dump(web_data, f, indent=4)
        
    with open(out_path_data, "w") as f:
        json.dump(web_data, f, indent=4)
        
    print(f"[+] Successfully exported data to {out_path_web} and {out_path_data}")
"""
    # Replace from web_data_dir down to print statement
    idx1 = content.find('web_data_dir = os.path.join(root_dir, "web", "data")')
    if idx1 != -1:
        idx2 = content.find('print(f"[+] Successfully exported data', idx1)
        if idx2 != -1:
            idx2 = content.find('\n', idx2)
            content = content[:idx1] + replace_str + content[idx2:]
    
    with open(path, "w") as f:
        f.write(content)

if __name__ == "__main__":
    do_task9()
