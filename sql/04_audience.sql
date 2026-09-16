-- ==============================================================================
-- 04_audience.sql
-- Audience Demographic & Interest Segment Analysis
-- Includes Sample-Size Qualification Flags and Ratio-of-Sums Metrics
-- ==============================================================================

-- 1. Performance by Age Bracket
DROP VIEW IF EXISTS view_audience_age;

CREATE VIEW view_audience_age AS
SELECT
    age,
    COUNT(ad_id) AS ad_count,
    SUM(impressions) AS total_impressions,
    SUM(clicks) AS total_clicks,
    ROUND(SUM(spent), 2) AS total_spend,
    SUM(total_conversion) AS total_conversions,
    SUM(approved_conversion) AS approved_conversions,
    ROUND(CAST(SUM(clicks) AS FLOAT) / NULLIF(SUM(impressions), 0), 6) AS ctr,
    ROUND(CAST(SUM(spent) AS FLOAT) / NULLIF(SUM(clicks), 0), 4) AS cpc,
    ROUND((CAST(SUM(spent) AS FLOAT) / NULLIF(SUM(impressions), 0)) * 1000.0, 4) AS cpm,
    ROUND(CAST(SUM(approved_conversion) AS FLOAT) / NULLIF(SUM(clicks), 0), 4) AS click_to_approved_rate,
    ROUND(CAST(SUM(spent) AS FLOAT) / NULLIF(SUM(approved_conversion), 0), 2) AS cost_per_approved_conv,
    CASE 
        WHEN SUM(clicks) >= 50 THEN 'Qualified (High Sample)'
        WHEN SUM(clicks) >= 25 THEN 'Qualified (Medium Sample)'
        WHEN SUM(clicks) >= 10 THEN 'Directional (Low Sample)'
        ELSE 'Unreliable (Sample < 10)'
    END AS sample_qualification
FROM view_clean_ad_campaigns
GROUP BY age
ORDER BY age;

-- 2. Performance by Gender
DROP VIEW IF EXISTS view_audience_gender;

CREATE VIEW view_audience_gender AS
SELECT
    gender,
    COUNT(ad_id) AS ad_count,
    SUM(impressions) AS total_impressions,
    SUM(clicks) AS total_clicks,
    ROUND(SUM(spent), 2) AS total_spend,
    SUM(total_conversion) AS total_conversions,
    SUM(approved_conversion) AS approved_conversions,
    ROUND(CAST(SUM(clicks) AS FLOAT) / NULLIF(SUM(impressions), 0), 6) AS ctr,
    ROUND(CAST(SUM(spent) AS FLOAT) / NULLIF(SUM(clicks), 0), 4) AS cpc,
    ROUND((CAST(SUM(spent) AS FLOAT) / NULLIF(SUM(impressions), 0)) * 1000.0, 4) AS cpm,
    ROUND(CAST(SUM(approved_conversion) AS FLOAT) / NULLIF(SUM(clicks), 0), 4) AS click_to_approved_rate,
    ROUND(CAST(SUM(spent) AS FLOAT) / NULLIF(SUM(approved_conversion), 0), 2) AS cost_per_approved_conv,
    'Qualified (High Sample)' AS sample_qualification
FROM view_clean_ad_campaigns
GROUP BY gender
ORDER BY gender;

-- 3. Performance by Age x Gender Interaction
DROP VIEW IF EXISTS view_audience_age_gender;

CREATE VIEW view_audience_age_gender AS
SELECT
    age,
    gender,
    COUNT(ad_id) AS ad_count,
    SUM(impressions) AS total_impressions,
    SUM(clicks) AS total_clicks,
    ROUND(SUM(spent), 2) AS total_spend,
    SUM(total_conversion) AS total_conversions,
    SUM(approved_conversion) AS approved_conversions,
    ROUND(CAST(SUM(clicks) AS FLOAT) / NULLIF(SUM(impressions), 0), 6) AS ctr,
    ROUND(CAST(SUM(spent) AS FLOAT) / NULLIF(SUM(clicks), 0), 4) AS cpc,
    ROUND((CAST(SUM(spent) AS FLOAT) / NULLIF(SUM(impressions), 0)) * 1000.0, 4) AS cpm,
    ROUND(CAST(SUM(approved_conversion) AS FLOAT) / NULLIF(SUM(clicks), 0), 4) AS click_to_approved_rate,
    ROUND(CAST(SUM(spent) AS FLOAT) / NULLIF(SUM(approved_conversion), 0), 2) AS cost_per_approved_conv,
    CASE 
        WHEN SUM(clicks) >= 50 THEN 'Qualified (High Sample)'
        WHEN SUM(clicks) >= 25 THEN 'Qualified (Medium Sample)'
        WHEN SUM(clicks) >= 10 THEN 'Directional (Low Sample)'
        ELSE 'Unreliable (Sample < 10)'
    END AS sample_qualification
FROM view_clean_ad_campaigns
GROUP BY age, gender
ORDER BY age, gender;

-- 4. Performance by Interest Category (Ranked by volume)
DROP VIEW IF EXISTS view_audience_interest;

CREATE VIEW view_audience_interest AS
SELECT
    interest,
    COUNT(ad_id) AS ad_count,
    SUM(impressions) AS total_impressions,
    SUM(clicks) AS total_clicks,
    ROUND(SUM(spent), 2) AS total_spend,
    SUM(total_conversion) AS total_conversions,
    SUM(approved_conversion) AS approved_conversions,
    ROUND(CAST(SUM(clicks) AS FLOAT) / NULLIF(SUM(impressions), 0), 6) AS ctr,
    ROUND(CAST(SUM(spent) AS FLOAT) / NULLIF(SUM(clicks), 0), 4) AS cpc,
    ROUND((CAST(SUM(spent) AS FLOAT) / NULLIF(SUM(impressions), 0)) * 1000.0, 4) AS cpm,
    ROUND(CAST(SUM(approved_conversion) AS FLOAT) / NULLIF(SUM(clicks), 0), 4) AS click_to_approved_rate,
    ROUND(CAST(SUM(spent) AS FLOAT) / NULLIF(SUM(approved_conversion), 0), 2) AS cost_per_approved_conv,
    CASE 
        WHEN SUM(clicks) >= 50 THEN 'Qualified (High Sample)'
        WHEN SUM(clicks) >= 25 THEN 'Qualified (Medium Sample)'
        WHEN SUM(clicks) >= 10 THEN 'Directional (Low Sample)'
        ELSE 'Unreliable (Sample < 10)'
    END AS sample_qualification
FROM view_clean_ad_campaigns
GROUP BY interest
ORDER BY total_clicks DESC;
