SELECT
    license_category,
    season_year,
    season_quarter,
    quantileExact(0.5)(newi_rating) as median_irating,
    quantileExact(0.5)(prior_year_rating) as yago_median_irating,
    quantileExact(0.99)(newi_rating) as top_1_percent,
    quantileExact(0.99)(prior_year_rating) as yago_top_1_percent,
    quantileExact(0.95)(newi_rating) as top_5_percent,
    quantileExact(0.95)(prior_year_rating) as yago_top_5_percent,
    quantileExact(0.90)(newi_rating) as top_10_percent,
    quantileExact(0.90)(prior_year_rating) as yago_top_10_percent,
    stddevPop(newi_rating) as rating_std_dev,
    stddevPop(prior_year_rating) as yago_stg_dev,
    avg(newi_rating) as avg_irating,
    avg(prior_year_rating) as yago_avg_irating,
    count(*) as active_drivers
FROM iracing_api.fct_irating_distribution
WHERE
    license_category = %(license)s
AND season_year = %(year)s
AND season_quarter = %(quarter)s
GROUP BY
    license_category,
    season_year,
    season_quarter
ORDER BY
    license_category,
    season_year,
    season_quarter