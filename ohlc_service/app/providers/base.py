from abc import ABC, abstractmethod

class BaseProvider(ABC):
    @abstractmethod
    def fetch_ohlc(self, symbol: str, interval: str, limit: int = 100):
        pass
