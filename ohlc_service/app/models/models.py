from sqlalchemy import Column, String, Float, TIMESTAMP, Integer
from app.db import Base

class OHLCPrice(Base):
    __tablename__ = "ohlc_prices"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    interval = Column(String)
    timestamp = Column(TIMESTAMP, index=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)
