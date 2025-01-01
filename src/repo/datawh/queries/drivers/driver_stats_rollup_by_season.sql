select
    season_year,
    season_quarter,
    count(*) as total_events,
    SUM(IF(sr.simsession_type = 6, 1, 0)) as total_races,
    sum(if(sr.simsession_type = 6 AND sr.finish_position_in_class = 0, 1, 0)) AS total_wins,
    sum(if(sr.simsession_type = 6 AND sr.finish_position_in_class <= 2, 1, 0)) AS podiums,
    sum(if(sr.simsession_type = 6 AND sr.finish_position_in_class <= 4, 1, 0)) AS top_5,
    avg(if(sr.simsession_type = 6, sr.laps_complete, null)) as irating_events_avg_laps_completed,
    round(avg(sr.finish_position_in_class), 2) + 1 as avg_finish_position_in_class,
    round(avg(sr.starting_position_in_class), 2) + 1 as avg_start_position_in_class
from iracing.mv_session_results sr
inner join iracing.v_series s
    on sr.subsession_id = s.subsession_id
where
    1=1
and sr.cust_id = %(cust_id)s
and sr.simsession_number = 0
group by ROLLUP(season_year, season_quarter)
ORDER BY season_year desc nulls last, season_quarter desc nulls last