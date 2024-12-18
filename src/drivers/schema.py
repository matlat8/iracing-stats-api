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
        
class DriverInformationResponse(BaseModel):
    wins: DriverWins
    
    