from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import json
import sys
from contextvars import ContextVar
from time import perf_counter
import uuid
from logtail import LogtailHandler
from config import settings

logtail_handler = LogtailHandler(source_token=settings.logtail_source_token)

def json_serializer(record):
    log_entry = {
        "time": record["time"].strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
        "level": record["level"].name,
        "message": record["message"],
        "file": record["file"].path,
        "function": record["function"],
        "line": record["line"],
        "trace_id": record["extra"].get("trace_id", None)
    }
    return json.dumps(log_entry)

def setup_logging(log_file="log.json"):
    logger.remove()  # Remove the default logger
    logger.add(log_file, serialize=True, enqueue=True, backtrace=True)
    logger.add(sys.stdout, format="{time} {level} {message}", level=settings.log_level.upper())
    
    # Only send logs to betterstack if the environment is not dev
    if settings.environment != "dev":
        logger.add(
            logtail_handler,
            format="{message}",
            level="DEBUG",
            serialize=True,
            backtrace=True,
            diagnose=False
        )
        

# Call the setup function to configure the logger at import time
setup_logging()

trace_id_var: ContextVar[str] = ContextVar("trace_id", default=None)

class TraceIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        trace_id = str(uuid.uuid4())
        request.state.trace_id = trace_id
        trace_id_var.set(trace_id)
        with logger.contextualize(trace_id=trace_id, environment=settings.environment):
            st = perf_counter()
            
            response = await call_next(request)
            
            et = perf_counter()
            
            logger.info(f"{request.base_url} - {request.client.host} - {request.method} - {request.url.path} - {response.status_code} - {et - st:.2f}s")
        return response