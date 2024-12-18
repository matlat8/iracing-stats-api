select
    sr.cust_id,
    sr.display_name,
    SUM(IF(sr.finish_position_in_class = 0, 1, 0))                               AS total_wins,
    SUM(IF(s.license_category_id = 1 AND sr.finish_position_in_class = 0, 1, 0)) AS oval_wins,
    SUM(IF(s.license_category_id = 2 AND sr.finish_position_in_class = 0, 1, 0)) AS road_wins,
    SUM(IF(s.license_category_id = 3 AND sr.finish_position_in_class = 0, 1, 0)) AS dirt_oval_wins,
    SUM(IF(s.license_category_id = 4 AND sr.finish_position_in_class = 0, 1, 0)) AS dirt_road_wins,
    SUM(IF(s.license_category_id = 5 AND sr.finish_position_in_class = 0, 1, 0)) AS sports_car_wins,
    SUM(IF(s.license_category_id = 6 AND sr.finish_position_in_class = 0, 1, 0)) AS formula_car_wins
from iracing.session_results sr
inner join iracing.v_series s
    on sr.subsession_id = s.subsession_id
where 1=1
AND cust_id = %(cust_id)s
AND simsession_number = 0
AND simsession_type = 6
GROUP BY ALL
ORDER BY total_wins DESC