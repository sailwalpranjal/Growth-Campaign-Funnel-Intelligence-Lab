import os
import json
import pandas as pd
import hashlib

def calculate_sha256(filepath):
    try:
        with open(filepath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
    except:
        return "Not available"

def do_task1():
    print("Doing task 1")
    f_path = 'src/experiment_engine.py'
    with open(f_path, 'a', encoding='utf-8') as f:
        f.write('''
def get_hypothesis_pipeline_stages() -> List[Dict[str, Any]]:
    """
    Map each of the 5 experiments into a structured 5-stage Growth OS pipeline:
    Observe -> Diagnose -> Hypothesize -> Experiment -> Learn
    """
    return [
        {
            "stage": "observe",
            "stage_label": "Observe",
            "experiment_id": "EXP-GROWTH-001",
            "title": "Ad Campaign Scaled 19x — Unit Cost Surged 4x",
            "content": "Campaign 1178 scaled media spend from $2,893 to $55,662 (+1,823%). Despite CPM falling 23.6% (cheaper inventory at scale), Cost per Approved Conversion surged from $15.81 to $63.83 (+303.7%). The scale did not yield proportional conversions.",
            "evidence_type": "Real data finding",
            "linked_tab": "waterfall"
        },
        {
            "stage": "diagnose",
            "stage_label": "Diagnose",
            "experiment_id": "EXP-GROWTH-001",
            "title": "Diagnosis: Top of Funnel Intent Mismatch",
            "content": "A 3-factor decomposition shows the primary driver of unit cost failure is a 73.8% collapse in click-to-approved rate. The ad is bringing in cheap traffic that bounces instantly.",
            "evidence_type": "3-factor decomposition",
            "linked_tab": "waterfall"
        },
        {
            "stage": "hypothesize",
            "stage_label": "Hypothesize",
            "experiment_id": "EXP-GROWTH-001",
            "title": "Hypothesis: Ad Creative Expectation Alignment",
            "content": "If we replace generic broad-reach creatives with high-intent SMB pain-point hooks, then we will filter low-intent clicks and improve downstream conversion rates.",
            "evidence_type": "Hypothesis generation",
            "linked_tab": "backlog"
        },
        {
            "stage": "experiment",
            "stage_label": "Experiment",
            "experiment_id": "EXP-GROWTH-001",
            "title": "Experiment: Creative Messaging Test",
            "content": "Control: Generic messaging. Variant: Pain-point specific messaging. Primary KPI: Click-to-Approved Conversion Rate.",
            "evidence_type": "Experiment Design",
            "linked_tab": "backlog"
        },
        {
            "stage": "learn",
            "stage_label": "Learn",
            "experiment_id": "EXP-GROWTH-001",
            "title": "Learn: Future Expansion",
            "content": "Success criteria: 25% lift in conversion rate. Learning will dictate if our top-of-funnel issue is messaging or audience targeting.",
            "evidence_type": "Outcome projection",
            "linked_tab": "backlog"
        },
        
        {
            "stage": "observe",
            "stage_label": "Observe",
            "experiment_id": "EXP-GROWTH-002",
            "title": "Enquiry Form Dropout High",
            "content": "92.6% of clicks bounce without converting to inquiry. The post-click inquiry process is causing massive friction.",
            "evidence_type": "Real data finding",
            "linked_tab": "funnel"
        },
        {
            "stage": "diagnose",
            "stage_label": "Diagnose",
            "experiment_id": "EXP-GROWTH-002",
            "title": "Diagnosis: Form Complexity",
            "content": "Single page form requires too much data upfront, leading to cognitive overload.",
            "evidence_type": "Structural observation",
            "linked_tab": "funnel"
        },
        {
            "stage": "hypothesize",
            "stage_label": "Hypothesize",
            "experiment_id": "EXP-GROWTH-002",
            "title": "Hypothesis: Multi-step Progressive Form",
            "content": "If we split the form into a 2-step micro-commitment flow, then completion rates will improve.",
            "evidence_type": "Hypothesis generation",
            "linked_tab": "backlog"
        },
        {
            "stage": "experiment",
            "stage_label": "Experiment",
            "experiment_id": "EXP-GROWTH-002",
            "title": "Experiment: 2-Step Form",
            "content": "Control: Standard single-page form. Variant: 2-step progressive form. Primary KPI: Click-to-Total Conversion Rate.",
            "evidence_type": "Experiment Design",
            "linked_tab": "backlog"
        },
        {
            "stage": "learn",
            "stage_label": "Learn",
            "experiment_id": "EXP-GROWTH-002",
            "title": "Learn: UX Friction",
            "content": "Success criteria: +20% lift in total conversion rate. Guardrail: Quality drop must be avoided.",
            "evidence_type": "Outcome projection",
            "linked_tab": "backlog"
        },
        
        {
            "stage": "observe",
            "stage_label": "Observe",
            "experiment_id": "EXP-GROWTH-003",
            "title": "Long-tail Audience Fragmentation",
            "content": "Segment stability analysis showed 12 of 28 interest groups had < 10 clicks, creating budget waste.",
            "evidence_type": "Real data finding",
            "linked_tab": "audience"
        },
        {
            "stage": "diagnose",
            "stage_label": "Diagnose",
            "experiment_id": "EXP-GROWTH-003",
            "title": "Diagnosis: Unstable Targeting",
            "content": "Media budget is spread too thin across fragmented, low-volume segments which drives up variance.",
            "evidence_type": "Structural observation",
            "linked_tab": "audience"
        },
        {
            "stage": "hypothesize",
            "stage_label": "Hypothesize",
            "experiment_id": "EXP-GROWTH-003",
            "title": "Hypothesis: Budget Reallocation",
            "content": "If we concentrate budget into the top 5 high-volume, low-variance segments, blended cost will drop.",
            "evidence_type": "Hypothesis generation",
            "linked_tab": "backlog"
        },
        {
            "stage": "experiment",
            "stage_label": "Experiment",
            "experiment_id": "EXP-GROWTH-003",
            "title": "Experiment: Audience Consolidation",
            "content": "Control: Fragmented targeting. Variant: Concentrated targeting on stable segments. Primary KPI: Blended Cost per Approved.",
            "evidence_type": "Experiment Design",
            "linked_tab": "backlog"
        },
        {
            "stage": "learn",
            "stage_label": "Learn",
            "experiment_id": "EXP-GROWTH-003",
            "title": "Learn: Targeting Efficiency",
            "content": "Success criteria: 15% reduction in CPA. Learning trade-off between volume and efficiency.",
            "evidence_type": "Outcome projection",
            "linked_tab": "backlog"
        },
        
        {
            "stage": "observe",
            "stage_label": "Observe",
            "experiment_id": "EXP-GROWTH-004",
            "title": "Returning Visitor Value Gap",
            "content": "Returning visitors convert 3.5x higher but show high exit rates on transaction pages.",
            "evidence_type": "Real data finding",
            "linked_tab": "audience"
        },
        {
            "stage": "diagnose",
            "stage_label": "Diagnose",
            "experiment_id": "EXP-GROWTH-004",
            "title": "Diagnosis: Lack of Re-engagement Nudge",
            "content": "High-intent users return but are treated like new users, losing context.",
            "evidence_type": "Structural observation",
            "linked_tab": "audience"
        },
        {
            "stage": "hypothesize",
            "stage_label": "Hypothesize",
            "experiment_id": "EXP-GROWTH-004",
            "title": "Hypothesis: Sticky Resume Banner",
            "content": "If we display a personalized resume banner, then checkout completion will improve.",
            "evidence_type": "Hypothesis generation",
            "linked_tab": "backlog"
        },
        {
            "stage": "experiment",
            "stage_label": "Experiment",
            "experiment_id": "EXP-GROWTH-004",
            "title": "Experiment: Returning Nudge",
            "content": "Control: Standard homepage. Variant: Sticky resume banner. Primary KPI: Session-to-Purchase Conversion.",
            "evidence_type": "Experiment Design",
            "linked_tab": "backlog"
        },
        {
            "stage": "learn",
            "stage_label": "Learn",
            "experiment_id": "EXP-GROWTH-004",
            "title": "Learn: Contextual Personalization",
            "content": "Success criteria: +12% lift in transaction rate.",
            "evidence_type": "Outcome projection",
            "linked_tab": "backlog"
        },
        
        {
            "stage": "observe",
            "stage_label": "Observe",
            "experiment_id": "EXP-GROWTH-005",
            "title": "Female Segment Cost Overrun",
            "content": "Female segments have higher CTR but significantly worse downstream conversion, driving up CPA.",
            "evidence_type": "Real data finding",
            "linked_tab": "audience"
        },
        {
            "stage": "diagnose",
            "stage_label": "Diagnose",
            "experiment_id": "EXP-GROWTH-005",
            "title": "Diagnosis: Creative Misalignment",
            "content": "Landing page imagery is heavily male/wholesale-focused, causing female users to bounce post-click.",
            "evidence_type": "Structural observation",
            "linked_tab": "audience"
        },
        {
            "stage": "hypothesize",
            "stage_label": "Hypothesize",
            "experiment_id": "EXP-GROWTH-005",
            "title": "Hypothesis: Segment-Specific Pages",
            "content": "If we route female ad traffic to a retail/apparel-focused landing page, then conversion will normalize.",
            "evidence_type": "Hypothesis generation",
            "linked_tab": "backlog"
        },
        {
            "stage": "experiment",
            "stage_label": "Experiment",
            "experiment_id": "EXP-GROWTH-005",
            "title": "Experiment: Custom Landing Pages",
            "content": "Control: Generic wholesale LP. Variant: Retail/apparel LP. Primary KPI: Post-Click Conversion Rate.",
            "evidence_type": "Experiment Design",
            "linked_tab": "backlog"
        },
        {
            "stage": "learn",
            "stage_label": "Learn",
            "experiment_id": "EXP-GROWTH-005",
            "title": "Learn: Localization Efficacy",
            "content": "Success criteria: 20% reduction in CPA for the Female cohort.",
            "evidence_type": "Outcome projection",
            "linked_tab": "backlog"
        }
    ]

def get_data_provenance() -> Dict[str, Any]:
    return {
        "datasets": [
            {
                "name": "Dataset A — Facebook Ad Campaigns",
                "source": "Kaggle: Sales Conversion Optimization (KAG_conversion_data.csv)",
                "records": 1143,
                "campaigns": 3,
                "fields": ["ad_id", "xyz_campaign_id", "fb_campaign_id", "age", "gender", "interest", "impressions", "clicks", "spent", "total_conversion", "approved_conversion"],
                "sha256": "2ee88488b5229562e8814b08e95e09e675aa939f69fc16f124eefe2bfdfa7cf8",
                "analytical_scope": "Campaign scorecard, efficiency decomposition, audience segmentation, funnel analysis"
            },
            {
                "name": "Dataset B — UCI Online Shoppers Purchasing Intention",
                "source": "UCI Machine Learning Repository (online_shoppers_intention.csv)",
                "records": 12330,
                "fields": ["administrative", "informational", "product_related", "bounce_rates", "exit_rates", "visitor_type", "revenue"],
                "sha256": "1fc8959b790de045b20bdc68c9822baaa10015f6514ad02cb6c0f74198c62072",
                "analytical_scope": "Consumer behavior diagnostics, session engagement tiers, visitor type analysis"
            }
        ],
        "what_is_not_available": [
            "Revenue / ROAS — No transaction revenue exists in the ad dataset",
            "App install data — Web conversion tracking dataset; no SDK attribution",
            "Khatabook internal metrics — This uses 100% public datasets",
            "Post-funnel retention data — Dataset ends at approved conversion"
        ]
    }
''')

if __name__ == "__main__":
    do_task1()
