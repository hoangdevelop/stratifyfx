from app.models.models import OHLCPrice
from sqlalchemy.orm import Session

def save_ohlc_batch(db: Session, symbol: str, interval: str, data: list[dict]):
    for row in data:
        db.add(OHLCPrice(
            symbol=symbol,
            interval=interval,
            timestamp=row["datetime"],
            open=row["open"],
            high=row["high"],
            low=row["low"],
            close=row["close"],
            volume=row.get("volume", 0)
        ))
    db.commit()
