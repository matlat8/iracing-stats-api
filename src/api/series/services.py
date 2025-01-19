
from src.repo.datawh.data import DataWH

from .schemas import SeriesParticipationObject, SeriesParticipation

async def series_latest_season_participation(datawh: DataWH, series_id: int) -> dict:
    
    data = await datawh.series_latest_season_participation(series_id=series_id)
    this_season = None
    
    if len(data) > 0 and isinstance(data[0].get('participant_count'), int):
        this_season = data[0]['participant_count']
    
    weeks = []
    for index, item in enumerate(data):
        if index not in (0, 1):
            weeks.append(SeriesParticipation.model_validate(item))
    
        
    
    return SeriesParticipationObject(this_season=this_season, weeks=weeks)