"""
src/experiment_engine.py
------------------------
Growth Experimentation Backlog & Prioritization Engine.
Translates real empirical findings into structured, disciplined experiment proposals.
Uses ICE (Impact, Confidence/Evidence, Ease) growth scoring.
"""

from typing import Dict, List, Any
import pandas as pd


def generate_experiment_proposals() -> List[Dict[str, Any]]:
    """
    Generate structured, production-grade growth experiment proposals directly derived from
    empirical anomalies in the dataset.
    
    IMPORTANT: These are structured growth proposals based on real data;
    they are NOT claimed to have been executed in production.
    """
    proposals = [
        {
            "experiment_id": "EXP-GROWTH-001",
            "title": "Ad Creative Value Prop Realignment for Scaled Campaigns",
            "observed_evidence": (
                "Campaign 1178 scaled budget to $55,662 and achieved lower CPM ($0.27 vs $0.36), "
                "but post-click approved conversion collapsed by 73.8% (from 9.22% in Camp 936 to 2.42% in Camp 1178), "
                "causing cost per approved conversion to inflate from $15.81 to $63.83."
            ),
            "hypothesis": (
                "Broad-reach ad creatives in Campaign 1178 set generic or misaligned user expectations that fail to convert "
                "on the post-click enquiry form. Replacing generic reach hooks with high-intent SMB pain-point hooks "
                "(e.g., 'Track daily udhaar payments instantly') will filter low-intent clicks and improve post-click conversion."
            ),
            "target_audience": "Scaled acquisition audience (broad demographic, ages 30-49, top interest categories).",
            "test_variable": "Ad Creative Hook & Headline Messaging",
            "control": "Generic broad benefit creative: 'Grow your business with smart digital tools'",
            "variant": "High-intent operational pain-point creative: 'Stop losing money to forgotten credits: 1-click ledger tracking'",
            "primary_kpi": "Click-to-Approved Conversion Rate (%)",
            "secondary_kpi": "Cost per Approved Conversion ($)",
            "guardrail": "CTR must not drop below 0.012% (protect traffic volume)",
            "success_criteria": ">= +25% relative lift in click-to-approved conversion rate with p < 0.05 and no CAC degradation",
            "expected_learning": "Determines whether qualification-focused copy improves downstream unit economics at scale.",
            "data_requirement": "Impression, click, enquiry, and approved conversion tracking at creative level.",
            "impact_score": 9,      # 1-10
            "evidence_score": 9,    # 1-10 (4x cost difference proven by decomposition bridge)
            "ease_score": 8,        # 1-10 (Creative swap is fast on social platforms)
            "ice_score": 8.67,
            "priority": "P0 (Immediate Sprint)",
            "priority_reason": "Directly attacks the largest source of cost leakage ($48.02 cost-per-approved surge)."
        },
        {
            "experiment_id": "EXP-GROWTH-002",
            "title": "Post-Click Landing Form Friction Reduction & Micro-Commitment",
            "observed_evidence": (
                "Funnel drop-off analysis reveals that 92.6% of users who click Campaign 1178 ads drop off before completing "
                "the initial enquiry form (Click-to-Enquiry is only 7.40% vs 27.07% in Campaign 936)."
            ),
            "hypothesis": (
                "The current post-click enquiry form requires too many fields upfront. Replacing the single multi-field form "
                "with a 2-step micro-commitment form (Step 1: Business category selection, Step 2: Contact info) "
                "will reduce cognitive friction and increase completion rates."
            ),
            "target_audience": "All post-click web traffic from paid campaigns.",
            "test_variable": "Landing Page Form Architecture",
            "control": "Single-page static form with 5 mandatory fields (Name, Phone, City, Business Type, Revenue).",
            "variant": "Progressive 2-step form: Step 1 (1-tap business type chip), Step 2 (Phone number OTP autofill).",
            "primary_kpi": "Click-to-Total Conversion (Enquiry) Rate (%)",
            "secondary_kpi": "Form Initiation Rate (%)",
            "guardrail": "Total-to-Approved qualification rate must remain >= 30% (protect lead quality).",
            "success_criteria": ">= +20% lift in total conversion rate with p < 0.05 and no drop in approval rate.",
            "expected_learning": "Identifies whether top-of-funnel conversion leakage is caused by UX form fatigue.",
            "data_requirement": "Session-level form field analytics, step completion timestamps, and approval backend sync.",
            "impact_score": 9,
            "evidence_score": 8,
            "ease_score": 7,
            "ice_score": 8.00,
            "priority": "P0 (Immediate Sprint)",
            "priority_reason": "High leverage on 36,000+ clicks where 92.6% currently bounce without converting."
        },
        {
            "experiment_id": "EXP-GROWTH-003",
            "title": "Audience Concentration & Budget Reallocation to Stable Interest Segments",
            "observed_evidence": (
                "Segment stability analysis showed that 12 of the 28 interest groups evaluated have < 10 clicks, "
                "exhibiting extreme variance in cost per approved conversion, while top interests (e.g. ID 16, 27) "
                "demonstrate consistent sub-$25 cost per approved conversion across 50+ click thresholds."
            ),
            "hypothesis": (
                "Reallocating 30% of media budget away from unstable, fragmented interest segments into the top 5 "
                "sample-stable segments will improve overall blended campaign efficiency by eliminating long-tail spend waste."
            ),
            "target_audience": "Campaign budget allocation across interest categories.",
            "test_variable": "Audience Targeting Concentration",
            "control": "Fragmented broad targeting across all 30+ interest codes.",
            "variant": "Concentrated tier-1 targeting strictly limited to stable interest clusters with >50 clicks history.",
            "primary_kpi": "Blended Cost per Approved Conversion ($)",
            "secondary_kpi": "Total Approved Conversions per Week",
            "guardrail": "Weekly impression delivery volume must not decline by more than 15%.",
            "success_criteria": ">= 15% reduction in blended cost per approved conversion without frequency spike.",
            "expected_learning": "Tests the tradeoff between demographic scale and segment conversion efficiency.",
            "data_requirement": "Campaign budget split, weekly ad spend, and segment-level approved conversions.",
            "impact_score": 8,
            "evidence_score": 9,
            "ease_score": 9,
            "ice_score": 8.67,
            "priority": "P0 (Immediate Sprint)",
            "priority_reason": "Zero engineering required; actionable immediately within ad campaign budget settings."
        },
        {
            "experiment_id": "EXP-GROWTH-004",
            "title": "Returning Visitor Personalized High-Intent Nudge (Consumer Behavior)",
            "observed_evidence": (
                "UCI consumer behavior diagnostics show that Returning Visitors have a 3.5x higher purchase rate (16.9% vs 4.8%) "
                "and average page value of $7.82 vs $1.15 for New Visitors, but exhibit high exit rates (0.045) on cart pages."
            ),
            "hypothesis": (
                "Displaying a personalized re-engagement banner ('Continue where you left off + free merchant QR setup') "
                "to returning visitors within 5 seconds of session start will increase transaction completion."
            ),
            "target_audience": "Returning visitors on web/mobile sessions.",
            "test_variable": "On-site Returning Visitor Modal / Top-Banner",
            "control": "Standard landing view with generic homepage promotions.",
            "variant": "Personalized sticky top-bar showing last viewed feature with 1-click resume CTA.",
            "primary_kpi": "Session-to-Purchase Conversion Rate (%)",
            "secondary_kpi": "Add-to-Cart / Feature Usage Initiation Rate (%)",
            "guardrail": "Session bounce rate must not increase by > 2% absolute.",
            "success_criteria": ">= +12% relative lift in transaction rate among returning cohort with p < 0.05.",
            "expected_learning": "Quantifies the conversion lift of context-aware personalization for high-intent users.",
            "data_requirement": "Cookie/session identity persistence, on-site event stream, transaction confirmation webhook.",
            "impact_score": 7,
            "evidence_score": 8,
            "ease_score": 6,
            "ice_score": 7.00,
            "priority": "P1 (Next Sprint)",
            "priority_reason": "Capitalizes on high baseline intent with proven behavioral divergence."
        },
        {
            "experiment_id": "EXP-GROWTH-005",
            "title": "Demographic Gender-Specific Creative Framing Test",
            "observed_evidence": (
                "Audience analysis reveals Female segments generate higher CTR (0.024% vs 0.016%) but incur a higher cost per "
                "approved conversion ($68.20 vs $42.10 for Males) due to post-click enquiry friction."
            ),
            "hypothesis": (
                "Current creative hooks appeal to female SMB owners' visual interest but downstream product copy is tailored "
                "predominantly to male-dominated wholesale trade. Creating retail/apparel-specific merchant landing copy for female "
                "audiences will bridge the post-click intent gap."
            ),
            "target_audience": "Female business owners aged 30-49.",
            "test_variable": "Landing Page Merchant Vertical Imagery & Testimonials",
            "control": "General wholesale distribution merchant testimonials and imagery.",
            "variant": "Retail, boutique, and local apparel merchant testimonials and workflow screenshots.",
            "primary_kpi": "Post-Click Approved Conversion Rate (%)",
            "secondary_kpi": "Cost per Approved Conversion ($)",
            "guardrail": "CPC must not increase by > 10%.",
            "success_criteria": ">= 20% reduction in Cost per Approved Conversion for Female cohort.",
            "expected_learning": "Reveals whether demographic conversion gaps are structural or artifacts of vertical misrepresentation.",
            "data_requirement": "Gender-segmented ad sets, separate landing page URLs, conversion tracking.",
            "impact_score": 7,
            "evidence_score": 7,
            "ease_score": 7,
            "ice_score": 7.00,
            "priority": "P1 (Next Sprint)",
            "priority_reason": "High initial click engagement indicates strong top-of-funnel resonance that is currently squandered."
        }
    ]
    return proposals


def get_experiment_backlog_df() -> pd.DataFrame:
    """Return the experiment backlog as a clean, formatted DataFrame."""
    proposals = generate_experiment_proposals()
    return pd.DataFrame(proposals)
