import os

def do_task3():
    path = "backend/main.py"
    with open(path, "r") as f:
        content = f.read()
    
    # insert endpoints after /api/experiments
    endpoints_str = """
@app.get("/api/market-intelligence")
def get_market_intelligence() -> Dict[str, Any]:
    \"\"\"Return structured market intelligence: MSME landscape, competitor matrix, growth loops.\"\"\"
    try:
        import json, os
        data_path = os.path.join(root_dir, "data", "dashboard_data.json")
        with open(data_path) as f:
            data = json.load(f)
        return {"status": "success", "market_intelligence": data.get("market_intelligence", {})}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/hypothesis-pipeline")
def get_hypothesis_pipeline() -> Dict[str, Any]:
    \"\"\"Return Growth OS hypothesis pipeline — all 5 experiments across 5 stages.\"\"\"
    try:
        import json, os
        data_path = os.path.join(root_dir, "data", "dashboard_data.json")
        with open(data_path) as f:
            data = json.load(f)
        return {"status": "success", "count": len(data.get("growth_os", [])), "pipeline": data.get("growth_os", [])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/metric-dictionary")
def get_metric_dictionary() -> Dict[str, Any]:
    \"\"\"Return full metric dictionary with formulas, availability, and business rationale.\"\"\"
    try:
        import json, os
        data_path = os.path.join(root_dir, "data", "dashboard_data.json")
        with open(data_path) as f:
            data = json.load(f)
        return {"status": "success", "count": len(data.get("metric_dictionary", [])), "metrics": data.get("metric_dictionary", [])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
"""
    if "def get_market_intelligence" not in content:
        # find @app.get("/api/experiments")
        idx = content.find('@app.get("/api/experiments")')
        if idx != -1:
            end_idx = content.find('@app.get', idx + 1)
            if end_idx == -1:
                end_idx = len(content)
            content = content[:end_idx] + endpoints_str + content[end_idx:]

    # update root endpoint endpoints dict
    dict_update = """
        "/api/market-intelligence": "Market intelligence & competitor data",
        "/api/hypothesis-pipeline": "Growth OS hypothesis pipeline",
        "/api/metric-dictionary": "Metric definitions & business relevance",
"""
    if "/api/market-intelligence" not in content:
        dict_idx = content.find('"endpoints": {')
        if dict_idx != -1:
            insert_idx = content.find('}', dict_idx)
            if content[insert_idx - 1] != ',':
                # might need comma
                last_quote_idx = content.rfind('"', dict_idx, insert_idx)
                # just add a comma if there isn't one
                content = content[:insert_idx-1] + ",\n" + dict_update + content[insert_idx-1:]
            
    with open(path, "w", encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    do_task3()
