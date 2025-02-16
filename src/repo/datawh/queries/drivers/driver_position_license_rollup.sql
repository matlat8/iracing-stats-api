select
    license_category,
    sum(if(simsession_type = 6 AND simsession_number = 0, 1, 0)) as total_events,
    avg(if(simsession_type = 4, finish_position_in_class, null)) AS qualifying_avg_finish_pos,
    avg(if(simsession_type = 6 AND simsession_number = 0, finish_position_in_class, null)) AS race_avg_finish_pos
from iracing_api.results
where cust_id = %(cust_id)s
group by rollup (license_category)
order by license_category nulls last