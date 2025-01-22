import functools
import hashlib
import json
import redis
from typing import Any, Callable
from datetime import datetime
import redis.asyncio

from config import settings

redis_client = redis.asyncio.Redis(host=settings.redis_host, port=settings.redis_port, db=settings.redis_db, password=settings.redis_pass)

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if hasattr(obj, 'model_dump'):
            return obj.model_dump()
        elif hasattr(obj, 'dict'):
            return obj.dict()
        
        return super().default(obj)

def cachefunc(
    r: redis.asyncio.Redis,
    ttl: int = 3600,
    skip_first_arg: bool = True,
    skip_kwargs: list = None # Enable if using within class
) -> Callable:
    """
    A decorator that caches function results in Redis.
    
    Args:
        expire_seconds: Time in seconds before cache entry expires
        redis_host: Redis server host
        redis_port: Redis server port
    """
    
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            
            if skip_first_arg:
                cache_args = args[1:] if args else ()  # Skip the first arg (self)
            else:
                cache_args = args
                
            # Skip any kwargs that are not needed for cache key
            if skip_kwargs:
                for kw in skip_kwargs:
                    kwargs.pop(kw, None)
                
            # Create a unique cache key by combining function name and arguments
            cache_key = f"data:{func.__module__}:{func.__name__}:"
            
            # Convert args and kwargs to a consistent string format
            args_str = json.dumps(cache_args, sort_keys=True, cls=CustomJSONEncoder)
            kwargs_str = json.dumps(kwargs, sort_keys=True, cls=CustomJSONEncoder)
            
            # Create hash of the arguments
            key_hash = hashlib.md5(
                f"{args_str}:{kwargs_str}".encode()
            ).hexdigest()
            
            cache_key += key_hash
            
            # Try to get cached result
            cached_result = await r.get(cache_key)
            if cached_result is not None:
                return json.loads(cached_result)
            
            # If not in cache, execute function and cache result
            result = await func(*args, **kwargs)
            
            # Cache the result
            await r.setex(
                cache_key,
                ttl,
                json.dumps(result, cls=CustomJSONEncoder)
            )
            
            return result
        return wrapper
    return decorator