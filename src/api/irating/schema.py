from pydantic import BaseModel
from typing import List

class IRatingDistributionChartEntry(BaseModel):
    irating_group: int
    total: int
    
class IRatingDistributionResponse(BaseModel):
    chart: List[IRatingDistributionChartEntry]
    
class IRatingDistributionFiltersQuery(BaseModel):
    license: str
    period: str
    
    @property
    def year(self):
        return int(f'20{self.period[1:3]}')
    
    @property
    def quarter(self):
        return int(self.period[-1])