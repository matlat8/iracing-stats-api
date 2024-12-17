from pydantic import BaseModel
from typing import List, Optional

class Driver(BaseModel):
    cust_id: int
    display_name: str
    total_events: Optional[int] = None
    irating_events: Optional[int] = None
    irating_events_avg_laps_completed: Optional[float] = None
    avg_finish_position_in_class: Optional[float] = None
    avg_start_position_in_class: Optional[float] = None
    
class DriverResponse(BaseModel):
    drivers: List[Driver]