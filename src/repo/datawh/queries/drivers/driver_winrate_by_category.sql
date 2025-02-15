SELECT
    license_category,
    count(*) as total_events,
    sum(if(finish_position_in_class = 0, 1, 0))     as wins,
    coalesce(divide(wins, total_events), 0)         as win_rate,
    SUM(IF(finish_position_in_class <= 2, 1, 0))    as top_3,
    SUM(IF(finish_position_in_class <= 4, 1, 0))    as top_5,
    avg(finish_position_in_class)                   as avg_finishing_position
FROM
    iracing_api.results
WHERE
    cust_id = %(cust_id)s
AND simsession_type = 6
GROUP BY ALL
ORDER BY
    license_category