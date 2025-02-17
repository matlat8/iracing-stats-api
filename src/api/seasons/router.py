from fastapi import APIRouter

from src.repo.datawh.injection import DataRepository

from . import services

router = APIRouter()

@router.get("/seasons/{season_id}/weeks/{week_num}/avg_irating_laptime")
async def get_avg_irating_laptime(season_id: int, week_num: int, repo: DataRepository):
    return {'chart': await repo.week_irating_avg(season_id, week_num)}

@router.get('/seasons/{season_id}')
async def get_season_info(season_id: int, repo: DataRepository):
    return {'data': await repo.season_info(season_id)}

@router.get('/seasons/{season_id}/weeks/{week_num}')
async def get_season_week_info(season_id: int, week_num: int, repo: DataRepository):
    return {'data': await services.get_week_info(repo, season_id, week_num)}