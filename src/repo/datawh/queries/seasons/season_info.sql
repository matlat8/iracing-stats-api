select
    series_id,
    series_name,
    series_short_name,
    season_id,
    season_year,
    season_quarter,
    license_category,
    min(start_time) as min_start,
    max(end_time) as max_end

from iracing.v_series
where season_id = %(season_id)s
group by all