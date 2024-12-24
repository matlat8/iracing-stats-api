from fastapi import FastAPI, Request
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse

from src.drivers.router import drivers as drivers_router
from src.connections.db import ClickhouseConn

from version import __version__
from config import settings

app = FastAPI(app_name=settings.app_name, version=__version__)

app.include_router(drivers_router)

@app.get("/health")
async def get_health(ch: ClickhouseConn):
    return {"status": "ok", "version": __version__, "db": await ch.check_connection_to_click_house()}

@app.exception_handler(ResponseValidationError)
async def response_validation_exception_handler(request: Request, exc: ResponseValidationError):
    return JSONResponse(
        status_code=500,
        content={
            "detail": exc.errors()
        }
    )