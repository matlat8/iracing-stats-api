from functools import lru_cache
from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "iRacing Stats API"
    ch_host: str
    ch_port: int = 9000
    ch_user: str = "default"
    ch_pass: str = "default"
    ch_db: str    
    redis_host: str = 'localhost'
    redis_port: int = 6379
    redis_db: int = 0
    redis_user: Optional[str] = None
    redis_pass: Optional[str] = None

@lru_cache()   
def get_settings():
    return Settings() 

settings = get_settings()



