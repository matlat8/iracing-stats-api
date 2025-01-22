from pydantic import BaseModel
from fastapi import Query, Depends
from fastapi.encoders import jsonable_encoder
from typing import Annotated

class Pagination(BaseModel):
    page: int = Query(1, ge=1, description="Page number")
    limit: int = Query(1000, le=1000, description="Limit per page")

    @property
    def limit_value(self) -> int:
        return min(self.limit, 1000)
    
    @limit_value.setter
    def limit_value(self, value: int) -> None:
        self.limit = min(value, 1000)
        
    @property
    def offset(self) -> int:
        return (self.page - 1) * self.limit
    
    def __json__(self):
        return {
            'page': self.page,
            'limit': self.limit
        }
        
PaginationParams = Annotated[Pagination, Depends()]