WITH ranked_data AS (
    SELECT
        cust_id,
        newi_rating,
        floor(newi_rating / 50) * 50 as irating_group,
        count(*) OVER () as total_count,
        row_number() OVER (ORDER BY newi_rating) as row_num
    FROM iracing.v_results r
    INNER JOIN (
        SELECT cust_id, max(start_time) as mst
        FROM iracing.v_results
        GROUP BY cust_id
    ) x ON r.cust_id = x.cust_id AND r.start_time = x.mst
    WHERE newi_rating <> -1
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
ORDER BY irating_group;