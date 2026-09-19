import pytest
from src.experiment_engine import generate_experiment_proposals, get_experiment_backlog_df

def test_experiment_count():
    proposals = generate_experiment_proposals()
    assert len(proposals) == 5

def test_required_experiment_fields():
    proposals = generate_experiment_proposals()
    required = ["experiment_id", "title", "hypothesis", "primary_kpi", "ice_score", "impact_score", "evidence_score", "ease_score", "priority"]
    for p in proposals:
        for field in required:
            assert field in p, f"Missing field '{field}' in {p.get('experiment_id', 'unknown')}"

def test_ice_score_range():
    proposals = generate_experiment_proposals()
    for p in proposals:
        assert 0 < p["ice_score"] <= 10, f"ICE score {p['ice_score']} out of valid range"
        assert 0 < p["impact_score"] <= 10
        assert 0 < p["evidence_score"] <= 10
        assert 0 < p["ease_score"] <= 10

def test_p0_experiments_exist():
    proposals = generate_experiment_proposals()
    p0_count = sum(1 for p in proposals if "P0" in p["priority"])
    assert p0_count >= 2, "Should have at least 2 P0 priority experiments"

def test_ice_score_consistency():
    proposals = generate_experiment_proposals()
    for p in proposals:
        expected = round((p["impact_score"] + p["evidence_score"] + p["ease_score"]) / 3, 2)
        assert abs(p["ice_score"] - expected) < 0.1, f"ICE score inconsistency in {p['experiment_id']}"

def test_backlog_df_shape():
    df = get_experiment_backlog_df()
    assert len(df) == 5
    assert "experiment_id" in df.columns
    assert "ice_score" in df.columns
