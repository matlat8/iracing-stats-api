from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

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
    
    
# /series/{series_id}/seasons
class SeriesSeasonObject(BaseModel):
    season_id: int
    season_year: int
    season_quarter: int
    min_st: datetime
    max_st: datetime
    is_active_season: bool
    practice_sessions: int
    race_sessions: int
    time_trial_sessions: int
    total_sessions: int
    
class SeriesSeasonsResponse(BaseModel):
    seasons: List[SeriesSeasonObject]
    
# /series/{series_id}/seasons/{season_id}/weeks

class SeriesSeasonWeekCar(BaseModel):
    car_name: str
    car_image: str

class SeriesSeasonWeekWeek(BaseModel):
    race_week_num: int
    track_name: str
    config_name: Optional[str]
    cars: List[SeriesSeasonWeekCar]
    car_class_names: List[str]
    small_track_image: str
    splits_this_week: int