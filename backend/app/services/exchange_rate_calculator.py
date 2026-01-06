from collections import defaultdict
from datetime import date

from app.schemas.exchange_rate import MonthlyAverageRate
from app.services.exchange_rate_client import ExchangeRateClient
from app.utils.dates import month_key


class MonthlyAverageCalculator:
    def __init__(self, client: ExchangeRateClient):
        self.client = client

    def calculate(self, start: date, end: date) -> list[MonthlyAverageRate]:
        rates = self.client.fetch(start, end)

        buckets: dict[str, list[float]] = defaultdict(list)

        for day_str, rate in rates.items():
            day = date.fromisoformat(day_str)
            buckets[month_key(day)].append(rate)

        return [
            MonthlyAverageRate(
                month=month,
                average_rate=round(sum(values) / len(values), 4),
            )
            for month, values in sorted(buckets.items())
        ]
