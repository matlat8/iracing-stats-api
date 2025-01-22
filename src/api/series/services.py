import json
from fastapi import HTTPException
from src.repo.datawh.data import DataWH

from .schemas import SeriesParticipationObject, SeriesParticipation, SeriesSeasonsResponse, SeriesSeasonObject
from . import schemas

async def series_latest_season_participation(datawh: DataWH, series_id: int) -> dict:
    
    # Get the data from the warehouse
    data = await datawh.series_latest_season_participation(series_id=series_id)
    print(json.dumps(data, indent=2))
    this_season = None
    
    # If there is no data, then the series does not exist
    if not data or len(data) == 0:
        raise HTTPException(
            status_code=404,
            detail=f"Series with id {series_id} not found"
        )
    
    # Since this warehosue obj uses "GROUP BY ROLLUP", parse out the rollup row
    if len(data) > 0 and isinstance(data[0].get('participant_count'), int):
        this_season = data[0]['participant_count']
    
    # Same for each weeks. Start grabbing rows from index 2 - 0 & 1 contain the rollup data
    weeks = []
    for index, item in enumerate(data):
        if index not in (0, 1):
            weeks.append(SeriesParticipation.model_validate(item))
    
    return SeriesParticipationObject(this_season=this_season, weeks=weeks)

async def series_seasons(datawh: DataWH, series_id: int) -> SeriesSeasonsResponse:
    
    data = await datawh.series_seasons_stats(series_id)
    if not data or len(data) == 0:
        raise HTTPException(
            status_code=404,
            detail=f"Series with id {series_id} not found"
        )
    
    
    return SeriesSeasonsResponse(
        seasons=[SeriesSeasonObject.model_validate(item) for item in data]
    )
    
async def series_season_weeks(datawh: DataWH, series_id: int, season_id: int):
    data = await datawh.series_season_weeks(series_id=series_id, season_id=season_id)
    
    # If there is no data, then the series does not exist
    if not data or len(data) == 0:
        raise HTTPException(
            status_code=404,
            detail=f"Series with id {series_id} not found or season with id {season_id} not found"
        )
        
    final = []
    for i in data:
        cars = []
        
        # Extract the car names and images
        zip_car = zip(i['car_names'], i['small_car_images'])
        for car in zip_car:
            cars.append(schemas.SeriesSeasonWeekCar(
                car_name=car[0],
                car_image=car[1]
            ))
        week = schemas.SeriesSeasonWeekWeek(**i, cars=cars)
        final.append(week)
    
    return final
        