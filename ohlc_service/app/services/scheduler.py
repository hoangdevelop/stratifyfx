from apscheduler.schedulers.background import BackgroundScheduler
from app.providers.twelvedata import TwelveDataProvider
from app.core.db import SessionLocal
from app.services.crud import save_ohlc_batch
from app.providers.fastforex import FastForexProvider

def job():
    provider = TwelveDataProvider()
    db = SessionLocal()

    for symbol in ["GBP/USD"]:
        for interval in ["1min"]:
            data = provider.fetch_ohlc(symbol.replace("/", ""), interval)
            save_ohlc_batch(db, symbol, interval, data)

    provider = FastForexProvider()
    data = provider.fetch_ohlc("GBP/USD", "1min")

    db.close()

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, "interval", minutes=1)
    scheduler.start()
