select
    series_id,
    series_name,
    license_category,
    race_week_num,
    --max(race_week_num) as race_week_numm,
    count(*) as event_count
from iracing.v_series s
inner join (
    select
        series_id,
        max(race_week_num) max_race_week_num --oddly getting better performance with the
    from iracing.v_series                   -- inner join compared to the max() - 200ms difference
    where season_year = 2025
    and season_quarter = 1
    group by all
) x
on s.series_id = x.series_id
and s.race_week_num = x.max_race_week_num
where season_year = 2025
and season_quarter = 1
group by all
order by event_count desc, series_name