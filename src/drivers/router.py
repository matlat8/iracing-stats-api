from fastapi import APIRouter

from src.connections.db import ClickhouseConn

drivers = APIRouter(prefix="/drivers", tags=["drivers"])

@drivers.get("")
async def get_all_drivers(ch: ClickhouseConn):
    query = "select 1 as numba union all select 2 as numba"
    result = await ch.fetchall(query)
    return {'data': result}
    