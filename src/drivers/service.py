from src.repo.datawh.data import DataWH

async def get_drivers(datawh: DataWH):
    return await datawh.get_drivers()

async def get_driver_info(datawh: DataWH, cust_id: int):
    wins = await datawh.get_driver_wins(cust_id)
    return {'wins': wins}