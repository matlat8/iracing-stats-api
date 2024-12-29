select
    cust_id,
    display_name,
    car_name,
    starting_position + 1 as starting_position,
    finish_position + 1 as finish_position,
    incidents,
    `interval`,
    oldi_rating,
    newi_rating
from iracing.mv_session_results
where subsession_id = %(subsession_id)s
and simsession_number = 0
order by finish_position