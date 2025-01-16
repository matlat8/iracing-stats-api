from typing import Annotated
from fastapi import APIRouter, Query

from src.repo.datawh.injection import DataRepository

from . import services, schema

router = APIRouter(prefix="/irating", tags=["irating"])

@router.get("/distribution")
async def get_irating_distribution(datawh: DataRepository,
                                    params: Annotated[schema.IRatingDistributionFiltersQuery, Query()],
                              ):
    return {
        'distribution': await services.irating_distribution(datawh, params), 
        'kpis': await datawh.irating_distribution_kpis(params.license, params.year, params.quarter)
        }

@router.get("/filters")
async def get_irating_filters(datawh: DataRepository):
    return {'distribution': await datawh.irating_filters()}