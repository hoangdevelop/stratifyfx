from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.db import SessionLocal
from app.models.models import OHLCPrice
from app.models.schemas import OHLCResponse
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