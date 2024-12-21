from aiocache import caches, RedisCache
#from aiocache.backends.redis import RedisCache
from aiocache.serializers import JsonSerializer
import os
import os

from config import settings

caches.set_config(
    {
        "default": {
            "cache": "aiocache.RedisCache",
            "endpoint": settings.redis_host,
            "port": settings.redis_port,
            "db": settings.redis_db,
            "serializer": {"class": "aiocache.serializers.JsonSerializer"},
        }
    }
)

redis_connection = RedisCache(endpoint=settings.redis_host, 
                         port=settings.redis_port, 
                         db=settings.redis_db, 
                         password=settings.redis_pass,
                         serializer=JsonSerializer())