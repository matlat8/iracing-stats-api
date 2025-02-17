from pydantic import BaseModel
from typing import List, Optional

class AllDriversDriver(BaseModel):
    cust_id: int
    display_name: str
    total_events: Optional[int] = None
    irating_events: Optional[int] = None
    irating_events_avg_laps_completed: Optional[float] = None
    avg_finish_position_in_class: Optional[float] = None
    avg_start_position_in_class: Optional[float] = None
    
class AllDriverResponse(BaseModel):
    drivers: List[AllDriversDriver]
    

    
    
class DriverWins(BaseModel):
    total_wins: Optional[int] = None
    oval_wins: Optional[int] = None
    road_wins: Optional[int] = None
    dirt_oval_wins: Optional[int] = None
    dirt_road_wins: Optional[int] = None
    sports_car_wins: Optional[int] = None
    formula_car_wins: Optional[int] = None
    
class DriverRival(BaseModel):
    cust_id: Optional[int] = None
    name: Optional[str] = None
    times_beaten: Optional[int] = None
    club_name: Optional[str] = None
    country_code: Optional[str] = None
    oval_rating: Optional[int] = None
    road_rating: Optional[int] = None
    dirt_oval_rating: Optional[int] = None
    dirt_road_rating: Optional[int] = None
    sports_car_rating: Optional[int] = None
    formula_car_rating: Optional[int] = None
        
        
class DriverInformation(BaseModel):
    cust_id: int
    display_name: str
    club_name: Optional[str] = None
    country_code: Optional[str] = None
    total_events: Optional[int] = None
    total_races: Optional[int] = None
    total_wins: Optional[int] = None
    podiums: Optional[int] = None
    top_5: Optional[int] = None
    irating_events_avg_laps_completed: Optional[float] = None
    avg_finish_position_in_class: Optional[float] = None
    avg_start_position_in_class: Optional[float] = None
class DriverInformationResponse(BaseModel):
    information: Optional[DriverInformation] = None
    wins: Optional[DriverWins] = None
    rival: Optional[DriverRival] = None
    
class SearchDriverResponse(BaseModel):
    data: List[DriverInformation]
    
    
class AllTimeDriverWinRateByLicense(BaseModel):
    license_category: Optional[str] = None
    total_events: Optional[int] = None
    wins: Optional[int] = None
    win_rate: Optional[float] = None
    top_3: Optional[int] = None
    top_5: Optional[int] = None
    avg_finishing_position: Optional[float] = None
    
class AllTimeDriverWinRate(BaseModel):
    total_events: Optional[int] = None
    wins: Optional[int] = None
    win_rate: Optional[float] = None
    top_3: Optional[int] = None
    top_5: Optional[int] = None
    avg_finishing_position: Optional[float] = None

class AllTimeDriver(BaseModel):
    all: Optional[AllTimeDriverWinRate] = None
    categories: Optional[List[AllTimeDriverWinRateByLicense]] = None

class DriverWinRateResponse(BaseModel):
    all_time: Optional[AllTimeDriver] = None

class DriverLinkBody(BaseModel):
    cust_id: int