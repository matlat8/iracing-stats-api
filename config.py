from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "iRacing Stats API"
    ch_host: str
    ch_port: int = 9000
    ch_user: str = "default"
    ch_pass: str = "default"
    ch_db: str    

@lru_cache()   
def get_settings():
    return Settings() 

settings = get_settings()



