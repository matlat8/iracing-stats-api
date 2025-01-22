select
    race_week_num,
    t.track_name,
    t.config_name,
    array_agg(distinct c.car_name) as car_names,
    array_agg(distinct r.car_class_name) as car_class_names,
    'https://images-static.iracing.com' || t.folder || '/' || t.small_image as small_track_image,
    array_agg(distinct 'https://images-static.iracing.com' || c.folder || '/' || c.small_image) as small_car_images,
    count(distinct subsession_id) as splits_this_week
from iracing.v_results r
left join iracing.tracks t FINAL
    on tupleElement(r.track, 2) = t.track_id
left join iracing.cars c FINAL
    on r.car_id = c.car_id
where season_id = %(season_id)s
and series_id = %(series_id)s
group by all
order by race_week_num