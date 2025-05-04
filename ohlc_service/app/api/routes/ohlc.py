from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.db import SessionLocal
from app.models.models import OHLCPrice
from app.models.schemas import OHLCResponse, OHLCRequest
from typing import List

router = APIRouter(prefix="/ohlc", tags=["OHLC"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[OHLCResponse])
def get_ohlc(
    symbol: str = Query(...),
    interval: str = Query(...),
    limit: int = Query(100),
    db: Session = Depends(get_db)
):
    rows = db.query(OHLCPrice).filter(
        OHLCPrice.symbol == symbol,
        OHLCPrice.interval == interval
    ).order_by(OHLCPrice.timestamp.desc()).limit(limit).all()
    return rows

@router.post("/", response_model=OHLCResponse)
def create_ohlc(
    ohlc: OHLCRequest,
    db: Session = Depends(get_db)
):
    db_ohlc = OHLCPrice(
        symbol=ohlc.symbol,
        interval=ohlc.interval,
        timestamp=ohlc.timestamp,
        open=ohlc.open,
        high=ohlc.high,
        low=ohlc.low,
        close=ohlc.close,
        volume=ohlc.volume
    )
    db.add(db_ohlc)
    db.commit()
    db.refresh(db_ohlc)
    return db_ohlc