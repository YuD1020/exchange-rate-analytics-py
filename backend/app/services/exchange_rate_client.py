from datetime import date
from typing import Protocol

import httpx


class ExchangeRateClient(Protocol):
    def fetch(self, start: date, end: date) -> dict[str, float]: ...


class ExchangeRateHostClient:
    BASE_URL = "https://api.exchangerate.host/timeseries"

    def fetch(self, start: date, end: date) -> dict[str, float]:
        response = httpx.get(
            self.BASE_URL,
            params={
                "base": "USD",
                "symbols": "ILS",
                "start_date": start.isoformat(),
                "end_date": end.isoformat(),
            },
            timeout=10,
        )
        response.raise_for_status()

        data = response.json()["rates"]
        return {d: v["ILS"] for d, v in data.items()}
