select
    cust_id,
    display_name,
    car_name,
    car_class_short_name,
    starting_position + 1 as starting_position,
    starting_position_in_class + 1 as starting_position_in_class,
    finish_position + 1 as finish_position,
    finish_position_in_class + 1 as finish_position_in_class,
    incidents,
    `interval`,
    class_interval,
    oldi_rating,
    newi_rating,
    newi_rating - oldi_rating as ir_change,
    round(old_cpi, 2) as old_cpi,
    round(new_cpi, 2) as new_cpi,
    round(new_cpi - old_cpi, 2) as cpi_change,
    laps_complete,
    laps_lead
from iracing.mv_session_results
where subsession_id = %(subsession_id)s
and simsession_number = 0
order by finish_position