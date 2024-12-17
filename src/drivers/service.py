

from src.repo.datawh.data import DataWH

async def get_drivers(datawh: DataWH):
    return await datawh.get_drivers()