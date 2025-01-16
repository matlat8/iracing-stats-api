select
    distinct license_category,
             'Y' || right(toString(season_year), 2) || '-S' || season_quarter as period
from iracing_api.fct_irating_distribution
order by 2 desc, 1