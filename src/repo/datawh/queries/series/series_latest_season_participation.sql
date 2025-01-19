select
    series_id,
    race_week_num,
    count(*) as participant_count
from iracing.v_results r
inner join (
    select distinct season_year, season_quarter
    from iracing.v_series
    order by season_year desc, season_quarter desc
    limit 1
) x
on r.season_year = x.season_year
and r.season_quarter = x.season_quarter
where series_id = %(series_id)s
and simsession_number = 0
and simsession_type = 6
group by rollup (series_id, race_week_num)
order by series_id nulls first, race_week_num nulls first