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
    total_wins: int
    oval_wins: int
    road_wins: int
    dirt_oval_wins: int
    dirt_road_wins: int
    sports_car_wins: int
    formula_car_wins: int
    
class DriverRival(BaseModel):
    cust_id: Optional[int] = None
    name: str
    times_beaten: int
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
    club_name: str
    country_code: str
    oval_rating: Optional[int] = None
    road_rating: Optional[int] = None
    dirt_oval_rating: Optional[int] = None
    dirt_road_rating: Optional[int] = None
    sports_car_rating: Optional[int] = None
    formula_car_rating: Optional[int] = None
class DriverInformationResponse(BaseModel):
    information: DriverInformation
    wins: DriverWins
    rival: DriverRival
    
    