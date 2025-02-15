SELECT 
    *
FROM 
    iracing_prod_model.dim_drivers
WHERE 
    display_name ILIKE %(search_term)s
ORDER BY 
    cust_id desc
LIMIT 
    %(limit)s
OFFSET %(offset)s