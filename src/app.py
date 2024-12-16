from fastapi import FastAPI

from src.drivers.router import drivers as drivers_router
from version import __version__

app = FastAPI()

app.include_router(drivers_router)

@app.get("/health")
async def get_health():
    return {"status": "ok", "version": __version__}