SELECT 
    cust_id, 
    display_name,
    club_name,
    country_code
FROM 
    iracing_prod_model.dim_drivers
WHERE 
    display_name ILIKE %(search_term)s
ORDER BY 
    cust_id
LIMIT 
    %(limit)s
OFFSET %(offset)s