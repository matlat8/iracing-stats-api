select group_id,
       name,
       lap_number + 1 as lap_number,
       lap_position
from iracing.results_lap_chart_data
where subsession_id = %(subsession_id)s