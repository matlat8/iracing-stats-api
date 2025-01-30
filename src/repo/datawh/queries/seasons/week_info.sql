select
    series_id,
    series_name,
    series_short_name,
    season_id,
    season_year,
    season_quarter,
    race_week_num,
    t.track_name,
    t.config_name,
    'https://images-static.iracing.com' || t.folder || '/' || t.large_image as track_image,
    license_category,
    min(start_time) as min_start,
    max(end_time) as max_end,
    avg(incidents) as avg_incidents,
    count(distinct cust_id) as unique_drivers,
    count(distinct subsession_id) as total_splits,
    sum(laps_complete) as total_laps_completed
from iracing.v_results r
left join iracing.tracks t FINAL
    ON tupleElement(r.track, 2) = t.track_id
left join iracing.cars c FINAL
    on r.car_id = c.car_id
where season_id = %(season_id)s
and race_week_num = %(week_num)s
and simsession_type = 6
and simsession_number = 0
group by all