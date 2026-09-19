"""
tests/test_backend.py
---------------------
Unit and integration tests for FastAPI backend service endpoints.
"""

import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_root_endpoint():
    res = client.get("/")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "online"
    assert data["interactive_docs"] == "/docs"


def test_health_check_endpoint():
    res = client.get("/health")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "healthy"
    assert data["service"] == "Growth Intelligence Lab API"


def test_campaign_scorecard_endpoint():
    res = client.get("/api/scorecard")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "success"
    assert len(data["campaigns"]) == 3
    # Verify campaign 936
    c936 = [c for c in data["campaigns"] if c["campaign_id"] == 936][0]
    assert c936["approved_conversions"] == 183


def test_decomposition_endpoint():
    res = client.get("/api/decomposition?base=936&target=1178")
    assert res.status_code == 200
    data = res.json()
    bridge = data["bridge"]
    assert pytest.approx(bridge["cost_gap"], rel=1e-4) == 48.02
    assert bridge["reconciliation_error"] < 1e-6


def test_ab_test_endpoint():
    payload = {
        "control_conversions": 100,
        "control_sample": 1000,
        "treatment_conversions": 130,
        "treatment_sample": 1000,
        "alpha": 0.05
    }
    res = client.post("/api/ab-test", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "success"
    results = data["results"]
    assert results["decision"] == "Promote cautiously"
    assert results["is_statistically_significant"] is True


def test_sample_size_endpoint():
    payload = {
        "baseline_conversion_rate": 0.05,
        "minimum_detectable_effect": 0.20
    }
    res = client.post("/api/sample-size", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert 7000 <= data["sample_required_per_variant"] <= 8500


def test_experiments_endpoint():
    res = client.get("/api/experiments")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "success"
    assert data["count"] == 5
    assert len(data["experiments"]) == 5
    exp0 = data["experiments"][0]
    assert "experiment_id" in exp0
    assert "ice_score" in exp0
    assert "status" in exp0


def test_market_intelligence_endpoint():
    res = client.get("/api/market-intelligence")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "success"
    intel = data["market_intelligence"]
    assert "msme_landscape" in intel
    assert "competitors" in intel
    assert len(intel["competitors"]) >= 4


def test_hypothesis_pipeline_endpoint():
    res = client.get("/api/hypothesis-pipeline")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "success"
    assert data["count"] == 5
    assert len(data["pipeline"]) == 5


def test_metric_dictionary_endpoint():
    res = client.get("/api/metric-dictionary")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "success"
    assert data["count"] >= 10
    metrics = data["metrics"]
    names = [m["metric"] for m in metrics]
    assert any("CTR" in n for n in names)
    assert any("CAC" in n for n in names)

