from apscheduler.schedulers.background import BackgroundScheduler
from app.core.db import SessionLocal
from app.services.crud import save_ohlc_batch
from app.providers.fastforex import FastForexProvider

def job():
    provider = FastForexProvider()  
    db = SessionLocal()

    for symbol in ["GBP/USD"]:
        for interval in ["1min"]:
            data = provider.fetch_ohlc(symbol.replace("/", ""), interval)
            save_ohlc_batch(db, symbol, interval, data)

    db.close()

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, "interval", minutes=1)
    scheduler.start()
