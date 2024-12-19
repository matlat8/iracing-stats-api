import asyncio
from src.repo.datawh.data import DataWH

from . import schema

async def get_drivers(datawh: DataWH):
    return await datawh.get_drivers()

async def get_driver_info(datawh: DataWH, cust_id: int):
    info, wins = await asyncio.gather(datawh.get_driver_info(cust_id), datawh.get_driver_wins(cust_id))
    return schema.DriverInformationResponse(information=info, wins=wins)

async def get_driver_events(datawh: DataWH, cust_id: int):
    return {'data': await datawh.get_driver_events(cust_id)}