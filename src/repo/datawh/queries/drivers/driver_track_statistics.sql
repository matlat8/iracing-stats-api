SELECT
    tracks as track,
    count(tracks) as raced,
    sum(ir_change) as ir_change,
    round(sum(cpi_change), 2) as cpi_change
FROM (
    select
        tupleElement(track, 2) AS track_id,
        tupleElement(track, 1) as track_config,
        tupleElement(track, 3) as track_name,
        if(track_config = 'N/A', '', track_config) as good_track_config,
        track_name || ' ' || good_track_config as tracks,
        finish_position_in_class + 1 as finish_position_in_class,
        oldi_rating - newi_rating as ir_change,
        old_cpi - new_cpi as cpi_change
    from iracing.v_results
    where cust_id = %(cust_id)s
    AND simsession_number = 0
    AND simsession_type = 6
)
GROUP BY track
ORDER BY ir_change desc