import asyncio
from src.repo.datawh.data import DataWH
from src.pagination import Pagination

from . import schema

async def get_drivers(datawh: DataWH):
    return await datawh.get_drivers()

async def get_driver_info(datawh: DataWH, cust_id: int):
    
    info_task = datawh.get_driver_info(cust_id)
    wins_task = datawh.get_driver_wins(cust_id)
    rival_task = datawh.get_driver_rival(cust_id)
    
    info, wins, rival = await asyncio.gather(info_task, wins_task, rival_task)
    return schema.DriverInformationResponse(information=info, wins=wins, rival=rival)

async def get_driver_events(datawh: DataWH, cust_id: int):
    return {'data': await datawh.get_driver_events(cust_id)}

async def search_driver(datawh: DataWH, search_term: str, pagination: Pagination):
    return {'data': await datawh.search_driver(search_term, pagination)}