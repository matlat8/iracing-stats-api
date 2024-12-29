from fastapi import APIRouter

from src.repo.datawh.injection import DataRepository

router = APIRouter(prefix="/sessions", tags=["sessions"])

@router.get("/{subsession_id}")
async def get_session_info(subsession_id: int, datawh: DataRepository):
    return {'data': await datawh.session_info(subsession_id)}