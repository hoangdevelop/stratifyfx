from fastapi import FastAPI
from app.core.db import engine
from app.db import Base
from app.services.scheduler import start as start_scheduler
from app.api.routes.ohlc import router as ohlc_router

app = FastAPI(title="OHLC Data Service")

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)
    start_scheduler()

app.include_router(ohlc_router)
