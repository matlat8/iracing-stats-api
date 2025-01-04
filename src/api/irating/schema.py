from pydantic import BaseModel
from typing import List

class IRatingDistributionChartEntry(BaseModel):
    irating_group: int
    total: int
    
class IRatingDistributionResponse(BaseModel):
    chart: List[IRatingDistributionChartEntry]