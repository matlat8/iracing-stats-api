select
    season_id, season_year, season_quarter
from iracing.v_series
where series_id = %(series)s
order by season_year desc, season_quarter desc
limit 1