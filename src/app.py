from fastapi import FastAPI

from src.drivers.router import drivers as drivers_router
from src.connections.db import ClickhouseConn
from version import __version__

app = FastAPI()

app.include_router(drivers_router)

@app.get("/health")
async def get_health(ch: ClickhouseConn):
    return {"status": "ok", "version": __version__, "db": await ch.check_connection_to_click_house()}