select sr.cust_id,
       sr.newi_rating,
       s.start_time,
       s.license_category,
       s.license_category_id,
       sr.simsession_type,
       sr.simsession_type_name
from iracing.mv_session_results sr
inner join iracing.v_series s
    on sr.subsession_id = s.subsession_id
where
    1=1
AND sr.cust_id = %(cust_id)s
AND sr.simsession_type in (6)
order by s.start_time desc