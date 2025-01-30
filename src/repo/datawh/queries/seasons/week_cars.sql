select
    distinct car_name as name,
             'https://images-static.iracing.com' || c.folder || '/' || c.small_image as image
from iracing.v_results r
left join iracing.cars c FINAL
    on r.car_id = c.car_id
where season_id = %(season_id)s
and race_week_num = %(week_num)s
and simsession_type = 6
and simsession_number = 0
order by race_week_num