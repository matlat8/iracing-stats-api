WITH irating_cte as (
    SELECT
        cust_id,
        display_name,
        max(case when license_category_id = 1 then newi_rating end) as oval_rating,
        max(case when license_category_id = 2 then newi_rating end) as road_rating,
        max(case when license_category_id = 3 then newi_rating end) as dirt_oval_rating,
        max(case when license_category_id = 4 then newi_rating end) as dirt_road_rating,
        max(case when license_category_id = 5 then newi_rating end) as sports_car_rating,
        max(case when license_category_id = 6 then newi_rating end) as formula_car_rating
    FROM (
        SELECT
            sr.cust_id,
            sr.display_name,
            s.license_category,
            s.license_category_id,
            sr.newi_rating,
            s.end_time,
            ROW_NUMBER() OVER (
                PARTITION BY sr.cust_id, s.license_category
                ORDER BY s.end_time DESC
            ) as rn
        FROM iracing.session_results sr
        LEFT JOIN iracing.v_series s
            ON sr.subsession_id = s.subsession_id
    ) x
    WHERE rn = 1
    GROUP BY cust_id, display_name
)
SELECT
    DISTINCT sr.cust_id                 as cust_id,
             sr.display_name            as display_name,  
             sr.club_name               as club_name,
             sr.country_code            as country_code,
             ir.oval_rating             as oval_rating,
             ir.road_rating             as road_rating,
             ir.dirt_oval_rating        as dirt_oval_rating,
             ir.dirt_road_rating        as dirt_road_rating,
             ir.sports_car_rating       as sports_car_rating,
             ir.formula_car_rating      as formula_car_rating
FROM
    iracing.session_results sr
LEFT JOIN
    iracing.v_series s
        ON sr.subsession_id = s.subsession_id
LEFT JOIN
    irating_cte ir
        ON sr.cust_id = ir.cust_id
WHERE
    sr.cust_id = %(cust_id)s