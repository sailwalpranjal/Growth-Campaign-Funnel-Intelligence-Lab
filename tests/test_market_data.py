import pytest
import json
import os

@pytest.fixture
def dashboard_data():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(root, "data", "dashboard_data.json")) as f:
        return json.load(f)

def test_market_intelligence_exists(dashboard_data):
    assert "market_intelligence" in dashboard_data

def test_competitors_count(dashboard_data):
    competitors = dashboard_data["market_intelligence"]["competitors"]
    assert len(competitors) == 5

def test_competitor_required_fields(dashboard_data):
    required = ["name", "core_identity", "merchant_segment", "key_differentiator", "app_store_rating"]
    for c in dashboard_data["market_intelligence"]["competitors"]:
        for field in required:
            assert field in c, f"Missing field '{field}' in competitor {c.get('name')}"

def test_growth_loops_count(dashboard_data):
    loops = dashboard_data["market_intelligence"]["khatabook_growth_loops"]
    assert len(loops) == 3

def test_growth_os_exists(dashboard_data):
    assert "growth_os" in dashboard_data
    assert len(dashboard_data["growth_os"]) == 5

def test_growth_os_stages(dashboard_data):
    required_stages = ["observe", "diagnose", "hypothesize", "experiment", "learn"]
    for item in dashboard_data["growth_os"]:
        for stage in required_stages:
            assert stage in item["stages"], f"Missing stage '{stage}' in {item.get('experiment_id')}"

def test_metric_dictionary_exists(dashboard_data):
    assert "metric_dictionary" in dashboard_data
    assert len(dashboard_data["metric_dictionary"]) >= 10

def test_metric_required_fields(dashboard_data):
    required = ["metric", "formula", "availability", "confidence", "khatabook_relevance"]
    for m in dashboard_data["metric_dictionary"]:
        for field in required:
            assert field in m, f"Missing '{field}' in metric {m.get('metric')}"
