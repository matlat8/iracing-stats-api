from fastapi import APIRouter

from src.connections.db import ClickhouseConn
from src.repo.datawh.data import DataWH
from .service import get_drivers
from .schema import DriverResponse

drivers = APIRouter(prefix="/drivers", tags=["drivers"])

@drivers.get("", response_model=DriverResponse)
async def get_all_drivers(ch: ClickhouseConn):
    datawh = DataWH(ch)
    data = await get_drivers(datawh)
    return {'drivers': data}
    