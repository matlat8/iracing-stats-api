from fastapi import APIRouter, Query

from src.repo.datawh.injection import DataRepository

from . import services, schemas

router = APIRouter(prefix="/series", tags=["series"])

@router.get("/this_week", response_model=schemas.SeriesThisWeekResponse)
async def get_series_this_week(datawh: DataRepository):
    return schemas.SeriesThisWeekResponse(
        data=await datawh.series_this_week_by_participation()
        )
    
@router.get("/{series_id}")
async def lookup_series(datawh: DataRepository, series_id: int):
    return schemas.SeriesLookupResponse(
        seasons=await datawh.lookup_series_seasons_by_id(series_id),
        participation=await services.series_latest_season_participation(datawh, series_id)
    )