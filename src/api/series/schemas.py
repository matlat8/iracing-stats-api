from typing import List
from pydantic import BaseModel

class SeriesThisWeekObject(BaseModel):
    series_id: int
    series_name: str
    license_category: str
    race_week_num: int
    event_count: int

class SeriesThisWeekResponse(BaseModel):
    data: List[SeriesThisWeekObject]