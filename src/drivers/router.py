from fastapi import APIRouter

from src.connections.db import ClickhouseConn
from src.repo.datawh.data import DataWH
from src.pagination import PaginationParams

from src.repo.datawh.injection import DataRepository

from . import service, schema, utility


drivers = APIRouter(prefix="/drivers", tags=["drivers"])

@drivers.get("") # , response_model=schema.AllDriverResponse
async def get_all_drivers(ch: ClickhouseConn):
    datawh = DataWH(ch)
    data = await service.get_drivers(datawh)
    return {'drivers': data}
    
@drivers.get("/search") # , response_model=schema.SearchDriverResponse
async def search_for_drivers(search_term: str, pagination: PaginationParams, ch: ClickhouseConn):
    datawh = DataWH(ch)
    return await service.search_driver(datawh, search_term, pagination)

@drivers.get("/top/wins")
async def top_driver_by_wins(dwh: DataRepository):
    return {'data': await dwh.top_drivers_by_wins_this_season(limit=10)}
    
@drivers.get("/{cust_id}", response_model=schema.DriverInformationResponse)
async def get_driver_info(cust_id, ch: ClickhouseConn):
    datawh = DataWH(ch)
    return await service.get_driver_info(datawh, cust_id)

@drivers.get("/{cust_id}/events")
async def driver_events(cust_id, pagination: PaginationParams, ch: ClickhouseConn):
    datawh = DataWH(ch)
    return await service.get_driver_events(datawh, cust_id, pagination)

@drivers.get("/{cust_id}/win-rate", response_class=utility.NanJSONResponse)
async def driver_win_rate(cust_id, ch: ClickhouseConn):
    datawh = DataWH(ch)
    return await service.get_driver_winrate(datawh, cust_id)

@drivers.get("/{cust_id}/stats")
async def driver_stats(cust_id, datawh: DataRepository):
    return {
        'seasons_rollup': await datawh.driver_stats_rollup_by_season(cust_id)
    }
    
@drivers.get("/{cust_id}/tracks")
async def driver_track_stats(cust_id, datawh: DataRepository):
    return {'data': await datawh.driver_track_stats(cust_id)}

@drivers.get("/{cust_id}/irating")
async def driver_irating(cust_id: int, ch: ClickhouseConn):
    datawh = DataWH(ch)
    return await service.get_driver_irating(datawh, cust_id)