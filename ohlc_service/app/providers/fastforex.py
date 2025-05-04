import requests
from app.providers.base import BaseProvider
from app.core.config import settings

class FastForexProvider(BaseProvider):
    def fetch_ohlc(self, symbol, interval, limit=100):
        # Split symbol into from_currency and to_currency
        from_currency, to_currency = symbol.split("/")
        
        url = "https://api.fastforex.io/fetch-one"
        params = {
            "from": from_currency,
            "to": to_currency,
            "api_key": settings.FASTFOREX_API_KEY
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        # Convert FastForex response to OHLC format
        rate = data["result"][to_currency]
        timestamp = data["updated"]
        
        # Create a single OHLC data point
        ohlc_data = [{
            "datetime": timestamp,
            "open": rate,
            "high": rate,
            "low": rate,
            "close": rate,
            "volume": 0  # FastForex doesn't provide volume data
        }]
        
        return ohlc_data 