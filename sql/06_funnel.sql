-- ==============================================================================
-- 06_funnel.sql
-- Observable Multi-Stage Acquisition Funnel Analysis
-- Real Observable Stages: Impression -> Click -> Total Conversion -> Approved Conversion
-- Strictly excludes unobservable app stages (installs, logins) to maintain analytical discipline.
-- ==============================================================================

DROP VIEW IF EXISTS view_funnel_by_campaign;

CREATE VIEW view_funnel_by_campaign AS
SELECT
    xyz_campaign_id AS campaign_id,
    SUM(impressions) AS stage_1_impressions,
    SUM(clicks) AS stage_2_clicks,
    SUM(total_conversion) AS stage_3_total_conversions,
    SUM(approved_conversion) AS stage_4_approved_conversions,
    
    -- Step Conversion Rates
    ROUND(CAST(SUM(clicks) AS FLOAT) / NULLIF(SUM(impressions), 0), 6) AS step_1_to_2_ctr,
    ROUND(CAST(SUM(total_conversion) AS FLOAT) / NULLIF(SUM(clicks), 0), 4) AS step_2_to_3_enquiry_rate,
    ROUND(CAST(SUM(approved_conversion) AS FLOAT) / NULLIF(SUM(total_conversion), 0), 4) AS step_3_to_4_approval_rate,
    
    -- Cumulative End-to-End Conversion Rate
    ROUND(CAST(SUM(approved_conversion) AS FLOAT) / NULLIF(SUM(impressions), 0), 8) AS cumulative_imp_to_approved_rate,
    
    -- Drop-off Volumes
    SUM(impressions) - SUM(clicks) AS drop_1_unclicked_impressions,
    SUM(clicks) - SUM(total_conversion) AS drop_2_non_converting_clicks,
    SUM(total_conversion) - SUM(approved_conversion) AS drop_3_unapproved_enquiries,
    
    -- Relative Drop-off Percentages
    ROUND(1.0 - (CAST(SUM(clicks) AS FLOAT) / NULLIF(SUM(impressions), 0)), 6) AS drop_rate_impressions_to_clicks,
    ROUND(1.0 - (CAST(SUM(total_conversion) AS FLOAT) / NULLIF(SUM(clicks), 0)), 4) AS drop_rate_clicks_to_total,
    ROUND(1.0 - (CAST(SUM(approved_conversion) AS FLOAT) / NULLIF(SUM(total_conversion), 0)), 4) AS drop_rate_total_to_approved
FROM view_clean_ad_campaigns
GROUP BY xyz_campaign_id
ORDER BY xyz_campaign_id;
