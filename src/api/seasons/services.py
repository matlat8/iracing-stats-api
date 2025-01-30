import asyncio
from src.repo.datawh.data import DataWH

async def get_week_info(repo: DataWH, season_id: int, week_num: int):
    week_info, cars = await asyncio.gather(
        repo.season_week_info(season_id, week_num),
        repo.season_week_cars(season_id, week_num)
    )
    
    if cars:
        week_info['cars'] = cars
    
    return week_info