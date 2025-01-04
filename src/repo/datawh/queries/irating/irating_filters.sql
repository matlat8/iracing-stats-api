select
    groupArray(distinct season_year) as years,
    groupArray(distinct season_quarter) as quarters
from iracing.v_results