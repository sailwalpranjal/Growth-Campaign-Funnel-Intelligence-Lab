-- ==============================================================================
-- 03_metrics.sql
-- Campaign Scorecard & 3-Factor Efficiency Decomposition
-- Aggregation Rule: STRICT RATIO-OF-SUMS (Never average of row rates)
-- ==============================================================================

DROP VIEW IF EXISTS view_campaign_scorecard;

CREATE VIEW view_campaign_scorecard AS
SELECT
    xyz_campaign_id AS campaign_id,
    COUNT(ad_id) AS total_ads,
    SUM(impressions) AS total_impressions,
    SUM(clicks) AS total_clicks,
    ROUND(SUM(spent), 2) AS total_spend,
    SUM(total_conversion) AS total_conversions,
    SUM(approved_conversion) AS approved_conversions,
    
    -- Primary Efficiency Ratios (Ratio of Sums)
    ROUND(CAST(SUM(clicks) AS FLOAT) / NULLIF(SUM(impressions), 0), 6) AS ctr,
    ROUND(CAST(SUM(spent) AS FLOAT) / NULLIF(SUM(clicks), 0), 4) AS cpc,
    ROUND((CAST(SUM(spent) AS FLOAT) / NULLIF(SUM(impressions), 0)) * 1000.0, 4) AS cpm,
    
    -- Conversion Rates
    ROUND(CAST(SUM(total_conversion) AS FLOAT) / NULLIF(SUM(clicks), 0), 4) AS click_to_total_conv_rate,
    ROUND(CAST(SUM(approved_conversion) AS FLOAT) / NULLIF(SUM(clicks), 0), 4) AS click_to_approved_conv_rate,
    ROUND(CAST(SUM(approved_conversion) AS FLOAT) / NULLIF(SUM(total_conversion), 0), 4) AS total_to_approved_rate,
    
    -- Cost Efficiencies
    ROUND(CAST(SUM(spent) AS FLOAT) / NULLIF(SUM(total_conversion), 0), 2) AS cost_per_total_conv,
    ROUND(CAST(SUM(spent) AS FLOAT) / NULLIF(SUM(approved_conversion), 0), 2) AS cost_per_approved_conv,
    
    -- 3-Factor Efficiency Decomposition Levers
    -- Cost per Approved = (Spend / Impressions) * (Impressions / Clicks) * (Clicks / Approved)
    --                   = (CPM / 1000) * (1 / CTR) * (1 / Click_to_Approved_Rate)
    ROUND(CAST(SUM(spent) AS FLOAT) / NULLIF(SUM(impressions), 0), 6) AS lever_1_cost_per_impression,
    ROUND(CAST(SUM(impressions) AS FLOAT) / NULLIF(SUM(clicks), 0), 2) AS lever_2_impressions_per_click,
    ROUND(CAST(SUM(clicks) AS FLOAT) / NULLIF(SUM(approved_conversion), 0), 2) AS lever_3_clicks_per_approved
FROM view_clean_ad_campaigns
GROUP BY xyz_campaign_id
ORDER BY xyz_campaign_id;
