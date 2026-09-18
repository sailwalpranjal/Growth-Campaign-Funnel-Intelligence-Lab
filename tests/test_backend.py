"""
tests/test_backend.py
---------------------
Unit and integration tests for FastAPI backend service endpoints.
"""

import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


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
