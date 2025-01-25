WITH RECURSIVE numbers AS (
    SELECT 0 AS n
    UNION ALL
    SELECT n + 1
    FROM numbers
    WHERE n < 200
),
irating_groups AS (
    SELECT n * 50 AS irating_group
    FROM numbers
)
SELECT
    ig.irating_group,
    nullIf(avg(r.best_lap_time) / 10000, 0) as avg_best_lap_time,
    nullIf(avg(r.average_lap) / 10000, 0) as avg_avg_lap_time,
    nullIf(count(*), 1) as participants
FROM irating_groups ig
LEFT JOIN (
    SELECT
        round(oldi_rating/50)*50 as irating_group,
        best_lap_time,
        average_lap
    FROM iracing.v_results
    WHERE simsession_number = 0
    AND simsession_type = 6
    AND season_id = %(season_id)s
    AND race_week_num = %(race_week)s
    AND best_lap_time not in (-1, 0)
) r ON ig.irating_group = r.irating_group
GROUP BY ig.irating_group
ORDER BY ig.irating_group
;