"""
backend/main.py
---------------
Lightweight FastAPI service for Growth Campaign & Funnel Intelligence Lab.
Designed for 1-click free deployment on Render.com.
Provides REST endpoints for live statistical A/B testing, campaign scorecards, and decomposition.
"""

import os
import sys
from typing import Dict, Any, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Ensure project root is in sys.path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from src.data_loader import load_raw_ad_campaigns
from src.metrics import aggregate_campaign_scorecard
from src.diagnostics import decompose_efficiency_bridge
from src.statistics import two_proportion_z_test, calculate_sample_size_required
from src.experiment_engine import generate_experiment_proposals

app = FastAPI(
    title="Growth Campaign & Funnel Intelligence API",
    description="Backend service for Khatabook Growth Track analytics and live experimentation engine.",
    version="1.0.0"
)

# Enable CORS for Vercel frontend and local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ABTestRequest(BaseModel):
    control_conversions: int = Field(..., ge=0, description="Conversions in control group")
    control_sample: int = Field(..., gt=0, description="Total sample in control group")
    treatment_conversions: int = Field(..., ge=0, description="Conversions in treatment group")
    treatment_sample: int = Field(..., gt=0, description="Total sample in treatment group")
    alpha: float = Field(0.05, gt=0, lt=1, description="Significance level (default 0.05)")
    mde_threshold: float = Field(0.05, gt=0, description="Minimum detectable effect threshold for practical relevance")


class SampleSizeRequest(BaseModel):
    baseline_conversion_rate: float = Field(..., gt=0, lt=1, description="Baseline conversion rate, e.g. 0.024")
    minimum_detectable_effect: float = Field(..., gt=0, description="Target relative lift to detect, e.g. 0.20 for +20%")
    alpha: float = Field(0.05, gt=0, lt=1)
    power: float = Field(0.80, gt=0, lt=1)


@app.get("/")
def root() -> Dict[str, Any]:
    """Root landing endpoint with system status, metadata, and service discovery."""
    return {
        "service": "Khatabook Growth Intelligence Platform API",
        "status": "online",
        "version": "1.0.0",
        "author": "Pranjal Sailwal",
        "repository": "https://github.com/sailwalpranjal/Growth-Campaign-Funnel-Intelligence-Lab",
        "interactive_docs": "/docs",
        "openapi_schema": "/openapi.json",
        "health_check": "/health",
        "endpoints": {
            "campaign_scorecard": "/api/scorecard",
            "efficiency_decomposition": "/api/decomposition?base=936&target=1178",
            "experiment_backlog": "/api/experiments",
            "ab_test_calculator": "POST /api/ab-test",
            "sample_size_planner": "POST /api/sample-size"
        }
    }


@app.get("/health")
def health_check() -> Dict[str, str]:
    """Health check endpoint for Render monitoring."""
    return {
        "status": "healthy",
        "service": "Growth Intelligence Lab API",
        "version": "1.0.0"
    }


@app.get("/api/scorecard")
def get_campaign_scorecard() -> Dict[str, Any]:
    """Return campaign scorecard aggregated via ratio-of-sums."""
    try:
        df_ads = load_raw_ad_campaigns()
        scorecard = aggregate_campaign_scorecard(df_ads)
        return {
            "status": "success",
            "campaigns": scorecard.to_dict(orient="records")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/decomposition")
def get_efficiency_decomposition(base: int = 936, target: int = 1178) -> Dict[str, Any]:
    """Return 3-factor efficiency decomposition bridge between two campaigns."""
    try:
        df_ads = load_raw_ad_campaigns()
        scorecard = aggregate_campaign_scorecard(df_ads)
        bridge = decompose_efficiency_bridge(scorecard, base_campaign_id=base, target_campaign_id=target)
        return {
            "status": "success",
            "bridge": bridge
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/ab-test")
def run_ab_test(payload: ABTestRequest) -> Dict[str, Any]:
    """Run two-proportion hypothesis test with p-value, z-score, 95% CI, and growth decision."""
    try:
        results = two_proportion_z_test(
            control_conversions=payload.control_conversions,
            control_sample=payload.control_sample,
            treatment_conversions=payload.treatment_conversions,
            treatment_sample=payload.treatment_sample,
            alpha=payload.alpha,
            mde_threshold=payload.mde_threshold
        )
        return {
            "status": "success",
            "results": results
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/sample-size")
def calculate_sample_size(payload: SampleSizeRequest) -> Dict[str, Any]:
    """Calculate sample size required per variant for next experiment."""
    try:
        required_sample = calculate_sample_size_required(
            baseline_conversion_rate=payload.baseline_conversion_rate,
            minimum_detectable_effect=payload.minimum_detectable_effect,
            alpha=payload.alpha,
            power=payload.power
        )
        return {
            "status": "success",
            "sample_required_per_variant": required_sample,
            "total_sample_both_variants": required_sample * 2
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/api/experiments")
def get_experiments() -> Dict[str, Any]:
    """Return prioritized growth experiment backlog with ICE scores."""
    try:
        proposals = generate_experiment_proposals()
        return {
            "status": "success",
            "count": len(proposals),
            "experiments": proposals
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("backend.main:app", host="0.0.0.0", port=port, reload=True)
