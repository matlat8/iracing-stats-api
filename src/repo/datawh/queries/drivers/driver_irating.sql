SELECT
    sr.cust_id,
    date_trunc('day', s.start_time) as race_date,
    argMax(if(s.license_category_id = 1, newi_rating, null), s.start_time) as oval_ir,
    argMax(if(s.license_category_id = 2, newi_rating, null), s.start_time) as road_ir,
    argMax(if(s.license_category_id = 3, newi_rating, null), s.start_time) as dirtoval_ir,
    argMax(if(s.license_category_id = 4, newi_rating, null), s.start_time) as dirtroad_ir,
    argMax(if(s.license_category_id = 5, newi_rating, null), s.start_time) as sportscar_ir,
    argMax(if(s.license_category_id = 6, newi_rating, null), s.start_time) as formulacar_ir
FROM iracing.mv_session_results sr
INNER JOIN iracing.v_series s
    ON sr.subsession_id = s.subsession_id
WHERE 
    1=1
    AND sr.cust_id = %(cust_id)s
    AND sr.simsession_type in (6)
GROUP BY
    sr.cust_id,
    date_trunc('day', s.start_time)
ORDER BY race_date;