select
    sr.cust_id AS cust_id,
    d.display_name AS display_name,
    d.club_name AS club_name,
    d.country_code as country_code,
    d.country_image_url as country_image_url,
    c.car_name as car_name,
    'https://images-static.iracing.com' || c.folder || '/' || c.large_image as large_car_image,
    'https://images-static.iracing.com' || c.folder || '/' || c.small_image as small_car_image,
    car_class_short_name,
    starting_position + 1 as starting_position,
    starting_position_in_class + 1 as starting_position_in_class,
    finish_position + 1 as finish_position,
    finish_position_in_class + 1 as finish_position_in_class,
    starting_position - finish_position as pos_change,
    starting_position_in_class - finish_position_in_class as pos_in_class_change,
    abs(pos_change) as abs_pos_change,
    abs(pos_in_class_change) as abs_pos_in_class_change,
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
from iracing.mv_session_results sr
left join iracing.cars c FINAL
    on sr.car_id = c.car_id
left join iracing_prod_model.dim_drivers d
    on sr.cust_id = d.cust_id
where subsession_id = %(subsession_id)s
and simsession_number = 0
order by finish_position