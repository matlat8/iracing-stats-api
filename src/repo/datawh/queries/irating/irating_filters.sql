
select
    groupArraySorted(5)(distinct season_year) as years,
    groupArraySorted(4)(distinct season_quarter) as quarters
from iracing.v_results