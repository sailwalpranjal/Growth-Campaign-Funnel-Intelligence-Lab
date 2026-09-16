-- ==============================================================================
-- 02_clean.sql
-- Cleansed analytical views with strict data hygiene filters
-- ==============================================================================

-- Cleaned advertising campaign dataset
DROP VIEW IF EXISTS view_clean_ad_campaigns;

CREATE VIEW view_clean_ad_campaigns AS
SELECT
    ad_id,
    xyz_campaign_id,
    fb_campaign_id,
    age,
    gender,
    interest,
    impressions,
    clicks,
    spent,
    total_conversion,
    approved_conversion,
    -- Analytical flags
    CASE WHEN clicks = 0 THEN 1 ELSE 0 END AS is_zero_click_ad,
    CASE WHEN impressions = 0 THEN 1 ELSE 0 END AS is_zero_impression_ad,
    CASE WHEN clicks < 10 THEN 1 ELSE 0 END AS is_low_sample_ad
FROM stg_ad_campaigns
WHERE
    impressions >= 0
    AND clicks >= 0
    AND spent >= 0
    AND total_conversion >= 0
    AND approved_conversion >= 0
    AND clicks <= impressions
    AND approved_conversion <= total_conversion;

-- Cleaned consumer behavior dataset (drops null outcome records)
DROP VIEW IF EXISTS view_clean_consumer_behavior;

CREATE VIEW view_clean_consumer_behavior AS
SELECT
    session_id,
    administrative,
    administrative_duration,
    informational,
    informational_duration,
    product_related,
    product_related_duration,
    bounce_rates,
    exit_rates,
    page_values,
    special_day,
    month,
    operating_systems,
    browser,
    region,
    traffic_type,
    visitor_type,
    weekend,
    revenue,
    -- Behavioral engagement segment
    CASE 
        WHEN product_related_duration > 600 AND bounce_rates < 0.05 THEN 'High Engagement'
        WHEN product_related_duration BETWEEN 120 AND 600 THEN 'Medium Engagement'
        ELSE 'Low Engagement / Skimmer'
    END AS engagement_tier
FROM stg_consumer_behavior
WHERE revenue IS NOT NULL;
