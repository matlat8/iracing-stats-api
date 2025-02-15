SELECT
    r.cust_id as x,
    r.display_name as y,
    drivers.cust_id as cust_id,
    r.winner_name as name,
    count(*) as times_beaten,
    drivers.oval_rating,
    drivers.road_rating,
    drivers.dirt_road_rating,
    drivers.dirt_oval_rating,
    drivers.sports_car_rating,
    drivers.formula_car_rating,
    drivers.club_name as club_name,
    drivers.country_code as country_code
FROM iracing_api.results r
LEFT JOIN
    iracing.dim_drivers drivers
        ON r.winner_name = drivers.display_name
WHERE
    y <> name
AND cust_id = %(cust_id)s
--AND cust_id = 490036
GROUP BY
    ALL
ORDER BY
    times_beaten DESC
LIMIT
    1