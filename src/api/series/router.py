from fastapi import APIRouter, Query

from src.repo.datawh.injection import DataRepository

from . import services, schemas

router = APIRouter(prefix="/series", tags=["series"])

@router.get("/this_week", response_model=schemas.SeriesThisWeekResponse)
async def get_series_this_week(datawh: DataRepository):
    return schemas.SeriesThisWeekResponse(
        data=await datawh.series_this_week_by_participation()
        )