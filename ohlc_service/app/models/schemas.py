from pydantic import BaseModel
from datetime import datetime

class OHLCResponse(BaseModel):
    symbol: str
    interval: str
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float

    class Config:
        orm_mode = True
