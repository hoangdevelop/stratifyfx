import requests
from app.providers.base import BaseProvider
from app.core.config import settings

class TwelveDataProvider(BaseProvider):
    def fetch_ohlc(self, symbol, interval, limit=100):
        url = f"https://api.twelvedata.com/time_series"
        params = {
            "symbol": symbol,
            "interval": interval,
            "apikey": settings.TWELVE_API_KEY,
            "outputsize": limit,
        }
        response = requests.get(url, params=params)
        data = response.json()
        for item in data.get("values", []):
            item["datetime"] = item.pop("datetime") if "datetime" in item else item.get("timestamp")
        return data.get("values", [])
