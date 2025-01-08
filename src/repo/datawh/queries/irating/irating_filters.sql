select
    groupArraySorted(5)(distinct season_year) as years,
    groupArraySorted(4)(distinct season_quarter) as quarters,
    groupArraySorted(12)(distinct license_category) as license_categories
from iracing.v_results