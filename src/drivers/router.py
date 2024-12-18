from fastapi import APIRouter

from src.connections.db import ClickhouseConn
from src.repo.datawh.data import DataWH

from . import service, schema


drivers = APIRouter(prefix="/drivers", tags=["drivers"])

@drivers.get("", response_model=schema.AllDriverResponse)
async def get_all_drivers(ch: ClickhouseConn):
    datawh = DataWH(ch)
    data = await service.get_drivers(datawh)
    return {'drivers': data}
    
    
@drivers.get("/{cust_id}", response_model=schema.DriverInformationResponse)
async def get_driver_info(cust_id, ch: ClickhouseConn):
    datawh = DataWH(ch)
    return await service.get_driver_info(datawh, cust_id)