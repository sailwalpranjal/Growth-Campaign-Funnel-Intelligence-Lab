"""
Recompute every headline number quoted in the README, the experiment backlog
and the dashboard straight from the raw CSVs, then check the published text
agrees. An earlier version of the backlog quoted figures that did not survive
recomputation (returning visitors "3.5x higher", gender CPA of $68.20 vs
$42.10, "12 of 28 interests under 10 clicks"). These tests exist so that
cannot happen again.
"""

import json
import os

import pandas as pd
import pytest

from src.data_loader import get_project_root, load_raw_ad_campaigns, load_raw_consumer_behavior
from src.diagnostics import analyze_consumer_behavior_diagnostics, decompose_efficiency_bridge
from src.metrics import aggregate_campaign_scorecard

ROOT = get_project_root()


def read(*parts: str) -> str:
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        return f.read()


@pytest.fixture(scope="module")
def ads() -> pd.DataFrame:
    return load_raw_ad_campaigns()


@pytest.fixture(scope="module")
def visitors() -> pd.DataFrame:
    return analyze_consumer_behavior_diagnostics(load_raw_consumer_behavior())["visitor_type"].set_index("visitor_type")


@pytest.fixture(scope="module")
def gender(ads) -> pd.DataFrame:
    g = ads.groupby("gender").agg(
        impressions=("impressions", "sum"),
        clicks=("clicks", "sum"),
        spent=("spent", "sum"),
        approved=("approved_conversion", "sum"),
    )
    g["ctr"] = g["clicks"] / g["impressions"]
    g["cpa"] = g["spent"] / g["approved"]
    return g


@pytest.fixture(scope="module")
def interests(ads) -> pd.DataFrame:
    return ads.groupby("interest").agg(
        clicks=("clicks", "sum"), approved=("approved_conversion", "sum"), spent=("spent", "sum")
    ).assign(cpa=lambda d: d["spent"] / d["approved"])


# ---- ad-level totals and the cost bridge -------------------------------------------------

def test_ad_totals(ads):
    assert len(ads) == 1143
    assert ads["clicks"].sum() == 38165
    assert ads["impressions"].sum() == 213_434_828
    assert round(ads["clicks"].sum() / ads["impressions"].sum() * 100, 4) == 0.0179
    assert round((ads["clicks"] / ads["impressions"]).mean() * 100, 4) == 0.0164


def test_campaign_cost_gap_and_bridge(ads):
    sc = aggregate_campaign_scorecard(ads)
    d = decompose_efficiency_bridge(sc, 936, 1178)
    assert round(d["base_metrics"]["cost_per_approved"], 2) == 15.81
    assert round(d["target_metrics"]["cost_per_approved"], 2) == 63.83
    assert round(d["cost_gap"], 2) == 48.02
    assert round(d["target_metrics"]["cost_per_approved"] / d["base_metrics"]["cost_per_approved"], 2) == 4.04
    assert (round(d["cpm_effect"], 2), round(d["ctr_effect"], 2), round(d["conv_effect"], 2)) == (-3.74, 4.66, 47.10)
    assert round(d["conv_effect"] / d["cost_gap"] * 100, 1) == 98.1


# ---- EXP-004: returning vs new visitors --------------------------------------------------

def test_visitor_conversion(visitors):
    new, ret = visitors.loc["New_Visitor"], visitors.loc["Returning_Visitor"]
    assert round(new["purchase_rate"] * 100, 1) == 24.9
    assert round(ret["purchase_rate"] * 100, 1) == 13.9
    assert new["purchase_rate"] > ret["purchase_rate"], "new visitors convert better, not returning"
    assert (int(new["transactions"]), int(new["total_sessions"])) == (422, 1694)
    assert (int(ret["transactions"]), int(ret["total_sessions"])) == (1470, 10551)
    assert (new["avg_page_value"], ret["avg_page_value"]) == (10.77, 5.01)
    assert round(ret["avg_exit_rate"], 4) == 0.0465


# ---- EXP-005: gender -----------------------------------------------------------------------

def test_gender_ctr_and_cpa(gender):
    assert round(gender.loc["F", "cpa"], 2) == 69.70
    assert round(gender.loc["M", "cpa"], 2) == 41.44
    assert round(gender.loc["F", "ctr"] * 100, 4) == 0.0208
    assert round(gender.loc["M", "ctr"] * 100, 4) == 0.0145


