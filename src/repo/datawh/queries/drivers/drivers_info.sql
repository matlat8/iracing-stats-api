select
    cust_id,
    display_name,
    count(*) as total_events,
    SUM(IF(simsession_type = 6, 1, 0)) as irating_events,
    avg(if(simsession_type = 6, laps_complete, null)) as irating_events_avg_laps_completed,
    round(avg(finish_position_in_class), 2) + 1 as avg_finish_position_in_class,
    round(avg(starting_position_in_class), 2) + 1 as avg_start_position_in_class
from iracing.session_results
where
    1=1
--and cust_id = 80653
and simsession_number = 0
group by all
order by total_events desc
limit 1000;