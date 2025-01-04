from fastapi import FastAPI, Request
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.connections.db import ClickhouseConn

from version import __version__
from config import settings

app = FastAPI(app_name=settings.app_name, version=__version__)


from src.drivers.router import drivers as drivers_router
from src.sessions.router import router as sessions_router
from src.api.irating.router import router as irating_router
app.include_router(drivers_router)
app.include_router(sessions_router)
app.include_router(irating_router)

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
    
origins = [
    "http://localhost:3000",
    "https://iracingstat.com",
    "http://beta.iracingstat.com"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)