WITH daily AS
(
    SELECT
        cust_id,
        date_trunc('day', start_time) AS start_day,
        avg(finish_position) AS avg_finish_position,
        avg(starting_position) AS avg_starting_position
    FROM
        iracing_api.results
    WHERE
        cust_id = %(cust_id)s
    AND simsession_type = 6
    AND simsession_number = 0
    GROUP BY cust_id, start_day
)
SELECT
    cust_id,
    start_day,
    avg_finish_position + 1 AS avg_finish_position,
    avg_starting_position + 1 AS avg_starting_position,
    /* Rolling average over the current row and the 6 preceding rows (i.e. total 7 days) */
    avg(avg_finish_position) OVER (
        ORDER BY start_day ASC
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS rolling_avg_finish_position,
    avg(avg_starting_position) OVER (
    ORDER BY start_day ASC
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS rolling_avg_starting_position
FROM daily
ORDER BY start_day DESC;