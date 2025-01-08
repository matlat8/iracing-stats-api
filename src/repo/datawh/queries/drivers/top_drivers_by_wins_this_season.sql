select
    cust_id,
    display_name,
    sum(if(finish_position_in_class = 0, 1, 0)) as wins,
    sum(if(finish_position_in_class = 0 AND license_category_id = 1, 1, 0)) as oval_wins,
    sum(if(finish_position_in_class = 0 AND license_category_id = 3, 1, 0)) as dirt_oval_wins,
    sum(if(finish_position_in_class = 0 AND license_category_id = 4, 1, 0)) as dirt_road_wins,
    sum(if(finish_position_in_class = 0 AND license_category_id = 5, 1, 0)) as sportscar_wins,
    sum(if(finish_position_in_class = 0 AND license_category_id = 6, 1, 0)) as formulacar_wins
from iracing.v_results r
inner join (
    select
        season_quarter as season_quarter,
        max(season_year) as season_year
    from iracing.v_series
    group by season_quarter
    order by season_year desc, season_quarter desc
    limit 1
) tp -- time period (latest season year and quarter)
on r.season_year = tp.season_year
and r.season_quarter = tp.season_quarter
group by cust_id, display_name
order by wins desc
limit %(limit)s