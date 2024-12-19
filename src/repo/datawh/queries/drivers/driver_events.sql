select distinct s.session_id,
                s.subsession_id,
                s.start_time,
                s.end_time,
                s.license_category_id,
                s.license_category,
                s.num_drivers,
                s.num_cautions,
                s.num_caution_laps,
                s.num_lead_changes,
                s.event_laps_complete,
                s.driver_changes,
                s.winner_group_id,
                s.winner_name,
                s.winner_ai,
                s.track,
                s.official_session,
                s.season_id,
                s.season_year,
                s.season_quarter,
                s.event_type_name,
                s.series_id,
                s.series_name,
                s.race_week_num,
                s.event_strength_of_field,
                s.event_average_lap,
                s.event_best_lap_time
from iracing.v_series s
inner join iracing.session_results sr
    on s.subsession_id = sr.subsession_id
where sr.cust_id = %(cust_id)s
and s.event_type = 5
order by end_time desc