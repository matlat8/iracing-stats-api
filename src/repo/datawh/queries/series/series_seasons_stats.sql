select
    season_id,
    season_year,
    season_quarter,
    'Y' || season_year || ' S' || season_quarter as season_title,
    date_trunc('day', min(start_time)) as min_st,
    date_trunc('day', max(start_time)) as max_st,
    if(date_trunc('week', max_st) = date_trunc('week', current_date()), true, false) as is_active_season,
    sum(if(event_type = 2, 1, 0)) as practice_sessions,
    sum(if(event_type = 5, 1, 0)) as race_sessions,
    sum(if(event_type = 4, 1, 0)) as time_trial_sessions,
    count(*) as total_sessions
from
    iracing.v_series
where
    series_id = %(series_id)s
group by
    all
order by
    season_year desc,
    season_quarter desc