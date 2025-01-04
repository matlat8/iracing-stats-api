from fastapi import APIRouter

from src.repo.datawh.injection import DataRepository

router = APIRouter(prefix="/irating", tags=["irating"])

@router.get("/distribution")
async def get_irating_distribution(datawh: DataRepository):
    return {'distribution': await datawh.irating_distribution()}

@router.get("/filters")
async def get_irating_filters(datawh: DataRepository):
    return {'distribution': await datawh.irating_filters()}