# ---- EXP-003: interests --------------------------------------------------------------------

def test_interest_facts(interests):
    assert len(interests) == 40
    assert interests["clicks"].min() == 128, "no interest has fewer than 10 clicks"
    assert int((interests["approved"] < 10).sum()) == 13
    enough = interests[interests["approved"] >= 50]
    assert len(enough) == 5
    assert enough["cpa"].idxmax() == 27
    assert round(enough["cpa"].max(), 2) == 95.85
    assert round(interests["cpa"].min(), 2) == 18.69
    assert round(interests["cpa"].max(), 2) == 107.97


# ---- the published text must match --------------------------------------------------------

STALE = [
    "28.4% vs 4.8%",
    "38,181",
    "3.5x higher",
    "16.9% vs 4.8%",
    "$68.20",
    "$42.10",
    "12 of 28",
    "12 of the 28",
    "$7.82",
    "0.024% vs 0.016%",
    "carries the worst CPA",
]

PUBLISHED = [
    "README.md",
    "docs/limitations.md",
    "exports/experiment_backlog.csv",
    "web/exports/experiment_backlog.csv",
    "reports/experiment_backlog.md",
    "reports/executive_summary.md",
    "data/dashboard_data.json",
    "web/data/dashboard_data.json",
    "web/docs/limitations.md",
]


@pytest.mark.parametrize("path", PUBLISHED)
def test_no_stale_claims_in_published_text(path):
    text = read(*path.split("/"))
    for phrase in STALE:
        assert phrase not in text, f"{path} still contains {phrase!r}"


def test_readme_quotes_recomputed_clicks():
    assert "38,165 clicks" in read("README.md")


def test_backlog_quotes_recomputed_numbers():
    backlog = read("exports", "experiment_backlog.csv")
    for expected in ["13.93%", "24.91%", "$69.70", "$41.44", "0.0208%", "0.0145%", "$95.85"]:
        assert expected in backlog, expected


def test_web_mirror_matches_exports():
    for name in ["experiment_backlog.csv", "campaign_scorecard.csv"]:
        assert read("exports", name) == read("web", "exports", name)


def test_dashboard_json_copies_agree():
    a = json.loads(read("data", "dashboard_data.json"))
    b = json.loads(read("web", "data", "dashboard_data.json"))
    assert a["growth_os"] == b["growth_os"]


# ---- the bridge depends on the order of substitution ---------------------------------------

def test_bridge_share_depends_on_substitution_order(ads):
    """The 98.1% post-click share is the order CPM, CTR, conversion. Other orders disagree."""
    import itertools
    import math

    def factors(cid):
        s = ads[ads["xyz_campaign_id"] == cid]
        return [
            s["spent"].sum() / s["impressions"].sum(),
            s["impressions"].sum() / s["clicks"].sum(),
            s["clicks"].sum() / s["approved_conversion"].sum(),
        ]

    a, b = factors(936), factors(1178)
    gap = math.prod(b) - math.prod(a)
    shares, shapley = [], [0.0, 0.0, 0.0]
    for order in itertools.permutations(range(3)):
        cur, step = a[:], [0.0] * 3
        for j in order:
            before = math.prod(cur)
            cur[j] = b[j]
            step[j] = math.prod(cur) - before
        assert abs(sum(step) - gap) < 1e-9
        shares.append(step[2] / gap)
        for j in range(3):
            shapley[j] += step[j] / 6
    assert round(min(shares) * 100, 1) == 70.8
    assert round(max(shares) * 100, 1) == 128.5
    assert [round(x, 2) for x in shapley] == [-11.08, 12.62, 46.48]
    assert round(shapley[2] / gap * 100, 1) == 96.8


def test_engagement_tier_conversion_quoted_in_limitations():
    tiers = analyze_consumer_behavior_diagnostics(load_raw_consumer_behavior())["engagement_tier"]
    rate = tiers.set_index("engagement_tier")["purchase_rate"]
    assert round(rate["High Engagement (>600s, Low Bounce)"] * 100, 1) == 22.7
    assert round(rate["Low Engagement / Skimmer (<120s)"] * 100, 1) == 3.9
    text = read("docs", "limitations.md")
    assert "22.7%" in text and "3.9%" in text
