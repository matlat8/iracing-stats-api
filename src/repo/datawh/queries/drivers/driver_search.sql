SELECT 
    cust_id,
    display_name,
    club_name,
    country_code,
    oval_rating,
    road_rating,
    dirt_oval_rating,
    dirt_road_rating,
    sports_car_rating,
    formula_car_rating
FROM 
    iracing.dim_drivers
WHERE 
    display_name ILIKE %(search_term)s
ORDER BY 
    cust_id
LIMIT 
    %(limit)s
OFFSET %(offset)s