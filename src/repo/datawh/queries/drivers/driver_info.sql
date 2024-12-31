select
    cust_id,
    display_name,
    club_name,
    country_code,
    count(*) as total_events,
    SUM(IF(simsession_type = 6, 1, 0)) as total_races,
    sum(if(simsession_type = 6 AND finish_position_in_class = 0, 1, 0)) AS total_wins,
    sum(if(simsession_type = 6 AND finish_position_in_class <= 2, 1, 0)) AS podiums,
    sum(if(simsession_type = 6 AND finish_position_in_class <= 4, 1, 0)) AS top_5,
    avg(if(simsession_type = 6, laps_complete, null)) as irating_events_avg_laps_completed,
    round(avg(finish_position_in_class), 2) + 1 as avg_finish_position_in_class,
    round(avg(starting_position_in_class), 2) + 1 as avg_start_position_in_class
from iracing.mv_session_results sr
-- INNER JOIN (
--     SELECT DISTINCT cust_id, display_name, club_name, country_code from iracing.mv_session_results
-- ) x
--on sr.cust_id = x.cust_id
where
    1=1
and cust_id = %(cust_id)s
and simsession_number = 0
group by all
order by total_events desc
limit 1