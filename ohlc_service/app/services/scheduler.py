from apscheduler.schedulers.background import BackgroundScheduler
from app.core.db import SessionLocal
from app.services.crud import save_ohlc_batch
from app.providers.fastforex import FastForexProvider
import logging

logger = logging.getLogger(__name__)

def job():
    try:
        provider = FastForexProvider()  
        db = SessionLocal()
        logger.info("Starting OHLC data fetch job")

        for symbol in ["GBP/USD"]:
            for interval in ["1min"]:
                try:
                    logger.info(f"Fetching data for {symbol} with interval {interval}")
                    data = provider.fetch_ohlc(symbol, interval)
                    save_ohlc_batch(db, symbol, interval, data)
                    logger.info(f"Successfully saved data for {symbol}")
                except Exception as e:
                    logger.error(f"Error processing {symbol} with interval {interval}: {str(e)}")
                    continue

        db.close()
    except Exception as e:
        logger.error(f"Error in scheduler job: {str(e)}")
        if 'db' in locals():
            db.close()

def start():
    try:
        scheduler = BackgroundScheduler()
        scheduler.add_job(job, "interval", minutes=1)
        scheduler.start()
        logger.info("Scheduler started successfully")
    except Exception as e:
        logger.error(f"Failed to start scheduler: {str(e)}")
        raise
