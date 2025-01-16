WITH ranked_data AS (
    SELECT *
    FROM 
        iracing_api.fct_irating_distribution
    WHERE 
        license_category = %(license)s
    AND season_year = %(year)s
    AND season_quarter = %(quarter)s
),
grouped_data AS (
    SELECT
        irating_group,
        COUNT(*) as count_in_group,
        min(row_num) as min_row,
        max(row_num) as max_row,
        any(total_count) as total_count
    FROM ranked_data
    GROUP BY irating_group
)
SELECT
    irating_group,
    count_in_group,
    round(max_row / total_count * 100, 2) as percentile
FROM grouped_data
WHERE irating_group <= 10000
ORDER BY irating_group;