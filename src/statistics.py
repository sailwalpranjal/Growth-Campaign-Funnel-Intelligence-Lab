"""
src/statistics.py
-----------------
Growth Experimentation & A/B Testing Engine:
1. Two-proportion hypothesis testing (z-score, p-value, standard error)
2. 95% Confidence Intervals for absolute and relative lift
3. Sample size and Minimum Detectable Effect (MDE) planning
4. Strict growth decision framework preventing premature winner declaration
"""

import math
from typing import Dict, Optional, Union, Any
from scipy import stats


def two_proportion_z_test(control_conversions: int,
                          control_sample: int,
                          treatment_conversions: int,
                          treatment_sample: int,
                          alpha: float = 0.05,
                          mde_threshold: float = 0.05) -> Dict[str, Any]:
    """
    Perform two-proportion z-test comparing treatment vs control conversion rates.
    
    Returns comprehensive metrics distinguishing:
    - Observed Lift
    - Statistical Evidence (p-value, z-score)
    - Precision / Confidence Intervals
    - Actionable Growth Decision (Continue, Run longer, Investigate, Promote cautiously, Do not conclude)
    """
    if control_sample <= 0 or treatment_sample <= 0:
        raise ValueError("Sample sizes must be greater than zero.")
        
    p1 = control_conversions / control_sample
    p2 = treatment_conversions / treatment_sample
    
    abs_lift = p2 - p1
    rel_lift = (abs_lift / p1) if p1 > 0 else 0.0
    
    # Pooled proportion for hypothesis testing (Null: p1 == p2)
    p_pool = (control_conversions + treatment_conversions) / (control_sample + treatment_sample)
    se_pool = math.sqrt(p_pool * (1.0 - p_pool) * (1.0 / control_sample + 1.0 / treatment_sample)) if p_pool > 0 and p_pool < 1 else 0.0
    
    if se_pool > 0:
        z_score = abs_lift / se_pool
        p_value = 2.0 * (1.0 - stats.norm.cdf(abs(z_score)))
    else:
        z_score = 0.0
        p_value = 1.0
        
    # Unpooled standard error for 95% Confidence Interval
    se_diff = math.sqrt((p1 * (1.0 - p1) / control_sample) + (p2 * (1.0 - p2) / treatment_sample))
    z_crit = stats.norm.ppf(1.0 - alpha / 2.0)
    
    ci_lower = abs_lift - z_crit * se_diff
    ci_upper = abs_lift + z_crit * se_diff
    
    # Relative lift confidence interval (delta method approximation)
    if p1 > 0:
        rel_ci_lower = ci_lower / p1
        rel_ci_upper = ci_upper / p1
    else:
        rel_ci_lower = 0.0
        rel_ci_upper = 0.0
        
    is_significant = bool(p_value < alpha)
    is_positive_lift = bool(abs_lift > 0)
    is_practically_meaningful = bool(abs(rel_lift) >= mde_threshold)
    
    # Disciplined Growth Decision Matrix
    # We deliberately avoid naive 'Winner' declarations
    if not is_significant:
        if control_sample < 500 or treatment_sample < 500:
            decision = "Run longer (Underpowered / Sample < 500)"
            action_rationale = "Sample size is insufficient to detect moderate effect sizes. Continue test until target sample is met."
        else:
            decision = "Do not conclude (Null Result / Inconclusive)"
            action_rationale = "P-value exceeds threshold (p >= 0.05). No statistically discernible difference between variants."
    else:
        if is_positive_lift and is_practically_meaningful:
            if ci_lower > 0:
                decision = "Promote cautiously"
                action_rationale = "Statistically significant positive lift with 95% CI strictly above zero. Verify guardrail metrics before full rollout."
            else:
                decision = "Investigate (Wide Confidence Interval)"
                action_rationale = "Significant result, but lower bound borders zero. Evaluate segment consistency before scaling."
        elif is_positive_lift and not is_practically_meaningful:
            decision = "Do not conclude (Statistically Significant but Economically Negligible)"
            action_rationale = "Observed relative lift is below business relevance threshold (MDE < 5%). Engineering cost outweighs impact."
        else:
            decision = "Investigate (Statistically Significant Underperformance)"
            action_rationale = "Treatment performed significantly worse than control. Terminate variant to prevent further revenue/conversion drag."

    return {
        "control_sample": control_sample,
        "control_conversions": control_conversions,
        "control_rate": round(p1, 6),
        "treatment_sample": treatment_sample,
        "treatment_conversions": treatment_conversions,
        "treatment_rate": round(p2, 6),
        "absolute_lift": round(abs_lift, 6),
        "relative_lift": round(rel_lift, 4),
        "z_score": round(z_score, 4),
        "p_value": round(p_value, 5),
        "is_statistically_significant": is_significant,
        "ci_95_absolute": [round(ci_lower, 6), round(ci_upper, 6)],
        "ci_95_relative": [round(rel_ci_lower, 4), round(rel_ci_upper, 4)],
        "decision": decision,
        "action_rationale": action_rationale
    }


def calculate_sample_size_required(baseline_conversion_rate: float,
                                   minimum_detectable_effect: float,
                                   alpha: float = 0.05,
                                   power: float = 0.80) -> int:
    """
    Calculate sample size required per variant for two-tailed two-proportion test.
    
    baseline_conversion_rate: Baseline rate (e.g. 0.05 for 5%)
    minimum_detectable_effect: Relative lift to detect (e.g. 0.20 for +20% lift)
    """
    if baseline_conversion_rate <= 0 or baseline_conversion_rate >= 1:
        raise ValueError("Baseline conversion rate must be between 0 and 1.")
    if minimum_detectable_effect <= 0:
        raise ValueError("Minimum detectable effect must be greater than 0.")
        
    p1 = baseline_conversion_rate
    p2 = p1 * (1.0 + minimum_detectable_effect)
    if p2 >= 1.0:
        p2 = 0.99
        
    z_alpha = stats.norm.ppf(1.0 - alpha / 2.0)
    z_beta = stats.norm.ppf(power)
    
    p_bar = (p1 + p2) / 2.0
    
    numerator = (z_alpha * math.sqrt(2.0 * p_bar * (1.0 - p_bar)) + z_beta * math.sqrt(p1 * (1.0 - p1) + p2 * (1.0 - p2))) ** 2
    denominator = (p2 - p1) ** 2
    
    sample_per_variant = math.ceil(numerator / denominator)
    return sample_per_variant
