
from src.repo.datawh.data import DataWH

from . import schema

async def irating_distribution(datawh: DataWH, params: schema.IRatingDistributionFiltersQuery):
    data = await datawh.irating_distribution(params.license, params.year, params.quarter)
    print(params.year)
    print(params.quarter)
    return data
    
    