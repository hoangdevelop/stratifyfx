from fastapi import FastAPI
from app.core.db import engine
from app.db import Base
from app.services.scheduler import start as start_scheduler
from app.api.routes.ohlc import router as ohlc_router
from app.core.logging import setup_logging
import logging

logger = logging.getLogger(__name__)

app = FastAPI(title="OHLC Data Service")

@app.on_event("startup")
def startup_event():
    setup_logging()
    logger.info("Starting application...")
    Base.metadata.create_all(bind=engine)
    try:
        start_scheduler()
        logger.info("Scheduler started successfully")
    except Exception as e:
        logger.error(f"Failed to start scheduler: {str(e)}")
        raise

app.include_router(ohlc_router)
