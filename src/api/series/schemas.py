from typing import List
from pydantic import BaseModel

class SeriesThisWeekObject(BaseModel):
    series_id: int
    series_name: str
    series_short_name: str
    license_category: str
    race_week_num: int
    event_count: int

class SeriesThisWeekResponse(BaseModel):
    data: List[SeriesThisWeekObject]
    
class SeriesParticipation(BaseModel):
    series_id: int
    race_week_num: int
    participant_count: int

class SeriesParticipationObject(BaseModel):
    this_season: int
    weeks: List[SeriesParticipation]

class SeriesLookupResponse(BaseModel):
    seasons: List[dict]
    participation: SeriesParticipationObject
    