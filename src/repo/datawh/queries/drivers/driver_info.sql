select cust_id,
       display_name,
       club_name,
       country_code,
       oval_rating,
       road_rating,
       dirt_oval_rating,
       dirt_road_rating,
       sports_car_rating,
       formula_car_rating
from iracing.dim_drivers
WHERE
    cust_id = %(cust_id)s