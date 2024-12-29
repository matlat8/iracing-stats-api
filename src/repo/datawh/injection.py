from typing import Annotated
from fastapi import Depends

from src.connections.db import ClickHouse
from .data import DataWH

async def get_repo():
    ch = ClickHouse()
    datawh = DataWH(ch)
    return datawh

DataRepository = Annotated[DataWH, Depends(get_repo)]